
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.metrics import dp

from kivy.uix.widget import Widget
from kivy.uix.image import Image

Builder.load_string("""

<RoudedImage>
    source: ''
    texture:None
    radius: [dp(5), 0, 0, dp(5)]
    canvas:
        Color:
            rgba:[1, 1, 1, 1]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: root.radius
            texture: root.texture
    size_hint_x:None
    width:'70dp'

""")

class RoudedImage(Widget):
    texture = ObjectProperty(None)
    source = StringProperty('')
    radius = ListProperty([dp(5), 0, 0, dp(5)])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_texture, 1)

    def create_texture(self, *args):
        image = Image(
            source=self.source, allow_stretch=True, keep_ratio=False, 
            size_hint=(None, None), size=self.size,
        )
        self.texture = image.texture
