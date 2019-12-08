def avoid(word, forb_letter):
	"""Returns True when the given word does not contain any of the forbidden letters."""
    for letter in word:
        if letter in forb_letter:
            return False
    return True

def avoids():
	"""Searches the words that don't contain any of the forbidden letters and returns the number of the words."""
	forb_letter = input('Please enter the forbidden letters: ')
	count = 0
	fin = open('words.txt')
	for line in fin:	
		word = line.strip()
		if avoid(word, forb_letter):
			count += 1
	print(count)


avoids()
