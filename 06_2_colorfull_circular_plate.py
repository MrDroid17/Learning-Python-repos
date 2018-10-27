import turtle 

ninja = turtle.Turtle()
 
# turtle speed 1- slowest 10-fast but setting it to 0 - fastest speed
ninja.speed(0)

for i in range(720):
    ninja.color('blue')
    ninja.forward(100)
    ninja.right(30)
    ninja.color('green')
    ninja.forward(20)
    ninja.left(60)
    ninja.color('violet')
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(0.5)
    
turtle.done()
