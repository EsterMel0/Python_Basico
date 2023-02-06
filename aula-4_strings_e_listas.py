'''
AULA 04: STRINGS E LISTAS
'''

frase = "oi, tudo bem?"
lista_nome = ["joao", "maria", "jose", "rosa"]
lista_nome.append("mirela") #o comando .append incluira o item a uma lista já existente
lista_nome.remove("jose") #o comando .remove excluirá um item de uma lista já existente
#lista_nome.clear() #o comando .clear limpa a lista_nome
lista_nome.insert(1, "mirela") #permite escolher em que posição inserir o item
lista_nome[0] = "julia" #permite trocar um item por outro
contador_mirela = lista_nome.count("mirela") #conta a quantida de um determinado item

#print(lista_nome[-1]) #imprime o ultimo item da lista
print(lista_nome) #imprime toda a lista
print(contador_mirela)
print(lista_nome.pop()) #retira o ultimo item da lista
#print(frase[1:5]) #imprime um intervalo entre os indices digitados