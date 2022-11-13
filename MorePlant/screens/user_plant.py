
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
#:import ColoredBoxLayout uix.boxlayout.ColoredBoxLayout

#:import icon utils.icon
#:import image utils.image

#:import CircularProgressBar uix.circular_bar.CircularProgressBar
#:import Pesquisa screens.pesquisa.Pesquisa
#:import Help screens.help.Help
#:import QRCode uix.camera.QRCode
#:import PlantCamera uix.camera.PlantCamera
#:import Label kivy.core.text.Label
#:import LabelToScroll uix.label.LabelToScroll

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
        ColoredBoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            width: root.box_widths[0]
            id: box_icons
            background_color: hex('#1e1c2a')
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
                    on_release: Pesquisa().open()
            AnchorIcon:
                size_hint_y: None
                height: '70dp'
                width: self.parent.width
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('help')
                    on_release: Help().open()
            Widget:

        ColoredBoxLayout:
            orientation: 'vertical'
            background_color: hex('#038c73')

            BoxLayout:
                id: box_mid
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '15dp'
                    size_hint_x: 0.7
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        padding: [0, dp(20), dp(10), 0]
                        BoxLayout:
                            orientation:'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            LabelToScroll:
                                text: 'ECO'
                                halign: 'center'
                                bold: True
                                font_size: '22sp'
                            LabelToScroll:
                                text: 'Plantae'
                                halign: 'center'
                                bold: True
                                font_size: '17sp'

                        ColoredBoxLayout:
                            size_hint: [None, None]
                            size: [self.minimum_width, '40dp']
                            background_color: hex('#cbd7ce')
                            radius: [dp(15), dp(15), dp(15), dp(15)]
                            padding: ('10dp', '0dp', '10dp', '0dp')
                            AnchorIcon:
                                width: '50dp'
                                ButtonIcon:
                                    size: ['35dp', '35dp']
                                    source: icon('camera')
                                    on_release: PlantCamera().open()
                            AnchorIcon:
                                width: '50dp'
                                ButtonIcon:
                                    size: ['35dp', '35dp']
                                    source: icon('qrcode')
                                    on_release: QRCode().open()
                    Image:
                        source: image('plant-2', 'png')
                        id: plant_image
                        spacing: '40dp'
                        padding: ('20dp', '35dp', '20dp', '0dp')

                AnchorLayout:
                    anchor_y: 'center'
                    anchor_x: 'center'
                    padding: [dp(15), 0, dp(30), 0]
                    ColoredBoxLayout:
                        padding: ('20dp', '20dp', '20dp', '20dp')
                        size_hint_y: None
                        height: self.minimum_height
                        background_color: hex('#26201a')
                        radius: [self.height/8]
                        orientation: 'vertical'
                        spacing: '20dp'
                        LabelToScroll:
                            text:'Dados da Planta:'
                            halign: 'left'
                        LabelToScroll:
                            default_text: '{}'
                            halign: 'left'
                            padding_x: dp(40)
                            id: plant_description
                        
                        LabelToScroll:
                            default_text: 'Nome: {}'
                            id: plant_name
                            halign: 'left'
                        LabelToScroll:
                            default_text: 'Idade: {}'
                            id: plant_years
                            halign: 'left'
                        LabelToScroll:
                            default_text: 'Família: {}'
                            id: plant_family
                            halign: 'left'
                        LabelToScroll:
                            default_text: 'Gênero: {}'
                            id: plant_genre
                            halign: 'left'

            ColoredBoxLayout:
                size_hint_y: None
                height: '30dp'
                background_color: hex('#2c2c2c')
                radius: [dp(10), dp(10), 0, 0]
                OptionLabel:
                    text: 'IP: 198.012.02.1'
                    color: hex('#ebeef2')
                    text_size: self.size
                    halign: 'center'
                    valign: 'center'
            ColoredBoxLayout:
                size_hint_y: None
                height: '170dp'
                background_color: hex('#014034')
                padding: [0, dp(15), 0, 0]
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
            self.ids.box_mid.padding = [self.box_widths[0], 0, 0, 0]
            return None
        
        self.ids.box_icons.width = self.box_widths[0]
        self.ids.box_mid.padding = [0, 0, 0, 0]
    
    def config_description(self, text, *args):
        option_label = self.ids.plant_description
        option_label.text = '\n'.join(map(lambda x: f"    {x}", text.split("\n")))
