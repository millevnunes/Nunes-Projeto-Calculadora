from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class CalculatorLayout(BoxLayout):
    display_text = StringProperty("0")

    def clear_display(self):
        self.display_text = "0"

    def update_display(self, text):
        if self.display_text == "0":
            self.display_text = text
        else:
            self.display_text += text

    def calculate_result(self):
        try:
            self.display_text = str(eval(self.display_text))
        except Exception as e:
            self.display_text = "Error"


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()
