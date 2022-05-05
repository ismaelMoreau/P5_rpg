
import p5

from settings import *

#TODO base class and ineheritance for different sections
class Sections:
    def __init__(self,monsters,player):
        self.monsters = monsters 
        self.player = player
        self.scaling = 0.0
        self.scale_multiply = 6
        self.current_monster = 0
        self.buttons = []

    def draw_section(self):
        self.scaling = min(self.scaling + 1.0, 6.0)
        with p5.push_matrix():
            p5.rect_mode(p5.CENTER)

            p5.translate(WIDTH/2, HEIGHT/2)
            
            p5.scale(self.scaling)
            
            p5.fill(25,0,0,63)
            p5.stroke(255)
            p5.stroke_weight(4)
            p5.rect((0,0), TILESIZE, TILESIZE)
            p5.no_stroke()
            p5.rect_mode(p5.CORNER)



    def add_text(self,label,tile_pos):
        # PARAMETRE tile_pos = 1*TILESIZE is center of the section so 5*TILESIZE mean botton of section
        p5.text_align(p5.CENTER)
        p5.fill(255)
        p5.no_stroke()
        p5.text(label,(WIDTH/2,HEIGHT/2+tile_pos*TILESIZE-6))
        p5.text_align(p5.CORNER)

    def reset_section(self):
        self.is_open=False
        self.scaling = 0.0
        