from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.utils import platform

# Naye Android versions ke liye permission mangna
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE])

KV = '''
MDScreen:
    md_bg_color: 0.9, 0.9, 0.9, 1

    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Plant Identifier AI"
            elevation: 2
            md_bg_color: 0.1, 0.5, 0.2, 1
            specific_text_color: 1, 1, 1, 1

        MDBoxLayout:
            orientation: 'vertical'
            padding: "10dp"
            spacing: "10dp"

            # Camera View Area (Black Box placeholder for camera)
            MDCard:
                size_hint: (1, 0.6)
                radius: [20, ]
                md_bg_color: 0, 0, 0, 1
                elevation: 3
                
                MDLabel:
                    text: "Camera Preview"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 0.5

            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: 0.4
                padding: "20dp"
                spacing: "20dp"

                MDLabel:
                    id: result_label
                    text: "Identify any plant instantly!"
                    halign: "center"
                    font_style: "H6"
                    theme_text_color: "Primary"

                MDFloatingActionButton:
                    icon: "camera"
                    icon_size: "35sp"
                    md_bg_color: 0.1, 0.5, 0.2, 1
                    pos_hint: {"center_x": .5}
                    on_release: app.identify_now()
'''

class PlantApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def identify_now(self):
        self.root.ids.result_label.text = "AI is scanning..."
        # Yahan aap apna identification logic add kar sakte hain

if __name__ == "__main__":
    PlantApp().run()
