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
            elevation: 4
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "20dp"

            MDLabel:
                id: status_label
                text: "Status: Ready"
                halign: "center"
                theme_text_color: "Primary"
                font_style: "H6"

            MDRaisedButton:
                text: "OPEN CAMERA"
                pos_hint: {"center_x": .5}
                size_hint_x: 0.8
                md_bg_color: 0, 0.4, 0.2, 1
                on_release: app.open_camera()

            MDRaisedButton:
                text: "OPEN GALLERY"
                pos_hint: {"center_x": .5}
                size_hint_x: 0.8
                md_bg_color: 0.1, 0.5, 0.8, 1
                on_release: app.open_gallery()
'''

class PlantIDApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def open_camera(self):
        if platform == 'android':
            try:
                from android import activity
                from jnius import autoclass
                Intent = autoclass('android.content.Intent')
                MediaStore = autoclass('android.provider.MediaStore')
                
                intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
                # Pixel 6 Fix: Activity result bind karna lazmi hai
                activity.bind(on_activity_result=self.on_result)
                activity.startActivityForResult(intent, 123)
                self.root.ids.status_label.text = "Opening Camera..."
            except Exception as e:
                self.root.ids.status_label.text = f"Error: {str(e)}"
        else:
            self.root.ids.status_label.text = "Desktop: Camera simulated"

    def open_gallery(self):
        if platform == 'android':
            try:
                from android import activity
                from jnius import autoclass
                Intent = autoclass('android.content.Intent')
                
                # Android 14 stable method
                intent = Intent(Intent.ACTION_GET_CONTENT)
                intent.setType("image/*")
                intent.addCategory(Intent.CATEGORY_OPENABLE)
                
                activity.bind(on_activity_result=self.on_result)
                chooser = Intent.createChooser(intent, "Select Plant Photo")
                activity.startActivityForResult(chooser, 456)
                self.root.ids.status_label.text = "Opening Gallery..."
            except Exception as e:
                self.root.ids.status_label.text = f"Error: {str(e)}"
        else:
            self.root.ids.status_label.text = "Desktop: Gallery simulated"

    def on_result(self, request_code, result_code, intent):
        # Jab user wapis app mein aaye
        if result_code == -1: # -1 means RESULT_OK
            self.root.ids.status_label.text = "Photo Selected Successfully!"
        else:
            self.root.ids.status_label.text = "Selection Cancelled"

if __name__ == "__main__":
    PlantIDApp().run()
