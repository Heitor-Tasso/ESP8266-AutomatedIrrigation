
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from threading import Thread

Builder.load_string("""

#:import IconInput uix.inputs.IconInput
#:import ButtonEffect uix.buttons.ButtonEffect
#:import ButtonIcon uix.icons.ButtonIcon
#:import LabelButton uix.label.LabelButton

#:import icon utils.icon

<Login>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        canvas:
            Color:
                rgba: hex('#2f3d46')
            Rectangle:
                size: self.size
                pos: self.pos
        ScreenManager:
            id: principal_manager
            size_hint: [None, None]
            size: [root.width/1.8, root.height/1.1]
            on_size: root.size_login(self, args[1])
            canvas:
                Color:
                    rgba: hex('#25333d')
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [dp(20), dp(20), dp(20), dp(20)]
            Screen:
                name:'Login'
                BoxLayout:
                    orientation: 'vertical'
                    padding: ('0dp', '30dp', '0dp', '0dp')
                    Widget:
                        size_hint_y: 0.25
                    Label:
                        text: 'Login'
                        font_size: '30sp'
                        size_hint_y: None
                        height: self.texture_size[1]
                    Widget:
                        size_hint_y: None
                        height: '30dp'
                    AnchorLayout:
                        size_hint_y: None
                        height: '180dp'
                        on_size:
                            self.padding = [self.width/9,dp(10),self.width/9,10] if \
                            self.width >= dp(600) else [dp(20), dp(10), dp(20), dp(10)]
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: '10dp'
                            IconInput:
                                id: input
                                radius: [0, 0, 0, 0]
                                icon_left_source: icon('user')
                                icon_left_size: [dp(30), dp(25)]
                                line_color: hex('#749f9d')
                                label_text: 'E-mail'
                                label_pos_color: green
                                on_enter: root.start_thread_login()
                                input_height: dp(55)
                            Widget:
                            IconInput:
                                radius: [0, 0, 0, 0]
                                icon_left_source: icon('password')
                                icon_left_size: [dp(30), dp(25)]
                                line_color: hex('#749f9d')
                                label_text: 'Senha'
                                label_pos_color: green
                                input_height: dp(55)

                    Widget:
                        size_hint_y: None
                        height: '30dp'
                    AnchorLayout:
                        size_hint_y: None
                        height: '40dp'
                        anchor_x: 'center'
                        ButtonEffect:
                            text: 'LOGIN'
                            size_hint_x: None
                            width: '150dp'
                            background_color: [hex('#697f83'), hex('#5c636b')]
                            color_line: [clear_white, white]
                            color_effect: light_gray
                            color_text: [1, 1, 1, 1]
                            radius: [0, 0, 0, 0]
                            on_press: root.parent.current = root.parent.next()
                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'
                        padding: ('0dp', '15dp', '0dp', '0dp')
                        BoxLayout:
                            id: cont
                            size_hint: [None, None]
                            size: [self.minimum_width, dp(45)]
                            padding: ('0dp', '5dp', '0dp', '0dp')
                            spacing: '20dp'
                            canvas:
                                Color:
                                    rgba: hex('#4b545c')
                                Rectangle:
                                    pos: [self.parent.x+dp(30), self.y+self.height-dp(2)]
                                    size: [principal_manager.width-dp(60), dp(2)]
                            Label:
                                text:'Você tem uma conta?'
                                size_hint_x: None
                                width: self.texture_size[0]
                            LabelButton:
                                text:'Registre aqui'
                                color: hex('#87dd9e')
                                on_release: principal_manager.current = 'SignUp'
                                size_hint_x: None
                                width: self.texture_size[0]
            Screen:
                name:'SignUp'
                BoxLayout:
                    orientation: 'vertical'
                    padding: ('0dp', '30dp', '0dp', '0dp')
                    Widget:
                        size_hint_y: 0.25
                    Label:
                        text: 'Sign Up'
                        font_size: '30sp'
                        size_hint_y: None
                        height: self.texture_size[1]
                    Widget:
                        size_hint_y: None
                        height: '30dp'
                    AnchorLayout:
                        size_hint_y: None
                        height: '180dp'
                        on_size:
                            self.padding = [self.width/9,dp(10),self.width/9,10] if \
                            self.width >= dp(600) else [dp(20), dp(10), dp(20), dp(10)]
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: '5dp'
                            IconInput:
                                id: input
                                radius: [0, 0, 0, 0]
                                icon_left_source: icon('user')
                                icon_left_size: [dp(30), dp(25)]
                                line_color: hex('#749f9d')
                                label_text: 'E-mail'
                                label_pos_color: green
                                on_enter: root.start_thread_login()
                                input_height: dp(55)
                            Widget:
                            IconInput:
                                radius: [0, 0, 0, 0]
                                icon_left_source: icon('password')
                                icon_left_size: [dp(30), dp(25)]
                                line_color: hex('#749f9d')
                                label_text: 'Senha'
                                label_pos_color: green
                                input_height: dp(55)
                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'
                        size_hint_y: None
                        height: '40dp'
                        BoxLayout:
                            size_hint: [None, None]
                            size: [self.minimum_width, dp(45)]
                            spacing: '10dp'
                            CheckBox:
                                size_hint_x: None
                                width: '25dp'
                            Label:
                                text:'Aceite nosso'
                                size_hint_x: None
                                width: self.texture_size[0]
                            LabelButton:
                                text:'Termo e condições'
                                color: hex('#87dd9e')
                                on_release: principal_manager.current = 'Login'
                                size_hint_x: None
                                width: self.texture_size[0]
                            Widget:
                    Widget:
                        size_hint_y: None
                        height: '30dp'
                    AnchorLayout:
                        size_hint_y: None
                        height: '40dp'
                        anchor_x: 'center'
                        ButtonEffect:
                            text: 'Criar Conta'
                            size_hint_x: None
                            width: '150dp'
                            background_color: [hex('#697f83'), hex('#5c636b')]
                            color_line: [clear_white, white]
                            color_effect: light_gray
                            color_text: [1, 1, 1, 1]
                            radius: [0, 0, 0, 0]
                            on_press: root.parent.current = root.parent.next()
                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'
                        padding: ('0dp', '15dp', '0dp', '0dp')
                        BoxLayout:
                            id: cont
                            size_hint: [None, None]
                            size: [self.minimum_width, dp(45)]
                            padding: ('0dp', '5dp', '0dp', '0dp')
                            spacing: '20dp'
                            canvas:
                                Color:
                                    rgba: hex('#4b545c')
                                Rectangle:
                                    pos: [self.parent.x+dp(30), self.y+self.height-dp(2)]
                                    size: [principal_manager.width-dp(60), dp(2)]
                            Label:
                                text:'Você já tem uma conta?'
                                size_hint_x: None
                                width: self.texture_size[0]
                            LabelButton:
                                text:'Faça login aqui'
                                color: hex('#87dd9e')
                                on_release: principal_manager.current = 'Login'
                                size_hint_x: None
                                width: self.texture_size[0]

""")

class Login(Screen):
    can_call_thread = False
    
    def start_thread_login(self, *args):
        if self.can_call_thread:
            return None
        
        username = self.ids.input.ids.input.text
        if not username:
            return None

        self.can_call_thread = True
        th = Thread(target=self.login_game)
        th.start()
    
    def login_game(self, *args):
        self.can_call_thread = False
    
    def size_login(self, box, size):
        w, h = size
        if w <= dp(340):
            box.width = self.width/1.2
        if h >= dp(650):
            box.height = h/1.25
