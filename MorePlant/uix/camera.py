from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.window import Window
from uix.triggers import BTrigger
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

from camera4kivy import Preview

Builder.load_string("""

#:import hex kivy.utils.get_color_from_hex

#:import icon utils.icon
#:import image utils.image

#:import IconInput uix.inputs.IconInput
#:import ButtonEffect uix.buttons.ButtonEffect
#:import ButtonIcon uix.icons.ButtonIcon
#:import AnchorIcon uix.icons.AnchorIcon


<QRCode>:
    on_enter: camera.connect_camera()
    on_leave: camera.disconnect_camera()
    camera: camera
    sc_prop: [0, 0, 0, 0] # w, h, x, y of scanner
    BoxLayout:
        orientation: 'vertical'
        Preview:
            id: camera
            aspect_ratio: '9:16'
            v_size: [0, 0]
            v_pos: [0, 0]
            on_size: root._update_camera_options()
            on_pos: root._update_camera_options()
            on_kv_post: root._update_camera_options()
        FloatLayout:
            size_hint: [None, None]
            size: [0, 0]
            BoxLayout:
                size_hint: [None, None]
                size: camera.v_size
                pos: camera.v_pos
                w_scann: (self.x+self.width-root.sc_prop[2]-root.sc_prop[0])
                h_top_scann: ((self.y+self.height)-(root.sc_prop[3]+root.sc_prop[1]))
                canvas.before:
                    Color:
                        rgba: [0.1, 0.2, 0.3, 0.4]
                    Rectangle:
                        pos: [self.x, self.y]
                        size: [(self.w_scann or 0), self.height]
                    Rectangle:
                        pos: [self.x+self.width-(self.w_scann or 0), self.y]
                        size: [(self.w_scann or 0), self.height]
                    
                    Rectangle:
                        pos: [self.x+(self.w_scann or 0), self.y+self.height-(self.h_top_scann or 0)]
                        size: [(root.sc_prop[0] or 0), (self.h_top_scann or 0)]
                    Rectangle:
                        pos: [self.x+(self.w_scann or 0), self.y]
                        size: [(root.sc_prop[0] or 0), (root.sc_prop[3] or 0)-self.y]

                BoxLayout:
                    orientation: 'vertical'
                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'
                        Widget:
                            id: scanner
                            size_hint: None, None
                            size: '300dp', '300dp'
                            on_size: root.sc_prop = [*self.size, *self.pos]
                            on_pos: root.sc_prop = [*self.size, *self.pos]

                            canvas:
                                Color:
                                    rgba: hex('#207afe')
                                Line:
                                    points: [self.x, self.y+dp(60), self.x, self.y, self.x+dp(60), self.y]
                                    width: dp(3)
                                Line:
                                    points: [self.x, self.y+self.height-dp(60), self.x, self.y+self.height, self.x+dp(60), self.y+self.height]
                                    width: dp(3)
                                Line:
                                    points: [self.x+self.width, self.y+self.height-dp(60), self.x+self.width, self.y+self.height, self.x+self.width-dp(60), self.y+self.height]
                                    width: dp(3)
                                Line:
                                    points: [self.x+self.width, self.y+dp(60), self.x+self.width, self.y, self.x+self.width-dp(60), self.y]
                                    width: dp(3)

                            Icon:
                                pos: self.parent.x+self.parent.width-self.width-dp(7), self.parent.y+dp(7)
                                background_color: [1, 1, 1, 1]
                                radius: [self.width/2] * 4
                                size_hint_y: None
                                size: ['35dp', '35dp']
                                icon_size: ['30dp', '30dp']
                                
                                source: icon('resize')
                                color: hex('#207afe')
                                mipmap: False

                                last_touch: 0
                                touch_in: False
                                on_touch_down:
                                    if (self.collide_point(*args[1].pos)): self.last_touch = args[1].x
                                    self.touch_in = True if (self.collide_point(*args[1].pos)) else False
                                on_touch_up: self.last_touch = 0
                                on_touch_move:
                                    if self.touch_in: scanner.width += args[1].x-self.last_touch
                                    if self.touch_in: scanner.height += args[1].x-self.last_touch
                                    if self.touch_in: self.last_touch = args[1].x
                    BoxLayout:
                        size_hint_y: None
                        height: '70dp'
                        padding: ['0dp', '0dp', '0dp', '50dp']
                        Widget:
                        AnchorIcon:
                            background_color: hex('#333333')
                            radius: [self.width/2] * 4
                            size_hint_y: None
                            size: '80dp', '80dp'
                            ButtonIcon:
                                size: ['45dp', '45dp']
                                source: icon('qrcode')
                                on_release: root.start_scann()
                                color: hex('#313131')
                                canvas:
                                    Color:
                                        rgba: [1, 1, 1, 1]
                                    RoundedRectangle:
                                        pos: self.pos
                                        size: self.size
                                        radius: [self.width/6] * 4
                        Widget:

                    
""")

class QRCode(Screen):

    camera = ObjectProperty(None)
    sc_prop = ListProperty([0, 0, 0, 0])
    started_scan = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        self.camera = self.ids.camera
        
        Window.bind(on_flip=self._update_camera_options)
        BTrigger(self._update_camera_options, 20, 0.1).start()

    def _update_camera_options(self, *args):
        self.camera.v_size = self.camera.preview.view_size
        self.camera.v_pos = self.camera.preview.view_pos
    
    def start_scann(self, *args):
        if self.started_scan: return None

        scanner = self.ids.scanner
        last_size = tuple(map(lambda x: x, scanner.size))
        get_over = lambda *a: self.go_back_scan(last_size)

        anim = Animation(size=tuple(map(lambda x: x*1.3, scanner.size)), d=0.5)
        anim.bind(on_complete=get_over)
        anim.start(scanner)
        self.started_scan = True

    def go_back_scan(self, size):
        scanner = self.ids.scanner
        anim = Animation(size=size, d=0.8)
        anim.bind(on_complete=lambda *a: self.end_scann())
        anim.start(scanner)

    def end_scann(self, *args):
        self.started_scan = False
        Clock.schedule_once(self.next_screen, 1)
    
    def next_screen(self, *args):
        self.manager.current = 'user'