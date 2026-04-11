import os
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

# UI Design
KV = '''
MDScreen:
    md_bg_color: 0.95, 0.95, 0.95, 1
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Plant Identifier Pro"
            elevation: 4
            md_bg_color: 0, 0.4, 0.2, 1
            specific_text_color: 1, 1, 1, 1
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "30dp"

            MDCard:
                size_hint: (1, 0.6)
                radius: [25, ]
                elevation: 2
                md_bg_color: 1, 1, 1, 1
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "20dp"
                    spacing: "10dp"
                    MDIconButton:
                        icon: "camera-iris"
                        icon_size: "120sp"
                        pos_hint: {"center_x": .5}
                        theme_icon_color: "Custom"
                        icon_color: 0, 0.4, 0.2, 1
                    MDLabel:
                        id: status_label
                        text: "Tap the button below to open camera"
                        halign: "center"
                        theme_text_color: "Secondary"
                        font_style: "Button"

            MDFloatingActionButton:
                icon: "camera"
                icon_size: "30sp"
                md_bg_color: 0, 0.4, 0.2, 1
                pos_hint: {"center_x": .5}
                on_release: app.open_native_camera()
'''

class PlantApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def open_native_camera(self):
        if platform == 'android':
            try:
                from android import activity
                from jnius import autoclass
                
                # Android's built-in camera call
                Intent = autoclass('android.content.Intent')
                MediaStore = autoclass('android.provider.MediaStore')
                
                intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
                activity.bind(on_activity_result=self.on_camera_result)
                activity.startActivityForResult(intent, 0x123)
            except Exception as e:
                self.root.ids.status_label.text = f"System Error: {str(e)}"
        else:
            self.root.ids.status_label.text = "This only works on a real Android phone!"

    def on_camera_result(self, request_code, result_code, intent):
        if request_code == 0x123:
            # Jab user photo khich kar OK kar de
            self.root.ids.status_label.text = "Photo Captured! Ready to Scan Plant."
            # Note: Screen par image dikhane ka code yahan add hota hai

if __name__ == "__main__":
    PlantApp().run()
