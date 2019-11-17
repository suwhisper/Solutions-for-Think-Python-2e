"""
Draws a snowflake with three koch curves(each curve with length n).
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

def snowflake(t, n):
	koch(t, n)
	t.rt(120)
	koch(t, n)
	t.rt(120)
	koch(t, n)

import turtle
bob = turtle.Turtle()
snowflake(bob, 200)
turtle.mainloop()
