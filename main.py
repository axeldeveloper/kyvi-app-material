from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class DashBoard(Screen):
    pass

class FirstScreen(Screen):
    pass

class Lavanderia(MDApp):
    def build(self):
        self.title="Texto Titulo"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file("main.kv")

    def proximo(self):
        self.root.ids.carousel.load_next(mode="proximo")# Próximo Card
    
    def fecharApp(self):
        self.stop()# Fecha Aplicativo

Lavanderia().run()