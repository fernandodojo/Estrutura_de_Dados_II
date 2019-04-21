#coding=utf-8
'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- colecao coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''


# Sua classe algoritmo de ordenação precisar ter um método ordenar
class SelectionSort(object):
    def ordenar(self, colecao):
        for i in range(0, len(colecao) - 1):    #inicia a verificação do inicio
            minIndex = i                        #estabelece o primeiro valor antes do proximo laço como indice de verificacao
            for j in range(i, len(colecao)):    #inicia laco a partir do indice corrente do laco anterior 
                if int(colecao[minIndex]['weight']) > int(colecao[j]['weight']): #compara o valor corrente do primeiro laco com todos os valores to atual i até o final no laco 
                    minIndex = j                #se a confirmacao de que o valor deste laco for menor que o do laco anterior, o indice é classificado como o novo menor valor
            if i != minIndex:
                colecao[minIndex], colecao[i] = colecao[i], colecao[minIndex] #se estes valores possuirem indices diferentes ocorre a troca

        return colecao


class InsertionSort(object):
    def ordenar(self, colecao):
        gap = 1                                 #como distancia 1 de checagem de valor
        for i in range(1, len(colecao)):        #laco da segunda posicao até o final  
            aux = colecao[i]                    #varia com indice corrente do laco ah ser colocado a parte ordenada
            j = i - gap                         #inde que varrera a parte "ordenada" em busca da posicao correta do aux
            while j >= 0 and int(colecao[j]['weight']) > int(aux['weight']): #verifica o valor de indice fora da parte ordenada com indice da parte ordenada
                colecao[j + gap] = colecao[j]   #caso o valor da variavel aux seja menor que o valor de determnado indice da parte ordenada, ocorre a troca temporaria
                j -= 1                          #decrementa para continuar a verificacao na parte ordenada
            colecao[j + gap] = aux              #finaliza-se a troca pro indice final

        return colecao


class ShellSort(object):
    def ordenar(self, colecao):
        gap = len(colecao) // 2                     #gap sempre a parte inteira da divisao do tamanho da lista por dois
        while gap >= 1:                             #enquanto o gap nao chegar a 1, como no insertion
            for i in range(gap, len(colecao)):      #laco da posicao do gap até o final  
                aux = colecao[i]                    #varia com indice corrente do laco ah ser colocado a parte ordenada
                j = i - gap                         #inde que varrera a parte "ordenada" em busca da posicao correta do aux de tantas em tantas posicoes
                while j >= 0 and int(colecao[j]['weight']) > int(
                        aux['weight']):             #verifica o valor de indice fora da parte ordenada com indice da parte ordenada
                    colecao[j + gap] = colecao[j]   #caso o valor da variavel aux seja menor que o valor de determnado indice da parte ordenada, ocorre a troca temporaria
                    j = j - gap                     #decrementa para continuar a verificacao na parte ordenada, atras da posicao corrente do i
                colecao[j + gap] = aux              #finaliza-se a troca pro indice final
            gap = gap // 2                          #divide a distancia por dois para verificar com indices mais proximos

        return colecao

class MergeSort(object):
    def ordenar(self, colecao):
        if len(colecao) > 1:                #enquanto a colecao tiver tamanho maior que 1, este sera subdivido em dois
            half = len(colecao) // 2        #encontra-se o meio para realizar a divisao da lista em duas aprtes
            left = colecao[:half]           #lista que vai do inicio ate a medate
            right = colecao[half:]          #lista que vai da metate atoe o fim

            self.ordenar(left)              #chamada recursiva que permite continuas subdivisoes ate atender a condicao de 1 item, com as subdivicoes da "esquerda"
            self.ordenar(right)             #chamada recursiva que permite continuas subdivisoes ate atender a condicao de 1 item, com as subdivicoes da "direita"

            i = j = k = 0                   #indice que permitiram a varredura da sublista para colocar na lista final, "colecao"
            while i < len(left) and j < len(right):                     #enquando os indices estiverem percorrendo dentro das sublistas
                if int(left[i]['weight']) < int(right[j]['weight']):    #se o item corrente da subslita da esquerda for menor que o da direira, este sera atribuido a colecao
                    colecao[k] = left[i]
                    i += 1                  #encrementa o indice i da sublista a esquerda para n se verificar o mesmo indice
                else:
                    colecao[k] = right[j]   #caso o da esquer nao seja menor, o da direira sera atribuido a colecao final
                    j += 1                  #encrementa-se para nao se repetir a verificacao
                k += 1                      #sempre que ocorrer alguma atribuicao das sublistas na lista colecao, o indice corrente da colecao sera encrementado para evitar sobrescrição

            while i < len(left):            #caso o vetor da direita termine e o da esquerda ainda tenha indices, este sera automaticamente atribuido a lista colecao
                colecao[k] = left[i]
                i += 1
                k += 1
            while j < len(right):           #caso o vetor da esquerda termine e o da direita ainda tenha indices, este sera automaticamente atribuido a lista colecao
                colecao[k] = right[j]
                j += 1
                k += 1

        return colecao



