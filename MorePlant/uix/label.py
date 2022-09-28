
from uix.behaviors.button import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty

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

""")

class LabelBottomStroke(ToggleButtonBehavior, Label):
    color_back_line = ListProperty([0, 0, 0, 0])

    def on_state(self, *args):
        if self.state == 'down':
            self.color_back_line = get_color_from_hex('#34FF00')
        else:
            self.color_back_line = [0, 0, 0, 0]