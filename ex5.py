#numero de carros
cars = 100
#enpacio en un carro
space_in_a_car = 4.0
#numero de conductores
drivers = 30
#numero de pasajeros
passengers = 90
#carros sin conductor
cars_not_driven = cars - drivers
#carros con conductor
cars_driven = drivers
#Total de espacio
carpool_capacity = cars_driven * space_in_a_car
#cantidad promedio de pasajeros por carro con conductor
average_passengers_per_car = passengers / cars_driven
#la siguiente line comnetada, contiene un error es y que la variable car_pool_capacity no exites, no se ha definido, o esta mal escrita
#por q la variable que se definio es carpool_capacity sin "_"entre car y pool.
#average_passengers_per_car = car_pool_capacity / passenger


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."