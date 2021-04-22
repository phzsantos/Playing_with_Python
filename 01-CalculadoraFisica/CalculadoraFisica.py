#OBJETIVO
#Fazer um programa que de para escolher qual tema resolver, escolhar qual formula usar e escolher qual vai ser a variavel (x).

#TEMAS
#Temperatura (PRONTO)
#1-Celsius (OK)
#2-Fahrenheit (OK)
#3-Kelvin (OK)

#Dilatação (EM CONSTRUÇÃO)
#1-Linear
#2-Volumetrica
#3-Superficial

#PLANO DE EXECUÇÃO
#1-Perguntar qual o tema a resolver; (PRONTO)
#2-Escolher qual formula se encaixa; (TEMP PRONTO)
#3-Determinar qual vai ser a variavel a ser resolvida; 
#4-Printar o resultado. (TEMP PRONTO) 

#INFORMAÇÕES QUE DEVEM ESTAR EM TODAS AS PAGINAS
#1-O que é temperatura; (PRONTO)
#2-Formula; (PRONTO)
#3-Valor da temperatura normal do corpo humano nas 3 escalas. (PRONTO)

#EXECUÇÃO:

#PARTE-1
print('Lista de opções:\n')
print('1-Temperatura\n')
print('2-Dilatação\n')
print('3-Calor Sensivel\n')
print('4-Calor Latente\n')
print('5-Calor Sensivel + Latente\n')
print('6-Gases Ideais\n')
print('Qual o tema a ser abordado?(responda de 1 a 6)')
p1=input()

#PARTE-2-3-4 (TEMPERATURA)
if p1=="1":
	print('\nVocê escolheu temperatura, aqui estão as alternativas:\n')
	print('1-Celsius para Kelvin\n')
	print('2-Celsius para Fahrenheit\n')
	print('3-Fahrenheit para Celsius\n')
	print('4-Fahrenheit para Kelvin\n')
	print('5-Kelvin para Celsius\n')
	print('6-Kelvin para Fahrenheit\n')
	print('7-Variação de temperatura\n')
	print('Qual a conversão que deseja fazer?(responda com 1 ate 7)')
	p2=input("")
	if p2=="1":
		print('\nTemperatura é uma grandeza microscopica, que é a média das velocidades das moleculas ou atomos de determinado corpo\n')
		print('Formula: Tc/5=Tk-273/5 ou Resumindo, fica o valor em Celsius + 273\n')
		print('valores da temperatura humana em:')
		print('kelvin: 309 K')
		print('Celsius: 36 ºC')
		print('Fahrenheit: 96,8 °F\n')
		valorcelsius=float(input('Qual o valor em Celsius?'))
		contacelsiuskelvin=valorcelsius+273
		print(f'Seu valor de Celsius convertido para Kelvin fica {contacelsiuskelvin} K')
	elif p2=="2":
		print('\nTemperatura é uma grandeza microscopica, que é a média das velocidades das moleculas ou atomos de determinado corpo\n')
		print('Formula: Tf=(Tc*9/5)+32\n')
		print('valores da temperatura humana em:')
		print('kelvin: 309 K')
		print('Celsius: 36 ºC')
		print('Fahrenheit: 96,8 °F\n')
		valorcelsius2=float(input('Qual o valor em Celsius?'))
		contacelsiusfahrenheit=(valorcelsius2*9/5)+32
		print(f'Seu valor de Celsius convertido para Fahrenheit fica {contacelsiusfahrenheit} ºF')
	elif p2=="3":
		print('\nTemperatura é uma grandeza microscopica, que é a média das velocidades das moleculas ou atomos de determinado corpo\n')
		print('Formula: Tc=(Tf-32)*5/9\n')
		print('valores da temperatura humana em:')
		print('kelvin: 309 K')
		print('Celsius: 36 ºC')
		print('Fahrenheit: 96,8 °F\n')
		valorfahrenheit=float(input('Qual o valor em Fahrenheit?'))
		contafahrenheitcelsius=(valorfahrenheit-32)*5/9
		print(f'Seu valor de Fahrenheit convertido para Celsius fica {contafahrenheitcelsius} ºC')
	elif p2=="4":
		print('\nTemperatura é uma grandeza microscopica, que é a média das velocidades das moleculas ou atomos de determinado corpo\n')
		print('Formula: Tk=(Tf-32)*5/9+273\n')
		print('valores da temperatura humana em:')
		print('kelvin: 309 K')
		print('Celsius: 36 ºC')
		print('Fahrenheit: 96,8 °F\n')
		valorfahrenheit2=float(input('Qual o valor em Fahrenheit?'))
		contafahrenheitkelvin=(valorfahrenheit2-32)*5/9+273
		print(f'Seu valor de Fahrenheit convertido para Kelvin fica {contafahrenheitkelvin} K')
	elif p2=="5":
		print('\nTemperatura é uma grandeza microscopica, que é a média das velocidades das moleculas ou atomos de determinado corpo\n')
		print('Formula: Tc=Tk-273\n')
		print('valores da temperatura humana em:')
		print('kelvin: 309 K')
		print('Celsius: 36 ºC')
		print('Fahrenheit: 96,8 °F\n')
		valorkelvin=float(input('Qual o valor em Kelvin?'))
		contakelvincelsius=valorkelvin-273
		print(f'Seu valor de Fahrenheit convertido para Kelvin fica {contakelvincelsius} ºC')
	elif p2=="6":
		print('\nTemperatura é uma grandeza microscopica, que é a média das velocidades das moleculas ou atomos de determinado corpo\n')
		print('Formula: Tf=(Tk-273)*9/5+32\n')
		print('valores da temperatura humana em:')
		print('kelvin: 309 K')
		print('Celsius: 36 ºC')
		print('Fahrenheit: 96,8 °F\n')
		valorkelvin2=float(input('Qual o valor em Kelvin?'))
		contakelvinfahrenheit=(valorkelvin2-273)*9/5+32
		print(f'Seu valor de Fahrenheit convertido para Kelvin fica {contakelvinfahrenheit} ºF')	

