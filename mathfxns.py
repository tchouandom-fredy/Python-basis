import math

p43 = math.pow(4,3)
print("the answer is : ", p43)

flr = math.floor(3.56)
print("the whole part is : ", flr)


cei = math.ceil(3.56)
print("the ceil part is : ", cei)

mod = abs(-4.6)#absolute value
print("the modulus part is : ", mod )

log1 = math.log(10)
print("the log of 10 base e is : ", log1)

log2 = math.log(100, 10)
print("the log of 100 base 10 is : ", log2)

root1 = math.sqrt(9)
print('the sqrt of 9 is', root1)


def total( initial = 5, *numbers, ** keywords):
	count = initial
	for i in numbers:
		count += i
	for j in keywords:
		count += keywords[j]
	return count
	
all_total = total(10,2,3,5, pen = 4, book = 5)
print('the total is : ', all_total)

# Docstrings

def add(a, b):
	''' this fxn is used to add a to b'''
	print(' the sum is : ', a+b)
	
add(5, 8)
help(add)
print(add.__doc__)

