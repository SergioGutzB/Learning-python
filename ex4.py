nombre = 'Sergio Gutierrez'
edad = 25 # not a lie
altura = 1 + .70000000000000 # metros
peso = 120 # lbs
ojos = 'Brown'
dientes = 'White'
pelo = 'Black'

print "Let's talk about %s." % nombre
print "He's %d inches tall." % altura
print "He's %d pounds heavy." % peso
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (ojos, pelo)
print "His teeth are usually %s depending on the coffee." % dientes

cadena = "edad +" + " altura " + '+ peso'

# this line is tricky, try to get it exactly right
print "If I add %d, %r, and %d I get %s %f." % (edad, altura, peso,'('+ cadena + ")", edad + altura + peso)