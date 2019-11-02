"""
Draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""

for i in range(2):
	for i in range(2):
		print('+','- '*4,end='')
	print('+')
	for i in range(4):
		print('|',' '*7,'|',' '*7,'|')
for i in range(2):
	print('+','- '*4,end='')
print('+')
