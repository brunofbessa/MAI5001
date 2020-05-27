#include <stdio.h>
#define MAX 100
struct itemLista{
  double codigo;
};
typedef struct elemento* Lista;

Lista* cria_lista();
void libera_lista(Lista* lista);
int insere_item_inicio(Lista* lista, struct itemLista *item);
int insere_item_final(Lista* lista, struct itemLista *item);
int insere_item_ordenado(Lista* lista, struct itemLista *item);
int remove_item(Lista* lista, int codigo_item);
int consulta_item(Lista* lista, struct itemLista item, struct itemLista *itembusca);
void lista_itens(Lista* lista);
void imprime_lista(Lista* lista);
Lista* merge_ordenadas(Lista* lista1, Lista* lista2);
Lista* merge_ordenadas2(Lista* lista1, Lista* lista2);
//Lista* merge_ordenadas_2(Lista *lista1, Lista *lista2, Lista *aux);
