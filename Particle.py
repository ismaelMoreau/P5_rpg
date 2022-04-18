from mimetypes import init
import p5

class Particle():
    def __init__(self,x,y) -> None:
        self.acceleration = p5.Vector(0, 0.25)
        self.velocity = p5.Vector(p5.random_uniform(-5, 5), p5.random_uniform(-5, 0))
        self.position = p5.Vector(x,y)
        self.origin = p5.Vector(x,y)
        self.lifespan = 255.0;
    def run(self):
        self.update()
        self.display()
    def update(self):
        self.velocity += self.acceleration 
        self.position += self.velocity
        self.lifespan -= 20.0
    def display(self):
        p5.stroke(255, self.lifespan)
        p5.fill(255, self.lifespan)
        p5.ellipse(self.position.x, self.position.y, 4, 4)
    def is_dead(self):
        if (self.lifespan < 0.0) or self.position.x > self.origin.x+20 or self.position.x < self.origin.x - 20 or self.position.y > self.origin.y+20 or self.position.y < self.origin.y - 20: 
            return True
        else: 
            return False
        