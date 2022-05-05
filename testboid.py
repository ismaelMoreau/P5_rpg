
import p5
from settings import *
import numpy as np

boids = []

r = 2.0
maxspeed = 2
maxforce = 0.03

def setup():
    for i in range(30):
        angle = np.pi * np.random.uniform(0, 2)
        velocity = np.array([np.cos(angle),np.sin(angle)])

        boids.append([np.array([50.0,50.0]),np.array([0.0,0.0]),velocity])

def draw():
    print(f"frames:{frame_count}")
    print(f"frames Rate:{frame_rate}")
    p5.background(50)
    for b in boids:
        b[0],b[1],b[2] = run(boids,b[0],b[1],b[2])


def run(boids,position,acceleration,velocity):
    sep = separate(boids,position,velocity)
    ali = align(boids,position,velocity)
    coh = cohesion(boids,position,velocity)

    sep = sep*1.5
    ali = ali*1.0
    coh = coh*1.0
    acceleration += sep
    acceleration += ali
    acceleration += coh

    #self.update()
    velocity += acceleration 
    velocity = np.clip(velocity,0,maxspeed)
    position += velocity
    acceleration *= 0
    
    #self.borders()
    if (position[0] < -2): position[0] = WIDTH+2
    if (position[1] < -2): position[1] = HEIGHT+2
    if (position[0] > WIDTH+2): position[0] = -2
    if (position[1] > HEIGHT+2): position[1] = -2
    
    #self.render()
    #with p5.push_matrix():
        #p5.translate(self.position.x,self.position.y)
    #p5.image(self.img,self.position.x,self.position.y,6,6)
    
        # p5.stroke(255)
        # p5.fill(255)
    p5.ellipse(position[0], position[1], 8, 8)
    return position,acceleration,velocity


def seek(target,position,velocity):
    desired = target - position
    desired = desired / np.linalg.norm(desired)
    desired *= maxspeed
    steer = desired - velocity
    steer= np.clip(steer,0,maxforce)
    return steer


    




def separate(boids,position,velocity):
    desiredseparation = 10
    steer = np.array([0.0,0.0])
    count = 0
    for b in boids:
        d = np.linalg.norm(position-b[0])
        if ((d > 0) and (d < desiredseparation)):
            diff = position-b[0]
            diff = diff / np.linalg.norm(diff)
            diff = diff.__truediv__(d)
            steer += diff
            count+=1
    if count > 0:
        steer = steer.__truediv__(count)
    if np.linalg.norm(steer) > 0.0 :
        steer = steer / np.linalg.norm(steer)
        steer = steer *maxspeed
        steer -= velocity
        steer= np.clip(steer,0,maxforce)
    return steer

def align(boids,position,velocity):
    neighbordist = 20
    sum  = np.array([0.0,0.0])
    count = 0
    for b in boids:
        d = np.linalg.norm(position-b[0])
        if ((d > 0) and (d < neighbordist)):
            sum += b[2]
            count+=1
    if count> 0:
        sum = sum.__truediv__(count)
        sum = sum / np.linalg.norm(sum)
        sum = sum * maxspeed
        steer = sum - velocity
        steer = np.clip(steer,0,maxforce)
        return steer
    else:
        r = np.array([0.0,0.0])
        return r

def cohesion(boids,position,velocity):
    neighbordist = 20
    sum  = np.array([0.0,0.0])
    count = 0
    for b in boids:
        d = np.linalg.norm(position-b[0])
        if ((d > 0) and (d < neighbordist)):
            sum += b[0]
            count+=1 
    if (count > 0):
        sum = sum.__truediv__(count) ##############################division ne semble pas etre implemente ds p5
        return seek(sum,position,velocity)
    else:
        return np.array([0.0,0.0])

if __name__ == '__main__':
        p5.run()
