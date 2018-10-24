# turtle is thing that moves in python
import turtle

def drawSquare(some_turtle):
    for i in range(1,5):
        some_turtle.speed(1)
        some_turtle.forward(100);         
        some_turtle.color('yellow')
        some_turtle.right(90)             


    # second turtle for circle shape
def drawCircle(some_turtle):
    some_turtle.shape('triangle')
    some_turtle.speed(6)
    some_turtle.circle(100)
    some_turtle.color('blue') 

def drawArt():
    window = turtle.Screen();
    window.bgcolor('red');
    kumar = turtle.Turtle()  
    kumar.color('blue')
    kumar.shape('turtle')
    drawSquare(kumar)

    sobhit = turtle.Turtle()
    drawCircle(sobhit)

    window.exitonclick()
        
drawArt()

