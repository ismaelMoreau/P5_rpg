import p5
class Section_Button:
    def __init__(self,label,position_x,position_y,width,height):
        self.color = 0
        self.label = label
        self.label_color = 255
        self.x = position_x
        self.y = position_y
        self.w = width
        self.h = height

    def draw_button(self):
        #p5.rect_mode(p5.CENTER)
        #p5.translate(WIDTH/2, HEIGHT/2)
        p5.rect_mode(p5.CENTER)
        p5.fill(self.color)
        p5.stroke(255)
        p5.stroke_weight(4)
        p5.rect((self.x,self.y),self.w, self.h)
        p5.text_align(p5.CENTER)
        p5.fill(self.label_color)
        p5.no_stroke()
        #p5.text_size(64)
        p5.text(self.label,(self.x,self.y-20))
        p5.rect_mode(p5.CORNER)

    def change_color(self,mouse_x,mouse_y):
        if(mouse_x > self.x -self.w/2 and mouse_y > self.y-self.h/2 
            and mouse_x< self.x +self.w/2 and mouse_y < self.y+self.h/2 ):
            self.color = 255
            self.label_color = 0
        else:
            self.color = 0
            self.label_color = 255
    
    def clicked_button(self,mouse_x,mouse_y):
        if(mouse_x > self.x -self.w/2 and mouse_y > self.y-self.h/2 
           and mouse_x< self.x +self.w/2 and mouse_y < self.y+self.h/2 ):
            return True


        