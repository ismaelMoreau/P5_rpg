
import p5
from Agent2 import *
from Encounter import Encounter
from Map import *
from Player import *
from Monster import *
import numpy as np 
import os
mymap = Map(TILEROW,TILECOL)

#agent = Agent1()
midle_tile_x = np.floor(WIDTH/TILESIZE/2)
midle_tile_y = np.floor(HEIGHT/TILESIZE/2)
map_imgs = {}
monsters_images_sets={}
monsters = {}
sample_of_x = np.random.choice(TILEROW,NBOFMONSTER)
sample_of_y = np.random.choice(TILECOL,NBOFMONSTER)
fonts = []
def setup():
        global player
        global map_imgs
        global encounter
        global fonts
        
        p5.size(WIDTH,HEIGHT)
        fonts.append(p5.create_font("./fonts/JosefinSans-Bold.ttf",32))
        fonts.append(p5.create_font("./fonts/Baloo-Regular.ttf",32))
        
        p5.text_font(fonts[0])
        #p5.stroke(100)
        #rect_mode("CENTER")
        #mymap.rnd_grid()
        mymap.readcsv_numpy_map("./oasis_Layer1.csv")
        map_imgs = load_a_set_of_img("/map_sprites")
        char1_imgs = load_a_set_of_img("/sprites/char1")
     
        #print(f"{midle_tile_x}:{midle_tile_y}")
        player = Player(midle_tile_x,midle_tile_y,char1_imgs[9],char1_imgs)
        
        for i in range(3):
                monsters_images_sets[i] = load_a_set_of_img(f"/sprites/mons{i+1}")
        
        for count in range(NBOFMONSTER):
                monsters[count]=Monster(sample_of_x[count],sample_of_y[count],monsters_images_sets[np.random.choice(3)])
        encounter = Encounter(monsters,player)
        
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
        
        #if frame_count % (3)==0:
        print(f"frames:{frame_count}")
        print(f"frames Rate:{frame_rate}")
        if not encounter.is_in_encounter:
                p5.no_loop()   
                p5.background(240,230,140) 
                #mymap.draw_map(player.position.x*TILESIZE,player.position.y*TILESIZE)
                
                mymap.draw_numpy_map(map_imgs)
                player.draw_player()
                for count in range(NBOFMONSTER):
                        monsters[count].draw_monster(mymap.worldmap_screen_position.x,mymap.worldmap_screen_position.y)
                draw_UI()
                
                #img = char1_imgs[1]
                #img.blend(img[1],"blend")
                
                #agent.draw_agent()
                
        #no_loop()
        
        encounter.draw_encounter()
        if encounter.is_in_encounter:
                p5.loop()
                for b in encounter.buttons:
                        b.change_color(mouse_x,mouse_y)
def draw_UI():
        with p5.push_matrix():
                p5.translate(0,HEIGHT-TILESIZE*2)
                p5.fill(0)
                p5.rect((0,0),WIDTH,TILESIZE*2)
                p5.fill(255)
                p5.text_font(fonts[1])
                p5.text("HP",TILESIZE,TILESIZE*0.2)
                player.draw_hearts(TILESIZE*3.5,TILESIZE)



def key_pressed():
        if not encounter.is_in_encounter:
                if (key=="w"):
                        world_step(0,-1)
                        player.choose_image(6,3)
                        # 6,7,3
                if (key=="s"):
                        world_step(0,1)
                        player.choose_image(9,10)
                        #9,10,11
                          
                if (key=="a"):
                        world_step(-1,0)
                        player.choose_image(1,2)
                        #1,2,5
                   
                if (key=="d"):
                       world_step(1,0)
                       player.choose_image(0,4)
                        #0 4 8
                       

def mouse_pressed(event):
        if encounter.is_in_encounter:
                if encounter.buttons[1].clicked_button(event.x,event.y):
                        encounter.is_in_encounter=False
                        encounter.scaling = 0.0
                
                        # if not encounter.is_in_encounter:
                        world_step(0,1)
                        player.choose_image(9,10)

def mouse_released(event):
        print(event.x,":",event.y)
def world_step(x,y):
        
        player.map_position += p5.Vector(x,y)
        
        mymap.worldmap_screen_position += p5.Vector(x,y)
        for count in monsters:
                if monsters[count].is_visible:
                        monsters[count].change_image()
        p5.redraw()      
        
if __name__ == '__main__':
        p5.run()
