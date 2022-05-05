
import p5
from settings import *
from Section_Button import *
from Sections import *

class Section_Encounter(Sections):
    def __init__(self,monsters,player):
        super().__init__(monsters,player)
        self.is_open = False
        self.buttons.append(Section_Button("attack",WIDTH/2,HEIGHT/2+2.5*TILESIZE, 6*TILESIZE, TILESIZE))
        self.buttons.append(Section_Button("escape",WIDTH/2,HEIGHT/2+1.5*TILESIZE, 6*TILESIZE, TILESIZE))
        self.text_action = "choose"
        self.rotation = 0

    def check_is_open(self):
        for count in range(len(self.monsters)):
            if self.monsters[count].is_visible:
                if self.monsters[count].map_position == self.player.map_position:
                    self.is_open = True
                    self.current_monster = count
    
    def draw_section(self):
        self.scaling = min(self.scaling + 1.0, 6.0)
        self.rotation = min(self.rotation+60,300)
        with p5.push_matrix():
            p5.rect_mode(p5.CENTER)
            p5.translate(WIDTH/2, HEIGHT/2)
            p5.rotate(self.rotation)
            p5.scale(self.scaling)
            p5.fill(25,0,0,63)
            p5.stroke(255)
            p5.stroke_weight(4)
            p5.rect((0,0), TILESIZE, TILESIZE)
            p5.no_stroke()
            p5.rect_mode(p5.CORNER)
       
        if self.scaling == 6.0:
            
            
            for b in self.buttons:
                b.draw_button()
            self.choose_encounter_texte(self.text_action)
            
        self.is_open = True
        
    
    def choose_encounter_texte(self,action):
        if action == "dead":
            self.add_text("you are dead...",-2)
        elif action == "choose":
            self.add_text("Choose...",-2)
        else:
            pass

    def reset_section(self):
        super().reset_section()
        self.rotation = 0