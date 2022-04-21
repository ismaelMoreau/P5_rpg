
import p5
from settings import *
from Section_Button import *
from Sections import *

class Section_Begin(Sections):
    def __init__(self,monsters,player):
        super().__init__(monsters,player)
        self.buttons.append(Section_Button("Begin",WIDTH/2,HEIGHT/2+2.5*TILESIZE, 6*TILESIZE, TILESIZE))
        self.is_open = True

    def draw_section(self):
        
        super().draw_section()
        if self.scaling == 6.0:
        
            for b in self.buttons:
                b.draw_button()
            self.add_text("\n \nattack = \n 50 percent chances \n\ng key add green tile \n \nb key add a bubble \n \np key remove bubble \n \nr key reset bubbles" ,-3)
            #self.add_text("agent rules: \n to die on sand \n monte carlos algo \n egreedy policy",0)