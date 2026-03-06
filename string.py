#this is a string object
name = 'Chandrakant'

if name.startswith('Chan'):
	print('yes the name starts with Chan')
if 'a' in name:
	print('yes it contains "a"')
if name.find('and') != -1:
	print('yes it contains the string "and"')

delimiter = '_*_'
mylist = [ 'Brasil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

# First letter capitalization
word1 = 'football'
print('the capitalised word is :', word1.capitalize())
print('there are {0} (0) in football '. format(word1.count("o")))

word2 = 'I am in amstrerdam'
print('there are {0} (am) in the string '. format(word2.count('am')))
print('the first a is found at location', word2.find('a'))
print('the first z is found at location', word2.find('z')) 
name3 = ('Tchouandom','Fredy','Desley')
name4 = '-'
print('My name is :', name4.join(name3))
























