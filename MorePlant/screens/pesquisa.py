
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import json
from utils import get_path, image
from kivy.clock import Clock

Builder.load_string("""

#:import IconInput uix.inputs.IconInput
#:import ToggleButtonIcon uix.icons.ToggleButtonIcon
#:import ButtonIcon uix.icons.ButtonIcon
#:import ScrollViewBar uix.scrollview.ScrollViewBar
#:import BarScroll uix.scrollview.BarScroll
#:import ButtonIcon uix.icons.ButtonIcon
#:import ResizableGrid uix.grid.ResizableGrid


#:import DampedScrollEffect kivy.effects.dampedscroll.DampedScrollEffect

#:import icon utils.icon
#:import image utils.image

#:import hex kivy.utils.get_color_from_hex

<PlantCard>:
    size_hint_y: None
    height: self.width
    padding: '20dp'
    source: ''
    canvas.before:
        Color:
            rgba: hex("#43d9ca")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8), dp(8), dp(8), dp(8)]
        
        Color:
            rgba: hex("#ebeef2")
        RoundedRectangle:
            pos: self.x+dp(5), self.y+dp(5)
            size: self.width-dp(10), self.height-dp(10)
            radius: [dp(8), dp(8), dp(8), dp(8)]
    
    ButtonIcon:
        size: root.width-dp(40), root.height-dp(40)
        icon_source: root.source
        icon_color: [[1, 1, 1, 1], hex("#aeb5bf")]
        effect_color: hex("#e06031")[0:-1] + [0.7]
        radius_effect: [self.width]*4
        duration_in: 0.8
        duration_out: 0.4


<Pesquisa>:
    BoxLayout:
        orientation: 'vertical'
        padding: ['0dp', '15dp', '0dp', '0dp']
        canvas.before:
            Color:
                rgba: hex('#002428')
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text:'Escolha uma planta'
            font_size: '20sp'
            bold: True
            size_hint_y: None
            height: '60dp'
        BoxLayout:
            padding: ['20dp', '20dp', '20dp', '20dp']
            spacing: '15dp'
            ScrollViewBar:
                id: scroll
                effect_cls: DampedScrollEffect
                BoxLayout:
                    orientation: 'vertical'
                    padding: ['0dp', '15dp', '0dp', '0dp']
                    size_hint_y: None
                    height: self.minimum_height
                    ResizableGrid:
                        size_hint_y: None
                        height: self.minimum_height
                        cols: 1
                        max_size: [dp(180), dp(200)]
                        id: grid_imgs
            BarScroll:
                scroll_view: scroll
                radius: [dp(7), dp(7), dp(7), dp(7)]
                bar_radius: [dp(3)]
                bar_width: dp(7)
                width: '15dp'
        AnchorIcon:
            size_hint_y: None
            height: '70dp'
            width: self.parent.width
            ButtonIcon:
                size: ['25dp', '25dp']
                source: icon('return')
                on_release: root.manager.current = "user"
""")

class PlantCard(BoxLayout):
    source = StringProperty("")

class Pesquisa(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        for k, v in self.get_json("config.json").items():
            img = PlantCard(source=image(v['url']))
            self.ids.grid_imgs.add_widget(img)
        
    def get_json(self, name, *args):
        with open(get_path(name), 'r', encoding='utf-8') as file:
            return json.load(file)

    def update_json(self, new_json, name):
        with open(get_path(name), 'w', encoding='utf-8') as file:
            file.write(json.dumps(new_json, indent=4))
