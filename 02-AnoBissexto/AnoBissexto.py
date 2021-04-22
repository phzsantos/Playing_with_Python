#------------------------------------ NOTAS ------------------------------------

print('Programa para saber se o ano é bissexto ou não.\n')

#------------------------------------ REGRA ------------------------------------

eEnt1 = int(input('diga-me um ano, eu te direi se ele é bissexto ou não: \n'))

if eEnt1 < 104:
	print('Antes do ano 104 d.c, não tinhamos anos bissexto. Portanto, o numero digitado não é um ano bissexto')

elif (eEnt1 % 4) == 0:
	print('Esse ano é bissexto')
	
elif (eEnt1 % 100) == 0:

	if (eEnt1 % 400) == 0:
		print('Esse ano é bissexto, pois atende todos os requisitos')

	else:
		('Esse ano não é bissexto, pois não é divisivel por 400')

else:
	print('Esse ano não é bissexto.')