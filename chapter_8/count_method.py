def count(word, letter):
	"""Returns the number of non-overlapping occurrences of substring word
	"""
	number = word.count(letter)
	print(number)

count('banana', 'a')
