# turtle is thing that moves in python
import turtle

def drawSquare():
    window = turtle.Screen();
    window.bgcolor('red');
    
    kumar = turtle.Turtle()
    
    kumar.color('blue')
    kumar.shape('turtle')
    kumar.speed(1)
    kumar.forward(100);         # move forward 100px
    kumar.color('yellow')
    kumar.right(90)              # turn right at 90 degree

    kumar.forward(100);         # move forward 100px
    kumar.shape('circle')
    kumar.speed(1)
    kumar.color('magenta')
    kumar.right(90)              # turn right at 90 degree

    kumar.forward(100);         # move forward 100px
    kumar.shape('triangle')
    kumar.speed(1)
    kumar.color('green')
    kumar.right(90)              # turn right at 90 degree

    kumar.forward(100);         # move forward 100px
    kumar.shape('square')
    kumar.speed(1)
    kumar.color('cyan')
    kumar.right(90)              # turn right at 90 degree

    # second turtle for circle shape
    sobhit = turtle.Turtle()
    sobhit.color('yellow')
    sobhit.shape('turtle')
    sobhit.speed(1)
    sobhit.circle(100)
    sobhit.color('orange')

    # third turtle for triangle shape
    rohit = turtle.Turtle()
    rohit.color('cyan')
    rohit.shape('arrow')
    rohit.speed(1)
    rohit.right(45)
    rohit.forward(150)
    rohit.right(120)
    rohit.forward(150)
    rohit.right(120)
    rohit.forward(150)
    rohit.right(60)
    rohit.color('orange')
   

    window.exitonclick()
    

drawSquare()

