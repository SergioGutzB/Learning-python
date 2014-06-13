#a la variable x se le asigna una cade que contiene un decimal que es convertido a texto. esta cadena contiene otra cadena
x = "There are %d types of people." % 10
#a la variable binary se le asigna la cadena "binary"
binary = "binary"
#a la variable do_not se le asigna la cadena "don't"
do_not = "don't"
#a la variable y se le asigna una cadena que contiene dos cadenas binary y do_not
y = "Those who know %s and those who %s." % (binary, do_not)
#se imprime el valor de la varibale "x" y "y"
print x
print y

#se inprime una cadena que contiene otra otra cadena (x)
print "I said: %r." % x
#se inprime una cadena que contiene otra otra cadena (y)
print "I also said: '%s'." % y
#se crea una varibale booleana
hilarious = False
#a la varible (joke_evaluation) se le asigna una cadena, esta cadena contiene otra cadena que no exite o es "", por lo que no es visivle
joke_evaluation = "Isn't that joke so funny?! %r"
# imprime las varibales joke_evaluation, hilarious concatenadas

print joke_evaluation % hilarious
#se crean dos variables con una cadena de texto cada una
w = "This is the left side of..."
e = "a string with a right side."
#se cocatenan las cadenas (w) y (e) y se imprimen
print w + e


#Se puede afirmar que hay 6 lugares donde se pone una cadena dentro de otra las lineas de codigo son las siguientes:
#Linea 2: x = "There are %d types of people
#linea 8: y = "Those who know %s and those who %s." % (binary, do_not) --- en esta cadena se pones dos cadenas
#linea 14: print "I said: %r." % x
#linea 16: print "I also said: '%s'." % y
#joke_evaluation = "Isn't that joke so funny?! %r" ---- en esta cadena se inserta una cadena vacia q supuestamente hace referencia a un flotante