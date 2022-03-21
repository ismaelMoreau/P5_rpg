
import p5
from Monster import Monster
from settings import *

#TODO base class and ineheritance for different sections
class Section_panel:
    def __init__(self,monsters,player,type):
        self.monsters = monsters 
        self.player = player
        self.is_open = False
        self.scaling = 0.0
        self.scale_multiply = 6
        self.current_monster = 0
        self.buttons = []
        self.type = type
        if type == "encounter":
            self.buttons.append(Button("attack",WIDTH/2,HEIGHT/2+2.5*TILESIZE, 6*TILESIZE, TILESIZE))
            self.buttons.append(Button("escape",WIDTH/2,HEIGHT/2+1.5*TILESIZE, 6*TILESIZE, TILESIZE))
            self.text_action = "choose"
        else:
            self.buttons.append(Button("Begin",WIDTH/2,HEIGHT/2+2.5*TILESIZE, 6*TILESIZE, TILESIZE))
            self.is_open = True

    def draw_section(self):
        if self.type == "encounter":
            for count in range(len(self.monsters)):
                if self.monsters[count].is_visible:
                    if self.monsters[count].map_position == self.player.map_position:
                        self.open_section()
                        if self.scaling == 6.0:
                           
                            
                            for b in self.buttons:
                                b.draw_button()
                            self.choose_encounter_texte(self.text_action)
                            
                        self.is_open = True
                        self.current_monster = count
        elif self.type == "begin_section":
            self.open_section()
            if self.scaling == 6.0:
            
                for b in self.buttons:
                    b.draw_button()
                self.add_text("\n \nattack = \n 50 percent chances \n\ng key add green tile \n \nb key add a bubble \n \np key remove bubble \n \nr key reset bubbles" ,-3)
                #self.add_text("agent rules: \n to die on sand \n monte carlos algo \n egreedy policy",0)
                    
    def open_section(self):
        with p5.push_matrix():
            p5.rect_mode(p5.CENTER)
            self.scaling = min(self.scaling + 1.0, 6.0)
        
            p5.translate(WIDTH/2, HEIGHT/2)
            
            p5.scale(self.scaling)
           
            p5.fill(25,0,0,63)
            p5.stroke(255)
            p5.stroke_weight(4)
            p5.rect((0,0), TILESIZE, TILESIZE)
            p5.no_stroke()
            p5.rect_mode(p5.CORNER)

    def choose_encounter_texte(self,action):
        if action == "dead":
            self.add_text("you are dead...",-2)
        elif action == "choose":
            self.add_text("Choose...",-2)
        else:
            pass

    def add_text(self,label,tile_pos):
        # PARAMETRE tile_pos = 1*TILESIZE is center of the section so 5*TILESIZE mean botton of section
        p5.text_align(p5.CENTER)
        p5.fill(255)
        p5.no_stroke()
        p5.text(label,(WIDTH/2,HEIGHT/2+tile_pos*TILESIZE-6))
        p5.text_align(p5.CORNER)

class Button:
    def __init__(self,label,position_x,position_y,width,height):
        self.color = 0
        self.label = label
        self.label_color = 255
        self.x = position_x
        self.y = position_y
        self.w = width
        self.h = height

    def draw_button(self):
        #p5.rect_mode(p5.CENTER)
        #p5.translate(WIDTH/2, HEIGHT/2)
        p5.rect_mode(p5.CENTER)
        p5.fill(self.color)
        p5.stroke(255)
        p5.stroke_weight(4)
        p5.rect((self.x,self.y),self.w, self.h)
        p5.text_align(p5.CENTER)
        p5.fill(self.label_color)
        p5.no_stroke()
        #p5.text_size(64)
        p5.text(self.label,(self.x,self.y-20))
        p5.rect_mode(p5.CORNER)

    def change_color(self,mouse_x,mouse_y):
        if(mouse_x > self.x -self.w/2 and mouse_y > self.y-self.h/2 
            and mouse_x< self.x +self.w/2 and mouse_y < self.y+self.h/2 ):
            self.color = 255
            self.label_color = 0
        else:
            self.color = 0
            self.label_color = 255
    
    def clicked_button(self,mouse_x,mouse_y):
        if(mouse_x > self.x -self.w/2 and mouse_y > self.y-self.h/2 
           and mouse_x< self.x +self.w/2 and mouse_y < self.y+self.h/2 ):
            return True
    

        