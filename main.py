from kivy.lang import Builder
from kivymd.app import MDApp

root_kv = """
BoxLayout:
    MDRaisedButton:
        text: "Click me!"
        on_release: print("Hi!")
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()