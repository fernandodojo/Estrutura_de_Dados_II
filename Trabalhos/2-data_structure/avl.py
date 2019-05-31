class node:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.pai = None
        self.altura = 1
        self.contador = 1

    def __str__(self):
        return str(self.contador) + " " + self.dado

    def __repr__(self):
        return str(self.contador) + " " + self.dado


class AVLTree:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        if self.raiz is None:
            self.raiz = node(dado)
        else:
            self._inserir(dado, self.raiz)

    def _inserir(self, dado, noatual):
        if dado < noatual.dado:
            if noatual.esquerda is None:
                noatual.esquerda = node(dado)
                noatual.esquerda.pai = noatual
                self._checar_insersao(noatual.esquerda)
            else:
                self._inserir(dado, noatual.esquerda)
        elif dado > noatual.dado:
            if noatual.direita is None:
                noatual.direita = node(dado)
                noatual.direita.pai = noatual
                self._checar_insersao(noatual.direita)
            else:
                self._inserir(dado, noatual.direita)
        elif dado == noatual.dado:
            noatual.contador += 1

    def print_tree(self):
        if self.raiz is not None:
            self._print_tree(self.raiz)

    def _print_tree(self, noatual):
        if noatual is not None:
            self._print_tree(noatual.esquerda)
            print('%s, h=%d' % (str(noatual.dado), noatual.altura))
            self._print_tree(noatual.direita)

    def printtree(self):
        self._printtree(self.raiz, 0)
        print()

    def _printtree(self, p, level):
        if p is None:
            return
        self._printtree(p.direita, level+1)
        print()

        for i in range(level):
            print("       ", end="")
        print(str(p.contador)+" " + p.dado)

        self._printtree(p.esquerda, level+1)

    def altura(self):
        if self.raiz is not None:
            return self._altura(self.raiz, 0)
        else:
            return 0

    def _altura(self, noatual, alturaatual):
        if noatual is None:
            return alturaatual
        esquerda_altura = self._altura(noatual.esquerda, alturaatual+1)
        direita_altura = self._altura(noatual.direita, alturaatual+1)
        return max(esquerda_altura, direita_altura)

    def achar(self, dado):
        if self.raiz is not None:
            return self._achar(dado, self.raiz)
        else:
            return None

    def _achar(self, dado, noatual):
        if dado == noatual.dado:
            print(noatual.dado, noatual.contador)
            return noatual
        elif dado < noatual.dado and noatual.esquerda is not None:
            return self._achar(dado, noatual.esquerda)
        elif dado > noatual.dado and noatual.direita is not None:
            return self._achar(dado, noatual.direita)

    def _checar_insersao(self, noatual, path=[]):
        if noatual.pai is None:
            return
        path = [noatual]+path

        esquerda_altura = self.pegar_altura(noatual.pai.esquerda)
        direita_altura = self.pegar_altura(noatual.pai.direita)

        if abs(esquerda_altura-direita_altura) > 1:
            path = [noatual.pai]+path
            self._rebalancear_no(path[0], path[1], path[2])
            return

        nova_altura = 1+noatual.altura
        if nova_altura > noatual.pai.altura:
            noatual.pai.altura = nova_altura

        self._checar_insersao(noatual.pai, path)

    def _rebalancear_no(self, z, y, x):
        if y == z.esquerda and x == y.esquerda:
            self._rotacao_direita(z)
        elif y == z.esquerda and x == y.direita:
            self._rotacao_esquerda(y)
            self._rotacao_direita(z)
        elif y == z.direita and x == y.direita:
            self._rotacao_esquerda(z)
        elif y == z.direita and x == y.esquerda:
            self._rotacao_direita(y)
            self._rotacao_esquerda(z)

    def _rotacao_direita(self, z):
        sub_raiz = z.pai
        y = z.esquerda
        t3 = y.direita
        y.direita = z
        z.pai = y
        z.esquerda = t3
        if t3 is not None:
            t3.pai = z
        y.pai = sub_raiz
        if y.pai is None:
            self.raiz = y
        else:
            if y.pai.esquerda == z:
                y.pai.esquerda = y
            else:
                y.pai.direita = y
        z.altura = 1+max(self.pegar_altura(z.esquerda),
                         self.pegar_altura(z.direita))
        y.altura = 1+max(self.pegar_altura(y.esquerda),
                         self.pegar_altura(y.direita))

    def _rotacao_esquerda(self, z):
        sub_raiz = z.pai
        y = z.direita
        t2 = y.esquerda
        y.esquerda = z
        z.pai = y
        z.direita = t2
        if t2 is not None:
            t2.pai = z
        y.pai = sub_raiz
        if y.pai is None:
            self.raiz = y
        else:
            if y.pai.esquerda == z:
                y.pai.esquerda = y
            else:
                y.pai.direita = y
        z.altura = 1+max(self.pegar_altura(z.esquerda),
                         self.pegar_altura(z.direita))
        y.altura = 1+max(self.pegar_altura(y.esquerda),
                         self.pegar_altura(y.direita))

    def pegar_altura(self, noatual):
        if noatual is None:
            return 0
        return noatual.altura

    def adiciona_lista(self):
        lista = []
        if self.raiz is not None:
            self._adiciona_lista(self.raiz, lista)
        return lista

    def _adiciona_lista(self, noatual, lista):
        if noatual is not None:
            self._adiciona_lista(noatual.esquerda, lista)
            lista.append(noatual)
            self._adiciona_lista(noatual.direita, lista)

    def lista_ordenada(self):
        l = self.adiciona_lista()
        l = sorted(l, key=lambda item: item.contador)
        print("###LISTA ORDENADA###")
        for x in l:
            print(x)

    def print_tree(self):
        if self.raiz is not None:
            self._print_tree(self.raiz)

    def _print_tree(self, noatual):
        if noatual is not None:
            self._print_tree(noatual.esquerda)
            print('%s, h=%d' % (str(noatual.dado), noatual.altura))
            self._print_tree(noatual.direita)


if __name__ == "__main__":
    a = AVLTree()
    ENTRADA = 'ptbr.txt'
    with open(ENTRADA, 'r') as entrada:
        palavra = entrada.readlines()

    for i in palavra:
        a.inserir(i)

    print("\n\n#### ARVORE  ##( RAIZ ----> FOLHAS )####")
    a.printtree()
    print(a.achar('povo'))
    a.lista_ordenada()
