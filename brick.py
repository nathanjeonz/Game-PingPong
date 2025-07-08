import turtle
import random
class BrickGroup():
    def __init__(self,x_range,y_range):
        self.bricks = []
        
        colors = ['blue','green', 'yellow','cyan','magenta','red','indigo']
        for j in range(y_range[0],y_range[1],-100):
            for i in range(x_range[0],x_range[1],100):
                t = turtle.Turtle()
                t.speed(100)
                t.penup()
                t.shape('square')
                t.shapesize(3,5)
                t.color(random.choice(colors))
                t.goto(i,j)
                self.bricks.append(t)
    def destroy(self,index):
        self.bricks[index].hideturtle()
        del self.bricks[index]


        


if __name__ == '__main__':

    bg = BrickGroup(  [-700,700],[500,0]  )
    bg.destroy(5)
    turtle.mainloop()
