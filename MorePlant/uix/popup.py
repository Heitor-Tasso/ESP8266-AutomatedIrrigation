
from kivy.uix.modalview import ModalView
from uix.boxlayout import ColoredBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

Builder.load_string("""

#: import Icon uix.icons.Icon
#: import ButtonIcon uix.icons.ButtonIcon
#: import ColoredBoxLayout uix.boxlayout.ColoredBoxLayout
#: import ScrollViewBar uix.scrollview.ScrollViewBar
#: import BarScroll uix.scrollview.BarScroll
#: import InputIcon uix.input.InputIcon

#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import icon utils.path.icon

<ProjectTopBar>:
    size_hint_y: None
    height: '50dp'
    background_color: hex('#0b1426')
    radius: [dp(15), dp(15), 0, 0]
    title: ''
    screen: None
    AnchorIcon:
        Icon:
            source: icon('tool_suport')
            icon_size: '45dp', '45dp'
    Label:
        text: root.title
        size_hint_x: None
        width: self.texture_size[0]
        font_size: '17sp'
        bold: True
    
    Widget:
    AnchorIcon:
        ButtonIcon:
            icon_source: icon('close')
            size: '35dp', '35dp'
            on_release: if root.screen is not None: root.screen.close_popup()

<ScrollContentScreens>:
    ScrollViewBar:
        do_scroll_x: False
        do_scroll_y: True
        id: _scroll_examples
        GridLayout:
            cols: max(min(round(_scroll_examples.width/dp(200)), 4), 1)
            size_hint_y: None
            height: self.minimum_height
            spacing: '30dp'
            padding: ['0dp', '30dp', '0dp', '30dp']
            id: _grid_screens


<ConfigInputIcon@InputIcon>:
    label_text: ''
    line_color: [hex('b8bfc1'), hex('#06c7ff')]
    input_height: dp(30)
    radius: [dp(5)]
    label_font_size: sp(15)
    label_padding: [[dp(15), 0], [dp(-25), 0]]
    label_bold: [False, True]


<DropOptions>:
    title: ''
    padding: [0, 0, 0, dp(5)]
    spacing: dp(5)
    size_hint_y: None
    height: dp(40) + _label.height
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: hex('#6d7071')
        RoundedRectangle:
            size: [self.width, dp(1.01)]
            pos: [self.x, self.y]
            
    Label:
        id: _label
        text: root.title
        bold: True
        size_hint: [None, None]
        size: self.texture_size
        font_size: sp(13)
    AnchorLayout:
        padding: [dp(5), 0, dp(5), 0]
        ColoredBoxLayout:
            background_color: hex('#6d7071')[0:-1] + [0.7]
            radius: [dp(4)]
            padding: [dp(15), 0, 0, 0]
            Label:
                text: 'Kivy'
                size_hint_x: None
                width: self.texture_size[0]
                font_size: sp(13)
            Widget:
            AnchorIcon:
                width: dp(30)
                ButtonIcon:
                    size: [dp(15), dp(15)]
                    icon_source: icon('play-white')



<NewProjectPopup>:
    auto_dismiss: False
    padding:
        ['230dp', '110dp', '230dp', '110dp'] \
        if app.root.width > dp(1300) and app.root.height > dp(600) \
        else ['100dp', '50dp', '100dp', '50dp']
    canvas:
        Clear:
        Color:
            rgba: [0, 0, 0, 0.75]
        Rectangle:
            pos:self.pos
            size: self.size
    ScreenManager:
        transition: FadeTransition()
        ConfigProjectScreen:
            name: 'config_project'
            popup: root

""")

class DropOptions(BoxLayout):
    pass

class ProjectTopBar(ColoredBoxLayout):
    pass

class NewProjectPopup(ModalView):
    pass

class ConfigProjectScreen(Screen):
    popup = ObjectProperty(None)

    def close_popup(self, *args):
        if self.popup is None:
            return None
        self.popup.dismiss()
    
    def start_project(self, *args):
        self.close_popup()

