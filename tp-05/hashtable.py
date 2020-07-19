__author__ = "Bruno F. Bessa"
__email__ = "bruno.fernandes.oliveira@usp.br"

from datetime import datetime

CAPACIDADE_HASHTABLE = 10000

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
        self.capacidade = CAPACIDADE_HASHTABLE
        self.tamanho = 0
        self.buckets = [None] *  self.capacidade

    def _hashmap(self,key):
        hashsum = 0
        for _ind, _char in enumerate(key):
            hashsum += (_ind + len(key)) ** ord(_char)
            hashsum = hashsum % self.capacidade
        return hashsum


    def insere(self, key, value):
        self.tamanho += 1
        index = self._hashmap(key)
        nodo = self.buckets[index]
        if nodo is None:
            self.buckets[index] = Nodo(key,value)
            return
        #colisao encontrada
        prev = nodo
        while nodo is not None:
            prev = nodo
            nodo = nodo.next
        prev.next = Nodo(key,value)

    def find(self,key):
        #print('buscando key = ', key)
        index = self._hashmap(key)
        nodo = self.buckets[index]
        while nodo is not None and nodo.key != key:
            print(nodo.key)
            nodo = nodo.next
        if nodo is None:
            #Nao encontrado
            return None
        else:
            return nodo.value

    def remove(self,key):
        index = self._hashmap(key)
        nodo = self.buckets[index]
        while nodo is not None and nodo.key != key:
            prev = nodo
            nodo = nodo.next
        if nodo is None:
            #Nao encontrado
            return None
        else:
            self.tamanho -= 1
            temp = nodo.value
            if prev is None:
                nodo = None
            else:
                prev.next = prev.next.next
                return temp

def ler_arquivo():
    arq = open('dados.txt', 'r')
    arquivo_bruto = arq.readlines()
    linhas_arquivo = []
    for _ in arquivo_bruto:
        _ = _.rstrip('\n')
        if _ != '#':
            linha = _.split(',')
            linhas_arquivo.append(linha)
    arq.close()
    return linhas_arquivo

def main():

    H = HashTable()

    linhas_arquivo = ler_arquivo()
    for linha in linhas_arquivo:
        key = linha[0] + '_' + linha[1]
        value = linha[2]
        H.insere(key, value)

    try:
        while True:
            entrada = input()
            if entrada == '0' or entrada == '0\r':
                break
            else:
                if entrada == '1' or entrada == '1\r':
                    nome_consulta = input()
                    nome_consulta = nome_consulta.replace(' ', '').replace('\r', '')
                    ano_consulta = input()
                    ano_consulta = ano_consulta.replace(' ', '').replace('\r', '')

                    key_consulta = nome_consulta + '_' + ano_consulta

                    # t1 = datetime.now()
                    valor_consulta = H.find(key_consulta)
                    # t2 = datetime.now()
                    # Quanot tempo leva para realizar a consulta?
                    # print(t1 - t2)

                    if valor_consulta is None:
                        print('Inexistente')
                    else:
                        valor_consulta = float(valor_consulta)
                        valor_consulta = '{:.2f}'.format(valor_consulta)
                        print(nome_consulta + ' ' + str(valor_consulta))

    except Exception as EOFError:
        print('Entrada: ', entrada)
        print('Erro: ', EOFError)

if __name__ == '__main__':
    main()
