
__all__ = ['AnchorIcon', 'Icon', 'ButtonIcon', 'ToggleButtonIcon']

from .behaviors.button import ButtonBehavior, ToggleButtonBehavior
from .behaviors.touch_effecs import EffectBehavior
from .behaviors.hover import HoverBehavior

from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout

from kivy.properties import ListProperty, ObjectProperty

from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""

<AnchorIcon>:
    size_hint_x: None
    width: '70dp'
    radius: [0, 0, 0, 0]
    background_color: [0, 0, 0, 0]
    anchor_x: 'center'
    anchor_y: 'center'
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: self.radius or [0]

<Icon>:
    anchor_y: 'center'
    anchor_x: 'center'
    source: ''
    icon_size: ['30dp', '30dp']
    color: [1, 1, 1, 1]
    allow_stretch: True
    keep_ratio: False
    mipmap: True
    BoxLayout:
        padding: ['5dp', '5dp', '5dp', '5dp']
        size_hint: [None, None]
        size: root.icon_size
        Image:
            source: root.source
            allow_stretch: root.allow_stretch 
            keep_ratio: root.keep_ratio
            mipmap: root.mipmap
            color: root.color

<ButtonIcon>:
    size_hint: [None, None]
    size: ['40dp', '40dp']
    mipmap: True
    allow_strech: True
    keep_ratio: False
    canvas:
        Clear
    canvas.after:
        Color:
            rgba: self.color
        Rectangle:
            texture: self.texture
            pos: self.pos
            size: self.size

<ToggleButtonIcon>:
    size: ['30dp', '30dp']

""")

class AnchorIcon(AnchorLayout):
    background_color = ListProperty([0, 0, 0, 0])
    radius = ListProperty([0, 0, 0, 0])

class Icon(AnchorIcon):
    pass

class ButtonIcon(ButtonBehavior, Image, EffectBehavior, HoverBehavior):
    # Internal use
    _color_icon = ListProperty([1, 1, 1, 1])

    # Properties
    icon_color = ObjectProperty([1, 1, 1, 1])
    icon_source = ObjectProperty('')
    icon_state_source = ListProperty(['', ''])
    
    def __init__(self, **kwargs):
        self.type_button = 'rounded'
        super().__init__(**kwargs)
        Clock.schedule_once(self.set_color)
    
    def set_color(self, *args):
        if self.icon_source != '' and len(self.icon_source) != 2:
            self.source = self.icon_source
        elif len(self.icon_source) == 2 and '' not in self.icon_source:
            self.source = self.icon_source[0]
        elif len(self.icon_state_source) == 2 and '' not in self.icon_state_source:
            self.source = self.icon_state_source[0]
        
        if isinstance(self.icon_color[0], (int, float)):
            self.color = self.icon_color
        else:
            self.color = self.icon_color[0]
    
    def on_state(self, widget, state):
        if len(self.icon_state_source) == 2 and '' not in self.icon_state_source:
            if state == 'normal':
                self.source = self.icon_state_source[0]
            elif state == 'down':
                self.source = self.icon_state_source[1]

    def on_cursor_enter(self, *args):
        if len(self.icon_source) == 2 and '' not in self.icon_source:
            self.source = self.icon_source[1]

        if not isinstance(self.icon_color[0], (int, float)):
            self.color = self.icon_color[1]

        return super().on_cursor_enter(*args)

    def on_cursor_leave(self, *args):
        if len(self.icon_source) == 2 and '' not in self.icon_source:
            self.source = self.icon_source[0]
        
        if not isinstance(self.icon_color[0], (int, float)):
            self.color = self.icon_color[0]
            
        return super().on_cursor_leave(*args)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        
        # touch.grab(self)
        self.ripple_show(touch)
        return super().on_touch_down(touch)
        
    def on_touch_up(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        
        self.ripple_fade()
        return super().on_touch_up(touch)

class ToggleButtonIcon(ToggleButtonBehavior, ButtonIcon):
    pass

