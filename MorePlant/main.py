
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from utils import get_json, image
from screens.login import Login
from screens.user_plant import UserPlant
from screens.pesquisa import Pesquisa
from uix.popup import ConfirmPopup

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
        id: user_plant

""")

class GameScreens(ScreenManager):
    
    def chose_plant(self, plant_card):
        dic_plant = get_json("config.json")[plant_card.id_plant]
        plant_card.popup.dismiss()
        self.current = 'user'

        ids_plant = self.ids.user_plant.ids
        
        ids_plant.plant_name.text = ids_plant.plant_name.default_text.format(plant_card.id_plant)        
        ids_plant.plant_name.update_content()

        ids_plant.plant_image.source = image(*dic_plant['url'])
        del dic_plant['url']
        
        for k, v in dic_plant.items():
            pl = ids_plant[f'plant_{k}']
            pl.text = pl.default_text.format(v)
            pl.update_content()
    
    def login(self, *args):
        ids = self.ids.login.ids
    
        print("Email login -=> ", ids.input_email_login.input_text)
        print("Senha login -=> ", ids.input_pass_login.input_text)
        Pesquisa().open()

    def signup(self, *args):
        ids = self.ids.login.ids
        if not ids.check_terms_signin.active:
            ConfirmPopup().open()
            return None
        
        print("Email signin -=> ", ids.input_email_signin.input_text)
        print("Senha signin -=> ", ids.input_pass_signin.input_text)

        self.login()

class Program(App):
    def build(self):
        return GameScreens()

if __name__ == '__main__':
    Program().run()