class QuickSort3(object):
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)         #interface de usuario para atender requisito do kruskal

        return colecao

    def sort(self, colecao, left, right):
        if left<right:                                  #verifica se a lista a ser ordenada nao possui apenas um ou menos de 1 item
            p = self.partition(colecao, left, right)    #chama o particionamento que possui o pivo em sua devida posicao, para subdivir então os valores adjacentes ao pivo
            self.sort(colecao, left, p-1)               #chamada recursiva para realizar a ordenacao com todos os indices a esquerda do antigo pivo
            self.sort(colecao, p + 1, right)            #chamada recursiva para realizar a ordenacao com todos os indices a direita do antigo pivo

        
    def get_pivot(self, colecao, left, right):
        mid = (right + left) // 2                       #localiza o indice do meio da lista
        pivot = right                                   #valor temporario do pivo como o indice mais a direita
        
        if int(colecao[left]['weight']) < int(colecao[mid]['weight']):      #verifica se o valor mais esquer é menor que o do meio
            if int(colecao[mid]['weight']) < int(colecao[right]['weight']): #verifica se o valor do meio é menor que o valor mais a direita
                pivot = mid                             #o pivo sera o indece com valor entre a indice da esquerda e a direita
        elif int(colecao[left]['weight']) < int(colecao[right]['weight']):  #se o valor da esquer for menor que o da direita e ainda assim maior que o meio
            pivot = left                                #o pivo sera a indece da esquerda que correspode ao valor intermediario
        return pivot                                    #se nenhuma das condiões forem satisfeitas, o pivo continuara a ser o mais a indice da direita


    def partition(self, colecao, left, right):
        pindex = self.get_pivot(colecao, left, right)   #guarda o indice inicial do pivo
        pvalue = colecao[pindex]                        #guarda o valor do indice do pivo
        colecao[pindex], colecao[left] = colecao[left], colecao[pindex] #troca-se o valor entre os indices do pivo e o mais a esquerda, para seguir o algoritmo
        aux = left                                      #guarda o pivo, ja que este assumiu o valor mais a esquerda(apenas temporario)

        for i in range(left, right + 1):                #percorre toda a lista
            if int(colecao[i]['weight']) < int(pvalue['weight']):       #compara o valor de cada indice da lista com o do pivo
                aux += 1                                #se o o valor do indice for da lista for menor, o indice temporario do pivo sera incrementado
                colecao[i], colecao[aux] = colecao[aux], colecao[i]     #ocorre a troca entre os valores do do pivo com o item a ser verificado
        colecao[left], colecao[aux] = colecao[aux], colecao[left]       #ao final da verificacao ocorrere a troca real entre o valor mais a esquerda com o pivo, fazendo o pivo assumir sua posicao ao meio da lista,

        return (aux)                                    #ao garantindo ordenacao do menores a esquerda, e maiores a direita, nas linhas anterios, o pivo é retornado

class QuickSort2(object): #MESMO CODIGO ANTERIOR PEGANDO O PIVO A DIREITA DIRETAMENTE
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)

        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        pivot = right   #PIVO A DIREITA
        return pivot


    def partition(self, colecao, left, right):
        pindex = self.get_pivot(colecao, left, right)
        pvalue = colecao[pindex]
        colecao[pindex], colecao[left] = colecao[left], colecao[pindex]
        aux = left

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

