import math
def pie(t,length,n):
	"""Draws a pie, then moves into position to the right.

	t: Turtle
	length: length of the radial spokes
	n: number of segments
	"""
	angle=360/n
	length2=math.sqrt((length**2)*2-(2*length*length)*math.cos(math.radians(angle)))
	angle2=(180-angle)/2

	for i in range(n):
		t.fd(length)
		t.lt(180-angle2)	
		t.fd(length2)
		t.lt(180-angle2)
		t.fd(length)
		t.rt(180)



import turtle
bob=turtle.Turtle()
pie(bob,50,7)
bob.hideturtle()
turtle.mainloop()
