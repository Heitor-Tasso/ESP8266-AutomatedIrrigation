
from kivy.lang import Builder
from uix.popup import BoxPopup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty
from uix.buttons import ButtonEffect
from kivy.metrics import dp
from kivy.clock import Clock

Builder.load_string("""

#:import ToggleButtonIcon uix.icons.ToggleButtonIcon
#:import ButtonIcon uix.icons.ButtonIcon
#:import ScrollViewBar uix.scrollview.ScrollViewBar
#:import BarScroll uix.scrollview.BarScroll
#:import LabelButton uix.label.LabelButton

#:import DampedScrollEffect kivy.effects.dampedscroll.DampedScrollEffect
#:import icon utils.icon


<SectionDropDown>:
    text: 'Section Option'
    padding_x: '15dp'
    size_hint_y: None
    n_lines: 0
    d_height: 0
    on_size: self.update_content()
    text_size: self.size
    valign: 'center'
    multiline: True
    radius: [0, 0, 0, 0]

<DropDownSelect>:
    orientation: 'vertical'
    normal_height: dp(60)
    size_hint_y: None
    height: self.minimum_height
    padding: ('15dp', '0dp', '15dp', '0dp')
    text: 'DropDownSelect'
    background_color: [0, 0, 0, 0]
    radius: [0, 0, 0, 0]
    canvas:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: self.radius
    BoxLayout:
        size_hint_y: None
        height: root.normal_height
        padding: ('20dp', 0, 0, 0)
        LabelButton:
            text: root.text
            bold: True
            font_size: sp(15)
            text_size: self.size
            valign: 'center'
            multiline: True
        AnchorIcon:
            ToggleButtonIcon:
                icon_state_source: [icon('up-triangle'), icon('down-triangle')]
                on_release: root.update_content()

<Help>:
    box_background_color: hex('#002428')
    box_padding: [0, 0, 0, 0]
    box_radius: [0, 0, 0, 0]
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: None
            height: '50dp'
            AnchorIcon:
                width: 0
                padding: ('60dp', 0, 0, 0)
                ButtonIcon:
                    size: ['25dp', '25dp']
                    source: icon('return')
                    on_release: root.dismiss()
            Label:
                font_size: '20sp'
                bold: True
                text:'Bem-vindo ao Eco Plantae!'
        Label:
            size_hint_y: None
            height: '30dp'
            font_size: '15sp'
            bold: True
            text:'Qual a sua d??vida?'
        BoxLayout:
            padding: ["80dp", "35dp", "80dp", "35dp"]
            ScrollViewBar:
                id: scroll
                effect_cls: DampedScrollEffect
                BoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
                    DropDownSelect:
                        text: 'Qr Code?'
                        SectionDropDown:
                            text: 'Esse App foi desenvolvido para atingir seu tempo'
                        SectionDropDown:
                        SectionDropDown:
                        SectionDropDown:
                    DropDownSelect:
                        text: 'Como funciona os sensores?'
                        SectionDropDown:
                            text: 'Qr Code?'
                        SectionDropDown:
                    DropDownSelect:
                        text: 'O que as cores no gr??fico indica?'
                        SectionDropDown:
                        SectionDropDown:
                    DropDownSelect:
                        text: 'Quais os tipos de planta est??o dispon??veis no banco de dados?'
                        SectionDropDown:
                        SectionDropDown:
                    DropDownSelect:
                        text: 'Como trocar de planta?'
                        SectionDropDown:
                        SectionDropDown:
                    DropDownSelect:
                        text: 'Como descobrir a ordem da minha planta?'
                        SectionDropDown:
                        SectionDropDown:
                    DropDownSelect:
                        text: 'Quais cuidados devo ter com o prot??tipo?'
                        SectionDropDown:
                        SectionDropDown:
            BarScroll:
                scroll_view: scroll
                radius: [dp(5), dp(5), dp(5), dp(5)]
                bar_radius: [dp(3)]
                bar_width: dp(7)
                width: '15dp'
""")


class Help(BoxPopup):
    def __init__(self, **kw):
        super().__init__(**kw)

class SectionDropDown(ButtonEffect):
    n_lines = NumericProperty(0)
    d_height = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.update_content)

    def on_parent(self, *args):
        Clock.schedule_once(self.update_content)

    def update_content(self, *args):
        if self._label._cached_lines:
            self.n_lines = len(self._label._cached_lines)
            self.d_height = self._label._cached_lines[0].h
        self.height = max((self.d_height*self.n_lines)+dp(30), dp(40))

class DropDownSelect(BoxLayout):
    
    filds = ListProperty([])
    background_color = ListProperty([0, 0, 0, 0])
    radius = ListProperty([0, 0, 0, 0])
    opened = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        self.filds = self.children[0:-1]
        set(map(self.remove_widget, self.filds))

    def update_content(self, *args):
        if self.opened:
            set(map(self.remove_widget, self.filds))
            self.opened = False
            return None
        
        set(map(self.add_widget, reversed(self.filds)))
        self.filds[-1].radius = [0, 0, dp(10), dp(10)]
        self.filds[0].radius = [dp(10), dp(10), 0, 0]
        self.opened = True

