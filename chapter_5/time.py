def is_triangle():
	"""shows whether you can or cannot form a triangle from sticks with the given lengths.
	"""
	a = int(input("Please input a: "))
	b = int(input("Please input b: "))
	c = int(input("Please input c: "))
	if a < b + c and b < a+c and c<a+b:
		print("Yes")
	else:
		print("No")

is_triangle()	
