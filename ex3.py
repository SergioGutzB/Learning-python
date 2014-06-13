print "I will now count my chickens:"
#En la siguientes lineas se inmprime una cadena concatenada "," con el resultado de las operaciones matematicas

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"
#Se imprime el resultado de las operaciones matematicas: "3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6".
#Python reconoce el orden de los operadores.
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"
#Python en un operacion matematica cuando lee un operador logico, devuelve una respuesta logica tambien (true, o false), 
#por lo tanto en la siguiente linea imprime false. ya que [(3 + 2) < (5 - 7)] es igual a 5 < -2 y esto es falso.
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."
#por lo explicado en el comentario anterior.
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2