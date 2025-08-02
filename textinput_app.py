from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Text input field
        self.text_input = TextInput(multiline=False, size_hint=(1, 0.2))
        self.layout.add_widget(self.text_input)

        # Label to display entered text
        self.label = Label(text="Type something and press the button", size_hint=(1, 0.3))
        self.layout.add_widget(self.label)

        # Button to trigger display
        btn = Button(text="Show Text", size_hint=(1, 0.2))
        btn.bind(on_press=self.show_text)
        self.layout.add_widget(btn)

        return self.layout

    def show_text(self, instance):
        # Update label with text input value
        self.label.text = self.text_input.text

if __name__ == '__main__':
    TextInputApp().run()
