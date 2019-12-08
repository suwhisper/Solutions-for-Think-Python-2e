def is_abecedarian(word):
	previous = word[0]
	for letter in word:
		if letter < previous:
			return False
		previous = letter
	return True

print(is_abecedarian('word'))
