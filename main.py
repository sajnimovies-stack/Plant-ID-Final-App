import os
import requests
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

# Screen size for testing
Window.size = (360, 640)

KV = '''
MDScreen:
    md_bg_color: 0.95, 0.95, 0.95, 1

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "AI Plant Identifier"
            md_bg_color: 0, 0.4, 0.2, 1
            elevation: 4
            right_action_items: [["refresh", lambda x: app.reset_app()]]

        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "15dp"

            # Image Preview Area
            MDCard:
                size_hint: (1, 0.5)
                radius: [20, ]
                elevation: 2
                md_bg_color: 1, 1, 1, 1
                MDBoxLayout:
                    padding: "10dp"
                    AsyncImage:
                        id: plant_img
                        source: 'https://cdn-icons-png.flaticon.com/512/628/628283.png'
                        allow_stretch: True

            # Info Area
            MDCard:
                size_hint: (1, 0.3)
                radius: [20, ]
                padding: "15dp"
                orientation: 'vertical'
                MDLabel:
                    id: result_title
                    text: "Ready to Identify"
                    halign: "center"
                    font_style: "H6"
                    theme_text_color: "Primary"
                MDLabel:
                    id: result_detail
                    text: "Take a photo of a leaf to see details"
                    halign: "center"
                    theme_text_color: "Secondary"

            # Control Buttons
            MDBoxLayout:
                size_hint_y: 0.2
                spacing: "20dp"
                padding: "10dp"

                MDFloatingActionButton:
                    icon: "camera"
                    md_bg_color: 0, 0.4, 0.2, 1
                    on_release: app.open_camera()
                
                MDFloatingActionButton:
                    icon: "image-plus"
                    md_bg_color: 0, 0.5, 0.8, 1
                    on_release: app.open_gallery()

                MDRaisedButton:
                    text: "IDENTIFY NOW"
                    md_bg_color: 0.1, 0.6, 0.3, 1
                    size_hint_x: 1
                    on_release: app.identify_plant()
'''

class PlantIDApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def open_camera(self):
        # Native Intent for Pixel 6 stability
        if platform == 'android':
            try:
                from android import activity
                from jnius import autoclass
                Intent = autoclass('android.content.Intent')
                MediaStore = autoclass('android.provider.MediaStore')
                intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
                activity.startActivityForResult(intent, 123)
                self.root.ids.result_title.text = "Camera Opening..."
            except:
                self.root.ids.result_title.text = "Camera Error"
        else:
            self.root.ids.result_title.text = "Android Only"

    def open_gallery(self):
        self.root.ids.result_title.text = "Select from Gallery"
        # Logic for file picker goes here

    def identify_plant(self):
        self.root.ids.result_title.text = "Analyzing..."
        self.root.ids.result_detail.text = "Connecting to AI Server..."
        # Simulated AI Response
        Clock.schedule_once(self.show_mock_result, 2)

    def show_mock_result(self, dt):
        self.root.ids.result_title.text = "Monstera Deliciosa"
        self.root.ids.result_detail.text = "Confidence: 98%\\nType: Indoor Plant\\nWater: Once a week"

    def reset_app(self):
        self.root.ids.result_title.text = "Ready to Identify"
        self.root.ids.result_detail.text = "Take a photo of a leaf"
        self.root.ids.plant_img.source = 'https://cdn-icons-png.flaticon.com/512/628/628283.png'

if __name__ == "__main__":
    PlantIDApp().run()
