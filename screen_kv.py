screen_helper = """
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

Screen:
    BoxLayout:
        orientation: "vertical" 
        spacing: 10
        MDToolbar:
            id: toolbar
            title: "APP controle  Carro"
            md_bg_color: app.theme_cls.primary_color
            background_palette: "Primary"
            background_hue: "500"
            elevation: 10
        BoxLayout:
            orientation: "vertical"
            padding: 10
            spacing: 10
            MDRaisedButton:
                text: "Incluir"
            
    WindowManager:
        id: main_screen_manager 
        MenuScreem:
            id: menu
        LoginScreen:
            id: login
        TaskScreen:
            id: task
        UserScreem:
            id: user
        FailedLoginScreen:
            id: failed    

<WindowManager>:
    transition: SlideTransition(direction='right') #<-- Im getting error with this
    


<MenuScreem>: 
    name: 'menu'
    BoxLayout:
        orientation: "vertical"
        GridLayout:
            cols: 2
            padding: 100
            spacing: 10
            MDRectangleFlatButton:
                text: "Login"
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 1 
                    root.manager.current = 'login' 
            MDRectangleFlatButton:
                text: 'User'
                on_press: 
                    root.manager.transition = SlideTransition(direction='right')
                    root.manager.transition.duration = 1 
                    root.manager.current = 'user'  
            MDRectangleFlatButton:
                text: "Task"
                on_press: root.manager.current = 'task'
            MDRectangleFlatButton:
                text: 'Menu'
                on_press: root.manager.current = 'menu'  
   
<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: "vertical"
        GridLayout:
            rows: 4
            cols: 1
            padding: 80
            spacing: 5
            row_default_height: 30
            MDTextField:
                hint_text: "Email"
                id: loginnamevalue
            MDTextField:
                hint_text: "Password"
                id: loginpasswordvalue
                password: True
            MDRectangleFlatButton:
                text: "Login"
                on_press: root.login_button_action()
            MDRectangleFlatButton:
                text: 'profile'
                on_press: root.manager.current = 'menu'    

<UserScreem>:
    name: 'user'
    BoxLayout:
        orientation: "vertical"
        GridLayout:
            rows: 5
            cols: 1
            padding: 80
            spacing: 5
            row_default_height: 30
            MDTextField:
                hint_text: "Name"
                id: usernamevalue
            MDTextField:
                hint_text: "Email"
                id: useremailvalue
            MDTextField:
                hint_text: "Password"
                id: userpasswordvalue
                password: True
            MDRectangleFlatButton:
                text: "Gravar"
                on_press: root.user_button_action()
            MDRectangleFlatButton:
                text: 'Cancelar'
                on_press: root.manager.current = 'menu'  


<TaskScreen>:
    name: 'task'
    BoxLayout:
        orientation: "vertical"
        padding: 60
        spacing: 0
        ScrollView:
            MDList:
                id: tasklist
                padding: 5

<FailedLoginScreen>:
    name: "failed"
    BoxLayout:
        orientation: "vertical"
        padding: 10
        spacing: 10
        MDLabel:
            text: "Login Failed sdsd "
        MDRectangleFlatButton:
            text: 'Back To Login'
            on_press: root.manager.current = 'login'


"""
