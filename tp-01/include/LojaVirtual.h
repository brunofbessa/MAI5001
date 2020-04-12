/*
Descrição dos Dados dos Produtos junto ao Cadastro:
Código = Valor Inteiro (valor positivo de 0 a 9999) - Max 10.000 produtos
Descrição = String (max. 40 caracteres)
Preço = Valor em Ponto Flutuante (double ou float) - Considerar valores com 2 casas após a virgula.

Comandos:
I = Insere no Final
O = Insere Ordenado (ordena pelo código do produto)
C = Consulta (pelo código do produto)
R = Remove (pelo código do produto)
L = Lista Produtos (todos)
F = Fim

*/
#include <stdio.h>

struct itemLista{
  int codigo;
  char descricao[40];
  float preco;
};
typedef struct lista Lista;

Lista* cria_lista();
void libera_lista(Lista* lista);
int insere_item_final(Lista* lista, struct itemLista item);
int insere_item_ordenado(Lista* lista, struct itemLista item);
int remove_item(Lista* lista, int codigo);
//int consuta_item(Lista* lista, int codigo, struct itemLista *item);
void lista_itens(Lista* lista);
