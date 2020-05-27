#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "DEQ.h"
#define less(A, B) (A <= B)

struct elemento{
  struct elemento *anterior;
  struct elemento *proximo;
  struct itemLista *dado;
};

typedef struct elemento Elem;

Lista* cria_lista(){
  Lista *lista;
  lista = (Lista*) malloc(sizeof(Lista));
  if (lista != NULL){
    *lista = NULL;
  }
  return lista;
}

void libera_lista(Lista* lista){
  if (lista != NULL){
    Elem* nodo;
    while ((*lista) != NULL){
      nodo = *lista;
      *lista = (*lista)->proximo;
      free(nodo);
    }
    free(lista);
  }
}

int lista_cheia(Lista* lista){
  return 0;
}

int lista_vazia(Lista* lista){
  if (lista == NULL){
    return 1;
  }
  if (*lista == NULL){
    return 1;
  }
  return 0;
}

int insere_item_inicio(Lista* lista, struct itemLista *item){
  if (lista == NULL){
    return 0;
  }
  Elem* nodo;
  nodo = (Elem*) malloc(sizeof(Elem));
  if (nodo == NULL){
    return 0;
  }
  nodo->dado = item;
  nodo->anterior = NULL;
  nodo->proximo = (*lista);
  if (*lista != NULL){
    (*lista)->anterior = nodo;
  }
  *lista = nodo;
  return 1;
}

int insere_item_final(Lista* lista, struct itemLista *item){
  if (lista == NULL){
    return 0;
  }
  Elem *nodo;
  nodo = (Elem*) malloc(sizeof(Elem));
  if (nodo == NULL){
    return 0;
  }
  nodo->dado = item;
  nodo->proximo = NULL;
  if (*lista == NULL){
    nodo->anterior = NULL;
    *lista = nodo;
  } else {
    Elem *temp = *lista;
    while(temp->proximo != NULL){
      temp = temp->proximo;
    }
    temp->proximo = nodo;
    nodo->anterior = temp;
  }
  return 1;
}

int insere_item_ordenado(Lista* lista, struct itemLista *item){

  if (lista == NULL){
    return 0;
  }
  Elem *nodo;
  nodo = (Elem*) malloc(sizeof(Elem));
  if (nodo == NULL){
    return 0;
  }
  nodo->dado = item;

  // Lista vazia
  if ((*lista) == NULL){
    nodo->anterior = NULL;
    nodo->proximo = NULL;
    *lista = nodo;
    return 1;
  }
  else{
    Elem *anterior, *atual = *lista;
    while (atual != NULL && atual->dado->codigo < nodo->dado->codigo){
      anterior = atual;
      atual = atual->proximo;
    }
    if (atual == *lista){
      // insercao no inicio
      nodo->anterior = NULL;
      (*lista)->anterior = nodo;
      nodo->proximo = (*lista);
      *lista = nodo;
    }
    else{
      nodo->proximo = anterior->proximo;
      nodo->anterior = anterior;
      anterior->proximo = nodo;
      if (atual != NULL){
        atual->anterior = nodo;
      }
    }
    return 1;
  }
}

int remove_item(Lista* lista, int codigo_item){
  if (lista == NULL){
    return 0;
  }
  if ((*lista) == NULL)
    //lista vazia
    return 0;

  Elem *nodo = *lista;
  while (nodo != NULL && nodo->dado->codigo != codigo_item){
    nodo = nodo->proximo;
  }
  if (nodo == NULL)
    //nao encontrado
    return 0;

  if (nodo->anterior == NULL)
    //remover primeiro
    *lista = nodo->proximo;
  else
      nodo->anterior->proximo = nodo->proximo;

  if (nodo->proximo != NULL)
      //não e o último
      nodo->proximo->anterior = nodo->anterior;

  free(nodo);
  return 1;
}

