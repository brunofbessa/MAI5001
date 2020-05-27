class Nodo:

	def __init__(self, valor):
		self.valor = valor
		self.proximo = None

	def getValor(self):
		return self.valor

	def setValor(self, valor):
		self.label = label

	def getProximo(self):
		return self.proximo

	def setProximo(self, proximo):
		self.proximo = proximo


class ListaEncadeada:

	def __init__(self):
		self.cabeca = None
		self.calda = None
		self.tamanho = 0

	def length(self):
		return self.tamanho

	def empty(self):
		if self.cabeca == None:
			return True
		return False

	def func(self):
		pass

	def push(self, valor, index):

		if index >= 0:

			# cria o novo nó
			nodo = Nodo(valor)

			# verifica se a lista está vazia
			if self.empty():
				self.cabeca = nodo
				self.calda = nodo
			else:

				if index == 0:
					# inserção no início
					nodo.setProximo(self.cabeca)
					self.cabeca = nodo
				elif index >= self.tamanho:
					# inserção ao final
					self.calda.setProximo(nodo)
					self.calda = nodo
				else:
					# inserção no meio
					nodo_anterior = self.cabeca
					nodo_atual = self.cabeca.getProximo()
					nodo_atual_index = 1

					while nodo_atual != None:

						if nodo_atual_index == index:
							# seta o nodo_atual como o próximo do nó
							nodo.setProximo(nodo_atual)
							# seta o nodo como o próximo do prev_nodos
							nodo_anterior.setProximo(nodo)

						nodo_anterior = nodo_atual
						nodo_atual = nodo_atual.getProximo()
						nodo_atual_index += 1

			# atualiza o tamanho da lista
			self.tamanho += 1

	def pop(self, index):

		if not self.empty() and index >= 0 and index < self.tamanho:

			flag_remove = False

			if self.cabeca.getProximo() == None:
				# possui apenas 1 elemento
				self.cabeca = None
				self.calda = None
				flag_remove = True
			elif index == 0:
				# remove do início, mas possui mais de 1 elemento
				self.cabeca = self.cabeca.getProximo()
				flag_remove = True
			else:
				'''
					Lista possui mais de 1 elemento e a remoção não é no início
				'''

				nodo_anterior = self.cabeca
				nodo_atual = self.cabeca.getProximo()
				nodo_atual_index = 1

				while nodo_atual != None:

					if index == nodo_atual_index:
						# o próximo do anterior aponta para o próximo do nó corrente
						nodo_anterior.setProximo(nodo_atual.getProximo())
						nodo_atual.setProximo(None)
						flag_remove = True
						break

					nodo_anterior = nodo_atual
					nodo_atual = nodo_atual.getProximo()
					nodo_atual_index += 1

			if flag_remove:
				# atualiza o tamanho da lista
				self.tamanho -= 1


#	def insert_ordenado(self, valor):
#		nodo = Nodo(valor)
#		nodo_atual = self.cabeca
#        while (nodo_atual != None):
#            pass
#			if nodo.valor <= nodo_atual.getValor():
#                nodo_atual.getProximo()
#				pass

	def imprime_lista(self):
		nodo_atual = self.cabeca
		lista_valores = []
		while (nodo_atual != None):
			valor = str(nodo_atual.getValor())
			lista_valores.append(valor)
			nodo_atual = nodo_atual.getProximo()
		saida = ','.join(lista_valores)
		print(saida)
