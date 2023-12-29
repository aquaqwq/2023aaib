a = int(input())

for i in range(a):
	star = a-i-1
	for k in range(star):
		print(' ',end='')
	star = 2 * i+1
	for k in range(star):
		print('*', end='')
		
	print()