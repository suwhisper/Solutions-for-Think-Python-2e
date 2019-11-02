"""
Draws a grid like the following:
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
"""

for i in range(3):
	for i in range(3):
		print('+','- '*4,end='')
	print('+')
	for i in range(4):
		print('|',' '*7,'|',' '*7,'|',' '*7,'|')
for i in range(3):
	print('+','- '*4,end='')
print('+')
