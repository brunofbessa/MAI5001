__author__ = "Bruno F. Bessa"
__email__ = "bruno.fernandes.oliveir@usp.br"

class Nodo:

    def __init__(self, info):
        self.info = info
        self.esq = None
        self.dir = None

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def getEsq(self):
        return self.esq

    def getDir(self):
        return self.dir

    def setEsq(self, esq):
        self.esq = esq

    def setDir(self, dir):
        self.dir = dir

class ArvoreBinaria:

    def __init__(self):
        self.root = None

    def empty(self):
        if self.root == None:
            return True
        return False

    def getRoot(self):
        return self.root

    def insere_bst(self, info):
        nodo = Nodo(info)

        if self.empty():
            self.root = nodo
        else:
            nodo_anterior = None
            nodo_atual = self.root
            while True:
                if nodo_atual != None:
                    nodo_anteiror = nodo_atual
                    # tetativa recursiva a esquerda e direira
                    if nodo.getInfo() < nodo_atual.getInfo():
                        nodo_atual = nodo_atual.getEsq()
                    else:
                        nodo_atual = nodo_atual.getDir()
                else:
                    #encontrou o nodo a inserir
                    if nodo.getInfo() < nodo_anteiror.getInfo():
                        nodo_anteiror.setEsq(nodo)
                    else:
                        nodo_anteiror.setDir(nodo)
                    break

    def insere(self, linha):

        nodo = Nodo(linha[0])
        _ = Nodo(linha[1])
        nodo.setEsq(_)
        _ = Nodo(linha[2])
        nodo.setDir(_)

        if self.empty():
            self.root = nodo
            self.setEsq = linha[1]
            self.setEsq = linha[2]
        else:
            self._insere(linha, self.root)

    def _insere(self, linha, nodo_atual):
        nodo = Nodo(linha[0])
        _ = Nodo(linha[1])
        nodo.setEsq(_)
        _ = Nodo(linha[2])
        nodo.setDir(_)

        #print('Comparando ', nodo.getInfo(), 'com ', nodo_atual.getInfo())
        if nodo.getInfo() != nodo_atual.getInfo():
            if nodo_atual.getEsq():
                self._insere(linha, nodo_atual.getEsq())
            if nodo_atual.getDir():
                self._insere(linha, nodo_atual.getDir())
        else:
            # Nodo a ser inserido é o nodo nodo_atual
            nodo_atual.setEsq(nodo.getEsq())
            nodo_atual.setDir(nodo.getDir())
            return

    def imprime_preordem(self, nodo_atual):
        if nodo_atual != None:
            if nodo_atual.getInfo() != 'X':
                if nodo_atual.getInfo == 'X':
                    print('e folha')
                #print(nodo_atual.getInfo())
                info_nodo = nodo_atual.getInfo()
                filhos = 0
                filho_esq = False
                filho_dir = False
                tipo_nodo = ''

                if nodo_atual.getEsq():
                    if nodo_atual.getEsq().getInfo() != 'X':
                        filhos += 1
                        filho_esq = True
                if nodo_atual.getDir():
                    if nodo_atual.getDir().getInfo() != 'X':
                        filhos += 1
                        filho_dir = True

                if filho_esq and filho_dir:
                    tipo_nodo = 'ED'
                elif filho_esq and not filho_dir:
                    tipo_nodo = 'E'
                elif not filho_esq and filho_dir:
                    tipo_nodo = 'D'
                else:
                    tipo_nodo = 'F'

                itens_saida = [info_nodo, str(filhos), tipo_nodo]
                saida = ' '.join(itens_saida)
                print(saida)

                self.imprime_preordem(nodo_atual.getEsq())
                self.imprime_preordem(nodo_atual.getDir())

    def total_niveis(self, nodo_atual):
        if self.root == None:
            return 0
        else:
            niveis_esq = 0
            niveis_dir = 0

            if nodo_atual.getEsq():
                if nodo_atual.getEsq().getInfo() != 'X':
                    niveis_esq = self.total_niveis(nodo_atual.getEsq())
            if nodo_atual.getDir():
                if nodo_atual.getDir().getInfo() != 'X':
                    niveis_esq = self.total_niveis(nodo_atual.getDir())

            if niveis_esq > niveis_dir:
                return niveis_esq + 1
            else:
                return niveis_dir + 1

    def total_saidas(self, nodo_atual):
        if self.root == None:
            return 0
        else:
            num_saidas = 0
            num_saidas_esq = 0
            num_saidas_dir = 0

            if nodo_atual.getInfo()[0] == 'S':
                num_saidas += 1
            if nodo_atual.getEsq():
                if nodo_atual.getEsq().getInfo() != 'X':
                    num_saidas_esq = self.total_saidas(nodo_atual.getEsq())
            if nodo_atual.getDir():
                if nodo_atual.getDir().getInfo() != 'X':
                    num_saidas_dir = self.total_saidas(nodo_atual.getDir())

            return num_saidas + num_saidas_esq + num_saidas_dir

    def total_nodos(self, nodo_atual):
        if self.root == None:
            return 0
        else:
            num_nodos_esq = 0
            num_nodos_dir = 0

            if nodo_atual.getInfo() != 'X':
                num_nodos = 1

            if nodo_atual.getEsq():
                if nodo_atual.getEsq().getInfo() != 'X':
                    num_nodos_esq = self.total_nodos(nodo_atual.getEsq())
            if nodo_atual.getDir():
                if nodo_atual.getDir().getInfo() != 'X':
                    num_nodos_dir = self.total_nodos(nodo_atual.getDir())

            return num_nodos + num_nodos_esq + num_nodos_dir


    def imprime_preordem_simples(self, nodo_atual):
        if nodo_atual != None:
            print(nodo_atual.getInfo())
            self.imprime_preordem(nodo_atual.getEsq())
            self.imprime_preordem(nodo_atual.getDir())


#################

arq = open('dados.txt', 'r')
arquivo_bruto = arq.readlines()
linhas_arquivo = []
for _ in arquivo_bruto:
    _ = _.rstrip('\n')
    if _ != 'X,X,X':
        linha = _.split(',')
        linhas_arquivo.append(linha)
arq.close()

t = ArvoreBinaria()
for linha in linhas_arquivo:
    t.insere(linha)

t.imprime_preordem(t.getRoot())
print('TNv', t.total_niveis(t.getRoot()))
print('TSd', t.total_saidas(t.getRoot()))
print('TNd', t.total_nodos(t.getRoot()))
