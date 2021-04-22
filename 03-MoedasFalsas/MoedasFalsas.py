# ------------------------------------ NOTAS ------------------------------------

print('Enunciado: \nVocê tem 5 moedas, uma delas é falsa, e a falsa tem o peso menor que as outras. Desenvolva uma regra para fazer o minimo numero de pesagens e descobrir a falsa (tem como resolver com 2 pesagens)')

print('\nNOTA! \nEste programa é uma simulação de pesagem ou seja, quando te pedir para colocar o peso das 4 primeiras moedas, ele está supondo que na vida real você pesaria as 4 juntas. Eliminando o fator de ter que ficar pesando elas uma por uma.\n')

#------------------------------------ REGRA ------------------------------------

eEnt1 = float(input('testar peso da 1º moeda: '))

eEnt2 = float(input('testar peso das 4 primeiras moedas: '))

if eEnt2/4 == eEnt1:
	print(f'A ultima é falsa, pois a primeira tem o valor de {eEnt1}. Pesando a primeira com as proximas três e dividindo o valor por 4, da exatamente o valor de {eEnt1}, sendo assim, todas as 4 são verdadeiras, sendo a ultima a falsa, pois obviamente vai ter o valor diferente das demais.')

elif eEnt2/4 > eEnt1:
	print('A primeira é falsa, pois ao juntar ela com as proximas 3 e pesar, se dividirmos o valor por 4, da um valor unitario para cada uma maior do que o valor original da primeira, como sabemos que a falsa pesa menos do que as originais, basta comparar o valor da media das 4 com o valor unitario da primeira.')

else:
	print('A falsa está no meio das 3 que foram pesadas junto com a verdadeira, a primeira não é falsa pois o valor dela deveria ser menor do que a media das 4 para que ela seja falsa, e a ultima também não é falsa pois, pois se multiplicarmos o valor da primeira por 4, não condiz com o que pesamos, portanto, a falsa está no meio das 3 depois da verdadeira.')
