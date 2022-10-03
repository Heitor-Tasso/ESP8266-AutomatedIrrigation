
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty
from uix.triggers import BTrigger

Builder.load_string("""

#:import IconInput uix.inputs.IconInput
#:import ButtonEffect uix.buttons.ButtonEffect
#:import ButtonIcon uix.icons.ButtonIcon

#:import icon utils.icon
#:import image utils.image

#:import CircularProgressBar uix.circular_bar.CircularProgressBar
#:import Label kivy.core.text.Label

#:import Clock kivy.clock.Clock
#:import Window kivy.core.window.Window

<OptionLabel@Label>:
    size_hint_y: None
    height: '30dp'
    text_size: self.size
    padding_y: '30dp'
    haling: 'left'
    valign: 'center'
    

<GraphicCircular>:
    anchor_x: 'center'
    anchor_y: 'center'
    name: ''
    percent: 0
    on_size: circular_bar._draw()
    on_pos: circular_bar._draw()
    on_kv_post: Window.bind(on_flip=lambda *a: circular_bar._draw())

    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: max(label.width, flt_bar.width), self.minimum_height
        AnchorLayout:
            anchor_x: 'center'
            size_hint_y: None
            height: '80dp'
            FloatLayout:
                id: flt_bar
                size_hint_x: None
                width: '90dp'
                CircularProgressBar:
                    id: circular_bar
                    cap_style: "SqUArE"
                    thickness: 5
                    progress_colour: hex('#ffffff')
                    background_colour: hex('#fec560')
                    background: hex('#383637')
                    cap_precision: 100
                    max: 10
                    value: root.percent
                    widget_size: round(self.parent.width)
                    pos: self.parent.pos
                    label: Label(text="{}%", font_size=sp(20))
        OptionLabel:
            id: label
            text: root.name
            halign: 'center'
            color: [1, 1, 1, 1]

<UserPlant>:
    BoxLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            width: '50dp'
            canvas.before:
                Color:
                    rgba: hex('#1e1c2a')
                Rectangle:
                    pos: self.pos
                    size: self.size

            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('box-options')
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('home-boll')
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('search')
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('help')
            Widget:
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('return')
                    on_release: root.manager.current = "login"

        BoxLayout:
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: hex('#002428')
                Rectangle:
                    pos: self.pos
                    size: self.size
            BoxLayout:
                padding: ('30dp', '0dp', '0dp', '0dp')
                size_hint_y: None
                height: '60dp'
                BoxLayout:
                    size_hint: [None, None]
                    size: self.minimum_width, '40dp'
                    canvas.before:
                        Color:
                            rgba: [1, 1, 1, 1]
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [dp(15), dp(15), dp(15), dp(15)]
                    AnchorIcon:
                        ButtonIcon:
                            size: ['35dp', '35dp']
                            source: icon('camera')
                            on_release: root.manager.current = "camera"
                    AnchorIcon:
                        ButtonIcon:
                            size: ['35dp', '35dp']
                            source: icon('qrcode')
                            on_release: root.manager.current = "qrcode"

                Widget:
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: None
                    width: 0 if not self.children else max(self.children[0].width, self.children[1].width)
                    OptionLabel:
                        text: 'ECO'
                        halign: 'center'
                    OptionLabel:
                        text: 'Plantae'
                        halign: 'center'
            BoxLayout:
                orientation: 'vertical'
                padding: ('40dp', '15dp', '0dp', '15dp')
                size_hint_y: None
                height: self.minimum_height
                OptionLabel:
                    text:'Dados da Planta:'
                OptionLabel:
                    text: '     Lorem Ipsum'
            BoxLayout:
                spacing: '20dp'
                padding: ['20dp', '0dp', '0dp', '0dp']
                Image:
                    source: image('PlantVase-1', 'png')
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: 0.5
                    OptionLabel:
                        text: 'Nome:'
                    OptionLabel:
                        text: 'Idade:'
                    OptionLabel:
                        text: 'Família:'
                    OptionLabel:
                        text: 'Gênero:'
                    Widget:
            Widget:
                size_hint_y: None
                height: '15dp'
            BoxLayout:
                size_hint_y: None
                height: '30dp'
                canvas.before:
                    Color:
                        rgba: hex('#c1d6fa')
                    Rectangle:
                        pos: self.pos
                        size: self.size
                AnchorLayout:
                    anchor_y: 'center'
                    OptionLabel:
                        text: 'IP:'
                        color: [0, 0, 0, 1]
            BoxLayout:
                size_hint_y: None
                height: '150dp'
                canvas.before:
                    Color:
                        rgba: hex('#4b548a')
                    Rectangle:
                        pos: self.pos
                        size: self.size

                GraphicCircular:
                    name: 'Luminosidade'
                GraphicCircular:
                    name: 'Temperatura'
                GraphicCircular:
                    name: 'Umidade'
""")

class GraphicCircular(AnchorLayout):
    
    percent = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        function = self.ids.circular_bar._draw
        BTrigger(function, 10, 0.2).start()


class UserPlant(Screen):
    pass


