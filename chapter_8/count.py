def count(word, letter):
	"""Counts the number of times a letter appears in a word."""
	count = 0
	index = 0
	while index < len(word):
		if word[index] == letter:
			count = count + 1
		index = index + 1
	return count


def count_update(word, letter, n):
	"""Counts the number of times a letter appears in a word. In this version you can start the count from any letter of the word.

	n: index in word where the function should start looking.
	"""
	count = 0
	index = n - 1
	while index < len(word):
		if word[index] == letter:
			count = count + 1
		index = index + 1
	return count

print(count('apple', 'p'))
print(count_update('apple', 'p', 3))