#PARTE-2-3-4 (DILATAÇÃO TERMICA)		
elif p1=="2":
	print('ainda esta em construção.')
	print('Você escolheu Dilatação Termica\n')
	print('Qual sua icognita?(responda com )')
	p3=input()

#PARTE-2-3-4 (CALOR SENSIVEL)	
elif p1=="3":
	print('\nVocê escolheu Calor Sensivel\n')
	print('Qual sua icognita?(responda com Q,M,C ou Delta0)')
	p4=input()
	if p4=="Q":
		print('\nEssa é a formula usada: Q=m.c.delta0\n')
		M=float(input('Qual é sua M?(sempre em gramas)\n'))
		C=float(input('Qual é seu Calor especifico?\n'))
		delta0=float(input('Qual é sua variação de temperatura?(temperatura final - inicial)\n'))
		contaequiQ=M*C*delta0
		print(f'O valor de Q é {contaequiQ} + unidade da sua questão')
	elif p4=="M":
		print('\nEssa é a formula usada: Q=m.c.delta0\n')
		Q=float(input('Qual é sua Q?\n'))
		C=float(input('Qual é seu Calor especifico?\n'))
		delta0=float(input('Qual é sua variação de temperatura?(temperatura final - inicial)\n'))
		contaequiM=Q/(C*delta0)
		print(f'O valor de Q é {contaequiM} + unidade da sua questão')
	elif p4=="C":
		print('\nEssa é a formula usada: Q=m.c.delta0\n')
		Q=float(input('Qual é sua Q?\n'))
		M=float(input('Qual é sua M?(sempre em gramas)\n'))
		delta0=float(input('Qual é sua variação de temperatura?(temperatura final - inicial)\n'))	
		contaequiC=Q/(M*delta0)
		print(f'O valor de Q é {contaequiC} + unidade da sua questão')
	elif p4=="Delta0":
		final_ou_inicial=input('\nA temperatura que você tem é final ou inicial?\n')
		if final_ou_inicial=="inicial":
			print('\nEssa é a formula usada: Q=m.c.delta0\n')
			Q=float(input('Qual é sua Q?\n'))
			M=float(input('Qual é sua M?(sempre em gramas)\n'))
			C=float(input('Qual é seu Calor especifico?\n'))
			inicial=float(input('Qual a temperatura incial?'))
			contaequiDinicial1=(M*C)
			contaequiDinicial2=(Q-(contaequiDinicial1*inicial))/contaequiDinicial1
			print(f'O valor de Q é {contaequiDinicial2} + unidade da sua questão')
		elif final_ou_inicial=="final":
			print('\nEssa é a formula usada: Q=m.c.delta0\n')
			Q=float(input('Qual é sua Q?\n'))
			M=float(input('Qual é sua M?(sempre em gramas)\n'))
			C=float(input('Qual é seu Calor especifico?\n'))
			final=float(input('Qual a temperatura final?'))
			contaequiDfinal1=(M*C)
			contaequiDfinal2=(Q-(contaequiDfinal1*final))/contaequiDfinal1
			print(f'O valor de Q é {contaequiDfinal2} + unidade da sua questão')

