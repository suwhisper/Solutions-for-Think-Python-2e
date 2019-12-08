def has_no_e(word):
	"""Returns True when the given word has no letter e."""
	for letter in word:
		if letter == 'e':
			return False
	return True

print(has_no_e('like'))
