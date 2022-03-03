
from re import T
import p5
from global_var import *
import numpy as np 

class Player:
    def __init__(self,position_x,position_y,image,set_of_images):
        self.map_position=p5.Vector(position_x,position_y)
        self.screen_midle_position=p5.Vector(position_x,position_y)
        self.image = image
        self.image_bool = True
        self.images = set_of_images
        self.current_number_of_hearts = 8
        self.number_of_hearts = 8
        self.monster_killed = 0
            
    def draw_player(self):
        #p5.image_mode(p5.CORNER)
        #p5.fill(255,64,64)
        #p5.ellipse((self.position.x*TILESIZE+10+offset_x,self.position.y*TILESIZE+10+offset_y),TILESIZE-20,TILESIZE-20)
        #p5.ellipse((offset_x,offset_y),TILESIZE,TILESIZE)
        if self.image != None:
            p5.image(self.image.blend(self.image,"blend"),self.screen_midle_position.x*TILESIZE,self.screen_midle_position.y*TILESIZE,TILESIZE,TILESIZE)

        
    
    def change_image(self,int1,int2):
        if self.image_bool:
            self.image = self.images[int1]
            self.image_bool = False
        else:
            self.image = self.images[int2]
            self.image_bool = True

    def draw_hearts(self,pos_first_x,pos_first_y):
        p5.stroke(255)
        p5.stroke_weight(4)
        for i in range(self.number_of_hearts):
            with p5.push_matrix():
                if i < self.current_number_of_hearts:
                    p5.fill(255,0,0)
                else:
                    p5.no_fill()
                p5.translate(pos_first_x+TILESIZE*i,pos_first_y)
                p5.begin_shape()
                for a in np.arange(0.0,p5.TWO_PI,0.01):
                    scale=1
                    x = scale*16*np.power(np.sin(a),3)
                    y = -scale*(13*np.cos(a)-5*np.cos(2*a)-2*np.cos(3*a)-np.cos(4*a))
                    p5.vertex(x,y)
                p5.end_shape()
        p5.no_stroke()

    
