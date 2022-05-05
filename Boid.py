
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
     
    
    def run(self,boids):
        r = 20.0
        maxspeed = 20
        maxforce = 0.1
        sep = self.separate(boids,maxspeed,maxforce)
        ali = self.align(boids,maxspeed,maxforce)
        coh = self.cohesion(boids,maxspeed,maxforce)

        sep*=1.5

        self.acceleration += sep
        self.acceleration += ali
        self.acceleration += coh
 
        #self.update()
        self.velocity += self.acceleration 
        self.velocity.limit(maxspeed)
        self.position += self.velocity
        self.acceleration *= 0
        
        #self.borders()
        if (self.position.x < -r): self.position.x = WIDTH+r
        if (self.position.y < -r): self.position.y = HEIGHT+r
        if (self.position.x > WIDTH+r): self.position.x = -r
        if (self.position.y > HEIGHT+r): self.position.y = -r
        
        #self.render()
        #with p5.push_matrix():
            #p5.translate(self.position.x,self.position.y)
        p5.image(self.img,self.position.x,self.position.y,64,64)
        
            # p5.stroke(255)
            # p5.fill(255)
        #p5.ellipse(self.position.x, self.position.y, 4, 4)


    
    def seek(self,target,maxspeed,maxforce):
        desired = target - self.position
        desired = desired.normalize()
        desired *= maxspeed
        steer = desired - self.velocity
        steer.limit(maxforce)
        return steer
    

      
    


    
    def separate(self,boids,maxspeed,maxforce):
        desiredseparation = 100
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
            steer = steer *maxspeed
            steer -= self.velocity
            steer.limit(maxforce)
        return steer
    
    def align(self,boids,maxspeed,maxforce):
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
            sum = sum *maxspeed
            steer = sum - self.velocity
            steer.limit(maxforce)
            return steer
        else:
            r = p5.Vector(0,0)
            return r

    def cohesion(self,boids,maxspeed,maxforce):
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
            return self.seek(sum,maxspeed,maxforce)
        else:
            return p5.Vector(0,0)
