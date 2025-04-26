import turtle

sides = int(input("How many sides do you want for your shape: "))

def draw_polygon(turtle, sides, length, turn='left'):

    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)

        if turn == 'left':
            turtle.left(angle)
        else:
            turtle.right(angle)

def draw_star_pattern(sides, length=80):

    laki = turtle.Turtle()
    laki.speed(0)
    
    turn_angle = 360 / sides
    
    for _ in range(sides):

        current_direction = laki.heading()
        
        laki.forward(length)

        current_pos = laki.pos()
        
        laki.left(turn_angle)
        
        laki.penup()
        laki.goto(current_pos)
        laki.setheading(current_direction + turn_angle) 
        laki.pendown()
        
        draw_polygon(laki, sides, length, 'right')
        
        laki.penup()
        laki.goto(current_pos)
        laki.setheading(current_direction + turn_angle)
        laki.pendown()
    turtle.done()

draw_star_pattern(sides, 80)