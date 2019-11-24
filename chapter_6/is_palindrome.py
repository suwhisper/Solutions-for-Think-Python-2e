def first(word):
	"""Returns the first character of a string."""
	return word[0]

def last(word):
	"""Returns the last of a string."""
	return word[-1]

def middle(word):
	"""Returns all but the first and last characters of a string."""
	return word[1:-1]

def is_palindrome(word):
	"""Returns True if word is a palindrome."""
	if len(word) <= 1:
		return True
	elif first(word) != last(word):
		return False
	return is_palindrome(middle(word))

print(is_palindrome("a"))
print(is_palindrome("ana"))
print(is_palindrome("redivider"))
