from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


# Alert(title='oops!', text='invalid inputs')
class Alert(Popup):

    def __init__(self, title, text):
        super(Alert, self).__init__()

        content = AnchorLayout(anchor_x='center', anchor_y='bottom')

        content.add_widget(Label(text=text, halign='left', valign='top'))
        # content.add_widget(Label(text=text))

        # ok_button = Button(text='Ok', size_hint=(None, None),size=(Window.width / 9, Window.height / 9))
        # ok_button = Button(text='Ok', size_hint=(None, None), size=(256, 256))
        ok_button = Button(text='ok', size_hint_y=None, height=40)
        content.add_widget(ok_button)

        # content.add_widget(ok_button)

        popup = Popup(
            title=title,
            title_size=(30),
            title_align='center',
            content=content,
            size_hint=(None, None),
            # size=(Window.width / 3, Window.height / 3),
            size=(256, 200),
            auto_dismiss=True,
        )

        ok_button.bind(on_press=popup.dismiss)
        # content.bind(on_press=popup.dismiss)
        popup.open()
