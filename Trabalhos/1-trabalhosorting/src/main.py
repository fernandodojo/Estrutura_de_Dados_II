# coding=utf-8
from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import click


@click.command()
@click.option('--vertices','-v', type=str, required=True, help='Numero de vertices [7, 100, 1000, 10000, 100000]')
@click.option('--sort','-s', type=str, required=True, help='Algoritmo de ordenacao [insert, select, shell, merge')
@click.option('--pivo','-p', type=str, required=False, default='3', help='Tipo de pivo para o QuickSort 1 - Inicio, 2 - Fim, 3 - Mediana, DEFAULT = 3')


def main(vertices, sort, pivo):

    if sort == 'insert':
        algoritimoDeOrdenacao = InsertionSort()
    elif sort == 'select':
        algoritimoDeOrdenacao = SelectionSort()
    elif sort == 'shell':
        algoritimoDeOrdenacao = ShellSort()
    elif sort == 'merge':
        algoritimoDeOrdenacao = MergeSort()
    elif sort == 'quick' and pivo =='1':
        algoritimoDeOrdenacao = QuickSort1()
    elif sort == 'quick' and pivo =='2':
        algoritimoDeOrdenacao = QuickSort2()
    elif sort == 'quick' and pivo =='3':
        algoritimoDeOrdenacao = QuickSort3()
    

    arquivoJson = '../graph/'+vertices+'.json'
    arquivoDeSaida = '../results/'+vertices +'-'+sort+'_sort'+'.txt'


    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal()
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

if __name__ == "__main__":
    main()