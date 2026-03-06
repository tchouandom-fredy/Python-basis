#........Strings...........
#this is a string object
name = 'Chandrakant'

if name.startswith('Chan'):
    print("yes it's name starts with Chan")
if name.endswith('kant'):
	print("Yes it ensd with kant")
if 'a' in name:
	print('yes it contains "a"')
if name.find('and') != -1:
	print('yes it contains the string "and"')

delimiter = '_*_'
boundary = '-|-'
mylist = [ 'Brasil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
print(boundary.join(mylist))
#........format method.......
age = 2
name2 = 'Programming hub'

print(' {0} is {1} yrs old and teaches more than 20 progarmming languages' . format(name2, age) )

#......Escape seq.......
          #....New line....
print(" Number1 \n Number2\n")
          #.....Tabs......
print(" Number1 \t Number2\n")
          #..prevent effects of slash commands  
print(r" Number1 \n Number2\n")

print(R" Number1 \n Number2\n")


















