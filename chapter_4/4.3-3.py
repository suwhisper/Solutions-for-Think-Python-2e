def polygon(t,n,length):
	"""Draws a polygon with n sides.

	t: Turtle
	n: number of sides
	length: length of each side.
	"""
	for i in range(n):
		t.fd(length)
		t.lt(360/n)
   
import turtle
bob=turtle.Turtle()
polygon(bob,5,50)
turtle.mainloop()
