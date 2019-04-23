import turtle   #get all turtle features

t = turtle.Turtle() #creates turtle object called t
t.up()
t.speed(0) #makes t draw fast.

def make_sky(): #Makes a 500 pixle wide square that's blue
  t.goto(-200,0)
  t.down()
  t.color("#2bc3ff")
  t.begin_fill()
  for i in range(4):
    t.forward(500)
    t.lt(90)
  t.end_fill()
  t.up()

def make_sun(): #create yellow circle top left.
  t.goto(-120, 350)
  t.color("yellow")
  t.begin_fill()
  t.circle(50)
  t.end_fill()
  t.up()

def make_ocean():
  t.up()
  x = -200;
  y = 30;

  r = 0
  g = 0
  b = 255
  def make_square(r,g,b):
    t.down()
    t.color(r,g,b)
    t.begin_fill()
    for i in range(4):
      t.forward(50)
      t.rt(90)
    t.end_fill()
    t.up()

  for down in range (5):  #make 5 rows
    x = -200
    y = y - 30
    for count in range (10): #put 10 squares in each row
      t.goto(x ,y)
      make_square(r,g,b) #call make_square function
      g = g + 5
      r = r + 5
      x = x + 50

def make_island():
  t.up()
  t.goto(-70, -100)
  t.color("green")
  t.begin_fill()
  t.circle(80)
  t.end_fill()
  t.up()

def make_bird(): #draws 4 lines 
  t.goto(120, 350)
  t.color("black")
  t.down()
  t.lt(40)
  t.forward(30)
  t.rt(80)
  t.forward(30)
  t.lt(80)
  t.forward(30)
  t.rt(80)
  t.forward(30)
  t.up()
  t.rt(320) #corrects t position before making ocean


make_sky() #1
make_sun() #2
make_island() #3
make_bird() #4
make_ocean() #5
