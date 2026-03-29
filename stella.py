from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class StellaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10)
        self.label = Label(text="🌌 STELLA ETERNAL OS: ANDROID\nWelcome Owner!", font_size='20sp')
        self.input = TextInput(hint_text='Owner, write here...', multiline=False)
        self.input.bind(on_text_validate=self.on_enter)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        return self.layout

    def on_enter(self, instance):
        user_text = self.input.text
        self.label.text = f"Owner says: {user_text}\n(processing...)"
        self.input.text = ""

if __name__ == "__main__":
    StellaApp().run()
