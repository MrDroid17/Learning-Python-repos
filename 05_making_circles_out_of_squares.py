# turtle is thing that moves in python
import turtle

def drawSquare(some_turtle):
    for i in range(1,5):
        some_turtle.speed(4)
        some_turtle.forward(100);         
        some_turtle.color('yellow')
        some_turtle.right(90)             

def drawArt():
    window = turtle.Screen();
    window.bgcolor('red');
    kumar = turtle.Turtle()  
    kumar.color('blue')
    kumar.shape('turtle')

    for i in range(1, 37):
        drawSquare(kumar)
        kumar.right(10)
    
    window.exitonclick()
        
drawArt()
