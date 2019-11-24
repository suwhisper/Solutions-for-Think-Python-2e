def is_power(a, b):
	"""Returns true if a is power of b."""
	if a == b:
		return True
	elif a % b != 0:
		return False
	return is_power(a/b, b)

print(is_power(8, 2))
print(is_power(9, 2))
