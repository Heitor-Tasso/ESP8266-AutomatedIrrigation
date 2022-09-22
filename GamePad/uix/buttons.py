
__all__ = ['ButtonEffect', 'ButtonDropDown']

from kivy.properties import ObjectProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.clock import Clock

from .behaviors.touch_effecs import EffectBehavior
from .behaviors.button import ButtonBehavior
from .behaviors.hover import HoverBehavior
from uix.floatlayout import FloatContent
from kivy.uix.button import Button
from kivy.uix.label import Label


Builder.load_string("""

<ButtonEffect>:
    background_color:[1, 1, 1, 0]
    radius: [0, 0, 0, 0]
    canvas.before:
        Color:
            rgba:self.background
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius or [0]
    canvas.after:
        Color:
            rgba:self.background_line
        Line:
            rounded_rectangle:(self.pos + self.size + self.radius + [100])
            width:self.width_line

<ButtonDropDown>:
    size_hint_x: None
    width: '70dp'
    halign: 'center'
    background_color: [0, 0, 0, 0]
    color_back_line: [0, 0, 0, 0]
    canvas.after:
        Color:
            rgba: self.color_back_line
        Rectangle:
            size: ((self.texture_size[0]+dp(15)), dp(3))
            pos: (self.x+(self.width/2)-((self.texture_size[0]+dp(15))/2)), (0 if self.parent is None else self.parent.y+dp(3))

""", filename="buttons.kv")

class ButtonEffect(ButtonBehavior, Label, EffectBehavior, HoverBehavior):
    #Colors
    background_line = ListProperty([0, 0, 0, 0])
    background = ListProperty([0, 0, 0, 0])
    
    down_color_text = ListProperty([0, 0, 0, 0])
    down_color_line = ListProperty([0, 0, 0, 0])

    background_color = ListProperty([[0.05, 0.0, 0.4, 1], [0.0625, 0.0, 0.5, 1]])
    color_line = ListProperty([[1, 1, 1, 1], [0.8, 0.925, 1, 1]])
    color_text = ListProperty([[1, 1, 1, 1], [0.8, 0.925, 1, 1]])

    duration_back = NumericProperty(0.2)

    #Sizes
    width_line = NumericProperty(1.01)
    _pressed = False

    def __init__(self, **kwargs):
        self.bind(
            background_color=self.set_color,
            color_line=self.set_color,
            color_text=self.set_color)
        self.type_button = 'rounded'
        super(ButtonEffect, self).__init__(**kwargs)
        Clock.schedule_once(self.set_color)
    
    def set_color(self, *args):
        self.background = self.get_color(self.background_color, 0)
        self.background_line = self.get_color(self.color_line, 0)
        self.color = self.get_color(self.color_text, 0)
    
    def get_color(self, object, index):
        if isinstance(object, (list, tuple)):
            if len(object) == 2 and index > -1 and index < 3:
                return object[index]
        return object


    def set_pressed(self, *args):
        if self.down_color_text[-1] != 0:
            self.color = self.down_color_text
        if self.down_color_line[-1] != 0:
            self.background_line = self.down_color_line

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False

        Animation.cancel_all(self, 'color', 'background_line')
        self.set_pressed()
        
        touch.grab(self)
        self.ripple_show(touch)
        self._pressed = True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_fade()
        
        if not self.collide_point(*touch.pos):
            return False
        
        anim = Animation(
            color=self.get_color(self.color_text, 1),
            background_line=self.get_color(self.color_line, 1),
            t=self.transition_out,
            duration=self.duration_out)
        anim.bind(on_complete=self.on_touch_anim_end)
        anim.start(self)
        return super().on_touch_up(touch)

    def on_touch_anim_end(self, *args):
        self._pressed = False
        self.new_dispatch()
        self.hover_visible = True

    def on_cursor_enter(self, *args):
        if not self._pressed:
            self.background_line = self.get_color(self.color_line, 1)
            self.color = self.get_color(self.color_text, 1)
        anim = Animation(
            background=self.get_color(self.background_color, 1),
            d=self.duration_back, t='out_quad')
        anim.start(self)
        return super().on_cursor_enter(*args)

    def on_cursor_leave(self, *args):
        anim = Animation(
            background=self.get_color(self.background_color, 0),
            d=self.duration_back, t='out_quad')
        anim.start(self)
        if not self._pressed:
            self.color = self.get_color(self.color_text, 0)
            self.background_line = self.get_color(self.color_line, 0)
        return super().on_cursor_leave(*args)

class ButtonDropDown(Button, HoverBehavior):
    content = ObjectProperty(None)
    opened = ObjectProperty(False)
    color_back_line = ListProperty([0, 0, 0, 0])
    down_quit = True
    repeat_callback = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.update_content)
        self.bind(pos=self.update_content)
        Clock.schedule_once(self.start)
    
    def start(self, *args):
        if not self.children:
            return None
        
        if len(self.children) > 1:
            raise IndexError('ButtonDropDown pode ter somente um Widget pai')

        wid = self.children[0]
        self.remove_widget(wid)
        self.content = FloatContent()
        self.content.add_widget(wid)
        self.update_content()

    def update_content(self, *args):
        if self.content is None:
            return None
        
        _win = self.get_parent_window()
        if _win is None:
            return None
        
        root_w, root_h = self.content.content.size
        sx, sy = self.to_window(*self.pos)
        root_y = (sy - root_h)
        root_x = (sx + (self.width/2) - (root_w/2))
        if (root_x + root_w) > _win.width:
            root_x = (_win.width - root_w)
        
        self.content.content.pos = (root_x, root_y)

    def on_cursor_enter(self, *args):
        if not self.opened and not self.down_quit:
            self.opened = True
            Clock.schedule_once(self.open, 0.5)
        return super().on_cursor_enter(*args)

    def on_cursor_leave(self, *args):
        if self.opened:
            collide = self.content.content.collide_point
            if not collide(*self.content.content.to_window(*self.cursor_pos)):
                self.dismiss()
        else:
            Clock.unschedule(self.open)
            self.opened = False
            self.down_quit = False
        return super().on_cursor_leave(*args)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            collide = self.content.content.collide_point
            if not collide(*self.content.content.to_window(*touch.pos)):
                self.dismiss()
                self.down_quit = True
            return False
        
        if self.down_quit and not self.opened:
            self.open()
            self.down_quit = False
        elif self.opened:
            self.dismiss()
            self.down_quit = True
        return super().on_touch_down(touch)

    def dismiss(self, *args):
        _win = self.get_parent_window()
        if _win is None:
            return None

        self.opened = False
        _win.remove_widget(self.content)
        self.color_back_line = [0, 0, 0, 0]

    def open(self, *args):
        _win = self.get_parent_window()
        if _win is None:
            return None

        if self.content in _win.children:
            self.dismiss()
            return None
        
        _win.add_widget(self.content)
        self.opened = True
        self.color_back_line = get_color_from_hex('#34FF00')
