#  if Statement
number = 25 
guess = int(input(" Enter an Interger"))
if guess == number:
	print("You had it")
elif guess < number:
	print("It is a little higher")
elif guess > number:
	print(" It is a little lower")
	
# adding while loop
number = 25
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('You had it.')
        running = False
    elif guess < number:
        print('it is a little higher.')
    elif guess > number:
        print('it is a little lower .')
else:
    print('The while loop is over.')

print('Done')

# for loop
for i in range(1,5):# it takes[1, 5[
	print(i)
for i in range(5):#it asumes [0,5[
	print(i)
for i in range(1,10,2):#2 is the step
	print(i)
else:
	print("the loop is over")

#	break
while True:
	s = input('Enter something:  ')
	if s == 'quit':
		break
	print('The lenght of the string is: ', len(s))
print('Done')

#   continue  

while True:
	s = input('Enter something:  ')
	if s == 'quit':
		break
	if len(s) < 3:
	   	print('Too small')
	   	continue
	print('The input is of sufficient lenght')
    



















