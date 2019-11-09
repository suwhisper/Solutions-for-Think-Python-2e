def arc(t,r,angle):
	"""Draws an arc with the given radius and angle.

	t: Turtle
	r: radius
	angle: angle subtended by the arc, in degrees
	"""
	arc_length=2*math.pi*r*angle/360
	n=int(arc_length/3)+1
	step_length=arc_length/n
	step_angle=angle/n

	for i in range(n):
		t.fd(step_length)
		t.lt(step_angle)

import math
import turtle
bob=turtle.Turtle()
arc(bob,50, 300)
turtle.mainloop()
