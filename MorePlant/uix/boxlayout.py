
from kivy.uix.boxlayout import BoxLayout
from .behaviors.hover import HoverBehavior
from kivy.lang.builder import Builder

Builder.load_string("""

<ColoredBoxLayout>:
    background_color: [0, 0, 0, 0]
    radius: [0, 0, 0, 0]
    stroke_color: [0, 0 ,0 ,0]
    stroke_width: dp(2)
    canvas.before: 
        Color:
            rgba: self.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: self.radius or [0, 0, 0, 0]
    canvas.after:
        Color:
            rgba: self.stroke_color or [0, 0, 0, 0]
        Line:
            rounded_rectangle: [*self.pos, *self.size, *(self.radius or [0, 0, 0, 0])]
            width: self.stroke_width or dp(1)

""")

class ColoredBoxLayout(BoxLayout, HoverBehavior):
    pass
