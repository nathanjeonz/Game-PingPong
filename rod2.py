# make rod classand set shapesize to 5,2 ... left rogt ,, goto(x,y)
import turtle


class Rod2(turtle.Turtle):
    def __init__(self,c='red'):
        super().__init__()        
        self.color('Black')
        self.shape('square')
        self.penup()
        self.shapesize(1,7)
        self.setheading(90)
        self.color(c)
        self.goto(700,0)
        
    def move_up2(self):
        self.forward(50)
    def move_down2(self):
        self.forward(-50)

if __name__ == "__main__":

# input for direction
    r = Rod2()
    turtle.listen()
    turtle.onkey(r.move_up2,'w')
    turtle.onkey(r.move_down2,'s')


    turtle.mainloop()
