import turtle
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.color('yellow')
    brad.speed(10)
    brad.shape('turtle')
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #angie = turtle.Turtle()
    #angie.shape('arrow')
    #angie.color('blue')
    #angie.circle(100)

    window.exitonclick()    
    
def draw_square(some_turtle):
    sides = 0 
    while (sides < 4):
        some_turtle.forward(100)
        some_turtle.right(90)
        sides = sides + 1
    
draw_art()
