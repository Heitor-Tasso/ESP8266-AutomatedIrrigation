
from kivy.lang import Builder
from utils import get_json, update_json
from kivy.uix.boxlayout import BoxLayout
from uix.popup import BoxPopup, ConfirmPopup
from uix.label import LabelButton
from kivy.properties import StringProperty, ObjectProperty
from utils import image
from kivy.clock import Clock
import re
from kivy.app import App


Builder.load_string("""

#:import IconInput uix.inputs.IconInput
#:import ToggleButtonIcon uix.icons.ToggleButtonIcon
#:import ButtonIcon uix.icons.ButtonIcon
#:import ScrollViewBar uix.scrollview.ScrollViewBar
#:import BarScroll uix.scrollview.BarScroll
#:import ButtonIcon uix.icons.ButtonIcon
#:import ResizableGrid uix.grid.ResizableGrid
#:import QRCode uix.camera.QRCode
#:import BoxPopup uix.popup.BoxPopup

#:import DampedScrollEffect kivy.effects.dampedscroll.DampedScrollEffect

#:import icon utils.icon
#:import image utils.image

#:import hex kivy.utils.get_color_from_hex

<PlantCard>:
    size_hint_y: None
    height: self.width
    padding: '20dp'
    source: ''
    id_plant: ''
    popup: None
    canvas.before:
        Color:
            rgba: hex("#43d9ca")
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8), dp(8), dp(8), dp(8)]
        
        Color:
            rgba: hex("#ebeef2")
        RoundedRectangle:
            pos: self.x+dp(5), self.y+dp(5)
            size: self.width-dp(10), self.height-dp(10)
            radius: [dp(8), dp(8), dp(8), dp(8)]
    
    ButtonIcon:
        size: root.width-dp(40), root.height-dp(40)
        icon_source: root.source
        icon_color: [[1, 1, 1, 1], hex("#aeb5bf")]
        effect_color: hex("#e06031")[0:-1] + [0.7]
        radius_effect: [self.width]*4
        duration_in: 0.8
        duration_out: 0.4
        on_release: app.root.chose_plant(root)


<Pesquisa>:
    box_background_color: hex('#002428')
    overlay_color: [0, 0, 0, .7]
    padding:
        ['130dp', '70dp', '130dp', '70dp'] \
        if app.root.width > dp(1300) and app.root.height > dp(600) \
        else ['80dp', '30dp', '60dp', '30dp']
    Label:
        text:'Escolha uma planta'
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
                ResizableGrid:
                    size_hint_y: None
                    height: self.minimum_height
                    cols: 1
                    max_size: [dp(130), dp(180)]
                    id: grid_imgs
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

<LabelIP>:
    size_hint_y: None
    height: "50dp"
    LabelButton:
        text: root.text
        font_size: "20dp"
        bold: True
        on_release: root.popup_ips.choose_ip(self)
    AnchorIcon:
        ButtonIcon:
            size: ['25dp', '25dp']
            source: icon('close')
            on_release: root.popup_ips.remove_label_ip(root)
    


<Dot@Label>:
    text:'.'
    font_size: '18sp'
    bold: True
    size_hint_x: None
    width: self.texture_size[0]


<NewIPPopup>:
    box_background_color: hex('#002428')
    overlay_color: [0, 0, 0, .7]
    box_padding: [0, 0, 0, 0]
    padding:
        [dp(330), dp(210), dp(330), dp(210)] \
        if app.root.width > dp(1300) and app.root.height > dp(600) \
        else [dp(130), dp(100), dp(130), dp(100)]
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        ColoredBoxLayout:
            size_hint_y: None
            height: self.minimum_height
            background_color: hex('#014034')
            radius: [dp(20), dp(20), 0, 0]
            AnchorLayout:
                anchor_y: 'center'
                size_hint_y: None
                height: lb_t.height + dp(20)
                padding: [dp(10), 0, 0, 0]
                LabelToScroll:
                    text: "Escreva o IP do ESP abaixo"
                    font_size: "17sp"
                    bold: True
                    halign: 'left'
                    valign: 'center'
                    color: hex('#FFFFFF')
                    id: lb_t
            AnchorIcon:
                size_hint_y: None
                height: lb_t.parent.height
                ButtonIcon:
                    size: ['35dp', '35dp']
                    source: icon('return')
                    on_release: root.dismiss()
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            size_hint_y: None
            height: '50dp'
            id: box_inputs
            size_hint_x: None
            width: '300dp'
            next: lambda *a: a[1] in {'\t', ' '}
            IconInput:
                id: first
                radius: [0, 0, 0, 0]
                line_color: hex('#749f9d')
                input_height: dp(45)
                next: lambda *a: a[1] in {'\t', ' '}
                on_enter: second.select()
                on_input_text:
                    if box_inputs.next(*args): self.un_select()
                    if box_inputs.next(*args): second.select()
                    if box_inputs.next(*args): self.input_text = self.input_text[0:-1]
            Dot:
            IconInput:
                id: second
                radius: [0, 0, 0, 0]
                line_color: hex('#749f9d')
                input_height: dp(45)
                on_enter: third.select()
                on_input_text:
                    if box_inputs.next(*args): self.un_select()
                    if box_inputs.next(*args): third.select()
                    if box_inputs.next(*args): self.input_text = self.input_text[0:-1]
            Dot:
            IconInput:
                id: third
                radius: [0, 0, 0, 0]
                line_color: hex('#749f9d')
                input_height: dp(45)
                on_enter: fourth.select()
                on_input_text:
                    if box_inputs.next(*args): self.un_select()
                    if box_inputs.next(*args): fourth.select()
                    if box_inputs.next(*args): self.input_text = self.input_text[0:-1]
            Dot:
            IconInput:
                id: fourth
                radius: [0, 0, 0, 0]
                line_color: hex('#749f9d')
                input_height: dp(45)
                on_enter: fifth.select()
                on_input_text:
                    if box_inputs.next(*args): self.un_select()
                    if box_inputs.next(*args): fifth.select()
                    if box_inputs.next(*args): self.input_text = self.input_text[0:-1]
            Dot:
                text: ':'
            IconInput:
                id: fifth
                default_text: "Opcional"
                radius: [0, 0, 0, 0]
                line_color: hex('#749f9d')
                input_height: dp(45)
                on_enter: root.add_ip()
        
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        size_hint_y: None
        height: '60dp'
        padding: [0, 0, 0, '15dp']
        ButtonEffect:
            text: 'Adicionar'
            size_hint: None, None
            size: ['100dp', '45dp']
            on_press: root.add_ip()
            

<EspIPS>:
    box_background_color: hex('#002428')
    overlay_color: [0, 0, 0, .7]
    padding:
        ['130dp', '70dp', '130dp', '70dp'] \
        if app.root.width > dp(1300) and app.root.height > dp(600) \
        else ['80dp', '30dp', '60dp', '30dp']
    BoxLayout:
        size_hint_y: None
        height: '60dp'
        padding: ['40dp', '0dp', '40dp', '0dp']
        AnchorIcon:
            width: '50dp'
            canvas:
                Color:
                    rgba: [1, 1, 1, 1]
                Ellipse:
                    size: [dp(40), dp(40)]
                    pos: self.center_x-dp(20), self.center_y-dp(20)
            ButtonIcon:
                size: ['25dp', '25dp']
                source: icon('plus')
                icon_color: [0, 0, 0, 1]
                on_release: root.open_new_ips()
        Label:
            text:'Escolha o ip do ESP'
            font_size: '20sp'
            bold: True
        AnchorIcon:
            width: '50dp'
            canvas:
                Color:
                    rgba: [1, 1, 1, 1]
                Ellipse:
                    size: [dp(40), dp(40)]
                    pos: self.center_x-dp(20), self.center_y-dp(20)
            ButtonIcon:
                size: ['35dp', '35dp']
                source: icon('qrcode')
                on_release: QRCode(callback=root.add_ip).open()
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
                id: box_ips
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

""")

