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
            title: "Plant ID - Final Fix"
            md_bg_color: 0, 0.4, 0.2, 1
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "20dp"

            MDLabel:
                id: status_label
                text: "Status: Ready"
                halign: "center"
                theme_text_color: "Primary"

            MDRaisedButton:
                text: "OPEN CAMERA"
                pos_hint: {"center_x": .5}
                size_hint_x: 0.8
                on_release: app.open_camera()

            MDRaisedButton:
                text: "OPEN GALLERY"
                pos_hint: {"center_x": .5}
                size_hint_x: 0.8
                on_release: app.open_gallery()
'''

class PlantIDApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def open_camera(self):
        if platform == 'android':
            from android import activity
            from jnius import autoclass
            Intent = autoclass('android.content.Intent')
            MediaStore = autoclass('android.provider.MediaStore')
            intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
            activity.startActivityForResult(intent, 123)
        else:
            print("Camera call")

    def open_gallery(self):
        if platform == 'android':
            from android import activity
            from jnius import autoclass
            Intent = autoclass('android.content.Intent')
            intent = Intent(Intent.ACTION_PICK)
            intent.setType("image/*")
            activity.startActivityForResult(intent, 456)
        else:
            print("Gallery call")

if __name__ == "__main__":
    PlantIDApp().run()
