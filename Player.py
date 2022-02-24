
import p5
from global_var import *

class Player:
    def __init__(self,position_x,position_y,image,set_of_images):
        self.map_position=p5.Vector(position_x,position_y)
        self.screen_midle_position=p5.Vector(position_x,position_y)
        self.image = image
        self.image_bool = True
        self.images = set_of_images
            
    def draw_player(self):
        #p5.image_mode(p5.CORNER)
        #p5.fill(255,64,64)
        #p5.ellipse((self.position.x*TILESIZE+10+offset_x,self.position.y*TILESIZE+10+offset_y),TILESIZE-20,TILESIZE-20)
        #p5.ellipse((offset_x,offset_y),TILESIZE,TILESIZE)
        if self.image != None:
            p5.image(self.image.blend(self.image,"blend"),(self.screen_midle_position.x*TILESIZE,self.screen_midle_position.y*TILESIZE))

        
    
    def choose_image(self,int1,int2):
        if self.image_bool:
            self.image = self.images[int1]
            self.image_bool = False
        else:
            self.image = self.images[int2]
            self.image_bool = True
