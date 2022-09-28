from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.utils import get_color_from_hex
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp

from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget


Builder.load_string("""

<BarScroll>:
    size_hint_x: None
    width: '40dp'
    canvas.after:
        Color:
            rgba: hex('#dfe0e5')
        RoundedRectangle:
            size: [(self.bar_width*2), self.height]
            pos: [(self.x+(self.width/2)-(self.bar_width*2/2)), self.y]
            radius: [self.bar_width]
        Color:
            rgba: self._bar_color
        RoundedRectangle:
            size: [self.bar_width, self.bar_height]
            pos: [(self.x+(self.width/2)-(self.bar_width/2)), self.bar_y]
            radius: [self.bar_width/2]

<ScrollViewBar>:
    bar_color: [0, 0, 0, 0]
    bar_inactive_color: [0, 0, 0, 0]
    effect_cls: 'ScrollEffect'

""")

class ScrollViewBar(ScrollView):
    pass

class BarScroll(Widget):
    scroll_view = ObjectProperty(None)
    _last_scroll_view = None
    bar_width = NumericProperty(dp(4))
    bar_height = NumericProperty(0)
    bar_y = NumericProperty(0)
    bar_color = ListProperty(get_color_from_hex('#737373'))
    _bar_color = ListProperty([0, 0, 0, 0])
    can_scroll = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.start)
    
    def start(self, *args):
        Window.bind(on_restore=self.update_scroll)
        
        if self.scroll_view is not None:
            self._last_scroll_view = self.scroll_view
            self.scroll_view.bind(vbar=self.update_scroll)
        Clock.schedule_once(self.update_scroll)
    
    def on_scroll_view(self, *args):
        if self.scroll_view is None:
            return None
        if self._last_scroll_view is not None:
            self._last_scroll_view.unbind(vbar=self.update_scroll)
        self._last_scroll_view = self.scroll_view
        self.scroll_view.bind(vbar=self.update_scroll)
        Clock.schedule_once(self.update_scroll)

    def update_scroll(self, *args):
        if self.scroll_view is None:
            return None
        
        if self.scroll_view.height >= self.scroll_view.children[0].height:
            self._bar_color = [0, 0, 0, 0]
        else:
            self._bar_color = self.bar_color

        vy, vh = self.scroll_view._get_vbar()
        self.bar_y = self.y+(self.height*vy)
        self.bar_height = self.height*vh
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.can_scroll = True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.can_scroll:
            self.can_scroll = False
        return super().on_touch_up(touch)

    def on_touch_move(self, touch):
        if not self.can_scroll or self.scroll_view is None:
            return None
            
        height = self.scroll_view.height
        dy = touch.dy / float(max((height - height * self.scroll_view.vbar[1]), 1))
        self.scroll_view.scroll_y = float(min(max(self.scroll_view.scroll_y + dy, 0), 1))
