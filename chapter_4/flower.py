from arc import arc

def flower(t,r,n):
	petal_ang=360/n

	for i in range(n):
		arc(t,r,petal_ang)
		t.lt(180-petal_ang)
		arc(t,r,petal_ang)
		t.rt(180)

def flower_2(t,r,n):
	petal_ang=(360/n)*2

	for i in range(n):
		arc(t,r,petal_ang)
		t.lt(180-petal_ang)
		arc(t,r,petal_ang)
		t.lt(180-360/n)

def move(t, length):
	t.pu()
	t.fd(length)
	t.pd()
		
import turtle
bob=turtle.Turtle()

move(bob, -100)
flower(bob, 70, 6)

move(bob, 100)
flower_2(bob, 50, 10)

move(bob, 100)
flower(bob, 200, 20)

bob.hideturtle()
turtle.mainloop()
