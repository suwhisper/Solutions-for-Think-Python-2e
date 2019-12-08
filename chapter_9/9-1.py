"""Reads words.txt and prints the words with more than 20 characters."""
fin = open('words.txt')

for line in fin:
	word = line.strip()
	if len(word) > 20:
		print(word)

print(fin.readlines()[1])
