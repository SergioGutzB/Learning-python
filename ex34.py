animals = ['bear','python','peacock','kangaroo','whale','platypus']

print "The animal at 1: %s" % animals[1]
print "The third (3rd) animal: %s" % animals[2]
print "The first (1st) animal: %s" % animals[0]
print "The animal at 3: %s" % animals[3]
print "The fifth (5th) animal: %s" % animals[4]
print "The animal at 2: %s" % animals[2]
print "The sixth (6th) animal: %s" % animals[5]
print "The animal at 4: %s" % animals[4]



ex={'1':ex1,'2': ex2,'3': ex3,'4':ex4,'5': ex5,'6':ex6}

opcion=raw_input('elija un ejercicio del numero 1 al 34 :  ')
try:
	op=ex[opcion]()
except:
	print 'Escoja un ejercicio valido'