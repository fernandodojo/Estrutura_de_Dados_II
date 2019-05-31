import sys


class Node():
    def __init__(self, dado):
        self.dado = dado
        self.pai = None
        self.esquerda = None
        self.direita = None
        self.cor = 1  # 1 . Red, 0 . Black
        self.contador = 1

    def __str__(self):
        s_cor = "RED" if self.cor == 1 else "BLACK"
        return (str(self.contador) + "(" + s_cor + ")" + str(self.dado))

    def __repr__(self):
        s_cor = "RED" if self.cor == 1 else "BLACK"
        return (str(self.contador) + "(" + s_cor + ")" + str(self.dado))


class RedBlackTree():
    def __init__(self):
        self._nulo = Node('None')
        self.raiz = self._nulo

    def preordem(self):
        self._pre_ordem(self.raiz)

    def _pre_ordem(self, node):
        if node != self._nulo:
            print(node.dado, " ")
            self._pre_ordem(node.esquerda)
            self._pre_ordem(node.direita)

    def achar(self, k):
        return self._achar(self.raiz, k)

    def _achar(self, node, key):
        if node == self._nulo or node is None:
            print("Não foi possivel encontrar")
            return None
        if key > node.dado:
            return self._achar(node.direita, key)
        elif key < node.dado:
            return self._achar(node.esquerda, key)
        else:
            s_cor = "RED" if node.cor == 1 else "BLACK"
            print("Resultado de busca:" + str(node.contador) +
                  "(" + s_cor + ")" + str(node.dado))
            return node

    def __rb_transplant(self, u, v):
        if u.pai == None:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    # fix the red-black tree
    def _fix_insersao(self, k):
        while k.pai.cor == 1:
            if k.pai == k.pai.pai.direita:
                u = k.pai.pai.esquerda  # uncle
                if u.cor == 1:
                    # case 3.1
                    u.cor = 0
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    k = k.pai.pai
                else:
                    if k == k.pai.esquerda:
                        # case 3.2.2
                        k = k.pai
                        self.rotacao_direita(k)
                    # case 3.2.1
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    self.rotacao_esquerda(k.pai.pai)
            else:
                u = k.pai.pai.direita  # uncle

                if u.cor == 1:
                    # mirror case 3.1
                    u.cor = 0
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    k = k.pai.pai
                else:
                    if k == k.pai.direita:
                        # mirror case 3.2.2
                        k = k.pai
                        self.rotacao_esquerda(k)
                    # mirror case 3.2.1
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    self.rotacao_direita(k.pai.pai)
            if k == self.raiz:
                break
        self.raiz.cor = 0

    def printtree(self):
        self._printtree(self.raiz, "", True, 0)

    def _printtree(self, node, indent, last, level):
        # print the tree structure on the screen
        if node != self._nulo:
            # if node != None:
            self._printtree(node.direita, indent, True, level+1)
            print()

            for i in range(level):
                print("       ", end="")

            s_cor = "RED" if node.cor == 1 else "BLACK"
            print(str(node.contador) + "(" + s_cor + ")" + str(node.dado))

            self._printtree(node.esquerda, indent, False, level+1)

    def rotacao_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self._nulo:
            y.esquerda.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, x):
        y = x.esquerda
        x.esquerda = y.direita
        if y.direita != self._nulo:
            y.direita.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y
        y.direita = x
        x.pai = y

    def inserir(self, key):

        # Ordinary Binary Search inseririon
        node = Node(key)
        node.pai = None
        node.dado = key
        node.esquerda = self._nulo
        node.direita = self._nulo
        node.cor = 1  # novo no deve ser vermelho
        node.contador = 1  # contador de repeticao

        y = None
        x = self.raiz

        while x != self._nulo:
            y = x
            if node.dado == x.dado:
                x.contador += 1
                return
            if node.dado < x.dado:
                x = x.esquerda
            else:
                x = x.direita

        # y eh pai de x
        node.pai = y

        if y == None:
            self.raiz = node
        elif node.dado < y.dado:
            y.esquerda = node
        else:
            y.direita = node

        # se o novo no eh raiz, retorna
        if node.pai == None:
            node.cor = 0
            return

        # se o avo eh nulo, retorna
        if node.pai.pai == None:
            return

        self._fix_insersao(node)

    def get_raiz(self):
        return self.raiz

    def adiciona_lista(self):
        lista = []
        if self.raiz is not None:
            self._adiciona_lista(self.raiz, lista)
        return lista

    def _adiciona_lista(self, noatual, lista):
        if noatual is not None and noatual is not self._nulo:
            if noatual.esquerda is not None:
                self._adiciona_lista(noatual.esquerda, lista)
            lista.append(noatual)
            if noatual.direita is not None:
                self._adiciona_lista(noatual.direita, lista)

    def lista_ordenada(self):
        l = self.adiciona_lista()
        l = sorted(l, key=lambda item: item.contador)
        print("\n\n###LISTA ORDENADA###")
        for x in l:
            print(x)


if __name__ == "__main__":
    a = RedBlackTree()
    ENTRADA = 'ptbr.txt'
    with open(ENTRADA, 'r') as entrada:
        palavra = entrada.readlines()

    for i in palavra:
        a.inserir(i)

    print("\n\n#### ARVORE  ##( RAIZ ----> FOLHAS )####")
    a.printtree()
    a.lista_ordenada()
    a.achar('televisao')
