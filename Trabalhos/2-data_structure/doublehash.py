import time
import resource
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


class HashTable:
    def __init__(self, size=100000):
        self.size = size
        self.array = [None] * self.size
        self.n = 0

    def hash1(self, key):
        return (key % self.size)

    def hash2(self, key):
        return(3 - (key % self.size))

    def rehash(self, new_size):
        temp = HashTable(new_size)

        for i in range(self.size):
            if self.array[i] is not None and self.array[i].get_palavra_key() != -1:
                temp.insert(self.array[i])

        self.array = temp.array
        self.size = new_size

    def insert(self, newhashword):

        hash1 = self.hash1(newhashword.get_palavra_key())
        hash2 = self.hash2(newhashword.get_palavra_key())
        index = hash1

        for i in range(1, self.size):
            if self.array[index] is None or self.array[index].get_palavra_key() == -1:
                self.array[index] = newhashword
                self.n += 1
                return

            # if self.array[index].get_palavra_key() == index:
            if self.array[index].get_palavra_key() == newhashword.get_palavra_key():
                if(newhashword.get_palavra() == self.array[index].get_palavra()):
                    self.array[index].set_repeticoes()
                    return

            index = (index+hash2) % self.size

        print("Table is full:")

    def insert1(self, newhashword):
        if self.n >= self.size//2:
            self.rehash(self.next_prime(2*self.size))
            print("New table size is:", self.size)
            self.insert(newhashword)

    def next_prime(self, x):
        while self.is_prime(x) is not True:
            x = x+1
        return x

    def is_prime(self, x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def search(self, key):
        hash1 = self.hash1(key)
        hash2 = self.hash2(key)

        index = hash1

        for i in range(1, self.size):
            if self.array[index] is None or self.array[index].get_palavra_key() == -1:
                return None

            if self.array[index].get_palavra_key() == key:
                print("Resultado de busca:", self.array[index])
                return self.array[index]

            if index == hash1:
                break

            index = (index+hash2) % self.size

    def display_table(self):
        for i in range(self.size):
            if self.array[i] is not None and self.array[i].get_palavra_key() != -1:
                print("[", end="")
                print(i, end="")
                print("]", end="")
                print(self.array[i])

    def adiciona_lista(self):
        lista = []
        for x in self.array:
            if x is not None:
                # print(x)
                lista.append(x)
        return lista

    def lista_ordenada(self):
        l = self.adiciona_lista()
        l = sorted(l, key=lambda item: item.repeticoes)
        print("\n\n###LISTA ORDENADA###")
        for x in l:
            print(x)


def key_generator(word):
    key = 0
    for char in str(word[:2]):
        key += ord(char)
    return key

time_start = time.clock()

table = HashTable(10000)

ENTRADA = '1000.txt'

with open(ENTRADA, 'r') as entrada:
    word = entrada.readlines()

for x in word:
    table.insert(HashWord(key_generator(x), x))





#table.display_table()

table.lista_ordenada()
time_elapsed = (time.clock() - time_start)
print("Tempo para carregar: ", time_elapsed)
print("Memória usada: ",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
#table.search(key_generator("povo"))


'''time_elapsed = (time.clock() - time_start)
print("Tempo para carregar: ", time_elapsed)
print("Memória usada: ",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'''