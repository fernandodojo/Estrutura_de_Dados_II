import re
import string


ENTRADA = 'ptbr.txt'
SAIDA = 'palavras.txt'

import unicodedata

listapalavras = []
with open(ENTRADA, 'r' ) as entrada:

    for linha in entrada:
        linha = unicodedata.normalize('NFKD', linha).encode('ascii','ignore').decode('ascii') #remocao de acentos
        linha = linha.lower() #minusculo        
        linha = result = re.sub(r'\d+', '', linha) #remove numeros
        linha = linha.translate(str.maketrans('', '', string.punctuation)) #remove pontuacao
        linha = linha.strip() #tentativa de remover quebra de linhas espaços no final
        linha = linha.rstrip()#tentativa de remover quebra de linhas espaços no final
        linha = linha.lstrip()#tentativa de remover quebra de linhas espaços no final
        linha = linha.split() #quebra das string(frases) em palavras

        for x in linha:
            if linha and linha != "\n" and linha != " " and len(x)> 3:
                listapalavras.append(x)


with open(SAIDA, 'wt') as saida:
    for x in listapalavras:
        saida.write(x+'\n') #escrita da palavra com quebra de linha.  