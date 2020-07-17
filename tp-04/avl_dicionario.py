__author__ = "Bruno F. Bessa"
__email__ = "bruno.fernandes.oliveira@usp.br"

import os
class nodo:

    def __init__(self,info=None):
        self.info = info
        self.esq = None
        self.dir = None
        self.pai = None
        self.altura = 1

    def getInfo(self):
        return self.info

    def setInfo(self,info):
        self.info = info

    def getEsq(self):
        return self.esq

    def getDir(self):
        return self.dir

    def setEsq(self, esq):
        self.esq = esq

    def setDir(self, dir):
        self.dir = dir

class AVL:
    def __init__(self):
        self.raiz = None

    def __repr__(self):
        if self.raiz == None: return ''
        content = '\n' # to hold final string
        cur_nodes = [self.raiz] # all nodes at current level
        cur_altura = self.raiz.altura # altura of nodes at current level
        sep = ' '*(2**(cur_altura-1)) # variable sized separator between elements
        while True:
            cur_altura += -1 # decrement current altura
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None,None])
                    continue

                if n.info != None:
                    buf = ' '*int((5-len(str(n.info)))/2)
                    cur_row += '%s%s%s'%(buf,str(n.info),buf)+sep
                else:
                    cur_row += ' ' *5+sep

                if n.esq != None:
                    next_nodes.append(n.esq)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.dir != None:
                    next_nodes.append(n.dir)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_altura * '   ' + cur_row + '\n' + cur_altura * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' *int(len(sep)/2) # cut separator size in half
        return content


    def insere(self,info):
        if self.raiz == None:
            self.raiz = nodo(info)
        else:
            self._insere(info,self.raiz)

    def _insere(self,info,nodo_atual):
        if info < nodo_atual.info:
            if nodo_atual.esq == None:
                nodo_atual.esq = nodo(info)
                nodo_atual.esq.pai = nodo_atual # set pai
                self._inspect_insertion(nodo_atual.esq)
            else:
                self._insere(info,nodo_atual.esq)
        elif info>nodo_atual.info:
            if nodo_atual.dir == None:
                nodo_atual.dir = nodo(info)
                nodo_atual.dir.pai = nodo_atual # set pai
                self._inspect_insertion(nodo_atual.dir)
            else:
                self._insere(info,nodo_atual.dir)
        else:
            print('info already in tree!')

    def print_tree(self):
        if self.raiz != None:
            self._print_tree(self.raiz)

    def _print_tree(self,nodo_atual):
        if nodo_atual != None:
            self._print_tree(nodo_atual.esq)
            print('%s, h = %d'%(str(nodo_atual.info),nodo_atual.altura))
            self._print_tree(nodo_atual.dir)

    def altura(self):
        if self.raiz != None:
            return self._altura(self.raiz,0)
        else:
            return 0

    def _altura(self,nodo_atual,altura_atual):
        if nodo_atual == None: return altura_atual
        altura_esq = self._altura(nodo_atual.esq,altura_atual+1)
        altura_dir = self._altura(nodo_atual.dir,altura_atual+1)
        return max(altura_esq,altura_dir)

    def busca(self,info,opcao=None):
        nodos_visitados = 1
        if self.raiz != None:
            return self._busca(info,self.raiz,nodos_visitados,opcao)
        else:
            return None

    def _busca(self,info,nodo_atual,nodos_visitados,opcao):
        if info == nodo_atual.info[0]:
            if opcao == 'visita':
                return [nodo_atual.info, nodos_visitados]
            else:
                return nodo_atual
        elif info < nodo_atual.info[0] and nodo_atual.esq != None:
            return self._busca(info,nodo_atual.esq,nodos_visitados+1,opcao)
        elif info > nodo_atual.info[0] and nodo_atual.dir != None:
            return self._busca(info,nodo_atual.dir,nodos_visitados+1,opcao)
        elif info != nodo_atual.info[0] and opcao == 'visita':
            return ['<x>', nodos_visitados]

    def busca_ampla(self,info,opcao=None):
        nodos_visitados = 1
        if self.raiz != None:
            nodos_arvore = self._busca_ampla(self.raiz)
            if info not in nodos_arvore:
                return ['<x>', len(nodos_arvore)]
            else:
                return [info, nodos_arvore.index(info)+1]

    def _busca_ampla(self,nodo_atual):
        nodos_arvore = []
        if nodo_atual:
            nodos_arvore.append(nodo_atual.info[1])
            nodos_arvore = nodos_arvore + self._busca_ampla(nodo_atual.esq)
            nodos_arvore = nodos_arvore + self._busca_ampla(nodo_atual.dir)
        return nodos_arvore

    def deleta_info(self,info):
        return self.deleta_nodo(self.busca(info))

    def deleta_nodo(self,nodo):

        # Protect against deleting a nodo not found in the tree
        if nodo == None or self.busca(nodo.info) == None:
            print('<x>')
            return None

        # returns the nodo with min info in tree raized at input nodo
        def min_info_nodo(n):
            atual = n
            while atual.esq != None:
                atual = atual.esq
            return atual

        # returns the number of filhoren for the specified nodo
        def num_filhos(n):
            num_filhos = 0
            if n.esq != None: num_filhos += 1
            if n.dir != None: num_filhos += 1
            return num_filhos

        # get the pai of the nodo to be deleted
        nodo_pai = nodo.pai

        # get the number of filhoren of the nodo to be deleted
        nodo_filho = num_filhos(nodo)

        # break operation into different cases based on the
        # structure of the tree & nodo to be deleted

        # CASE 1 (nodo has no filhoren)
        if nodo_filho == 0:

            if nodo_pai != None:
                # remove reference to the nodo from the pai
                if nodo_pai.esq == nodo:
                    nodo_pai.esq = None
                else:
                    nodo_pai.dir = None
            else:
                self.raiz = None

        # CASE 2 (nodo has a single filho)
        if nodo_filho == 1:

            # get the single filho nodo
            if nodo.esq != None:
                filho = nodo.esq
            else:
                filho = nodo.dir

            if nodo_pai != None:
                # replace the nodo to be deleted with its filho
                if nodo_pai.esq == nodo:
                    nodo_pai.esq = filho
                else:
                    nodo_pai.dir = filho
            else:
                self.raiz = filho

            # correct the pai pointer in nodo
            filho.pai = nodo_pai

        # CASE 3 (nodo has two filhoren)
        if nodo_filho == 2:

            # get the inorder successor of the deleted nodo
            successor = min_info_nodo(nodo.dir)

            # copy the inorder successor's info to the nodo formerly
            # holding the info we wished to delete
            nodo.info = successor.info

            # delete the inorder successor now that it's info was
            # copied into the other nodo
            self.deleta_nodo(successor)

            # exit function so we don't call the _inspect_deletion twice
            return

        if nodo_pai != None:
            # fix the altura of the pai of current nodo
            nodo_pai.altura = 1+max(self.get_altura(nodo_pai.esq),self.get_altura(nodo_pai.dir))

            # begin to traverse back up the tree checking if there are
            # any sections which now invalidate the AVL balance rules
            self._inspect_deletion(nodo_pai)

    def search(self,info):
        if self.raiz != None:
            return self._search(info,self.raiz)
        else:
            return False

    def _search(self,info,nodo_atual):
        if info == nodo_atual.info:
            return True
        elif info<nodo_atual.info and nodo_atual.esq != None:
            return self._search(info,nodo_atual.esq)
        elif info>nodo_atual.info and nodo_atual.dir != None:
            return self._search(info,nodo_atual.dir)
        return False


    # Functions added for AVL...

    def _inspect_insertion(self,nodo_atual,path = []):
        if nodo_atual.pai == None: return
        path = [nodo_atual]+path

        left_altura  = self.get_altura(nodo_atual.pai.esq)
        right_altura = self.get_altura(nodo_atual.pai.dir)

        if abs(left_altura-right_altura)>1:
            path = [nodo_atual.pai]+path
            self._rebalance_nodo(path[0],path[1],path[2])
            return

        new_altura = 1+nodo_atual.altura
        if new_altura>nodo_atual.pai.altura:
            nodo_atual.pai.altura = new_altura

        self._inspect_insertion(nodo_atual.pai,path)

    def _inspect_deletion(self,nodo_atual):
        if nodo_atual == None: return

        left_altura  = self.get_altura(nodo_atual.esq)
        right_altura = self.get_altura(nodo_atual.dir)

        if abs(left_altura-right_altura)>1:
            y = self.taller_filho(nodo_atual)
            x = self.taller_filho(y)
            self._rebalance_nodo(nodo_atual,y,x)

        self._inspect_deletion(nodo_atual.pai)

    def _rebalance_nodo(self,z,y,x):
        if y == z.esq and x == y.esq:
            self._right_rotate(z)
        elif y == z.esq and x == y.dir:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.dir and x == y.dir:
            self._left_rotate(z)
        elif y == z.dir and x == y.esq:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_nodo: z,y,x nodo configuration not recognized!')

    def _right_rotate(self,z):
        sub_raiz = z.pai
        y = z.esq
        t3 = y.dir
        y.dir = z
        z.pai = y
        z.esq = t3
        if t3 != None: t3.pai = z
        y.pai = sub_raiz
        if y.pai == None:
                self.raiz = y
        else:
            if y.pai.esq == z:
                y.pai.esq = y
            else:
                y.pai.dir = y
        z.altura = 1+max(self.get_altura(z.esq),
            self.get_altura(z.dir))
        y.altura = 1+max(self.get_altura(y.esq),
            self.get_altura(y.dir))

    def _left_rotate(self,z):
        sub_raiz = z.pai
        y = z.dir
        t2 = y.esq
        y.esq = z
        z.pai = y
        z.dir = t2
        if t2 != None: t2.pai = z
        y.pai = sub_raiz
        if y.pai == None:
            self.raiz = y
        else:
            if y.pai.esq == z:
                y.pai.esq = y
            else:
                y.pai.dir = y
        z.altura = 1 + max(self.get_altura(z.esq),
            self.get_altura(z.dir))
        y.altura = 1 + max(self.get_altura(y.esq),
            self.get_altura(y.dir))

    def get_altura(self,nodo_atual):
        if nodo_atual == None: return 0
        return nodo_atual.altura

    def taller_filho(self,nodo_atual):
        left = self.get_altura(nodo_atual.esq)
        right = self.get_altura(nodo_atual.dir)
        return nodo_atual.esq if left >= right else nodo_atual.dir


