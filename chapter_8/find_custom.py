def find(word, letter, n):
	"""finds the index where a letter appears in a certain word.

	n: index in word where the function should start looking.
	"""
	index = n - 1
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

print(find('master', 't', 4))
print(find('master', 't', 5))
