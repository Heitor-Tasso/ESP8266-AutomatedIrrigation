
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from login import Login
from camera4kivy import Preview

Builder.load_string("""

#:import hex kivy.utils.get_color_from_hex

# PALLET 1
#:set super_gray hex('#0D0D0D')
#:set black_gray hex('#1A1A1A')
#:set mid_gray hex('#262626')
#:set gray hex('#333333')
#:set light_gray hex('#404040')

# PALLET 2
#:set black hex('#000000')
#:set green hex('#6FEE5D')
#:set clear_white hex('#F6F6F6')
#:set white hex('#FFFFFF')
#:set blue hex('#0064CE')

<GameScreens>:
    Login:
        id: login
        name: 'login'
    Screen:
        name: 'camera'
        on_enter: camera.connect_camera()
        on_leave: camera.disconnect_camera()
        BoxLayout:
            orientation: 'vertical'    
            Preview:
                id: camera
                aspect_ratio: '16:9'
            AnchorLayout:
                size_hint_y: None
                height: '40dp'
                anchor_x: 'center'
                ButtonEffect:
                    text: 'Next'
                    size_hint_x: None
                    width: '150dp'
                    background_color: [0, 0, 0, 0]
                    color_line: [clear_white, white]
                    color_effect: light_gray
                    radius: [dp(15), dp(15), dp(15), dp(15)]
                    on_press: root.current = root.next()
""")

class GameScreens(ScreenManager):
    pass

class Program(App):
    def build(self):
        return GameScreens()

if __name__ == '__main__':
    Program().run()