void imprime_lista(Lista* lista){
  if (lista == NULL){
    return;
  }
  Elem* nodo = *lista;
  while (nodo != NULL){
    printf("%g", nodo->dado->codigo);
    if (nodo->proximo != NULL){
      printf(",");
    }
    nodo = nodo->proximo;
  }
  printf("\n");
}


// Abaixo algoritmo de ordenacao merge sort
//https://www.techiedelight.com/merge-sort-singly-linked-list/
//https://www.geeksforgeeks.org/merge-sort-for-doubly-linked-list/


Lista* merge_ordenadas2(Lista* lista1, Lista* lista2){
  Elem *comeco;
  comeco = (Elem*) malloc(sizeof(Elem));


  //printf("Cod l1 %g\n", (*lista1)->proximo);

  Lista* dummy = &comeco;

  while (lista1 != NULL && lista2 != NULL){
    // c é o último nó da lista cuja cabeça é head
    printf("Comparando %g (1) e %g (2)\n", (*lista1)->dado->codigo, (*lista2)->dado->codigo);
    //if (less((*lista1)->dado->codigo, (*lista2)->dado->codigo)) {
    if ((*lista1)->dado->codigo <= (*lista2)->dado->codigo){
      //(*dummy)->proximo = lista1;
      //dummy = lista1;
      //printf("Cod l1 %g\n", (*dummy)->dado->codigo);
      printf("Cod l1 %g\n", (*lista1)->dado->codigo);
      lista1 = (*lista1)->proximo;
      if (lista1 == NULL){
        printf("NUlo");
      }
      //
    }class Deque:

	def __init__(self):
		self.deque = []
		self.len = 0

	def empty(self):
		if self.len == 0:
			return True
		return False

	def push_front(self, e):
		self.deque.insert(0, e)
		self.len += 1

	def push_back(self, e):
		self.deque.insert(self.len, e)
		self.len += 1

	def pop_front(self):
		if not self.empty():
			self.deque.pop(0)
			self.len -= 1

	def pop_back(self):
		if not self.empty():
			self.deque.pop(self.len - 1)
			self.len -= 1

	def front(self):
		if not self.empty():
			return self.deque[0]

	def back(self):
		if not self.empty():
			return self.deque[-1]

	def show(self):
		for i in self.deque:
			print(i, end=' ')


    else {
     (*dummy)->proximo = lista2;
     dummy = lista2;
     lista2 = (*lista2)->proximo;
    }
    (*dummy)->proximo = (lista1 == NULL) ? lista2 : lista1;
  }
  imprime_lista(comeco);
  return comeco->proximo;
  printf("%g", (*lista1)->dado->codigo);


}

Lista* merge_ordenadas(Lista* lista1, Lista* lista2){
  printf("merge_ordenadas\n");
  imprime_lista(lista1);
  imprime_lista(lista2);
  if (*lista1 == NULL){
    return lista2;
  }
  else if (*lista2 == NULL){
    return lista1;
  }

  Elem *resultado;
  resultado = (Elem*) malloc(sizeof(Elem));

  Lista *aux;

  if ((*lista1)->dado->codigo <= (*lista2)->dado->codigo){
    //printf("Comparando %g (1) e %g (2)\n", (*lista1)->dado->codigo, (*lista2)->dado->codigo);
    resultado = *lista1;
    resultado->anterior = NULL;
    aux = (*lista1)->proximo;
    if ((*lista1)->proximo != NULL){
        resultado->proximo = merge_ordenadas(&aux, lista2);
      }
      else{
        resultado->proximo = *lista2;
      }
  }
  else{
    resultado = *lista2;
    resultado->anterior = NULL;
    if ((*lista2)->proximo != NULL){
      aux = (*lista2)->proximo;
      if ((*lista2)->proximo != NULL){
        resultado->proximo = merge_ordenadas(lista1, &aux);
      }
      else {
        //printf("Proximo de lista2 sera NULL: \n");
        //imprime_lista(lista2);
        resultado->proximo = lista1;
      }
      //printf("Resultado: ");
      //imprime_lista(resultado);
    }
  }
  return resultado;
}
