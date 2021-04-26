#------------------------------------ NOTAS ------------------------------------

print('Programa para saber se o ano é bissexto ou não.\n')

#------------------------------------ REGRA ------------------------------------

Ano = int(input('diga-me um ano, eu te direi se ele é bissexto ou não: '))

if (Ano < 104):
	print('Antes do ano 104 d.c, não tinhamos anos bissexto. Portanto, o numero digitado não é um ano bissexto')

elif ((Ano % 400) == 0) or ((Ano % 4) == 0) and ((Ano % 100) != 0):
	print('Esse ano é bissexto.')

else:
	print('Esse ano não é bissexto.')