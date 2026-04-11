import os
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

# Pixel 6 aur Android 14 ke liye zaroori drivers
if platform == 'android':
    os.environ['KIVY_GL_BACKEND'] = 'sdl2'
    os.environ['KIVY_VIDEO'] = 'android' # Force Android native video engine

KV = '''
MDScreen:
    md_bg_color: 0.05, 0.05, 0.05, 1

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Plant Scanner Pro"
            elevation: 4
            md_bg_color: 0, 0.4, 0.2, 1
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            id: camera_layout
            size_hint_y: 0.7
            padding: "5dp"
            MDLabel:
                id: loading_msg
                text: "Waiting for System..."
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 0.5

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.25
            md_bg_color: 1, 1, 1, 1
            padding: "15dp"
            spacing: "10dp"
            radius: [25, 25, 0, 0]

            MDLabel:
                id: status_label
                text: "Initializing..."
                halign: "center"
                theme_text_color: "Primary"
                font_style: "H6"

            MDFloatingActionButton:
                icon: "camera"
                icon_size: "35sp"
                md_bg_color: 0, 0.4, 0.2, 1
                pos_hint: {"center_x": .5}
                on_release: app.take_photo()
'''

class PlantScannerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def on_start(self):
        # 3 second delay taake system permissions sahi se load hon
        Clock.schedule_once(self.check_permissions, 3)

    def check_permissions(self, dt):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions(
                [Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE], 
                self.start_camera_logic
            )
        else:
            self.start_camera_logic(True, [])

    def start_camera_logic(self, permissions_granted, grants):
        if permissions_granted:
            # Camera ko 1 second baad connect karein taake permissions active ho chuki hon
            Clock.schedule_once(self.deferred_camera_start, 1)
        else:
            self.root.ids.status_label.text = "Permission Denied!"

    def deferred_camera_start(self, dt):
        try:
            from camera4kivy import Preview
            self.preview = Preview()
            self.root.ids.camera_layout.clear_widgets()
            self.root.ids.camera_layout.add_widget(self.preview)
            # Pixel 6 fix: connect_camera ko default settings ke sath chalayein
            self.preview.connect_camera(enable_analyze_callback=True)
            self.root.ids.status_label.text = "Camera Active"
        except Exception as e:
            self.root.ids.status_label.text = "Retrying Camera..."
            # Agar fail ho toh 2 second baad dobara koshish karein
            Clock.schedule_once(self.deferred_camera_start, 2)

    def take_photo(self):
        if hasattr(self, 'preview'):
            self.root.ids.status_label.text = "Scanning..."
            self.preview.capture_screenshot("plant_scan.png")
            self.root.ids.status_label.text = "Saved to Gallery!"
        else:
            self.root.ids.status_label.text = "Camera not ready"

if __name__ == "__main__":
    PlantScannerApp().run()
