def check_fermat(a, b, c, n):
  """function that checks to see if Fermat’s theorem holds.
  """
	if n > 2 and a**n + b**n == c**n:
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn’t work.")

def check_fermat_custom():
	a = int(input("Please input a: "))
	b = int(input("Please input b: "))
	c = int(input("Please input c: "))
	n = int(input("Please input n: "))
	return check_fermat(a, b, c, n)
	
check_fermat_custom()	
