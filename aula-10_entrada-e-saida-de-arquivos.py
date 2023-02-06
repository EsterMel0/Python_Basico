'''
open('arquivo.txt', 'w') # 'w' o sistema gera um arquivo no modo write (escrita)

open('arquivo', 'r') # com 'r' o sistema gera um arquivo no modo leitura (read)

open('arquivo.txt', 'r+') # abre um arquivo de escrita e de leitura

open('arquivo.txt', 'a') # função de adicionar um novo dado no final do arquivo
'''

arquivo = open('arquivo.txt', 'a')
'''
arquivo.write("Hello world\n")
arquivo.write('Estefany\n')
arquivo.write('Carol\n')
arquivo.write('Lene\n')
'''
arquivo.write("NOME: ")
arquivo.write(input("Informe seu nome: "))
arquivo.write("\n")
arquivo.write("IDADE: ")
arquivo.write(input("Informe sua idade: "))
arquivo.write("\n")
arquivo.write("\n")

# print(arquivo.read()) - faz o conteudo de arquivo.txt aparecer no console, mas só lê se o código estiver no formato de comentário
