# Exercicio de logica:

**Enunciado**

Você tem 5 moedas, uma delas é falsa, e a falsa tem o peso menor que as outras. Desenvolva um programa para fazer o minimo numero de pesagens e descobrir a falsa (tem como resolver com 2 pesagens)

**Logica de como eu resolvi esse exercicio**

Legenda:

1 = moeda

Basicamente o pensamento que eu tive foi:

Eu tenho 5 moedas: 1 1 1 1 1 

Se eu pesar a primeira: 1 

Anotar o valor dela: 0.25

E logo em seguida pesar ela mais as proximas 3 e deixar a quinta de fora: 1 + 1 1 1 (Primeira + 3 seguintes) |   1 (Quinta que ficou de fora)

Agora eu tiro a media do peso dessas 4 moedas juntas: 0.25

SE o valor da média for maior que o da primeira moeda, a primeira é logicamente falsa. SE o valor da media for igual ao valor da primeira moeda, isso quer dizer que a ultima é falsa. E SE não for nenhuma dessas 2 situações ou seja, se o valor da media for menor que o valor da primeira moeda, isso quer dizer que a moeda falsa está no meio da 3 que foram pesadas junto da primeira e a primeira e a ultima são verdadeiras: 1 (Primeira) | 1 1 1 (A falsa está aqui dentro) | 1 (Quinta)  

Escrevendo isso em pseudo-codigo:

```
se(PesoQuatroPrimeirasMoedas/4 == PesoPrimeiraMoeda){
	escreva: A ultima é falsa.
}se(PesoQuatroPrimeirasMoedas/4 > PesoPrimeiraMoeda){
	escreva: A primeira é falsa.
}senao{
	escreva: A falsa está entre as 3 que foram pesadas junto da primeira.
}
```