def recurse(n,s): 
	if n==0:
		print(s)
	else:
		recurse(n-1,n+s)

recurse(3,0)

__main__   None
recurse    n→3,s→0
recurse    n→2,s→3
recurse    n→1,s→5
recurse    n→0,s→6
print      s→6
