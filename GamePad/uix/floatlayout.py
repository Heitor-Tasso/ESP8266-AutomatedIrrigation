
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from .behaviors.hover import HoverBehavior 


class FloatContent(FloatLayout, HoverBehavior):
    size_hint = ListProperty([None, None])
    size = ListProperty([0, 0])
    pos = ListProperty([0, 0])

    content = ObjectProperty(None)


    def on_children(self, *args):
        if not self.children:
            self.content = None
            return None
        elif len(self.children) > 1:
            raise ValueError('FloatContent accept only one Widget!!')
        
        self.content = self.children[0]

    def collide_point(self, x, y):
        if self.content is not None:
            return self.content.collide_point(x, y)
        return super().collide_point(x, y)

    # def on_touch_down(self, touch):
    #     if self.content is None:
    #         return False
            
    #     if self.collide_point(*touch.pos):    
    #         self.content.on_touch_down(touch)
    #         return True
    #     return False

    # def on_touch_up(self, touch):
    #     if self.content is None:
    #         return False

    #     if self.collide_point(*touch.pos):    
    #         self.content.on_touch_up(touch)
    #         return True
    #     return False
