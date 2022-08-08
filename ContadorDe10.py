

import time
cantidad = 10


# ~ while cantidad != 0:
	# ~ print (cantidad)
	# ~ if cantidad == 5:
		# ~ print ("Estamos a la mitad")
	# ~ elif cantidad == 3:
		# ~ print ("Prendan motores")
	# ~ elif cantidad == 1:
		# ~ print ("Despeguen")
	# ~ cantidad -= 1


while True:
	print (cantidad)
	if cantidad == 7:
		print ("Estamos a la mitad")
	elif cantidad == 3:
		print ("Prendan motores")
	elif cantidad == 1:
		print ("Despeguen")
	cantidad -= 1
	if cantidad == 0:
		break
	time.sleep(1)
# ~ lista = [1,2,3,4,5,6,7,8,9,10]
# ~ nueva = list(reversed(lista))
# ~ print(nueva)
