
import p5
from global_var import *

class Monster:
    def __init__(self,position_x,position_y,images):
        self.map_position=p5.Vector(position_x,position_y)
        self.is_visible=False
        self.images = images
        self.image_bool = True
        self.image_number = 0
    def draw_monster(self,screen_x,screen_y):
        #p5.image_mode(p5.CORNER)
        #p5.fill(255,64,64)
        #p5.ellipse((self.position.x*TILESIZE+10+offset_x,self.position.y*TILESIZE+10+offset_y),TILESIZE-20,TILESIZE-20)
        #p5.ellipse((offset_x,offset_y),TILESIZE,TILESIZE)
        if (not(self.map_position.x*TILESIZE<screen_x*TILESIZE+WIDTH) or not (self.map_position.y*TILESIZE<screen_y*TILESIZE+HEIGHT)
                or not(self.map_position.x*TILESIZE>=screen_x*TILESIZE) or not(self.map_position.y*TILESIZE>=screen_y*TILESIZE)):
                self.is_visible = False
                return
        p5.image(self.images[self.image_number].blend(self.images[self.image_number],"blend"),
            (self.map_position.x - screen_x) * TILESIZE,(self.map_position.y - screen_y)*TILESIZE,TILESIZE,TILESIZE)
        self.is_visible = True
        
    
    def change_image(self):
        if self.image_number >= len(self.images)-1:
            self.image_number = 0
        else:
            self.image_number +=1 
