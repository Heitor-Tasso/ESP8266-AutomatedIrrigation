
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

import socket
from threading import Thread

Builder.load_string("""

#:import IconInput uix.inputs.IconInput
#:import ButtonEffect uix.buttons.ButtonEffect
#:import ButtonIcon uix.icons.ButtonIcon

#:import icon utils.icon

<Login>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        canvas:
            Color:
                rgba: mid_gray
            Rectangle:
                size: self.size
                pos: self.pos
        BoxLayout:
            orientation: 'vertical'
            padding: ('0dp', '30dp', '0dp', '0dp')
            id: box_principal
            size_hint: [None, None]
            size: [root.width/1.8, root.height/1.1]
            on_size: root.size_login(self, args[1])
            canvas:
                Color:
                    rgba: light_gray
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [dp(20), dp(20), dp(20), dp(20)]
            Widget:
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
                        radius: [dp(8), dp(8), dp(8), dp(8)]
                        icon_left_source: icon('user')
                        icon_left_size: [dp(30), dp(25)]
                        label_text: 'Nome da Planta'
                        label_pos_color: green
                        on_enter: root.start_thread_login()
                    Widget:
                    IconInput:
                        radius: [dp(8), dp(8), dp(8), dp(8)]
                        icon_left_source: icon('password')
                        icon_left_size: [dp(30), dp(25)]
                        label_pos_color: green
                        label_text: 'IP do Produto'

            Widget:
                size_hint_y: None
                height: '30dp'
            AnchorLayout:
                size_hint_y: None
                height: '40dp'
                anchor_x: 'center'
                ButtonEffect:
                    text: 'Next'
                    size_hint_x: None
                    width: '150dp'
                    background_color: [0, 0, 0, 0]
                    color_line: [clear_white, white]
                    color_effect: light_gray
                    radius: [dp(15), dp(15), dp(15), dp(15)]
                    on_press: root.parent.current = root.parent.next()
            Widget:

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
