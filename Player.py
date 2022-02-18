import p5 as p5
from global_var import *

class Player:
    def __init__(self,position_x,position_y):
        self.position=p5.Vector(position_x,position_y)
            
    def draw_player(self,offset_x,offset_y):
        p5.ellipse_mode(p5.CORNER)
        p5.fill(255,64,64)
        #p5.ellipse((self.position.x*TILESIZE+10+offset_x,self.position.y*TILESIZE+10+offset_y),TILESIZE-20,TILESIZE-20)
        p5.ellipse((offset_x,offset_y),TILESIZE,TILESIZE)