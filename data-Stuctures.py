#  List
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have ', len(shoplist), ' Items to purchase')

print('these Items are ', end='  ')
for item in shoplist:
	print(item, end= '  ')
fruits = shoplist[0:2]#selects elts in the list fron index 0 inclusive to 2 exclusive ie. 0 to 1
print('there are ', len(fruits),'fruits in my list which are', fruits)

print('\n I also have to buy rice ')
shoplist.append('rice')#adding rice to the list
print(' My shoplist is now : ', shoplist[:])#similar to just shoplist

print('I will sort my list now')
shoplist.sort() #
print(' My shoplist is now : ', shoplist)

print('the first i tem i will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0] # deleting the bought item
print('I bought the ', olditem)
print('Now if remains me to buy', shoplist[:5])#items from index 0 to 4

print('the two last elements to buy are', shoplist[2:])

shoplist[3] = 'pasta'#update rice to pasta
print('the new remai ing list is ', shoplist)
 
shoplist.remove('banana')
print('I think I shall leave banana my list remains', shoplist)
print('\n\n')

# Tuple
zoo = ('python', 'elephant','penguine')
print('Number of animals in the zoo are: ', len(zoo))
new_zoo =('monkey', 'kamel',zoo)
print('Number of cages in the new the zoo : ', len(new_zoo))
print('The animals in the zoo are :',  new_zoo)
print('Total number of animals in the new zoo are : ', len(new_zoo) - 1 + len(new_zoo[2]))

del new_zoo # only oosdible to delete all elts in the tuple
print('\n\n')

#Dictionary
# let ab be 'a'ddress 'b'ook
ab ={
         'John':'johy@gmail.com',
         'Mary':'mary@gmail.com',
         'Jack':'jack@gmail.com',
         'Fredy':'fredy@gmail.com'
}

print("Fredy's address is ", ab['Fredy'])

del ab['Jack']#deleting a key pair value

print("There are" , len(ab), "contacts remaining in this address book")

for name,address in ab.items():
	print(" Contact {} at {} ". format(name,address))
	
ab['Guido'] = 'guido@gmail.com'# addind a key-pair value

if 'Guido' in ab:
	print(" \nGuido's address is ", ab['Guido'])
	
print(ab)

ab['Fredy'] = 'business@gmail.com'#updatting my address
print(" \n Fredy's new address is ", ab['Fredy'])
	
ab.clear()# clearing all elements in the dictionary without deleting if
print('.....',ab)

del ab# deletes the dictionary


	