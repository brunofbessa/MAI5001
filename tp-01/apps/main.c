#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "LojaVirtual.h"

int main(){

  Lista* lista = cria_lista();
  char comando;

  int saida = 0;

  while (saida==0){

    scanf("%c", &comando);

    switch(comando){
      case 'I':
        printf("Insere ao final\n");
        struct itemLista i;
        printf("Entre com o codigo do produto\n");
        scanf("%d", &i.codigo);
        printf("Entre com a descricao do produto\n");
        scanf("%s", i.descricao);
        printf("Entre com o preco do produto\n");
        scanf("%f", &i.preco);

        int status;
        status = insere_item_final(lista, i);
        if (status == 0){
          printf("Erro\n");
        }
        if (status == -1){
          printf("Duplicado");
        }
        if (status == 1){
          printf("Ok\n");
        }
        break;

/*      case 'O':
        printf("Insere ordenado\n");
        struct itemLista i;
        printf("Entre com o codigo do produto\n");
        scanf("%d", &i.codigo);
        printf("Entre com a descricao do produto\n");
        scanf("%s", i.descricao);
        printf("Entre com o preco do produto\n");
        scanf("%f", &i.preco);

        int status;
        status = insere_item_ordenado(lista, i);
        if (status == 0){
          printf("Erro\n");
        }
        if (status == -1){
          printf("Duplicado\n");
        }
        if (status == 1){
          printf("Ok\n");
        }
        break;

      case 'C':
        printf("Consulta pelo codigo\n");
        struct itemLista i;
        printf("Entre com o codigo do produto\n");
        scanf("%d", &i.codigo);

        int status;
        status = insere_item_final(lista, i);
        if (status == 0){
          printf("Erro\n");
        }
        if (status == -1){
          printf("Duplicado\n");
        }
        if (status == 1){
          printf("Ok\n");
        }
        break;
*/
      case 'R':
        printf("Remove pelo codigo\n");
        int codigo;
        printf("Entre com o codigo do produto\n");
        scanf("%d", &codigo);

        int status;
        status = remove_item(lista, codigo);
        if (status == 0){
          printf("Erro\n");
        }
        if (status == -1){
          printf("Duplicado\n");
        }
        if (status == 1){
          printf("Ok\n");
        }
        break;

      case 'L':
        lista_itens(lista);

      case 'F':
        printf("Fim\n");
        saida = 1;
        break;

      default:
        printf("Erro\n");

    } //end-switch
  } //end-while
  return 0;
} //end-main

/*
cgg -Wall -c main.c -o main.o
gcc main.o LojaVirtual.c -o program
*/
