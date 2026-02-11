Algoritmo "semnome"

Var
  primeira_nota:real
  segunda_nota:real
  terceira_nota:real
  soma:real
  media:real
  resultado:caractere
Inicio
escreva("digite a primeira nota: ")
leia(primeira_nota)

escreva("digite a segunda nota: ")
leia(segunda_nota)


soma<-primeira_nota+segunda_nota
media<-soma/2

se media >=7  entao
resultado<-"aprovado"
senao
resultado<-"reprovado"
fimse
escreval("a soma das suas notas sao: ", soma)
escreval("a media das suas notas é: ", media)
escreval("voce foi: ", resultado)




Fimalgoritmo