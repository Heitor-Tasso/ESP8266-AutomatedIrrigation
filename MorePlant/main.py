
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.help import Help
from screens.login import Login
from screens.user_plant import UserPlant
from screens.pesquisa import Pesquisa

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
    Login:
        id: login
        name: 'login'
    UserPlant:
        name: 'user'
    Help:
        name: 'help'
    Pesquisa:
        name: 'pesquisa'
    PlantCamera:
        name: 'camera'
    QRCode:
        name: 'qrcode'

""")

class GameScreens(ScreenManager):
    pass

class Program(App):
    def build(self):
        return GameScreens()

if __name__ == '__main__':
    Program().run()
