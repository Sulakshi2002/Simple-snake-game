import turtle #use to create pictures and craete shapes.like a pen for drawing
import time
import random


delay = 0.1  #used for delay

#score
score = 0
high_score = 0


#set up a screen or window 
wn = turtle.Screen() #window called wn
wn.title("Snake Game ") # The screen title is snake game
wn.bgcolor("#73EC8B") #bg color
wn.setup(width=600, height=600) #size of the window
wn.tracer(0) # turn off the animation on screen

#snake head moving around the screen
#create snake head
head = turtle.Turtle() #use turtle to show head
head.speed(0)
head.shape("square") #the shape of the head
head.color("blue") # color of the head
head.penup()#not drawing while moving
head.goto(0,0) # where does it start
head.direction = "stop"


#snake food called apple
apple = turtle.Turtle() #use turtle to show apple
apple.speed(0)
apple.shape("circle") #the shape of the food
apple.color("red") # color of the food
apple.penup()#not drawing while moving
apple.goto(100,200) # where does it start

#change the snake body
segments = []


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High Score: 0",align="center", font=("Courier", 25, "normal"))


#function for change the direction of head
def go_up():
    if head.direction != "down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"
    
def go_right():
    if head.direction != "left":
        head.direction="right"
    
def go_left():
    if head.direction != "right":
        head.direction="left"


#fuction for moving the turtle/head
def move():
    if head.direction =="up":
        y = head.ycor() #getting the y cordinate of the turtle
        head.sety(y + 17) #where does it change

    if head.direction =="down":
        y = head.ycor() 
        head.sety(y - 17) 

    if head.direction =="left":
        x = head.xcor() 
        head.setx(x - 17) 

    if head.direction =="right":
        x = head.xcor() 
        head.setx(x + 17) 

#keybord binding(get input from keys)
wn.listen() #take keyboard press
wn.onkeypress(go_up, "Up") 
wn.onkeypress(go_down, "Down") 
wn.onkeypress(go_left, "Left") 
wn.onkeypress(go_right, "Right") 


#Main game loop
while True:
    wn.update()#update the screen until while false

    #check for collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments list
        segments.clear()

        #Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("Courier", 25, "normal"))

    #check for collision with apple and snake
    if head.distance(apple) <20 : #the radius between turtle is 20
        #move the apple to a random position
        x = random.randint(-290,290)#window size
        y = random.randint(-290,290)
        apple.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square") 
        new_segment.color("grey") 
        new_segment.penup()
        segments.append(new_segment)#add segments to the segments

        #shorten the delay
        delay -= 0.001

        #increase the score
        score+=10
        if score>high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("Courier", 25, "normal"))


    #move the end segments first in reverse order
    for index in range(len(segments)-1,0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)   

    #move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        

    move()

   #check for head collision with the itself
    for segment in segments:
        if segment.distance(head) < 17:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segments list
            segments.clear()

            #Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("Courier", 25, "normal"))

    time.sleep(delay)# the turtle delay 0.1 second

wn.mainloop() #window open for us