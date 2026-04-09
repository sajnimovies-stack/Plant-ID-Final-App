from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class PlantApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 20
        self.label = Label(text="Plant Identifier Ready\nClick below to Start", halign="center")
        self.add_widget(self.label)
        
        self.btn = Button(text="Identify Now", size_hint=(1, 0.2), background_color=(0, 0.7, 0, 1))
        self.add_widget(self.btn)

class MainApp(App):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA, Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE])
        return PlantApp()

if __name__ == "__main__":
    MainApp().run()
