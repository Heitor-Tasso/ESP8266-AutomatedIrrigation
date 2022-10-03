
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from uix.triggers import BTrigger
from kivy.uix.screenmanager import ScreenManager

from login import Login
from user_plant import UserPlant
from uix.camera import PlantCamera, QRCode

Builder.load_string("""

#:import hex kivy.utils.get_color_from_hex

#:import icon utils.icon
#:import image utils.image

#:import IconInput uix.inputs.IconInput
#:import ButtonEffect uix.buttons.ButtonEffect
#:import ButtonIcon uix.icons.ButtonIcon
#:import AnchorIcon uix.icons.AnchorIcon

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
    UserPlant:
        name: 'user'
    Login:
        id: login
        name: 'login'
    PlantCamera:
        name: 'camera'
    # QRCode:
    #     name: 'qrcode'

""")

class GameScreens(ScreenManager):
    pass

class Program(App):
    def build(self):
        return GameScreens()

if __name__ == '__main__':
    Program().run()
