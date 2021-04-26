# Exercicio de logica:

**Anos bissextos:**

Normalmente, o ano tem 365 dias. Na verdade, é um valor quebrado, são 365 dias e 6h ou 365,25 dias...mas ia ser estranho um dia com menos de 24 horas, ia ser confuso. Então, pra compensar essas partes quebradas de dia, vez e outra temos um ano com 366 dias, que é a data 29 de fevereiro.

E eles ocorrem a cada 4 anos, menos nos múltiplos de 100 que não são múltiplos de 400. Ou seja, ele também é bissexto ser for múltiplo de 400.

Calma, respira fundo, leia de novo...é um pouco confuso mesmo no começo. Dê uma estudada sobre a história dos anos bissextos, calendários etc, pra relaxar um pouco:

https://pt.wikipedia.org/wiki/Ano_bissexto

Basicamente, de 4 em 4 anos temos anos bissextos:
1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036...

De 100 em 100 anos não temos ano bissexto...:
100, 200, 300 ... não são bissextos

... exceto se forem múltiplos de 400:
400, 800, 1200, 1600... são bissextos

**Logica de como eu resolvi esse exercicio**

Basicamente um ano bissexto é um ano que é divisivel por 400 ou divisivel por 4 e ao mesmo tempo não divisivel por 100.

Simplificando:

O ano tem que ser divisivel por 400;

OU

O ano tem que ser divisivel por 4 e ao mesmo não pode ser divisivel por 100.

SENÃO SE ENCAIXAR NAS DUAS CONDIÇÕES:

Ele não é bissexto

Escrevendo isso em pseudo-codigo:

```
se((ano / 400 == resto 0) OU (ano / 4 == resto 0) E (ano / 100 == resto diferente de 0)){
	escreva: esse ano é bissexto
}senao{
	escreva: esse ano não é bissexto
}
```