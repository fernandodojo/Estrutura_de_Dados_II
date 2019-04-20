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
    contador=0
    atri=0
    def ordenar(self, colecao):
    	
        for i in range(0, len(colecao) - 1):
            self.atri+=1
            minIndex = i
            for j in range(i, len(colecao)):
            	self.contador +=1
                if int(colecao[minIndex]['weight']) > int(colecao[j]['weight']):
                    self.atri+=1
                    minIndex = j
            self.contador +=1
            if i != minIndex:
                self.atri+=2
                colecao[minIndex], colecao[i] = colecao[i], colecao[minIndex]

        print (self.contador)
        print (self.atri)
        return colecao


class InsertionSort(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
        gap = 1
        self.atri+=1
        
        for i in range(1, len(colecao)):
            self.atri+=3
            aux = colecao[i]
            j = i - gap
            while j >= 0 and int(colecao[j]['weight']) > int(aux['weight']):
            	self.contador +=1
                self.atri+=2
                colecao[j + gap] = colecao[j]
                j -= 1
            self.contador +=1
            colecao[j + gap] = aux
        print(self.contador)
        print(self.atri)
        return colecao


class ShellSort(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
        self.atri+=1
        gap = len(colecao) // 2
        
        while gap >= 1:
            for i in range(gap, len(colecao)):
            	self.contador +=1
                self.atri+=3
                aux = colecao[i]
                j = i - gap
                while j >= 0 and int(colecao[j]['weight']) > int(
                        aux['weight']):
                    colecao[j + gap] = colecao[j]
                    j = j - gap
                    self.contador +=1
                colecao[j + gap] = aux
            self.contador +=1
            self.atri+=1
            gap = gap // 2
        print(self.contador)
        print(self.atri)
        return colecao

class MergeSort(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
        if len(colecao) > 1:
            self.atri+=6
            half = len(colecao) // 2
            left = colecao[:half]
            right = colecao[half:]
            self.contador +=1
            self.ordenar(left)
            self.ordenar(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
            	self.contador+=3
            	self.atri+=1
                if int(left[i]['weight']) < int(right[j]['weight']):
                    self.atri+=2
                    colecao[k] = left[i]
                    i += 1
                else:
                    self.atri+=2
                    colecao[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
            	self.contador+=1
                self.atri+=3
                colecao[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
            	self.contador+=1
                self.atri+=3
                colecao[k] = right[j]
                j += 1
                k += 1
        print("contador", self.contador)
        print("atribuicoes", self.atri)
        return colecao



class QuickSort3(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)
        print(self.contador)
        print(self.atri)
        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            self.atri+=1
            self.contador+=1
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        self.atri+=2
        mid = (right + left) // 2
        pivot = right
        
        if int(colecao[left]['weight']) < int(colecao[mid]['weight']):
            self.contador+=1
            if int(colecao[mid]['weight']) < int(colecao[right]['weight']):
                self.contador+=1
                self.atri+=1
                pivot = mid
        elif int(colecao[left]['weight']) < int(colecao[right]['weight']):
            self.atri+=1
            self.contador+=1
            pivot = left
        return pivot


    def partition(self, colecao, left, right):
        self.atri+=6
        pindex = self.get_pivot(colecao, left, right)
        pvalue = colecao[pindex]
        colecao[pindex], colecao[left] = colecao[left], colecao[pindex]
        aux = left

        for i in range(left, right + 1):
            self.contador+=2
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                self.atri+=2
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

class QuickSort2(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)
        print(self.contador)
        print(self.atri)
        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            self.atri+=1
            self.contador+=1
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        pivot = right
        self.atri+=1
        return pivot


    def partition(self, colecao, left, right):
        self.atri+=6
        pindex = self.get_pivot(colecao, left, right)
        pvalue = colecao[pindex]
        colecao[pindex], colecao[left] = colecao[left], colecao[pindex]
        aux = left

        for i in range(left, right + 1):
            self.contador+=2
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                self.atri+=2
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

class QuickSort1(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)
        print(self.contador)
        print(self.atri)
        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            self.atri+=1
            self.contador+=1
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        pivot = left     
        self.atri+=1
        return pivot


    def partition(self, colecao, left, right):
        self.atri+=4
        pindex = self.get_pivot(colecao, left, right)
        pvalue = colecao[pindex]
        aux = left

        for i in range(left, right + 1):
            self.contador+=2
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                self.atri+=2
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

class HeapSort(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
        self.atri+=2
        size = len(colecao)
        self.heapify(colecao, size)
        end = size-1
        while(end > 0):
        	self.atri+=3
        	self.contador+=1
        	colecao[0], colecao[end] = colecao[end], colecao[0]
        	self.switch(colecao, 0, end)
        	end -= 1
        print(self.contador)
        print(self.atri)
        return colecao

    def switch(self, colecao, i, size):
        self.atri+=3
        l = 2*i+1
        r = 2*i+2
        largest = i
        if l <= size-1 and int(colecao[l]['weight']) > int(colecao[i]['weight']):
            largest = l
            self.atri+=1
            self.contador+=1
        if r <= size-1 and int(colecao[r]['weight']) > int(colecao[largest]['weight']):
            largest = r
            self.atri+=1
            self.contador+=1
        if largest != i:
        	self.atri+=2
        	self.contador+=1
        	colecao[i], colecao[largest] = colecao[largest], colecao[i]
        	self.switch(colecao, largest, size)

    def heapify(self, colecao, size):
    	self.atri+=1
    	p = (size//2)-1
    	while p>=0:
    		self.atri+=1
    		self.switch(colecao, p, size)
    		p -= 1
    		self.contador+=1


class CountSort(object):
    contador=0
    atri=0
    def ordenar(self, colecao):
    	self.atri+=5
        n = len(colecao)
        mx = int(colecao[0]['weight'])
        for i in colecao:
            if int(i['weight'])> mx:
                self.atri+=1
                mx = int(i['weight'])
        	self.contador+=2
        mx = mx+1

        B = [0]*mx
        C = [0]*n

        for i in colecao:
            B[int(i['weight'])] += 1
            self.atri+=1
            self.contador+=1

        for i in range(len(B)-1):
            B[i+1] += B[i]
            self.atri+=1
            self.contador+=1

        for i in range(len(colecao)):
            C[B[int(colecao[i]['weight'])]-1] = colecao[i]
            B[int(colecao[i]['weight'])] -=1
            self.atri+=2
            self.contador+=1

        for i in range(0, len(C)):
            colecao[i] = C[i]
            self.atri+=1
            self.contador+=1
        print(self.contador)
        print(self.atri)
        return colecao

