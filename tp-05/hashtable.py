__author__ = "Bruno F. Bessa"
__email__ = "bruno.fernandes.oliveira@usp.br"

class Funcionario:

    def __init__(self,nome,ano,salario):
        self.nome = nome
        self.ano = ano
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_ano(self):
        return self.ano

    def get_salario(self):
        return self.salario

class Nodo:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self):
        self.hashtable = []

    def hashmap(self,nodo):
        valor = 7
        tam = len(nodo.nome)
        for i in range(tam):
            valor = 31 * valor + ord(nodo.nome[i])
        return valor

    def insere_nodo(self,nodo):
        index = self.hashmap(nodo)
        try:
            nodo = self.hashmap[index]
        except:
            print(nodo)

def main():
    a = Nodo('bruno',1988,1000)
    H = HashTable()
    H.insere_nodo(a)
    print(H)

if __name__ == '__main__':
    main()
