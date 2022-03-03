
import p5
from Encounter import *
from Map import *
from Player import *
from Monster import *
import numpy as np 
import os

mymap = Map(TILEROW,TILECOL)
midle_tile_x = np.floor(WIDTH/TILESIZE/2)
midle_tile_y = np.floor(HEIGHT/TILESIZE/2)
map_imgs = {}
monsters_images_sets=[]
monsters = []
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

        mymap.readcsv_numpy_map("./oasis_Layer1.csv")
        map_imgs = load_a_set_of_img("/map_sprites")
        char1_imgs = load_a_set_of_img("/sprites/char1")
        player = Player(midle_tile_x,midle_tile_y,char1_imgs[9],char1_imgs)
        
        for i in range(3):
                monsters_images_sets.append(load_a_set_of_img(f"/sprites/mons{i+1}"))
        for count in range(NBOFMONSTER):
                monsters.append(Monster(sample_of_x[count],sample_of_y[count],monsters_images_sets[np.random.choice(3)]))
        
        encounter = Encounter(monsters,player)
        
def load_a_set_of_img(path):
        img = {}
        directory = os.getcwd()
        for file in os.listdir(directory+path):
                number = "".join([s for s in list(file) if s.isdigit()])
                img[int(number)]= p5.load_image(f"{directory}{path}/{file}")
        return img

def draw():
        print(f"frames:{frame_count}")
        print(f"frames Rate:{frame_rate}")
        if not encounter.is_in_encounter:
                p5.no_loop()   
                p5.background(240,230,140) 
                mymap.draw_numpy_map(map_imgs)
                player.draw_player()
                for count in range(len(monsters)):
                        monsters[count].draw_monster(mymap.worldmap_screen_position.x,mymap.worldmap_screen_position.y)
                draw_UI()

        encounter.draw_encounter()
        if encounter.is_in_encounter:
                p5.loop()
                for b in encounter.buttons:
                        b.change_color(mouse_x,mouse_y)

def draw_UI():
        with p5.push_matrix():
                p5.translate(0,HEIGHT-TILESIZE)
                p5.fill(0)
                p5.rect((0,0),WIDTH,TILESIZE)
                p5.fill(255)
                p5.text_font(fonts[1])
                p5.text(f"Monsters left in the oasis : {len(monsters)}",TILESIZE*10,TILESIZE*0.2)
                player.draw_hearts(TILESIZE,TILESIZE/2)



def key_pressed():
        if not encounter.is_in_encounter:
                if (key=="w"):
                        world_step(0,-1)
                        player.change_image(6,3)
                        # 6,7,3 image 
                if (key=="s"):
                        world_step(0,1)
                        player.change_image(9,10)
                        #9,10,11 image 
                          
                if (key=="a"):
                        world_step(-1,0)
                        player.change_image(1,2)
                        #1,2,5
                   
                if (key=="d"):
                       world_step(1,0)
                       player.change_image(0,4)
                        #0 4 8
                       

def mouse_pressed(event):
        if encounter.is_in_encounter:
                if encounter.buttons[1].clicked_button(event.x,event.y):#escape
                        encounter.is_in_encounter=False
                        encounter.scaling = 0.0
                        world_step(0,1)
                        player.change_image(9,10)
                if encounter.buttons[0].clicked_button(event.x,event.y):#attack
                        r = np.random.random_sample()
                        if r>0.25:
                                encounter.is_in_encounter=False
                                encounter.scaling = 0.0
                                world_step(0,1)
                                player.change_image(9,10)
                                monsters.pop(encounter.current_monster)          
                        else:
                                player.current_number_of_hearts -=1
                                draw_UI()
                                if player.current_number_of_hearts<=0:
                                        encounter.text_action="dead"
                                else:
                                        encounter.add_text("Nice Try mouhahaha",0)
# def mouse_released(event):
#         print(event.x,":",event.y)

def world_step(x,y):
        player.map_position += p5.Vector(x,y)
        mymap.worldmap_screen_position += p5.Vector(x,y)
        for count in range(len(monsters)):
                if monsters[count].is_visible:
                        monsters[count].change_image()
        p5.redraw()      
        
if __name__ == '__main__':
        p5.run()
