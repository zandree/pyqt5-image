# -*- coding: utf:8 -*-
import sys
import numpy as np

#Convertendo uma imagem colorida PPM para escala de cinza PGM

#Checando os argumentos de linha de comando
if __name__ == "__main__":
  print(f'Quantos argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")

#Abrir os arquivos de entrada e de saída
entrada = open(sys.argv[1], "r+")
saida = open(sys.argv[2], "w+")

#Fazer o Processamento Digital de Imagens
linha = entrada.readline() # P3
linha = entrada.readline() # Comentário
linha = entrada.readline() # Dimensões
dimensoes = linha.split()
linha = entrada.readline() # Valor fixo
dimensoes = np.array(dimensoes, dtype=int)

linhas = entrada.readlines() # Lê o arquivo até o final
#converter para uma matriz de inteiros
image = np.array(list(linhas)) #array de uma dimensão
image = np.reshape(image, [dimensoes[1], dimensoes[0], 3]) # converte para matriz
image = image.astype(int)

# Escrever o arquivo de saída
saida.write('P2\n')
saida.write('# Criado por Andre\n')
largura = dimensoes[0]
altura = dimensoes[1]
saida.write(str(largura))
saida.write(' ')
saida.write(str(altura))
saida.write('\n')
saida.write('255\n')

for i in range(len(image)):
  for j in range(len(image[1])):
    pixel = int((image[i][j][0] + image[i][j][1] + image[i][j][2]) / 3)
    saida.write(str(pixel))
    saida.write(' ')

#Fechar os arquivos de entrada e de saída
entrada.close()
saida.close()