"""
draw a square whose length of the sides is 50
"""
def square(t):
	for i in range(4):
		t.fd(50)
		t.lt(90)

import turtle
bob=turtle.Turtle()
square(bob)
turtle.mainloop()
