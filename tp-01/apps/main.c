/* @source Minha Loja Virtual ****************************************************************
**
** Author: Bruno Fernandes Bessa de Oliveira, n.o USP 5881890
**
** Código do projeto pratico da disciplina MAI5001 ministrada por Fernando Osorio.
** A especificacao do programa pode ser encontrada em https://run.codes/exercises/view/14265
**
******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "LojaVirtual.h"

int entrada_dados(char comando, Lista* lista){
  int saida;
  int status;
  struct itemLista i;
  switch(comando){
    case 'I':
      // Insere ao final
      scanf("%d", &i.codigo);
      scanf("%s", i.descricao);
      scanf("%f", &i.preco);

      status = insere_item_final(lista, i);
      if (status == 0){
        printf("Erro\n");
      }
      else if (status == 2){
        printf("Duplicado\n");
        }
        else if (status == 1){
          printf("Ok\n");
        }
      break;

    case 'O':
      // Insere ordenado
      scanf("%d", &i.codigo);
      scanf("%s", i.descricao);
      scanf("%f", &i.preco);

      status = insere_item_ordenado(lista, i);
      if (status == 0){
        printf("Erro\n");
      }
      else if (status == 2){
        printf("Duplicado\n");
        }
        else if (status == 1){
          printf("Ok\n");
        }
      break;

    case 'C':
      // Consulta pelo codigo
      scanf("%d", &i.codigo);

      status = consulta_item(lista, i);
      if (status == 0){
        printf("Erro\n");
      }
      if (status == 1){
        printf("Ok\n");
      }
      break;

    case 'R':
      // Remove pelo codigo
      scanf("%d", &i.codigo);

      status = remove_item(lista, i);
      if (status == 0){
        printf("Erro\n");
      }
      if (status == 1){
        printf("Ok\n");
      }
      break;

    case 'L':
      // Exibir lista
      lista_itens(lista);
      break;

  } //end-switch
  return saida;
}

int main(){

  // Inicializando a lista, declaracao de comando de interface com usuario e sua primeira leitura antes do laco condicional
  Lista* lista = cria_lista();
  char comando;
  scanf("%c", &comando);

  while (comando!='F'){
    // Inicio do laco de captura de comandos do usuario (Encerra quando for inserido comando F)
    if (comando=='\n'){
      // sem acao
    }
    else if (!(comando=='I' || comando=='O' || comando=='C' || comando=='R' || comando=='L')){
      // Erro de entrada: comando de entrada e valido (I, O, C, R, L, F)
      printf("Erro\n");
    }
    else{
      entrada_dados(comando, lista);
    }
    // Obtento nova entrada
    scanf("%c", &comando);

  } //end-while

  // Termino do programa
  printf("Fim\n");
  return 0;
} //end-main

/*
cgg -Wall -c main.c -o main.o
gcc main.o LojaVirtual.c -o program
*/
