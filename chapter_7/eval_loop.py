import math

def eval_loop():
	"""
	Evaluates the value of mathmatical expressions.
	You can input 'done' to end the evaluation.
	"""
	while True:
		x = input('please input a string:')
		if x == 'done':
			break		
		print(eval(x))
	print('Done!')

eval_loop()
