from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import (MDExpansionPanel,
                                       MDExpansionPanelThreeLine)
from kivymd.uix.snackbar import Snackbar

from controller import controller

# Window.size = (700, 700)


class DashBoard(Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CategoriaScreem(Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snackbar = None

    def inserir_categoria(self):
        """
            data: paramentros de insert
        """
        LOADING.open()
        controller.add_category({
            'name': self.ids.txt_cat_name.text,
            'sub_name':  self.ids.txt_cat_sub_name.text,
        })

        if not self.snackbar:
            self.snackbar = Snackbar(
                text="Registro Incluido com sucesso !")
            self.snackbar.show()
            LOADING.dismiss()
        self.snackbar = None

        print(self.ids.keys())
        print(self.ids.txt_cat_name.text)
        # print(self.root.ids.categoria_screen.txt_cat_name.text)
        # print(root.categoria_screen.txt_cat_name.text)

        # app.progress_start():

        # app.progress_end():
        # LOADING.dismiss()


class Registration(Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LoginScreen(Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def authenticate(self):
        LOADING.open()

    def forgot_password(self):
        LOADING.open()

    def reset_register_form(self):
        #registration = self.root.ids.registration
        # registration.ids.reg_carousel.load_next(mode="next")
        LOADING.open()


class PincipalScreen(Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def reset_login_form(self):
        man = self.root.ids.screen_manager
        man.current = 'login'


class FormSnack (Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PanelImage(Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LoginForm(Screen):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snackbar = None
        self._interval = 0

    def build(self):
        self.ids.car_nome_text.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        # return self.screen

    def set_error_message(self, instance_textfield):
        self.ids.car_nome_text.error = True

    def wait_interval(self, interval):
        self._interval += interval
        if self._interval > self.snackbar.duration + 0.5:
            anim = Animation(y=dp(10), d=.2)
            anim.start(self.ids.button)
            Clock.unschedule(self.wait_interval)
            self._interval = 0
            self.snackbar = None

    def snackbar_show(self):
        if not self.snackbar:
            self.snackbar = Snackbar(text="This is a snackbar!")
            # self.snackbar.open()
            self.snackbar.show()
            anim = Animation(y=dp(72), d=.2)
            anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                self.wait_interval, 0))
            anim.start(self.ids.button)

    def check_data_login(self):
        if not self.snackbar:
            self.snackbar = Snackbar(text="estou na LoginForm!")
            # self.snackbar.open()
            self.snackbar.show()
            anim = Animation(y=dp(72), d=.2)
            anim.bind(on_complete=lambda *args: Clock.schedule_interval(
                self.wait_interval, 0))
            anim.start(self.ids.button)


class Loading(BoxLayout):

    def __init__(self, **kwargs):
        super(Loading, self).__init__(**kwargs)
        self.padding = '7dp'
        self.orientation = 'vertical'
        loading_image = Image(source='images/gnome.jpeg')
        self.add_widget(loading_image)


LOADING = Popup(title='Loading ...', content=Loading(),
                size_hint=(None, None), size=('169dp', '144dp'))


class Lavanderia(MDApp):
    background_color = ListProperty((0, 0, 1, .45))

    def __init__(self, **kwargs):
        super(Lavanderia, self).__init__(**kwargs)
        # self.screen_manager = ObjectProperty(None)
        # self.sql = SQLDatabase()
        self.title = "Texto Titulo"
        # self.theme_cls.primary_palette = "LightBlue"
        # self.theme_cls.theme_style = "Dark"  # "Light"
        # self.size = (700, 700)

    def build(self):

        return Builder.load_file("main.kv")

    def next_login(self):
        # screen_manager.current = 'login'
        # self.parent.ids.screen_manager.current = 'login'
        man = self.root.ids.screen_manager
        man.current = 'login'

    def proximo(self):
        dashboard = self.root.ids.dashboard
        carousel = dashboard.ids.carousel
        carousel.load_next(mode="proximo")
        # Same as
        # self.root.ids.dashboard.ids.carousel.load_next(mode="proximo")

    def fecharApp(self):
        self.stop()  # Fecha Aplicativo

    def next_card(self):

        registration = self.root.ids.registration

        print(registration.ids.keys())
        print(self.root.ids.keys())
        registration.ids.reg_carousel.load_next(mode="next")
        registration.ids.re_name_carousel.text_color = self.theme_cls.primary_color
        registration.ids.progress_one.value = 100
        registration.ids.re_name_button.text_color = self.theme_cls.primary_color
        registration.ids.re_name_button.icon = "check-decagram"

    def next_card_one(self):
        registration = self.root.ids.registration
        print(registration.ids.keys())
        print(self.root.ids.keys())

        registration.ids.reg_carousel.load_next(mode="next")
        registration.ids.re_contact_carousel.text_color = self.theme_cls.primary_color
        registration.ids.progress_two.value = 100
        registration.ids.re_contact_button.text_color = self.theme_cls.primary_color
        registration.ids.re_contact_button.icon = "check-decagram"

    def previous_card(self):
        registration = self.root.ids.registration
        registration.ids.reg_carousel.load_previous()
        registration.ids.re_name_carousel.text_color = 0, 0, 0, 1
        registration.ids.progress_one.value = 0
        registration.ids.re_name_button.text_color = 0, 0, 0, 1
        registration.ids.re_name_button.icon = "numeric-1-circle"

    def previous_card_one(self):
        registration = self.root.ids.registration
        registration.ids.reg_carousel.load_previous()
        self.root.ids.Contact.text_color = 0, 0, 0, 1
        self.root.ids.progress_two.value = 0
        self.root.ids.contact_button.text_color = 0, 0, 0, 1
        self.root.ids.contact_button.icon = "numeric-2-circle"

    def progress_start():
        LOADING.open()

    def progress_end():
        LOADING.dismiss()


if __name__ == '__main__':
    # Initialize database for models
    # initial_db()
    Lavanderia().run()
