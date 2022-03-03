from random import randint, choice
from global_var import *
import p5
import pandas as pd
import numpy as np
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = self.get_walls()
        self.tile_size = TILESIZE
        self.worldmap = []
        self.worldmap_screen_position =p5.Vector(0,0)

    def rnd_grid(self, width=2):
      
        for x in range(self.height):
            row_tmp = []
            for y in range(self.width):
                if (x, y) in self.walls:
                    row_tmp.append('#')#("%%-%ds" % width % '#', end="")
                else:
                    row_tmp.append('.')#("%%-%ds" % width % '.', end="")
            self.worldmap.append(row_tmp)
        #print(self.worldmap)


    def get_walls(self, pct=.3):
            """ pct is the percentage of the map covered by walls """
            out = []
            for i in range(int(self.height*self.width*pct)//2):

                x = randint(1, self.width-1)
                y = randint(1, self.height-2)
                """ We make two pieces of wall based on the same random x and y
                    but adding a bit of noise in order to have passages and more
                    cave-looking walls"""
                
                out.append((x, y))
                out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
            return out

    def draw_map(self,imgs):
        p5.fill(0)
        for row_index,row in enumerate(self.worldmap):
                #print(row,row_index)
                for col_index,col in enumerate(row):
                        #print(col,col_index)
                        x = col_index * TILESIZE - self.worldmap_screen_position.x * TILESIZE
                        y = row_index * TILESIZE - self.worldmap_screen_position.y * TILESIZE
                        if col == "#" and x<WIDTH and y<HEIGHT and x>0 and y>0:
                            p5.rect((x,y),TILESIZE,TILESIZE)
                            #p5.image(imgs[np.random.randint(0,600)], x, y,TILESIZE,TILESIZE)
                        # if int(col) < 600 and x<WIDTH and y<HEIGHT and x>0 and y>0:
                        #     p5.rect((x,y),TILESIZE,TILESIZE)
                        
                        # if col == "P":
                        #         fill(255,64,64)
                        #         ellipse((x+10,y+10),mymap.tile_size-10,mymap.tile_size-10) 
    def readcsv_numpy_map(self,path):
        tmp = pd.read_csv(path)
        self.worldmap = tmp.to_numpy()
        #print(self.worldmap)

    def draw_numpy_map(self,img):
        p5.fill(0)
        for index,data in np.ndenumerate(self.worldmap):
            x = index[0] * TILESIZE - self.worldmap_screen_position.x * TILESIZE
            y = index[1] * TILESIZE - self.worldmap_screen_position.y * TILESIZE
            #TILESIZE*2 is the place for ui
            if data != -1 and data != 10000 and x<WIDTH and y<HEIGHT-TILESIZE and x>=0 and y>=0:
                p5.image(img[data], x, y,TILESIZE,TILESIZE)
            # elif data == 10000 and x<WIDTH and y<HEIGHT and x>0 and y>0:
            #     p5.rect((x,y),TILESIZE,TILESIZE) 
                #p5.rect((x,y),TILESIZE,TILESIZE) 
            