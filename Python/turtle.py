import turtle
amy = turtle.Turtle()
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    for sides in [1,2,3,4]:   
        amy.forward(50) # Replace this line with a for loop!
        amy.penup()
    amy.forward(50)
    amy.pendown()