class QuickSort1(object): #MESMO CODIGO ANTERIOR PEGANDO O PIVO A ESQUERDA DIRETAMENTE
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)

        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        pivot = left     #PIVO A ESQUERDA
        return pivot


    def partition(self, colecao, left, right): #NAO REALIZA TROCA DE POSICAO COM O DA ESQUERDA, POS JÁ É O MAIS A ESQUERDA
        pindex = self.get_pivot(colecao, left, right)
        pvalue = colecao[pindex]
        aux = left

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

class HeapSort(object):   
    def ordenar(self, colecao):
        size = len(colecao)                         #verifica o tamanho da lista
        self.heapify(colecao, size)                 #chamada de funcao recursiva que permite percorrer o heap em forma de lista
        end = size-1                                #guarda o indice do final do vetor
        while(end > 0):                             #verifica a lista do final até o inicio
            colecao[0], colecao[end] = colecao[end], colecao[0] #troca o ultimo valor com o inicio para verificar do final ate o inicio, das folhas a raiz
            self.switch(colecao, 0, end)            #chamada recursiva para realizar troca
            end -= 1                                #continua decrementado a veriricacao
        return colecao       
    def switch(self, colecao, i, size):
        l = 2*i+1                                   #indice, a esquerda da raiz
        r = 2*i+2                                   #indice a direita da raiz  
        largest = i
        if l <= size-1 and int(colecao[l]['weight']) > int(colecao[i]['weight']):       #verifica raiz com todos os nois a esquerda até achar o de maior valor
            largest = l                             #troca o indice do maior para o do no com maior valor
        if r <= size-1 and int(colecao[r]['weight']) > int(colecao[largest]['weight']): #verifica raiz com todos os nois a direita até achar o de maior valor
            largest = r                             #troca o indice do maior para o do no com maior valor
        if largest != i:                            #se este indice do maior dor diferente da raiz
            colecao[i], colecao[largest] = colecao[largest], colecao[i]                 #é realizado a troca entra nos e a raiz sobe
            self.switch(colecao, largest, size)

    def heapify(self, colecao, size):
        p = (size//2)-1                             #ignora verificar nos inexistentes com as folhas como se fossem raizes
        while p>=0:                                 #enquanto nao chegar na raiz
            self.switch(colecao, p, size)           #chama funcao de troca
            p -= 1                                  #decrementa permitindo chegar no inicio


class CountSort(object):
    def ordenar(self, colecao):
        n = len(colecao)                #tamanho da lista
        mx = int(colecao[0]['weight'])  #guarda o valor do primeiro indice da lista
        for i in colecao:               #percorrera a lista em busca do indice com maior valor
            if int(i['weight'])> mx:    #verifica se o indice corrente tem valor superior ao da primeira posicao
                mx = int(i['weight'])   #se sim, mx guardara o novo maior valor
        mx = mx+1                       #mx tera seu valor acrescido de um para compensar a posicao que se inicia com 0

        B = [0]*mx                      #aloca-se lista com o mesmo tamanho do maior valor da lista
        C = [0]*n                       #aloca-se lista com mesmo tamanho da original

        for i in colecao:
            B[int(i['weight'])] += 1    #contabiliza a aparição de determinado valor e suas repetições no indice de mesmo valor na lista B

        for i in range(len(B)-1):       #varre a lista B, com o intuito de somar todos os valores de cada indice de B, atruibuindo ao indice seguinte
            B[i+1] += B[i]              #segundo o algoritmo esta soma ira calcular a real posição de cada valor, com vase na quatidade de numeros do inicio até o valor de fato

        for i in range(len(colecao)):
            C[B[int(colecao[i]['weight'])]-1] = colecao[i]  #varre a lista colecao, acesando o valor peso. A partir deste valor acessa a lista B como indice, que acessara a posicao real em B, para so entao atribuir a C, o valor do peso inicial
            B[int(colecao[i]['weight'])] -=1                #decrementa em B para nao haver sobrecricao de valores em caso de repeticao

        for i in range(0, len(C)):
            colecao[i] = C[i]           #atrinui-se valores de C na lista oricinal, por meio de apontamento, para não haver perda de dados.

        return colecao

