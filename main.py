from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.utils import platform
from kivy.clock import Clock

# Permissions request
def ask_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE])

KV = '''
MDScreen:
    md_bg_color: 0.95, 0.95, 0.95, 1
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Plant Identifier Pro"
            elevation: 2
            md_bg_color: 0, 0.4, 0.2, 1
            specific_text_color: 1, 1, 1, 1
            
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "20dp"
            
            # App Ka Graphics Wala Hissa (Main Container)
            MDCard:
                size_hint: (1, 0.6)
                radius: [25, ]
                md_bg_color: 1, 1, 1, 1
                elevation: 4
                padding: "10dp"
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDLabel:
                        id: status_label
                        text: "Ready to Scan"
                        halign: "center"
                        font_style: "H5"
                        theme_text_color: "Custom"
                        text_color: 0, 0.4, 0.2, 1
                        
                    # Yahan aap pauday ki image dikha sakte hain
                    MDIconButton:
                        icon: "leaf-circle"
                        icon_size: "120sp"
                        pos_hint: {"center_x": .5}
                        theme_icon_color: "Custom"
                        icon_color: 0, 0.4, 0.2, 0.8

            MDLabel:
                text: "Point your camera at a plant and press the button below"
                halign: "center"
                theme_text_color: "Secondary"
                font_style: "Caption"

            MDFloatingActionButton:
                icon: "camera"
                icon_size: "30sp"
                md_bg_color: 0, 0.4, 0.2, 1
                pos_hint: {"center_x": .5}
                on_release: app.scan_now()
'''

class PlantApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_once(lambda dt: ask_permissions(), 1)

    def scan_now(self):
        self.root.ids.status_label.text = "AI Scanning..."
        # Yahan camera open karne ya photo lene ka logic aayega

if __name__ == "__main__":
    PlantApp().run()
