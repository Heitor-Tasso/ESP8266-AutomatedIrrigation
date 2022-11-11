
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty
from uix.triggers import BTrigger
from random import randint

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
    text: "{}%"
    value: 0
    max: 100
    on_size: circular_bar._draw()
    on_pos: circular_bar._draw()
    on_kv_post: Window.bind(on_flip=lambda *a: circular_bar._draw())

    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: max(label.width, flt_bar.width), self.minimum_height
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            size_hint_y: None
            height: '110dp'
            FloatLayout:
                id: flt_bar
                size_hint_x: None
                width: '120dp'
                CircularProgressBar:
                    id: circular_bar
                    cap_style: "SqUArE"
                    thickness: 5
                    progress_colour: hex('#ffffff')
                    background_colour: hex('#702963')
                    background: 
                        hex('#C41E3A') if root.value < root.max/3 else (\
                        hex('#FFC300') if root.value < root.max/1.5 else hex('#1DB954'))
                    cap_precision: 100
                    max: root.max
                    value: root.value
                    widget_size: round(self.parent.width)
                    pos: self.parent.pos
                    label: Label(text=root.text, font_size=sp(20))
        OptionLabel:
            id: label
            text: root.name
            halign: 'center'
            color: [1, 1, 1, 1]

<UserPlant>:
    box_widths: [dp(50), 0]
    BoxLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            width: root.box_widths[0]
            id: box_icons
            canvas.before:
                Color:
                    rgba: hex('#1e1c2a')
                Rectangle:
                    pos: self.pos
                    size: self.size
        
            Widget:
                size_hint_y: None
                height: '70dp'
            
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('home-boll')
                    on_release: root.manager.current = "login"
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('search')
                    on_release: root.manager.current = "pesquisa"
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('help')
                    on_release: root.manager.current = "help"
            Widget:

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
                id: top_box
                BoxLayout:
                    size_hint: [None, None]
                    size: [self.minimum_width, '40dp']
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
                    source: image('plant-2', 'png')
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
                height: '20dp'
                canvas.before:
                    Color:
                        rgba: hex('#c1d6fa')
                    Rectangle:
                        pos: self.pos
                        size: self.size
                AnchorLayout:
                    anchor_y: 'center'
                    padding_x: '30dp'
                    OptionLabel:
                        text: 'IP:'
                        color: [0, 0, 0, 1]
            BoxLayout:
                size_hint_y: None
                height: '180dp'
                canvas.before:
                    Color:
                        rgba: hex('#4b548a')
                    Rectangle:
                        pos: self.pos
                        size: self.size
                
                GraphicCircular:
                    name: "Temperatura"
                    text: "{} °C"
                    id: celsius_graph
                    max: 60

                GraphicCircular:
                    name: "Umidade"
                    text: "{} g/m³"
                    id: humidity_graph
                    max: 100

                GraphicCircular:
                    name: "Luminosidade"
                    text: "{} Lux"
                    id: lux_graph
                    max: 800
        FloatLayout:
            size_hint: None, None
            size: 0, 0
            AnchorIcon:
                size_hint_y: None
                size: root.box_widths[0], '70dp'
                pos: root.x, box_icons.y+box_icons.height-self.height
                ToggleButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('box-options')
                    on_state: root.change_bar(self)

""")

class GraphicCircular(AnchorLayout):
    
    value = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        function = self.ids.circular_bar._draw
        BTrigger(function, 10, 0.2).start()


class UserPlant(Screen):

    box_widths = ListProperty([0, 0])

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.start)

    def start(self, *args):
        self.change_graph()
        Clock.schedule_interval(self.change_graph, 3)
        
    
    def change_graph(self, *args):
        anim1 = Animation(value=randint(0, self.ids.lux_graph.max), d=1)
        anim1.start(self.ids.lux_graph)
        
        anim2 = Animation(value=randint(0, self.ids.celsius_graph.max), d=1.5)
        anim2.start(self.ids.celsius_graph)
        
        anim2 = Animation(value=randint(0, self.ids.humidity_graph.max), d=2)
        anim2.start(self.ids.humidity_graph)

    def change_bar(self, toggle_icon):
        if toggle_icon.state == 'down':
            self.ids.box_icons.width = self.box_widths[1]
            self.ids.top_box.padding[0] += self.box_widths[0]
            return None
        
        self.ids.box_icons.width = self.box_widths[0]
        self.ids.top_box.padding[0] -= self.box_widths[0]
        
