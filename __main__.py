
import p5
from Section_panel import *
from Map import *
from Player import *
from Monster import *
from Agent_monte_carlos import *
import numpy as np 
import os
import time


mymap = Map(TILEROW,TILECOL)
midle_tile_x = np.floor(WIDTH/TILESIZE/2)
midle_tile_y = np.floor(HEIGHT/TILESIZE/2)
map_imgs = {}
monsters_images_sets=[]
monsters = []

arr= np.arange(30,70)#centered monsters's position 
sample_of_x = np.random.choice(arr,NBOFMONSTER)

sample_of_y = np.random.choice(arr,NBOFMONSTER)
fonts = []
bubbles =[]
def setup():
        global player
        global map_imgs
        global encounter
        global fonts
        global begin_section
        global bubbles
        global agent_imgs

        p5.size(WIDTH,HEIGHT)
        fonts.append(p5.create_font("./fonts/JosefinSans-Bold.ttf",32))
        fonts.append(p5.create_font("./fonts/Baloo-Regular.ttf",32))
        p5.text_font(fonts[0])

        mymap.readcsv_numpy_map("./oasis_Layer1.csv")
        map_imgs = load_a_set_of_img("/map_sprites")
        # mymap.rnd_grid()
        # mymap.get_walls()

        char1_imgs = load_a_set_of_img("/sprites/char1")
        agent_imgs = load_a_set_of_img("/sprites/agent1")
        player = Player(midle_tile_x+mymap.worldmap_screen_position.x,midle_tile_y+mymap.worldmap_screen_position.y,char1_imgs[9],char1_imgs)
        
        for i in range(3):
                monsters_images_sets.append(load_a_set_of_img(f"/sprites/mons{i+1}"))
        for count in range(NBOFMONSTER):
                monsters.append(Monster(sample_of_x[count],sample_of_y[count],monsters_images_sets[np.random.choice(3)]))
        
        encounter = Section_panel(monsters,player,"encounter")
        begin_section = Section_panel(monsters,player,"begin_section")
        for nb_bubs in range(NBOFAGENT1):
                bubbles.append(Agent_monte_carlos(TILEROW,TILECOL,50+np.random.randint(-5,5),50+np.random.randint(-5,5),mymap.worldmap,monsters,agent_imgs))
def load_a_set_of_img(path):
        img = {}
        directory = os.getcwd()
        for file in os.listdir(directory+path):
                number = "".join([s for s in list(file) if s.isdigit()])
                img[int(number)]= p5.load_image(f"{directory}{path}/{file}")
        return img

def draw():
        #print(f"frames:{frame_count}")
        #print(f"frames Rate:{frame_rate}")
        if not encounter.is_open and not begin_section.is_open:
                p5.no_loop()   
                p5.background(240,230,140) 
                mymap.draw_numpy_map(map_imgs)
                #mymap.draw_map(map_imgs)
                player.draw_player()
                for count in range(len(monsters)):
                        monsters[count].draw_monster(mymap.worldmap_screen_position.x,mymap.worldmap_screen_position.y)
                draw_UI()
                for count in range(len(bubbles)):
                        bubbles[count].draw_agent(mymap.worldmap_screen_position.x,mymap.worldmap_screen_position.y)
        if begin_section.is_open:
                #mymap.draw_numpy_map(map_imgs)
                p5.background(240,230,140) 
                player.draw_player()
                begin_section.draw_section()
        encounter.draw_section()
        if encounter.is_open:
                p5.loop()
                for b in encounter.buttons:
                        b.change_color(mouse_x,mouse_y)
        elif begin_section.is_open:
                p5.loop()
                for b in begin_section.buttons:
                        b.change_color(mouse_x,mouse_y)


def draw_UI():
        with p5.push_matrix():
                p5.translate(0,HEIGHT-TILESIZE)
                p5.fill(0)
                p5.rect((0,0),WIDTH,TILESIZE)
                p5.fill(255)
                p5.text_font(fonts[1])
                p5.text(f"Monsters left in the oasis : {len(monsters)}",TILESIZE*5,TILESIZE*0.2)
                for i,b in enumerate(bubbles):
                        p5.text(f"Bubble {i}:lvl {b.lvl}",TILESIZE*(13+(i*4)),TILESIZE*0.2)
                player.draw_hearts(TILESIZE,TILESIZE/2)



def key_pressed():
        if not encounter.is_open:#there is only one ai for now
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
                if (key =="g") and  mymap.worldmap[int(player.map_position.x),int(player.map_position.y)]==-1:
                        world_step(0,0)
                        mymap.worldmap[int(player.map_position.x),int(player.map_position.y)]=292
                if (key =="r"):
                        for b in bubbles:
                                b.agent_start_position_x = int(player.map_position.x)
                                b.agent_start_position_y = int(player.map_position.y)
                                b.total_reset()
                        world_step(0,0)
                if (key =="b"):
                        bubbles.append(Agent_monte_carlos(TILEROW,TILECOL,int(player.map_position.x), int(player.map_position.y),mymap.worldmap,monsters,agent_imgs))
                        world_step(0,0)
                if (key =="p"):
                        if len(bubbles)> 0:
                                bubbles.pop()
                        world_step(0,0)
#todo a reecrire..
def mouse_pressed(event):
        if encounter.is_open:
                if encounter.buttons[1].clicked_button(event.x,event.y):#escape
                        encounter.is_open=False
                        encounter.scaling = 0.0
                        world_step(0,1)
                        player.change_image(9,10)
                if encounter.buttons[0].clicked_button(event.x,event.y):#attack
                        r = np.random.random_sample()
                        if r>0.50:
                                encounter.is_open=False
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
        elif begin_section.is_open:
                if begin_section.buttons[0].clicked_button(event.x,event.y):#begin
                        begin_section.is_open=False
#         print(event.x,":",event.y)

def world_step(x,y):
        player.map_position += p5.Vector(x,y)
        mymap.worldmap_screen_position += p5.Vector(x,y)
        for count in range(len(monsters)):
                if monsters[count].is_visible:
                        monsters[count].change_image()
        ai_think_or_move()
        p5.redraw()      

def ai_think_or_move():
        for count in range(len(bubbles)):
                bubbles[count].real_step(bubbles[count].agent_position_x,bubbles[count].agent_position_y)
                #bubbles[count].step_max_by_episode = int(0.25*(abs((len(monsters)-1)-NBOFMONSTER)*STARTINGNUMBEROFMOVESBYEPISODE))
               
                print(bubbles[count].Q_table[bubbles[count].agent_position_x,bubbles[count].agent_position_y])

if __name__ == '__main__':
        p5.run()
