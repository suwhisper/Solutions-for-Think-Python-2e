def has_duplicates(t):
	b = []
	for i in t:
		b.append(i)
	for i in t:
		if i in b:
			return True
	return False

print(has_duplicates([1, 2, 2, 3]))
