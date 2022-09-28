
from kivy.uix.modalview import ModalView

from uix.boxlayout import ColoredBoxLayout

from functools import partial
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.clock import Clock
from utils.path import get_config, example

from kivy.properties import StringProperty, ObjectProperty
from .label import LabelBottomStroke

from kivy.metrics import dp


Builder.load_string("""

#: import Icon uix.icons.Icon
#: import ButtonIcon uix.icons.ButtonIcon
#: import ColoredBoxLayout uix.boxlayout.ColoredBoxLayout
#: import ScrollViewBar uix.scrollview.ScrollViewBar
#: import BarScroll uix.scrollview.BarScroll
#: import InputIcon uix.input.InputIcon

#: import FadeTransition kivy.uix.screenmanager.FadeTransition

#: import example utils.path.example
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

<ExampleContent>:
    source: ''
    title: ''
    orientation: 'vertical'
    size_hint_y: None
    height: self.minimum_height
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        size_hint_y: None
        height: '220dp'
        Image:
            source: root.source
            size_hint: None, None
            size: self.texture_size
            keep_ratio: True
            mipmap: True
    Label:
        text: root.title
        size_hint_y: None
        height: '35dp'

<NewProjectScreen>:
    ColoredBoxLayout:
        orientation: 'vertical'
        radius: [dp(15), dp(15), dp(15), dp(15)]
        background_color: hex('#262626')
        stroke_color: [1, 1, 1, 1]
        stroke_width: dp(1.01)
        ProjectTopBar:
            title: 'Project Template'
            screen: root
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            padding: ['80dp', '20dp', '80dp', '10dp']
            ColoredBoxLayout:
                orientation: 'vertical'
                stroke_color: hex('#2d3a54')
                radius: [dp(10)]
                AnchorLayout:
                    anchor_y: 'center'
                    padding: ['15dp', '0dp', '15dp', '0dp']
                    size_hint_y: None
                    height: '55dp'
                    ScrollViewBar:
                        do_scroll_y: False
                        do_scroll_x: True
                        size_hint_y: None
                        height: '40dp'
                        bar_color: [0, 0, 0, 0]
                        BoxLayout:
                            size_hint_x: None
                            width: self.minimum_width
                            id: _box_titles_phone
                BoxLayout:
                    ScreenManager:
                        id: _manager_content
                    AnchorLayout:
                        anchor_y: 'center'
                        size_hint_x: None
                        width: _bar_scroll.width
                        BarScroll:
                            id: _bar_scroll
                            scroll_view: None
                            size_hint_y: None
                            height: self.parent.height - dp(40)
        AnchorLayout:
            size_hint_y: None
            height: '60dp'
            anchor_x: 'center'
            anchor_y: 'center'
            padding: ['0dp', '0dp', '0dp', '10dp']
            BoxLayout:
                spacing: '10dp'
                size_hint_x: None
                width: self.minimum_width
                size_hint_y: None
                height: '30dp'
                ButtonEffect:
                    text: 'Cancel'
                    size_hint_x: None
                    width: '100dp'
                    background_color: hex('#375ca6')
                    text_color: [1, 1, 1, 1]
                    color_line: [0, 0, 0, 0]
                    radius: [dp(5)]
                    on_release: root.close_popup()
                ButtonEffect:
                    text: 'Next'
                    size_hint_x: None
                    width: '100dp'
                    background_color: hex('#375ca6')
                    text_color: [1, 1, 1, 1]
                    color_line: [0, 0, 0, 0]
                    radius: [dp(5)]
                    on_release: root.manager.current = root.manager.next()

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


<ConfigProjectScreen>:
    ColoredBoxLayout:
        orientation: 'vertical'
        radius: [dp(15), dp(15), dp(15), dp(15)]
        background_color: hex('#262626')
        stroke_color: [1, 1, 1, 1]
        stroke_width: dp(1.01)
        ProjectTopBar:
            title: 'Configure your Project'
            screen: root
        BoxLayout:
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                size_hint_x: 0.7
                id: _anc_phone
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size: self.minimum_width, self.minimum_height
                    Image:
                        source: example("BottomNavActivity")
                        size_hint: None, None
                        id: _phone_img
                        inc: (sum(_anc_phone.size)/2)
                        width: self.inc/2
                        height: self.inc/1.5
                        allow_stretch: True
                        keep_ratio: True
                        mipmap: True
                    Label:
                        text: "Bottom Navigation Activity"
                        size_hint_y: None
                        height: '35dp'
            BoxLayout:
                orientation: 'vertical'
                space_phone: (_anc_phone.width-_phone_img.texture_size[0])/3
                AnchorLayout:
                    anchor_y: 'center'
                    padding: ['0dp', '0dp', self.parent.space_phone, '0dp']
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: 'vertical'
                        spacing: dp(15)
                        
                        ConfigInputIcon:
                            label_text: 'Name'
                        ConfigInputIcon:
                            label_text: 'Package Name'
                        ConfigInputIcon:
                            label_text: 'Save Location'
                        
                        DropOptions:
                            title: 'Main Lib'
                        DropOptions:
                            title: 'System'

                Widget:
                    size_hint_y: None
                    height: dp(40)

                AnchorLayout:
                    size_hint_y: None
                    height: '60dp'
                    anchor_x: 'center'
                    anchor_y: 'center'
                    padding: ['0dp', '20dp', self.parent.space_phone, '10dp']
                    BoxLayout:
                        spacing: '10dp'
                        size_hint_x: None
                        width: self.minimum_width
                        size_hint_y: None
                        height: '30dp'
                        ButtonEffect:
                            text: 'Cancel'
                            size_hint_x: None
                            width: '100dp'
                            background_color: hex('#375ca6')
                            text_color: [1, 1, 1, 1]
                            color_line: [0, 0, 0, 0]
                            radius: [dp(5)]
                            on_release: root.close_popup()
                        ButtonEffect:
                            text: 'Previous'
                            size_hint_x: None
                            width: '100dp'
                            background_color: hex('#375ca6')
                            text_color: [1, 1, 1, 1]
                            color_line: [0, 0, 0, 0]
                            radius: [dp(5)]
                            on_release: root.manager.current = root.manager.previous()
                        ButtonEffect:
                            text: 'Finish'
                            size_hint_x: None
                            width: '100dp'
                            background_color: hex('#375ca6')
                            text_color: [1, 1, 1, 1]
                            color_line: [0, 0, 0, 0]
                            radius: [dp(5)]
                            on_release: root.start_project()
                Widget:
                    size_hint_y: None
                    height: dp(20)

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
        NewProjectScreen:
            name: 'new_project'
            popup: root
""")

