def is_palindrome(word):
	"""Returns True if a word is palindrome."""
	return word == word[::-1]

print(is_palindrome('ana'))
