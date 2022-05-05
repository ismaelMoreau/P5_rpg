
#  Flocking 
#  by Daniel Shiffman.  
 
#  An implementation of Craig Reynold's Boids program to simulate
#  the flocking behavior of birds. Each boid steers itself based on 
#  rules of avoidance, alignment, and coherence.
 
#  Click the mouse to add a new boid.

from Boid_not_optimized_cuz_python import *
class Flock:
    def __init__(self) -> None:
        self.boids = []

    def run(self):
        for b in self.boids:
            b.run(self.boids)

    def add_boid(self,x,y,img):
        self.boids.append(Boid(x,y,img))