
import p5 as p5
from Map import *
from Player import *
import numpy as np 
mymap = Map(TILEROW,TILECOL)
player = Player(0,0)
midle_tile_x = np.floor(WIDTH/TILESIZE/2)
midle_tile_y = np.floor(HEIGHT/TILESIZE/2)
img = {}
def setup():
        global img
        p5.size(WIDTH,HEIGHT)
        #p5.stroke(100)
        #rect_mode("CENTER")
        
        #mymap.rnd_grid()
        mymap.readcsv_numpy_map("./oasis_Layer1.csv")
        for x in range(1023):
                if x<10:
                        img[x]=p5.load_image(f"./map_sprites/tile00{x}.jpg")
                elif x<100:
                        img[x]=p5.load_image(f"./map_sprites/tile0{x}.jpg")
                else:        
                        img[x] = p5.load_image(f"./map_sprites/tile{x}.jpg")
                
        #ellipse_mode(CORNER)
        #mymap.worldmap[3][3] = "P"
        #print(mymap.walls)
        #print(mymap.worldmap)
        #mymap.draw_map(player.position.x*TILESIZE,player.position.y*TILESIZE)
        #set_frame_rate(4)
       

def draw():
        global img
        #p5.background(230)
        #if mouse_is_pressed:
        
        if frame_count % (3)==0:
                p5.background(240,230,140) 
                #mymap.draw_map(player.position.x*TILESIZE,player.position.y*TILESIZE)
                mymap.draw_numpy_map(player.position.x*TILESIZE,player.position.y*TILESIZE,img)
                player.draw_player(midle_tile_x*TILESIZE,midle_tile_y*TILESIZE)#
                print(f"frames:{frame_count}")
                print(f"frames Rate:{frame_rate}")
        #no_loop()
        

def key_pressed():
        if (key=="w"):
                player.position.y-=1
        if (key=="s"):
                player.position.y+=1
        if (key=="a"):
                player.position.x-=1
        if (key=="d"):
                player.position.x+=1
        
   
                

if __name__ == '__main__':
        p5.run()
