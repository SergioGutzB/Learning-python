the_count=[1,2,3,4,5]
fruits =['apples','oranges','pears','apricots']
change =[1,'pennies',2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
	print "This is count %d"%number

#save as above

for fruit in fruits:
	print "A fruit of type %s"%fruit

for i in change:
	print "I got %r"%i

elements = []

#the use the range function to do 0 to 5
for i in range(0,6):
	print "Adding %d to the list" % i
	#append is a function that list understand
	elements.append(i)

for i in elements:
	print "Element was: %d"%i