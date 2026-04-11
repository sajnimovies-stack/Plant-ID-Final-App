import os
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

KV = '''
MDScreen:
    md_bg_color: 0.95, 0.95, 0.95, 1
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Plant Identifier Fix"
            md_bg_color: 0.1, 0.5, 0.3, 1
            elevation: 4
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: "30dp"
            spacing: "20dp"

            MDCard:
                size_hint: (1, 0.5)
                radius: [20, ]
                elevation: 2
                MDBoxLayout:
                    padding: "15dp"
                    MDLabel:
                        id: status_label
                        text: "Hardware issues detected. Use the button below to pick 'Camera' from system menu."
                        halign: "center"
                        theme_text_color: "Secondary"

            MDRaisedButton:
                text: "START CAMERA / PICK IMAGE"
                pos_hint: {"center_x": .5}
                size_hint_x: 0.8
                md_bg_color: 0.1, 0.5, 0.3, 1
                on_release: app.open_universal_picker()
'''

class PlantApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def open_universal_picker(self):
        if platform == 'android':
            try:
                from android import activity
                from jnius import autoclass
                
                Intent = autoclass('android.content.Intent')
                # Yeh line system ko image choose karne ka kehti hai
                intent = Intent(Intent.ACTION_GET_CONTENT)
                intent.setType("image/*")
                intent.addCategory(Intent.CATEGORY_OPENABLE)
                
                # Chooser dikhana taake user camera ya gallery select kare
                chooser = Intent.createChooser(intent, "Select Source")
                activity.startActivityForResult(chooser, 100)
                self.root.ids.status_label.text = "System menu opened..."
            except Exception as e:
                self.root.ids.status_label.text = "System error. Try settings."
        else:
            self.root.ids.status_label.text = "Android only feature."

if __name__ == "__main__":
    PlantApp().run()
