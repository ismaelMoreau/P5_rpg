
import p5
from Agent2 import *
from Map import *
from Player import *
from Monster import *
import numpy as np 
import os
mymap = Map(TILEROW,TILECOL)

#agent = Agent1()
midle_tile_x = np.floor(WIDTH/TILESIZE/2)
midle_tile_y = np.floor(HEIGHT/TILESIZE/2)
map_img = {}
monsters_images_sets={}
monster = {}
sample_of_x = np.random.choice(TILEROW,NBOFMONSTER)
sample_of_y = np.random.choice(TILECOL,NBOFMONSTER)
def setup():
        global player
        global map_img
        
        
        p5.size(WIDTH,HEIGHT)
        #p5.stroke(100)
        #rect_mode("CENTER")
        #mymap.rnd_grid()
        mymap.readcsv_numpy_map("./oasis_Layer1.csv")
        map_img = load_a_set_of_img("/map_sprites")
        char1_imgs = load_a_set_of_img("/sprites/char1")
     
        #print(f"{midle_tile_x}:{midle_tile_y}")
        player = Player(midle_tile_x,midle_tile_y,char1_imgs[9],char1_imgs)
        for i in range(4):
                monsters_images_sets[i] = load_a_set_of_img(f"/sprites/mons{i+1}")
        
        for count in range(NBOFMONSTER):
                monster[count] = Monster(sample_of_x[count],sample_of_y[count],monsters_images_sets[np.random.choice(4)])
        
        #ellipse_mode(CORNER)
        #mymap.worldmap[3][3] = "P"
        #print(mymap.walls)
        #print(mymap.worldmap)
        #mymap.draw_map(player.position.x*TILESIZE,player.position.y*TILESIZE)
        #set_frame_rate(4)
def load_a_set_of_img(path):
        img = {}
        directory = os.getcwd()
        for file in os.listdir(directory+path):
                number = "".join([s for s in list(file) if s.isdigit()])
                img[int(number)]= p5.load_image(f"{directory}{path}/{file}")
                
        # if  bool(img_mask):
                
        #         for idx in sorted(img.keys()):
        #                 i = img[idx]
        #                 j= img_mask[idx]
        #                 img[idx]= i.mask(j)
        return img


def draw():
      
        #p5.background(230)
        #if mouse_is_pressed:
        
        if frame_count % (3)==0:
                p5.background(240,230,140) 
                #mymap.draw_map(player.position.x*TILESIZE,player.position.y*TILESIZE)
                mymap.draw_numpy_map(map_img)
                player.draw_player()
                for count in range(NBOFMONSTER):
                        monster[count].draw_monster(mymap.worldmap_screen_position.x,mymap.worldmap_screen_position.y)
                        
                #img = char1_imgs[1]
                #img.blend(img[1],"blend")
                
                #agent.draw_agent()
                print(f"frames:{frame_count}")
                print(f"frames Rate:{frame_rate}")
        #no_loop()
        

def key_pressed():
        if (key=="w"):
                player.map_position.y-=1
                player.choose_image(6,3)
                mymap.worldmap_screen_position.y-=1
            
                # 6,7,3
        if (key=="s"):
                player.map_position.y+=1
                mymap.worldmap_screen_position.y+=1

                #9,10,11
                player.choose_image(9,10)
  
        if (key=="a"):
                player.map_position.x-=1
                mymap.worldmap_screen_position.x-=1

                #1,2,5
                player.choose_image(1,2)
          
        if (key=="d"):
                player.map_position.x+=1
                mymap.worldmap_screen_position.x+=1
                #0 4 8
                player.choose_image(0,4)
             



        
if __name__ == '__main__':
        p5.run()