class DropOptions(BoxLayout):
    pass

class ExampleContent(BoxLayout):
    title = StringProperty('')
    source = StringProperty('')

class ScrollContentScreens(BoxLayout):
    def __init__(self, examples=[], **kwargs):
        super().__init__(**kwargs)
        for (title, source) in examples:
            exmp = ExampleContent(
                title=title, source=example(source))
            self.ids._grid_screens.add_widget(exmp)

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

class NewProjectScreen(Screen):
    popup = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.start)

    def start(self, *args):
        config = get_config('new_proj_popup')
        
        manager = self.ids._manager_content
        btp = self.ids._box_titles_phone

        for title, list_config in config['examples_screens'].items():
            lb_s = LabelBottomStroke(
                text=title, size_hint_x=None, halign='center',
                group='exmp_lbl_stroke', allow_no_selection=False,
                on_press=partial(self.change_screen_example, manager))
            btp.add_widget(lb_s)

            screen = Screen(name=title)
            screen.add_widget(ScrollContentScreens(examples=list_config))
            self.ids._manager_content.add_widget(screen)
        
        btp.children[-1].state = 'down'
        self.change_screen_example(manager)
        self.bind(width=self.update_lbl_strokes)
        Clock.schedule_once(self.update_lbl_strokes)

    def change_screen_example(self, manager, label_bottom_stroke=None):
        if label_bottom_stroke is not None:
            setattr(manager, 'current', label_bottom_stroke.text)
        scroll_content = manager.current_screen.children[0]
        self.ids._bar_scroll.scroll_view = scroll_content.ids._scroll_examples

    def update_lbl_strokes(self, *args):
        for lbl in self.ids._box_titles_phone.children:
            lbl.width = lbl.texture_size[0] + dp(20)

    def close_popup(self, *args):
        if self.popup is None:
            return None
        self.popup.dismiss()

