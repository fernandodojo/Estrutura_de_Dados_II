# coding=utf-8
import cProfile
from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *




def main():

    algoritimoDeOrdenacao = InsertionSort()

    '''
    algoritimoDeOrdenacao = InsertionSort()
    algoritimoDeOrdenacao = SelectionSort()    
    algoritimoDeOrdenacao = ShellSort()    
    algoritimoDeOrdenacao = MergeSort()    
    algoritimoDeOrdenacao = HeapSort()    
    algoritimoDeOrdenacao = QuickSort3()    
    algoritimoDeOrdenacao = QuickSort1()    
    algoritimoDeOrdenacao = QuickSort2()    
    algoritimoDeOrdenacao = QuickSort3()    
    algoritimoDeOrdenacao = CountSort()
    '''

  

    arquivoJson = '../graph/100000.json'
    arquivoDeSaida = '../results/100000-InsertionSort.txt'''


    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal()
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    pr.print_stats()