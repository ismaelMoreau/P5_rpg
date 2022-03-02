
from os import posix_fadvise
from tkinter import Button
from turtle import pos, position
import p5
from global_var import *

class Encounter:
    def __init__(self,monsters,player):
        self.monsters = monsters 
        self.player = player
        self.is_in_encounter = False
        self.scaling = 0.0
        
        self.buttons = []
        self.buttons.append(Button("attack all fuck",WIDTH/2,HEIGHT/2+5*TILESIZE, 12*TILESIZE, 2*TILESIZE))
        self.buttons.append(Button("escape the fuck",WIDTH/2,HEIGHT/2+3*TILESIZE, 12*TILESIZE, 2*TILESIZE))

    def draw_encounter(self):
        for count in range(NBOFMONSTER):
            if self.monsters[count].is_visible:
                if self.monsters[count].map_position == self.player.map_position:
                    self.open_section()
                    if self.scaling == 12.0:
                        # +1*TILESIZE is center of the section so 5*TILESIZE mean botton of section
                        
                        for b in self.buttons:
                            b.draw_button()

                        self.add_text("Choose the \n fuck right...",-5)
                    self.is_in_encounter = True
                    
                    
    def open_section(self):
        with p5.push_matrix():
            p5.rect_mode(p5.CENTER)
            self.scaling = min(self.scaling + 1.0, 12.0)
        
            p5.translate(WIDTH/2, HEIGHT/2)
            
            p5.scale(self.scaling)
           
            p5.fill(25,0,0,63)
            p5.stroke(255)
            p5.stroke_weight(4)
            p5.rect((0,0), TILESIZE, TILESIZE)
            p5.no_stroke()
            p5.rect_mode(p5.CORNER)

    def add_text(self,label,tile_pos):
        p5.text_align(p5.CENTER)
        p5.fill(255)
        p5.no_stroke()
        #p5.text_size(64)
        p5.text(label,(WIDTH/2,HEIGHT/2+tile_pos*TILESIZE-12))


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
        p5.text(self.label,(self.x,self.y-12))
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
        