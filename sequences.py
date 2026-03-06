# Sequenced inlvolves the list, tuple and string elements accessing

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'john'

#Indexing or subscription operations

for i in range(0,4):
	print("Item {} is {}". format(i, shoplist[i]))
    
print("Item at index -1 is ", shoplist[-1])

print("Item at index -2 is ", shoplist[-2])

print("character 0 is ", name[0].capitalize())

#Slicing ln a list

print("Item 1 to 3 are ", shoplist[1:3])
print("Item 2 to the end are",  shoplist[2:])
print("Items start to end are ", shoplist[:])
print("Items 1 to -1 are ", shoplist[1:-1])



print("Item 1 to 3 are ", name[1:3])
print("Item 2 to the end are",  name[2:])
print("Items start to end are ", name[:])
print("Items 1 to -1 are ", name[1:-1])

#adding the step

print("Items with an even index in the list are ", shoplist[::2])

print("Items with an odd index in the list are ", shoplist[1::2])

if 'mango' in shoplist:
	print("yes")
	
#Sets
bri = set(['brazil', 'russia', 'india'])
print(bri)
bric = bri.copy()
print(bric)
bric.add('china')
print(bric)

if bric.issuperset(bri):
	print("Yes")
bri.remove('russia')
print(bric & bri)







