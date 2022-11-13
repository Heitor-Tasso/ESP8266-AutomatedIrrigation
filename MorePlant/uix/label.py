
from uix.behaviors.button import ToggleButtonBehavior, ButtonBehavior
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.core.text.markup import MarkupLabel as CoreLabel

Builder.load_string("""

<LabelBottomStroke>:
    halign: 'center'
    background_color: [0, 0, 0, 0]
    color_back_line: [0, 0, 0, 0]
    canvas.after:
        Color:
            rgba: self.color_back_line
        Rectangle:
            size: [(self.texture_size[0]+dp(15)), dp(3)]
            pos:
                [\
                (self.x+(self.width/2)-((self.texture_size[0]+dp(15))/2)), \
                (0 if self.parent is None else self.parent.y+dp(3))\
                ]

<LabelButton>:
    color: [1, 1, 1, 1]

<LabelToScroll>:
    text: 'Section Option'
    padding_x: '15dp'
    size_hint_y: None
    on_size: self.update_content()
    text_size: self.size
    valign: 'center'
    halign: 'center'
    multiline: True


""")

class LabelBottomStroke(ToggleButtonBehavior, Label):
    color_back_line = ListProperty([0, 0, 0, 0])

    def on_state(self, *args):
        if self.state == 'down':
            self.color_back_line = get_color_from_hex('#34FF00')
        else:
            self.color_back_line = [0, 0, 0, 0]
    
class LabelButton(ButtonBehavior, Label):
    pass

class LabelToScroll(Label):
    n_lines = NumericProperty(0)
    d_height = NumericProperty(0)

    def update_content(self, *args):
        kw = self._label.options.copy()
        kw['text'] = self.text
        kw['text_size'] = [self.text_size[0], None]
        lb = CoreLabel(**kw)
        lb.refresh()
        self.height = lb.texture.size[1]
