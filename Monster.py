
import p5
from global_var import *

class Monster:
    def __init__(self,position_x,position_y,images):
        self.map_position=p5.Vector(position_x,position_y)
        
        self.images = images
        self.image_bool = True
            
    def draw_monster(self,screen_x,screen_y):
        #p5.image_mode(p5.CORNER)
        #p5.fill(255,64,64)
        #p5.ellipse((self.position.x*TILESIZE+10+offset_x,self.position.y*TILESIZE+10+offset_y),TILESIZE-20,TILESIZE-20)
        #p5.ellipse((offset_x,offset_y),TILESIZE,TILESIZE)
        if (self.map_position.x*TILESIZE<screen_x*TILESIZE+WIDTH and self.map_position.y*TILESIZE<screen_y*TILESIZE+HEIGHT
                and self.map_position.x*TILESIZE>=screen_x*TILESIZE and self.map_position.y*TILESIZE>=screen_y*TILESIZE):
            p5.image(self.images[0].blend(self.images[0],"blend"),
                ((self.map_position.x - screen_x) * TILESIZE,(self.map_position.y - screen_y)*TILESIZE))

        
    
    def choose_image(self,int1,int2,img):
        if self.image_bool:
            self.image = img[int1]
            self.image_bool = False
        else:
            self.image = img[int2]
            self.image_bool = True