###############################
###############################

def insere_dados_entrada():
    try:
        arq  =  open('dados.txt', 'r')
        arquivo_bruto  =  arq.readlines()
        linhas_arquivo  =  []
        for _ in arquivo_bruto:
            _  =  _.rstrip('\n')
            if _  !=  '$,$':
                linha  =  _.split(',')
                linhas_arquivo.append(linha)
        arq.close()

        Us2Pt = AVL()
        Pt2Us = AVL()
        for p in linhas_arquivo:
            Us2Pt.insere(p[::])
            Pt2Us.insere(p[::-1])

        return Us2Pt, Pt2Us
    except FileError:
        print('Houve erro no processamento do arquivo.\n', FileError)


Us2Pt, Pt2Us = insere_dados_entrada()

try:
    while True:
        entrada = input()
        if entrada == '0' or entrada == '0\r':
            break
        else:
            entrada = entrada.split(' ')
            modo_consulta = entrada[0]
            valor_consulta = entrada[1].replace(' ', '').replace('\r', '')

            if modo_consulta == '1':
                resposta1 = Us2Pt.busca(valor_consulta, opcao='visita')
                resposta2 = Pt2Us.busca_ampla(valor_consulta, opcao='visita')
                if resposta1[0] == '<x>':
                    resp_str = str(resposta1[0]) + ' ' + str(resposta1[-1]) + ' ' + str(resposta2[-1])
                else:
                    resp_str = str(resposta1[0][0]) + ' ' + str(resposta1[0][1]) + ' ' + str(resposta1[-1]) + ' ' + str(resposta2[-1])
                print(resp_str)
            elif modo_consulta == '2':
                resposta1 = Pt2Us.busca(valor_consulta, opcao='visita')
                resposta2 = Us2Pt.busca_ampla(valor_consulta, opcao='visita')
                if resposta1[0] == '<x>':
                    resp_str = str(resposta1[0]) + ' ' + str(resposta2[-1]) + ' ' + str(resposta1[-1])
                else:
                    resp_str = str(resposta1[0][0]) + ' ' + str(resposta1[0][1]) + ' ' + str(resposta2[-1]) + ' ' + str(resposta1[-1])
                print(resp_str)

except Exception as EOFError:
    print('Entrada: ', entrada)
    print('Erro: ', EOFError)
    pass
