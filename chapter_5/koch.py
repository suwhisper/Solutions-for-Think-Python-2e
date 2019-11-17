"""
Draws a koch curve with length n.
"""

def koch(t, n):
	if n < 3:
		t.fd(n)
		return
	m = n/3
	koch(t, m)
	t.lt(60)
	koch(t, m)
	t.rt(120)
	koch(t, m)
	t.lt(60)
	koch(t, m)

import turtle
bob = turtle.Turtle()
koch(bob, 200)
turtle.mainloop()
