#_________ WELCOME ALL OF YOU ON COMPUTER SOFT SKILLS CHANNEL __________

#........................ WISH HAPPY DIWALI USING PYHON TURTLE GRAPHICS ......................


import turtle
import random
import colorsys

# Turtle Window
wn = turtle.Screen()
wn.setup(800,750)
wn.title("Computer Soft Skills: HAPPY DEEPAVALI")

turtle.bgcolor('LAVENDER')
turtle.tracer(2)
t=turtle.Turtle()
t.hideturtle()
t.pensize(3)
hue=0.5

#___CRACKERS_______________

for i in range (50):
     x=random.randint(-400,500)
     y=random.randint(-200,450)
     z=random.randint(-300,600)
     t.speed(80)
     t.penup()
     t.goto(x,y)
     t.pendown()

     size=random.randint(10,250)

     for i in range(36):
          color=colorsys.hsv_to_rgb(hue,1,1)
          t.pencolor(color)
          t.fd(size)
          t.bk(size)
          t.lt(10)
          hue +=0.01

     def write(message,pos):
          x,y=pos
          t.penup()
          t.goto(x,y)
          style=('ARIAL BLACK',50,'normal')
          t.write(message,font=style)
     write('HAPPY DEEPAVALI',(-380,0))

      
turtle.done()







