# make a ball calss like bite one
import turtle
from random import randint

class Ball(turtle.Turtle):
    def __init__(self,x,y,x_movement=1,y_movement=1,color ='red'):
        super().__init__()        
        self.color(color)
        self.shape('circle')
        self.penup()
        self.shapesize(3,3)
        self.x = x
        self.y = y 
        self.x_movement = x_movement
        self.y_movement = y_movement
        self.goto(self.x,self.y)
    def reverse_x(self):
        self.x_movement *= -1

    def reverse_y(self):
        self.y_movement = self.y_movement * -1
        
        
    def movement(self):
        self.x = self.x + self.x_movement
        self.y = self.y + self.y_movement
        self.goto(self.x,self.y)




if __name__ == "__main__":

    b = Ball(0,0)

#constant moving
    while True:
        b.movement()
        if b.xcor()>800 or b.xcor()<-800:
            b.reverse_x()
        if b.ycor()>500 or b.ycor()<-500:
            b.reverse_y()
        print(b.xcor(),b.ycor())
        

    

    turtle.mainloop()
