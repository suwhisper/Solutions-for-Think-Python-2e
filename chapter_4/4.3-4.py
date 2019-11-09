def polygon(t,n,length):
	"""Draws a polygon with n sides.
	t: Turtle
	n: number of sides
	length: length of each side.
	"""
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

def circle(t,r):
	"""Draws a circle with the given radius.

	t: Turtle
	r: radius
	"""
	n=50
	circumference=2*math.pi*r
	length=circumference/n
	polygon(t,n,length)

import math
import turtle
bob=turtle.Turtle()
circle(bob,50)
turtle.mainloop()
