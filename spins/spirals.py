import turtle
E=turtle.Turtle()
E.speed(0)
E.right(50)

E.shape('circle')
turtle.bgcolor('black')
E.width(3)

def design5(E):
    for times in range(99):
        E.pencolor('white')
        E.circle(90)
        E.right(45)
        E.pencolor('BLUE')
        E.circle(180)
        E.circle(120)
        E.pencolor('RED')
        E.circle(140)
        E.circle(160)
        E.left(35)
        E.pencolor('YELLOW')
        E.right(15)
        E.circle(75)
    E.up()
    E.goto(-595,205)
    E.down()
    for times in range(99):
        E.pencolor('blue')
        E.circle(10)
        E.right(55)
        E.pencolor('red')
        E.circle(100)
        E.circle(60)
        E.pencolor('yellow')
        E.circle(65)
        E.circle(85)
        E.left(35)
        E.pencolor('white')
        E.right(15)
        E.circle(30)
    E.up()
    E.goto(593,205)
    E.down()
    for times in range(99):
        E.pencolor('red')
        E.circle(10)
        E.right(55)
        E.pencolor('yellow')
        E.circle(100)
        E.circle(65)
        E.pencolor('white')
        E.circle(65)
        E.circle(85)
        E.left(35)
        E.pencolor('blue')
        E.right(15)
        E.circle(30)
    E.up()
    E.goto(-595,-205)
    E.down()
    for times in range(99):
        E.pencolor('yellow')
        E.circle(10)
        E.right(55)
        E.pencolor('white')
        E.circle(100)
        E.circle(60)
        E.pencolor('blue')
        E.circle(65)
        E.circle(85)
        E.left(35)
        E.pencolor('red')
        E.right(15)
        E.circle(30)
    E.up()
    E.goto(593,-205)
    E.down()
    for times in range(99):
        E.pencolor('orange')
        E.circle(10)
        E.right(55)
        E.pencolor('green')
        E.circle(100)
        E.circle(60)
        E.pencolor('yellow')
        E.circle(65)
        E.circle(85)
        E.left(35)
        E.pencolor('white')
        E.right(15)
        E.circle(30)

    E.up()
    E.goto(-315,330)         
    E.down()
    for times in range(99):
        E.pencolor('blue')
        E.circle(25)
        E.right(15)
        E.pencolor('blue')
        E.circle(30)
        E.circle(30)
        E.pencolor('blue')
        E.circle(35)
        E.circle(35)
        E.left(20)
        E.pencolor('blue')
        E.right(25)
        E.circle(40)

    E.up()
    E.goto(-315,-330)         
    E.down()
    for times in range(99):
        E.pencolor('red')
        E.circle(25)
        E.right(15)
        E.pencolor('red')
        E.circle(30)
        E.circle(30)
        E.pencolor('red')
        E.circle(35)
        E.circle(35)
        E.left(20)
        E.pencolor('red')
        E.right(25)
        E.circle(40)

    E.up()
    E.goto(315,-330)
    E.down()
    for times in range(99):
        E.pencolor('yellow')
        E.circle(25)
        E.right(15)
        E.pencolor('yellow')
        E.circle(30)
        E.circle(30)
        E.pencolor('yellow')
        E.circle(35)
        E.circle(35)
        E.left(20)
        E.pencolor('yellow')
        E.right(25)
        E.circle(40)

    E.up()
    E.goto(315,330)
    E.down()
    for times in range(99):
        E.pencolor('white')
        E.circle(25)
        E.right(15)
        E.pencolor('white')
        E.circle(30)
        E.circle(30)
        E.pencolor('white')
        E.circle(35)
        E.circle(35)
        E.left(20)
        E.pencolor('white')
        E.right(25)
        E.circle(40)
        
    E.pencolor('blue')
    E.goto(400,0)
    E.pencolor('blue')
    E.goto(315,-330)
    E.pencolor('white')
    E.goto(0,-375)
    E.pencolor('white')
    E.goto(-315,-330)
    E.pencolor('yellow')
    E.goto(-400,0)
    E.pencolor('yellow')
    E.goto(-315,330)
    E.pencolor('red')
    E.goto(0,375)
    E.pencolor('red')
    E.goto(315,330)

    

        
design5(E)
turtle.ht









