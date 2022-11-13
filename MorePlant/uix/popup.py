
from kivy.uix.modalview import ModalView
from uix.boxlayout import ColoredBoxLayout
from kivy.lang.builder import Builder


Builder.load_string("""

#: import ColoredBoxLayout uix.boxlayout.ColoredBoxLayout
#: import LabelToScroll uix.label.LabelToScroll
#: import ButtonIcon uix.icons.ButtonIcon
#: import ButtonEffect uix.buttons.ButtonEffect
#: import ScrollViewBar uix.scrollview.ScrollViewBar
#: import BarScroll uix.scrollview.BarScroll
#: import get_path utils.get_path
#: import icon utils.icon


<BoxPopup>:
    box_background_color: [0, 0, 0, 0]
    box_padding: ['0dp', '15dp', '0dp', '0dp']
    border: [0, 0, 0, 0]
    auto_dismiss: False
    overlay_color: [0, 0, 0, 0]
    background_color: [0, 0, 0, 0]
    ColoredBoxLayout:
        orientation: 'vertical'
        padding: root.box_padding
        background_color: root.box_background_color
        radius: [dp(20), dp(20), dp(20), dp(20)]
        id: _colored_box

<TermsPopup>:
    box_background_color: hex('#002428')
    padding:
        ['230dp', '110dp', '230dp', '110dp'] \
        if app.root.width > dp(1300) and app.root.height > dp(600) \
        else ['80dp', '50dp', '80dp', '50dp']
    Label:
        text:'TERMO DE USO DE APLICATIVO'
        font_size: '20sp'
        bold: True
        size_hint_y: None
        height: '60dp'
    BoxLayout:
        padding: ['20dp', '20dp', '20dp', '20dp']
        spacing: '15dp'
        ScrollViewBar:
            id: scroll
            effect_cls: DampedScrollEffect
            BoxLayout:
                orientation: 'vertical'
                padding: ['0dp', '15dp', '0dp', '0dp']
                size_hint_y: None
                height: self.minimum_height
                LabelToScroll:
                    text: ''
                    on_kv_post:
                        with open(get_path("terms.md"), "r", encoding="utf-8") as f: \
                        self.text = f.read()
                    id: terms_text
                    
        BarScroll:
            scroll_view: scroll
            radius: [dp(7), dp(7), dp(7), dp(7)]
            bar_radius: [dp(3)]
            bar_width: dp(7)
            width: '15dp'
    AnchorIcon:
        size_hint_y: None
        height: '70dp'
        width: self.parent.width
        ButtonIcon:
            size: ['25dp', '25dp']
            source: icon('return')
            on_release: root.dismiss()

<ConfirmPopup>:
    box_background_color: hex("#038c73")
    padding:
        [dp(330), dp(210), dp(330), dp(210)] \
        if app.root.width > dp(1300) and app.root.height > dp(600) \
        else [dp(130), dp(100), dp(130), dp(100)]
    box_padding: [0, 0, 0, 0]
    overlay_color: [0, 0, 0, 0.7]
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        ColoredBoxLayout:
            size_hint_y: None
            height: self.minimum_height
            background_color: hex('#ebeef2')
            radius: [dp(20), dp(20), 0, 0]
            AnchorLayout:
                anchor_y: 'center'
                size_hint_y: None
                height: lb_t.height + dp(10)
                padding: [dp(10), 0, 0, 0]
                LabelToScroll:
                    text: "Alerta"
                    font_size: "30sp"
                    bold: True
                    halign: 'left'
                    valign: 'center'
                    color: hex('#e06031')
                    id: lb_t
            AnchorIcon:
                size_hint_y: None
                height: lb_t.parent.height
                ButtonIcon:
                    size: ['35dp', '35dp']
                    source: icon('close')
                    on_release: root.dismiss()

    AnchorLayout:
        anchor_y: 'center'
        LabelToScroll:
            text: 'É necessário aceitar os termos de uso!'
            font_size: "20sp"

    AnchorLayout:
        anchor_y: 'center'
        anchor_x: 'center'
        size_hint_y: None
        height: 0 if not self.children else self.children[0].height + dp(30)
        ButtonEffect:
            text: "Continuar"
            size_hint: None, None
            size: '120dp', '55dp'
            radius: [dp(15)]
            background_color: hex('#2c2c2c')
            bold: True
            font_size: '17sp'
            on_release: root.dismiss()
""")




class BoxPopup(ModalView):

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, ColoredBoxLayout):
            return super().add_widget(widget, *args, **kwargs)
        return self.ids._colored_box.add_widget(widget, *args, **kwargs)


class TermsPopup(BoxPopup):
    pass

class ConfirmPopup(BoxPopup):
    pass