def cumsum(t):
	x = 0
	new_list = []
	for i in t:
		x += i
		new_list.append(x)
	return(new_list)

print(cumsum([1,3,5,7,9]))
