#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "LojaVirtual.h"

struct lista{
  int quantidade;
  struct itemLista dados[];
};

Lista* cria_lista(){
  Lista *lista;
  lista = (Lista*) malloc(sizeof(struct lista));
  if (lista != NULL){
    lista->quantidade = 0;
  }
  return lista;
};

void libera_lista(Lista* lista){
  free(lista);
}

int tamanho_lista(Lista* lista){
  if (lista == NULL){
    return 0;
  }
  else{
    return lista->quantidade;
  }
}

int lista_vazia(Lista* lista){
  if (lista == NULL){
    return -1;
  }
  else{
    return (lista->quantidade == 0);
  }
}

int contem_item(Lista* lista, int codigo){
  if (lista == NULL){
    return 0;
  }
  if (lista->quantidade == 0){
    return 0;
  }

  int i = 0;
  while(i<lista->quantidade && lista->dados[i].codigo != codigo)
    i++;
  if (i==lista->quantidade){
    //elemento nao encontrado
    return 0;
  }
  // elemento encontrado na posicao 1:
  return 1;
}

int insere_item_final(Lista* lista, struct itemLista item){
  if (lista == NULL){
    return 0;
  }
  if (item.codigo<0 || item.codigo>9999){
    return 0;
  }
  if (strlen(item.descricao)>40){
    return 0;
  }
  if (contem_item(lista, item.codigo)==1){
    return 0;
  }
  lista->dados[lista->quantidade] = item;
  lista->quantidade++;
  return 1;
}

int insere_item_ordenado(Lista* lista, struct itemLista item){
  if (lista == NULL){
    return 0;
  }
  if (item.codigo<0 || item.codigo>9999){
    return 0;
  }
  if (strlen(item.descricao)>40){
    return 0;
  }
  if (contem_item(lista, item.codigo)==1){
    return 0;
  }

  int k, i = 0;
  while (i<lista->quantidade && lista->dados[i].codigo < item.codigo)
    i++;

  for (k=lista->quantidade-1; k>=i; k--)
      lista->dados[k+1] = lista->dados[k];

  lista->dados[i] = item;
  lista->quantidade++;
  return 1;
}

int remove_item(Lista* lista, int codigo){
  if (lista == NULL){
    return -1;
  }
  if (lista->quantidade == 0){
    return -1;
  }

  int k, i = 0;
  while(i<lista->quantidade && lista->dados[i].codigo != codigo)
    i++;
  if (i==lista->quantidade){
    //elemento nao encontrado
    return 0;
  }

  for (k=i; k<lista->quantidade-1; k++)
    lista->dados[k] = lista->dados[k+1];

  lista->quantidade--;
  return 1;
}


int consuta_item(Lista* lista, int codigo, struct itemLista *item){
  if (lista == NULL){
    return 0;
  }
  if (lista->quantidade == 0){
    return 0;
  }

  int i = 0;
  while(i<lista->quantidade && lista->dados[i].codigo != codigo)
    i++;
  if (i==lista->quantidade){
    //elemento nao encontrado
    return 0;
  }

  // elemento encontrado na posicao 1:
  *item = lista->dados[i];
  return 1;
}

void lista_itens(Lista* lista){
  if (lista == NULL){
    return;
  }
  int i;
  for (i=0; i<lista->quantidade; i++){
    printf("%d-%s-%f\n", lista->dados[i].codigo, lista->dados[i].descricao, lista->dados[i].preco);
    //printf("%s", lista->dados[i].descricao);
  }
}
