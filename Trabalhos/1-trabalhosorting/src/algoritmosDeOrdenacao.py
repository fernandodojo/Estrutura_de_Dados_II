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
        for i in range(0, len(colecao) - 1):
            minIndex = i
            for j in range(i, len(colecao)):
                if int(colecao[minIndex]['weight']) > int(colecao[j]['weight']):
                    minIndex = j
            if i != minIndex:
                colecao[minIndex], colecao[i] = colecao[i], colecao[minIndex]

        return colecao


class InsertionSort(object):
    def ordenar(self, colecao):
        gap = 1
        for i in range(1, len(colecao)):
            aux = colecao[i]
            j = i - gap
            while j >= 0 and int(colecao[j]['weight']) > int(aux['weight']):
                colecao[j + gap] = colecao[j]
                j -= 1
            colecao[j + gap] = aux

        return colecao


class ShellSort(object):
    def ordenar(self, colecao):
        gap = len(colecao) // 2

        while gap >= 1:
            for i in range(gap, len(colecao)):
                aux = colecao[i]
                j = i - gap
                while j >= 0 and int(colecao[j]['weight']) > int(
                        aux['weight']):
                    colecao[j + gap] = colecao[j]
                    j = j - gap
                colecao[j + gap] = aux
            gap = gap // 2

        return colecao

class MergeSort(object):
    def ordenar(self, colecao):
        if len(colecao) > 1:
            half = len(colecao) // 2
            left = colecao[:half]
            right = colecao[half:]

            self.ordenar(left)
            self.ordenar(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if int(left[i]['weight']) < int(right[j]['weight']):
                    colecao[k] = left[i]
                    i += 1
                else:
                    colecao[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                colecao[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                colecao[k] = right[j]
                j += 1
                k += 1

        return colecao



class QuickSort3(object):
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)

        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        mid = (right + left) // 2
        pivot = right
        
        if int(colecao[left]['weight']) < int(colecao[mid]['weight']):
            if int(colecao[mid]['weight']) < int(colecao[right]['weight']):
                pivot = mid
        elif int(colecao[left]['weight']) < int(colecao[right]['weight']):
            pivot = left
        return pivot


    def partition(self, colecao, left, right):
        pivotIndex = self.get_pivot(colecao, left, right)
        pivotValue = colecao[pivotIndex]
        colecao[pivotIndex], colecao[left] = colecao[left], colecao[pivotIndex]
        aux = left

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pivotValue['weight']):
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

class QuickSort2(object):
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)

        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        #mid = (right + left) // 2
        #pivot = right
        pivot = left
        
        '''if int(colecao[left]['weight']) < int(colecao[mid]['weight']):
            if int(colecao[mid]['weight']) < int(colecao[right]['weight']):
                pivot = mid
        elif int(colecao[left]['weight']) < int(colecao[right]['weight']):
            pivot = left'''
        return pivot


    def partition(self, colecao, left, right):
        pivotIndex = self.get_pivot(colecao, left, right)
        pivotValue = colecao[pivotIndex]
        colecao[pivotIndex], colecao[left] = colecao[left], colecao[pivotIndex]
        aux = left

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pivotValue['weight']):
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

class QuickSort1(object):
    def ordenar(self, colecao):
        self.sort(colecao, 0, len(colecao) - 1)

        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            p = self.partition(colecao, left, right)
            self.sort(colecao, left, p-1)
            self.sort(colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        #mid = (right + left) // 2
        pivot = right
        
        '''if int(colecao[left]['weight']) < int(colecao[mid]['weight']):
            if int(colecao[mid]['weight']) < int(colecao[right]['weight']):
                pivot = mid
        elif int(colecao[left]['weight']) < int(colecao[right]['weight']):
            pivot = left'''
        return pivot


    def partition(self, colecao, left, right):
        pivotIndex = self.get_pivot(colecao, left, right)
        pivotValue = colecao[pivotIndex]
        colecao[pivotIndex], colecao[left] = colecao[left], colecao[pivotIndex]
        aux = left

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pivotValue['weight']):
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
        colecao[left], colecao[aux] = colecao[aux], colecao[left]

        return (aux)

