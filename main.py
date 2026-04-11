import os
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

# Pixel 6 Graphics Fix
if platform == 'android':
    os.environ['KIVY_GL_BACKEND'] = 'sdl2'

# Camera4Kivy ka basic layout
KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Plant Scanner Pro"
            elevation: 4
            md_bg_color: 0, 0.4, 0.2, 1
            specific_text_color: 1, 1, 1, 1

        # Asli Camera View yahan load hoga
        MDBoxLayout:
            id: camera_layout
            size_hint_y: 0.7

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.2
            md_bg_color: 1, 1, 1, 1
            padding: "10dp"
            spacing: "10dp"
            radius: [25, 25, 0, 0]

            MDLabel:
                id: status_label
                text: "Point at a plant and tap"
                halign: "center"
                theme_text_color: "Primary"
                font_style: "Button"

            MDFloatingActionButton:
                icon: "camera"
                md_bg_color: 0, 0.4, 0.2, 1
                pos_hint: {"center_x": .5}
                on_release: app.take_screenshot()
'''

class PlantScannerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def on_start(self):
        # Permissions mangne ke baad camera start hoga
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE], self.start_camera)
        else:
            self.start_camera(True, [])

    def start_camera(self, permissions_granted, grants):
        if permissions_granted:
            # Camera4Kivy ko dynamic load karna takay crash na ho
            from camera4kivy import Preview
            self.preview = Preview()
            self.root.ids.camera_layout.add_widget(self.preview)
            self.preview.connect_camera(enable_analyze_callback=True)
        else:
            self.root.ids.status_label.text = "Permission Denied!"

    def take_screenshot(self):
        # Yeh function photo lega
        self.root.ids.status_label.text = "Scanning Plant... (AI)"
        # Note: Photo save logic yahan add hota hai
        if hasattr(self, 'preview'):
            self.preview.capture_screenshot("plant_capture.png")

if __name__ == "__main__":
    PlantScannerApp().run()
