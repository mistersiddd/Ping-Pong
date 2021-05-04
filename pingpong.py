import turtle

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600) 
wn.tracer(0)

#	Paddle A

paddle_a=turtle.Turtle()
paddle_a.speed(0) #	not the speed of the paddle
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()  #	using the pen up
paddle_a.goto(-350,0)

#	Paddle B

paddle_b=turtle.Turtle()
paddle_b.speed(0) #	not the speed of the paddle
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()  #	using the pen up
paddle_b.goto(350,0)

#	Score

score_a=0
score_b=0

#	Ball

ball=turtle.Turtle()
ball.speed(0) #	not the speed of the paddle
ball.shape("square")
ball.color("white")
ball.penup()  #	using the pen up
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

#	Pen

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() 
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0 Player B : 0" , align="center", font=("Arial", 24, "normal"))

def paddle_a_up():
	y=paddle_a.ycor()
	y+=25
	paddle_a.sety(y)
	

def paddle_a_down():
	y=paddle_a.ycor()
	y-=25
	paddle_a.sety(y)

def paddle_b_up():
	y=paddle_b.ycor()
	y+=25
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=25
	paddle_b.sety(y)

#	keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_down,"Down")

#	Main Loop
while True:
	#	Update the screen 
	wn.update() 

	#	Move the ball

	ball.sety(ball.ycor() + ball.dy)
	ball.setx(ball.xcor() + ball.dx)

	#	Border checking	

	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy*=-1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy*=-1

	if ball.xcor() > 390:
		ball.setx(390)
		ball.dx*=-1
		score_a+=1
		pen.clear()
		pen.write("Player A : {} Player B : {}".format(score_a,score_b) , align="center", font=("Arial", 24, "normal"))

	if ball.xcor() < -390:
		ball.setx(-390)
		ball.dx*=-1
		score_b+=1
		pen.clear()
		pen.write("Player A : {} Player B : {}".format(score_a,score_b) , align="center", font=("Arial", 24, "normal"))
	#Paddle and ball collision

	if(ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60) :
		ball.dx *=-1 			#	because x is decreasing after a collision
		ball.setx(340)

	if(ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60) :
		ball.dx *=-1		#	because x is decreasing after a collision
		ball.setx(-340)