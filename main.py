from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

class PlantIDApp(App):
    def build(self):
        # Background color white
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Logo ya Icon
        self.img = Image(source='logo.png', size_hint=(1, 0.4)) # Agar logo nahi hai to ye khali rahega
        
        self.label = Label(
            text="Plant Identifier AI", 
            font_size='24sp', 
            color=(0, 0.4, 0.2, 1),
            bold=True,
            size_hint=(1, 0.2)
        )
        
        btn = Button(
            text="Identify Plant",
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size='20sp',
            background_normal=''
        )
        btn.bind(on_release=self.on_click)
        
        layout.add_widget(self.img)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def on_click(self, instance):
        self.label.text = "Processing..."

if __name__ == "__main__":
    PlantIDApp().run()
