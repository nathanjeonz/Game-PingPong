# make rod classand set shapesize to 5,2 ... left rogt ,, goto(x,y)
import turtle


class Rod(turtle.Turtle):
    def __init__(self,c='blue',hdn=90,x=-700,y=0):
        super().__init__()        
        self.color('Black')
        self.shape('square')
        self.penup()
        self.shapesize(1,7)
        self.setheading(hdn)
        self.goto(x,y)
        self.color(c)
    def move_up(self):
        self.forward(50)
    def move_down(self):
        self.forward(-50)

if __name__ == "__main__":

# input for direction
    r = Rod()
    turtle.listen()
    turtle.onkey(r.move_up,'Up')
    turtle.onkey(r.move_down,'Down')


    turtle.mainloop()
