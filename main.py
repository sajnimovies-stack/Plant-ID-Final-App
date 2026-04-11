from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDFloatingActionButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.lang import Builder

# Graphics aur Design ka code (KV Language)
KV = '''
MDScreen:
    md_bg_color: 0.95, 0.95, 0.95, 1

    MDTopAppBar:
        title: "Plant Identifier AI"
        elevation: 4
        pos_hint: {"top": 1}
        md_bg_color: 0, 0.4, 0.2, 1  # Dark Green Theme
        specific_text_color: 1, 1, 1, 1

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height
        spacing: "20dp"
        padding: "20dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "Pauday ki tasveer upload karein"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Secondary"

        MDIconButton:
            icon: "leaf"
            icon_size: "100sp"
            theme_icon_color: "Custom"
            icon_color: 0, 0.5, 0.2, 1
            pos_hint: {"center_x": .5}

        MDRaisedButton:
            text: "TASVEER KHENCHEIN"
            md_bg_color: 0, 0.5, 0.2, 1
            size_hint_x: 0.8
            pos_hint: {"center_x": .5}
            on_release: app.identify_plant()

        MDLabel:
            id: result_label
            text: "Result yahan nazar aayega"
            halign: "center"
            theme_text_color: "Primary"
'''

class PlantApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def identify_plant(self):
        self.root.ids.result_label.text = "AI Tashkees kar raha hai..."

if __name__ == "__main__":
    PlantApp().run()
