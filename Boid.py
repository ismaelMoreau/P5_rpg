
#  Flocking 
#  by Daniel Shiffman.  
 
#  An implementation of Craig Reynold's Boids program to simulate
#  the flocking behavior of birds. Each boid steers itself based on 
#  rules of avoidance, alignment, and coherence.
 
#  Click the mouse to add a new boid.
import p5
import numpy as np
from settings import *
class Boid:
    def __init__(self,x,y,img=None) -> None:
        self.acceleration = p5.Vector(0, 0)

        self.img = img
        angle = np.pi * np.random.uniform(0, 2)
        self.velocity = p5.Vector(np.cos(angle),np.sin(angle))

        self.position = p5.Vector(x,y)
        self.r = 2.0
        self.maxspeed = 2
        self.maxforce = 0.03
    
    def run(self,boids):
        sep = self.separate(boids)
        ali = self.align(boids)
        coh = self.cohesion(boids)

        sep*=1.5

        self.acceleration += sep
        self.acceleration += ali
        self.acceleration += coh
 
        #self.update()
        self.velocity += self.acceleration 
        self.velocity.limit(self.maxspeed)
        self.position += self.velocity
        self.acceleration *= 0
        
        #self.borders()
        if (self.position.x < -2): self.position.x = WIDTH+2
        if (self.position.y < -2): self.position.y = HEIGHT+2
        if (self.position.x > WIDTH+2): self.position.x = -2
        if (self.position.y > HEIGHT+2): self.position.y = -2
        
        #self.render()
        #with p5.push_matrix():
            #p5.translate(self.position.x,self.position.y)
        p5.image(self.img,self.position.x,self.position.y,64,64)
        
            # p5.stroke(255)
            # p5.fill(255)
        #p5.ellipse(self.position.x, self.position.y, 4, 4)


    
    def seek(self,target):
        desired = target - self.position
        desired = desired.normalize()
        desired *= self.maxspeed
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        return steer
    

      
    


    
    def separate(self,boids):
        desiredseparation = 50
        steer = p5.Vector(0,0,0)
        count = 0
        for b in boids:
            d = self.position.dist(b.position)
            if ((d > 0) and (d < desiredseparation)):
                diff = self.position-b.position
                diff = diff.normalize()
                diff = diff.__truediv__(d)
                steer += diff
                count+=1
        if count > 0:
            steer = steer.__truediv__(count)
        if steer.magnitude > 0.0 :
            steer.normalize()
            steer = steer *self.maxspeed
            steer -= self.velocity
            steer.limit(self.maxforce)
        return steer
    
    def align(self,boids):
        neighbordist = 75
        sum  = p5.Vector(0,0)
        count = 0
        for b in boids:
            d = self.position.dist(b.position)
            if ((d > 0) and (d < neighbordist)):
                sum += b.velocity
                count+=1
        if count> 0:
            sum = sum.__truediv__(count)
            sum.normalize()
            sum = sum *self.maxspeed
            steer = sum - self.velocity
            steer.limit(self.maxforce)
            return steer
        else:
            r = p5.Vector(0,0)
            return r

    def cohesion(self,boids):
        neighbordist = 75
        sum  = p5.Vector(0,0)
        count = 0
        for b in boids:
            d = self.position.dist(b.position)
            if ((d > 0) and (d < neighbordist)):
                sum += b.position
                count+=1 
        if (count > 0):
            sum = sum.__truediv__(count)
            return self.seek(sum)
        else:
            return p5.Vector(0,0)