class PlantCard(BoxLayout):
    source = StringProperty("")
    id_plant = StringProperty("")
    popup = ObjectProperty(None)

class Pesquisa(BoxPopup):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        for k, v in get_json("config.json").items():
            img = PlantCard(source=image(*v['url']), popup=self)
            img.id_plant = k
            self.ids.grid_imgs.add_widget(img)


class LabelIP(BoxLayout):
    popup_ips = ObjectProperty(None)
    text = StringProperty("")


class NewIPPopup(BoxPopup):
    esp_ips = ObjectProperty(None)

    def add_ip(self, *args):
        inps = [self.ids.first, self.ids.second, self.ids.third, self.ids.fourth]
        ip = '.'.join(map(lambda i: i.input_text, inps)) + f":{self.ids.fifth.input_text}"

        if self.esp_ips.add_ip(ip):
            Clock.schedule_once(lambda *a: self.dismiss())


class EspIPS(BoxPopup):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        app = App.get_running_app().root
        for ip in get_json("logins.json")[app.user]["ips"]:
            self.add_label_ip(ip)
        
    def add_label_ip(self, ip):
        lb_ip = LabelIP(popup_ips=self, text=ip)
        self.ids.box_ips.add_widget(lb_ip)


    def add_ip(self, txt_qrcode):
        print("Recebeu callback -=> ", txt_qrcode)

        # Verifica se é um IP válido
        if re.search("^(\d{1,3}\.){3}\d{1,3}(:\d{1,3})?$", txt_qrcode):
            self.add_label_ip(txt_qrcode)
            app = App.get_running_app().root
            js = get_json("logins.json")
            js[app.user]["ips"].append(txt_qrcode)
            update_json(js, "logins.json")
            return True
        
        ConfirmPopup(title="Alerta!", msg='É necessário preencher todos os campos com valores válidos de um IP, numeros entre 0 a 9.').open()
        return False

    
    def open_new_ips(self, *args):
        NewIPPopup(esp_ips=self).open()


    def choose_ip(self, label_ip):
        app = App.get_running_app().root
        app.ip = label_ip.text
        self.dismiss()


    def remove_label_ip(self, label_ip):
        app = App.get_running_app().root
        js = get_json("logins.json")
        js[app.user]["ips"].remove(label_ip.text)
        update_json(js, "logins.json")
        self.ids.box_ips.remove_widget(label_ip)

