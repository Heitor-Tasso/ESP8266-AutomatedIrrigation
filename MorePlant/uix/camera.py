
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from uix.triggers import BTrigger
from kivy.uix.screenmanager import Screen

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
                BoxLayout:
                    orientation: 'vertical'
                    AnchorLayout:
                        anchor_x: 'center'
                        anchor_y: 'center'
                        Image:
                            size_hint: None, None
                            size: '300dp', '300dp'
                            allow_strech: True
                            keep_ratio: True
                            mipmap: True
                            source: icon('scanner_qr_code')
                    BoxLayout:
                        size_hint_y: None
                        height: '70dp'
                        padding: ['0dp', '0dp', '0dp', '50dp']
                        Widget:
                        AnchorIcon:
                            ButtonIcon:
                                size: ['70dp', '70dp']
                                source: icon('qr-code')
                                on_release: root.manager.current = 'user'
                        Widget:

                    
""")

class QRCode(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        Window.bind(on_flip=self._update_camera_options)
        
        BTrigger(self._update_camera_options, 20, 0.1).start()

    def _update_camera_options(self, *args):
        camera = self.ids.camera
        camera.v_size = camera.preview.view_size
        camera.v_pos = camera.preview.view_pos
