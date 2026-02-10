Algoritmo "semnome"


Var
//secao de declarções das variaveis
nome_usuario:caractere
idade:inteiro
primeira_nota:real
segunda_nota:real
soma:real
media:real
resultado:caractere
Inicio
//entrada de dados
escreval("você está vendo a sua nota a partir daqui")
escreva("digite seu nome de usuario: ")
leia(nome_usuario)
escreva("digite sua idade: ")
leia(idade)
escreva("digite a primeira nota: ")
leia(primeira_nota)

escreva("digite a segunda nota: ")
leia(segunda_nota)
//processando
soma<-primeira_nota+segunda_nota
media<-soma/2
//media<-(primeira_nota+segunda_nota)/2
se media>= 7 entao
resultado<-"aprovado"
senao
resultado<-"reprovado"
fimse
//saida
escreval
escreval("a soma das suas notas são: ", soma)
escreval("a media das duas notas é: ", media)
escreval("você foi: ", resultado)
escreval(nome_usuario, idade, "anos")



Fimalgoritmo