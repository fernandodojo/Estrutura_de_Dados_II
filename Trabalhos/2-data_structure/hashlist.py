class HashWord:
    def __init__(self, key, palavra):
        self.palavra_key = key
        self.repeticoes = 1
        self.palavra = palavra

    def get_palavra(self):
        return self.palavra

    def get_repeticoes(self):
        return self.repeticoes

    def get_palavra_key(self):
        return self.palavra_key

    def set_repeticoes(self):
        self.repeticoes += 1

    def __str__(self):
        return ("r:"+str(self.repeticoes) + " k:"+str(self.palavra_key)+" " + self.palavra)

    def __repr__(self):
        return ("r:"+str(self.repeticoes) + " k:"+str(self.palavra_key)+" " + self.palavra)


class Hasharray:
    def __init__(self):
        self.size = 30
        self.array = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        return key % self.size

    def add(self, newhashword):
        index = self._get_hash(newhashword.get_palavra_key())
        bucket = self.array[index]
        key_exists = False

        for i in range(len(bucket)):
            if bucket[i].get_palavra_key() == newhashword.get_palavra_key() and bucket[i].get_palavra() == newhashword.get_palavra():
                key_exists = True
                break
        if key_exists:
            bucket[i].set_repeticoes()
        else:
            bucket.append(newhashword)

    def search(self, key):
        index = self._get_hash(key)
        if self.array[index] is not None:
            for x in self.array[index]:
                print(x)
                if(x.get_palavra_key() == key):
                    print("Resultado de busca:", x)
                    return x
        return None

    def printhash(self):
        for i in range(1, len(self.array)):
            print(i, self.array[i])

    def adiciona_lista(self):
        lista = []
        for palavra in table.array:
            for item in palavra:
                lista.append(item)
        return lista

    def lista_ordenada(self):
        l = self.adiciona_lista()
        l = sorted(l, key=lambda item: item.repeticoes)
        print("\n\n###LISTA ORDENADA###")
        for x in l:
            print(x)


def key_generator(word):
    key = 0
    for char in str(word):
        key += ord(char)
    return key


table = Hasharray()

ENTRADA = 'ptbr.txt'

with open(ENTRADA, 'r') as entrada:
    palavra = entrada.readlines()

for x in palavra:
    table.add(HashWord(key_generator(x), x))


table.printhash()

table.lista_ordenada()

table.search(key_generator('povo\n'))
