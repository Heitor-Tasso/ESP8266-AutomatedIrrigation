__all__ = ['InputIcon', 'BaseInput']

from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.properties import (
    ListProperty, NumericProperty,
    ObjectProperty, OptionProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

Builder.load_string("""

#: import ButtonIcon uix.icons.ButtonIcon

<InputIcon>:
    hide: False
    size_hint_y: None
    BoxLayout:
        id: _box_input
        canvas:
            Color:
                rgba: root._color_line
            Line:
                rounded_rectangle: (self.pos + self.size + root.radius + [100])
                width: root.line_width
        canvas.before:
            Color:
                rgba: root.background_color
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: root.radius
        AnchorLayout:
            size_hint_x: None
            width: root.icon_left_size[0] + dp(20)
            padding: ['10dp', 0, 0, 0]
            anchor_y: 'center'
            anchor_x: 'center'
            ButtonIcon:
                id: icon_left
                size_hint: [None, None]
                size: root.icon_left_size
                icon_color: root.icon_left_color
                icon_source: root.icon_left_source
                icon_state_source: root.icon_left_state_source
                color_effect: root.icon_left_effect_color

                on_press: root.dispatch('on_icon_left_press')
                on_release: root.dispatch('on_icon_left_release')
                on_cursor_enter: root.dispatch('on_icon_left_cursor_enter')
                on_cursor_leave: root.dispatch('on_icon_left_cursor_leave')
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            padding: root.input_padding
            BaseInput:
                id: input
                size_hint_y: None
                on_focus: root._dispatch_focus()
                height: self.minimum_height
                window_root: root
                background_color: [1, 1, 1, 0]
                password: root.hide
                foreground_color: root.text_input_color
                multiline: False

        AnchorLayout:
            size_hint_x: None
            width: root.icon_right_size[0] + dp(20)
            padding: [0, 0, '10dp', 0]
            anchor_y: 'center'
            anchor_x: 'center'
            ButtonIcon:
                id: icon_right
                window_root: root
                size_hint: [None, None]
                size: root.icon_right_size
                icon_state_source: root.icon_right_state_source
                icon_source: root.icon_right_source
                icon_color: root.icon_right_color
                color_effect: root.icon_right_effect_color
                
                on_press: root.dispatch('on_icon_right_press')
                on_release: root.dispatch('on_icon_right_release')
                on_cursor_enter: root.dispatch('on_icon_right_cursor_enter')
                on_cursor_leave: root.dispatch('on_icon_right_cursor_leave')
        FloatLayout:
            size_hint: [None, None]
            size: [0, 0]
            pos: [0, 0]
            Label:
                id: label
                size_hint: [None, None]
                size: self.texture_size

""")

class BaseInput(TextInput):
    window_root = ObjectProperty(None)

    def insert_text(self, substring, from_undo=False):
        self.window_root.dispatch('on_text')
        return super(BaseInput, self).insert_text(substring, from_undo=from_undo)

class InputIcon(AnchorLayout):

     #################
    # SELF PROPERTIES #
    ###################
    background_color = ListProperty([0, 0, 0, 0])
    radius = ListProperty([dp(15), dp(15), dp(15), dp(15)])
    

     #################
    # LINE PROPERTIES #
    ###################
    line_color = ObjectProperty([1, 1, 1, 1])
    line_color_required = ObjectProperty([1, 1, 1, 1])
    line_color_filed = ObjectProperty([1, 1, 1, 1])
    line_width = NumericProperty(1.01)
    _color_line = ListProperty([1, 1, 1, 1])
    label_leave_pos = ListProperty([0, 0])
    label_enter_pos = ListProperty([0, 0])


     ###########
    # ICON LEFT #
    #############
    icon_left_type = OptionProperty('toggle', options=['toggle', 'button'])
    icon_left_size = ListProperty([dp(30), dp(30)])
    icon_left_effect_color = ListProperty([0, 0, 0, 0])

    # [0, 0, 0, 0] or [[0, 0, 0, 0], [0, 0, 0, 0]] | 0: Default color AND 1: Pos color
    icon_left_color = ObjectProperty([1, 1, 1, 1])

    # '' or ['', ''] | 0: Default source AND 1: Pos source
    icon_left_source = ObjectProperty('')
    icon_left_state_source = ListProperty(['', ''])


     ############
    # ICON RIGHT #
    ##############
    icon_right_state = OptionProperty('toggle', options=['toggle', 'button'])
    icon_right_size = ListProperty([dp(30), dp(30)])
    icon_right_effect_color = ListProperty([0, 0, 0, 0])

    # [0, 0, 0, 0] or [[0, 0, 0, 0], [0, 0, 0, 0]] | 0: Default color AND 1: Pos color
    icon_right_color = ObjectProperty([1, 1, 1, 1])
    
    # '' or ['', ''] | 0: Default source AND 1: Pos source
    icon_right_source = ObjectProperty('')
    icon_right_state_source = ListProperty(['', ''])


     ##################
    # LABEL PROPERTIES #
    ####################

    # 0: In label, 1: Out label
    label_text = ObjectProperty('')
    label_color = ListProperty([1, 1, 1, 1])
    state_label = OptionProperty('in', options=['in', 'out'])
    label_padding = ListProperty([0, 0])
    label_bold = ObjectProperty(False)
    label_font_size = ObjectProperty(sp(17))


     ##################
    # INPUT PROPERTIES #
    ####################
    text_input_color = ListProperty([1, 1, 1, 1])
    input_height = NumericProperty(dp(40))
    input_padding = ListProperty([0, 0, 0, 0])


    __events__ = (
        # ICON RIGHT
        'on_icon_right_press', 'on_icon_right_release',
        'on_icon_right_cursor_enter', 'on_icon_right_cursor_leave',

        # ICON LEFT
        'on_icon_left_press', 'on_icon_left_release',
        'on_icon_left_cursor_enter', 'on_icon_left_cursor_leave',

        # INPUT
        'on_press', 'on_release', 'on_text', 'on_focus'
    )

    def __init__(self, *args, **kwargs):
        events = (
            'size', 'on_restore', 'on_maximize', 'on_minimize',
            'on_draw', 'on_flip', 'on_rotate', 'on_restore', 'on_show',
        )
        [Window.bind(**{event:self.update_label}) for event in events]

        self.bind(size=self.update_label)
        self.bind(pos=self.update_label)

        super(InputIcon, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.config)

    def config(self, *args):
        self.set_properties_label(index=0)
        
        rmv_icon = self.ids._box_input.remove_widget
        if not self.icon_left_source and not self.icon_left_state_source[0]:
            rmv_icon(self.icon_left.parent)
            self.icon_left_size = [-1, -1]
        
        if not self.icon_right_source and not self.icon_right_state_source[0]:
            rmv_icon(self.icon_right.parent)
            self.icon_right_size = [-1, -1]
        
        self.update_label()

    def _dispatch_focus(self, *args):
        if self.focus:
            self.state_label = 'out'
        elif self.input.text == '':
            self.state_label = 'in'

        if isinstance(self.line_color[0], (int, float)):
            self._color_line = self.line_color
        elif not self.focus:
            self._color_line = self.line_color[0]
        else:
            self._color_line = self.line_color[1]

        self.update_label()
    
    def on_label_font_size(self, *args):
        self.update_label()
    
    def update_label(self, *args):
        # Update height to realoc label out
        self.label.font_size = self.get_font_size_label(index=1)
        self.label.texture_update()
        self.padding = [dp(10), self.label.height, dp(10), dp(10)]
        self.height = (self.input_height + self.padding[0] + self.label.height)
        
        # Verify is this function is called by callbacks or manualy
        can_animate = False
        if (len(args) == 1 and isinstance(args[0], (float, int))) or not args:
            can_animate = True

        # Check if has icon and use his pos or not
        if self.icon_left_size[0] == -1:
            x_label = (self.input.x + (self.radius[0]/2.5) + dp(5))
        elif self.state_label == 'out':
            x_label = (self.x + self.padding[0] + (self.radius[0]/2.5) + dp(5))
        else:
            x_label = (self.icon_left.right + dp(10))

        if self.state_label == 'in':
            # Label out of input
            y_label = (self.input.center_y - (self.label.height/2))
            padding = self.get_padding_label(index=0)
            x_label += padding[0]
            y_label += padding[1]
            self.label_leave_pos = [x_label, y_label]
            font_size = self.get_font_size_label(index=0)
            self.set_properties_label(index=0)
        else:
            # Label in input
            y_label = (self.top-self.padding[1]+dp(3))
            padding = self.get_padding_label(index=1)
            x_label += padding[1]
            y_label += padding[1]
            self.label_enter_pos = [x_label, y_label]
            font_size = self.get_font_size_label(index=1)
            self.set_properties_label(index=1)

        if can_animate:
            anim = Animation(
                pos=[x_label, y_label],
                font_size=font_size,
                d=0.2, t='out_sine')
            anim.start(self.label)
        else:
            # Set properties without animate to "update"
            self.label.pos = [x_label, y_label]
            self.label.font_size = font_size
        self.label.texture_update()

    def get_padding_label(self, index):
        if isinstance(self.label_padding[0], (int, float)):
            return self.label_padding
        else:
            return self.label_padding[index]
    
    def get_font_size_label(self, index):
        if isinstance(self.label_font_size, (int, float)):
            return self.label_font_size
        else:
            return self.label_font_size[index]

    def set_properties_label(self, index):
        if isinstance(self.label_color[0], (int, float)):
            self.label.color = self.label_color
        else:
            self.label.color = self.label_color[index]
        
        if isinstance(self.label_text, (list, tuple)):
            self.label.text = self.label_text[index]
        else:
            self.label.text = self.label_text

        if isinstance(self.label_bold, (list, tuple)):
            self.label.bold = self.label_bold[index]
        else:
            self.label.bold = self.label_bold


    ##############
    # PROPERTIES #

    @property
    def icon_left(self):
        return self.ids.icon_left

    @property
    def icon_right(self):
        return self.ids.icon_right
    
    @property
    def label(self):
        return self.ids.label
    
    @property
    def input(self):
        return self.ids.input

    @property
    def focus(self):
        return self.input.focus
    
    @focus.setter
    def focus(self, focus):
        self.input.focus = focus


    #######################
    # PROPERTIES CALLBACK #

    def on_icon_right_press(self):
        pass
    def on_icon_right_release(self):
        pass
    def on_icon_right_cursor_enter(self, *args):
        pass
    def on_icon_right_cursor_leave(self, *args):
        pass

    def on_icon_left_press(self):
        pass
    def on_icon_left_release(self):
        pass
    def on_icon_left_cursor_enter(self, *args):
        pass
    def on_icon_left_cursor_leave(self, *args):
        pass

    def on_press(self):
        pass
    def on_release(self):
        pass
    def on_text(self, *args):
        pass
    def on_focus(self, *args):
        pass
        

if __name__ == '__main__':
    KV = """
    BoxLayout:
        orientation:'vertical'
        InputIcon:
        InputIcon:
            label_text: 'Fixed Text'
            radius: [0]
        InputIcon:
            label_text: 'Fixed Text'
        InputIcon:
            background_color: [0.1, 0, 0.3, 1]
            line_color: [[0, 0.4, 0, 1], [1, 1, 1, 1]]
            label_text: 'Some Text'
            
            icon_left_source: ['assets/icons/kivy_logo.png', 'assets/icons/close.png']
            icon_left_color: [[0, 1, 0, 1], [1, 0, 0, 1]]
            icon_left_type: 'button'

            icon_right_state_source: ['assets/icons/close.png', 'assets/icons/kivy_logo.png']
            icon_right_color: [[0, 1, 0, 1], [1, 0, 0, 1]]
            icon_right_size: [dp(30), dp(30)]
            icon_right_state: 'button'
    """
    class Example(App):
        def build(self):
            return Builder.load_string(KV)
    Example().run()

