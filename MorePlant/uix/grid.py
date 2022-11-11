from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.core.window import Window

class ResizableGrid(GridLayout):

    max_size = ListProperty([dp(235), dp(250)])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.config)
    
    def config(self, *args):
        Window.bind(on_maximize=self.set_grid_cols)
        Window.bind(on_restore=self.set_grid_cols)
        self.set_grid_cols()


    def on_size(self, *args):
        # quando redimesionado, chama a função para
        # modificar as colunas da grid no proximo quadro
        Clock.schedule_once(self.set_grid_cols)

    def set_grid_cols(self, *args):
        # calculo para determinar a quantidade de colunas
        # corretas para a grid de acorod com **self.max_size**
        w1, w2 = self.max_size
        tc = max(2, len(self.children)+1)
        for i in range(1, tc):
            w = round(self.width/i)
            if (w > w1 and w < w2) or w < w1:
                self.cols = i-(1 if w < w1 and i > 1 else 0)
                break
            elif i == tc-1:
                self.cols = tc-1
        
        Clock.schedule_once(self.check_max_width, 0.1)
    
    def check_max_width(self, *args):
        w1, w2 = self.max_size
        if self.cols >= len(self.children):
            if self.children[0].width > (w2+dp(20)):
                t = int((self.children[0].width-w2)/2)
                self.padding = [t, 0, t, 0]
                self.spacing = t
            return None
        
        self.padding = dp(10)
        self.spacing = dp(10)
