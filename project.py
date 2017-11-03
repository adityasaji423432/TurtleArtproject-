import turtle
bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(17)

turtle.bgcolor(0,0,0)

for times in range(150):
           bob.begin_fill()
           bob.circle(56)
           bob.right(10)
           bob.width(times*0+2)
           bob.color(times*2+20,times*0+20,times+3)
           bob.end_fill()
           bob.forward(200)
           bob.right(250+1)
           bob.forward(20)
           bob.begin_fill()
           bob.circle(56)
           bob.right(10)
           bob.width(times*0+2)
           bob.color(times*2+20,times*0+20,times+3)
           bob.end_fill()
           bob.forward(200)
           bob.right(250+1)
           bob.forward(200)
turtle.done()

