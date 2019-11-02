"""
draw a square whose length of the sides is *length*
"""

def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

import turtle
bob=turtle.Turtle()
square(50)
turtle.mainloop()
