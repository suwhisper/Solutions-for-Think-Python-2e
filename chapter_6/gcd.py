def gcd(a, b):
	"""Returns the greatest common divisor of a and b.
	a, b: integers
	"""
	if b == 0:
		return a
	r = a % b
	return gcd(b, r)

print(gcd(2, 9))
