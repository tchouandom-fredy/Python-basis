# function call
def say_hello():
	print('hello boy')
say_hello()
say_hello()

#function parameters x Local variables
def print_max(a, b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b, " is maximum")
		
print_max(3, 4)
x=5
y=7
print_max(x, y)

#  functions x global variables
z = 10
def fxn():
	global z
	print('The value of z is ', z)
	z=2
	print('Changed value of z to ', z)
	
fxn()
print('value of z is', z)

# default argument values

def say(message, times = 1):
	print(message * times)
	
say('hello')
say('  world', 5)

# keyword arguments

def func(a, b=5, c=10):
	print('  a is ', a ,'  b is ', b, 'c is ', c)
	
func(3,  7)
func(24, c=25)
func(c = 50 , a = 100 )
	
# varargs for variable number of parameters 
def( initial=5, *number, **keywords):
	