#PARTE-2-3-4 (CALOR LATENTE)
elif p1=="4":
	print('\nVocê escolheu Calor Latente\n')
	print('Qual sua icognita?(responda com Q,M ou L)')
	p5=input()
	if p5=="Q":
		print('\nEssa é a formula usada: Q=m.l\n')
		M=float(input('Qual é sua M?(sempre em gramas)\n'))
		L=float(input('Qual é seu valor de L?\n'))
		contalatQ=M*L
		print(f'O valor de Q é {contalatQ} + unidade da sua questão')
	elif p5=="M":
		print('\nEssa é a formula usada: M=Q/l\n')
		Q=float(input('Qual é o valor do seu Q?\n'))
		L=float(input('Qual é seu valor de L?\n'))
		contalatM=Q/L
		print(f'O valor de M é {contalatM} + unidade da sua questão')
	elif p5=="L":
		print('\nEssa é a formula usada: L=Q/m\n')
		Q=float(input('Qual é o valor do seu Q?\n'))
		M=float(input('Qual é sua M?(sempre em gramas)\n'))
		contalatL=Q/M
		print(f'O valor de L é {contalatL} + unidade da sua questão')

#PARTE-2-3-4 (CALOR SENSIVEL + LATENTE)
elif p1=="5":
	print('\nVocê escolheu Calor Senvivel + Latente\n')
	print('Qual a sua icognita? (responda com Q,M,C ou Delta0)')
	p6=input()

#PARTE-2-3-4 (Gases Ideais)
elif p1=="6":
	print('\nVocê escolheu Gases ideais\n')
	print('como o desenvolvedor é preguiçoso, ele ainda não trabalhou na parte matematica e logica do bagulho, no entanto aqui estão alguns axiomas:\n')
	print('Axioma 0:')
	print('lei geral dos gases = P1.V1/T1 = P2.V2/T2\n')
	print('Axioma 1:')
	print('Temperatura sempre em Kelvin. Para passar de kelvin pra Celsius só subtrair 273 e o inverso é só somar 273\n')
	print('Axioma 2:')
	print('Volume = Litro ou metro³, para converter um para o outro é basicamente regra de 3, sendo 1000 litros = 1 m³\n')
	print('Axioma 3:')
	print('Pressão = atm ou N/m²(Pa), para converter um para o outro é 1 atm = 1.10^5 Pa\n')
	print('Axioma 4:')
	print('Isoterma = Temperatura constante, pressão e volume inversamente proporcionais, um aumenta e o outro diminui na mesma intensidade\n')
	print('Axioma 5:')
	print('Isobarica = Pressão constante, volume e temperatura diretamente proporcionais, um aumenta o outro aumenta junto na mesma intensidade\n')
	print('Axioma 6:')
	print('Isometrica/Isovolumetrica/Isocórica = Volume constante, Pressão e temperatura diretamente proporcionais, um aumenta o outro aumenta junto na mesma intensidade\n')

else:
	print('\nA opção que você escolheu não existe.')
	print('Você quer tentar novamente? [S/N]')
	p0=input()