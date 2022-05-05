
import p5
from Particle import *
class ParticleSysteme:
    def __init__(self,x,y) -> None:
        self.origin = p5.Vector(x,y)
        self.particles = []
        self.end = False
    
    def add_particle(self,nb):
        for p in range(nb):
            self.particles.append(Particle(self.origin.x,self.origin.y))
    
    def set_position(self,x,y):
        self.origin = p5.Vector(x,y) 

    def run(self):
        for i in range(len(self.particles)-1,0,-1):
            self.particles[i].run()
            if self.particles[i].is_dead():
                self.particles.pop(i)
        if len(self.particles) == 0:
            self.end = True    

        
