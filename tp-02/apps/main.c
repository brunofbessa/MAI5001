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
#include "DEQ.h"

void entrada_dados(double valores_entrada[], int *tam){
  int i;
  char tmp;
  double val[10];
  char texto[1024];
  //char texto[] = "10,5,12,6,X";
  const char FIM_LINHA = 'X';
  const char DELIM = ',';
  int count_delim = 0;
  int j = 0;

  //printf("entrada de valores separado por virgula.\n");
  fgets(texto,1000,stdin);

  while(texto[j] != '\0'){
    if (texto[j] == ','){
      count_delim++;
    }
    j++;
  }
  char* subtexto = strtok(texto, ",");
  for (i=0; i<count_delim;i++){

    sscanf(subtexto, "%lg%*[^,]", &valores_entrada[i]);
    //printf("%d: %g\n", i, valores_entrada[i]);
    subtexto = strtok(NULL, ",");
  }
  *tam = count_delim;
}

int main(){
/*
  struct itemLista teste1[4] = {4, 2, 1, 3};
  Lista* lista1 = cria_lista();
  for (int i=0; i<4; i++){
    insere_item_ordenado(lista1, &teste1[i]);
  }
  //imprime_lista(lista1);
  struct itemLista teste2[4] = {12, 11, 10, 9};
  Lista* lista2 = cria_lista();
  for (int i=0; i<4; i++){
    insere_item_ordenado(lista2, &teste2[i]);
  }
  //imprime_lista(lista2);
  Lista* lista_merge = cria_lista();
  *lista_merge = merge_ordenadas(lista1, lista2);
  printf("De volta para main()\n");
  imprime_lista(lista_merge);

  struct itemLista teste3[4] = {21, 22, 23};
  Lista* lista3 = cria_lista();
  for (int i=0; i<3; i++){
    insere_item_ordenado(lista3, &teste3[i]);
  }
  *lista_merge = merge_ordenadas(lista_merge, lista3);
  imprime_lista(lista_merge);
*/


  int tipo_arquivo;
  int quant_listas;
  scanf("%d\n", &tipo_arquivo);
  //printf("tipo_arquivo: %d\n", tipo_arquivo);
  scanf("%d\n", &quant_listas);
  //printf("quant_listas: %d\n", quant_listas);

  Lista* listas_entrada[quant_listas];
  int tam;
  double valores_entrada[quant_listas][10];
  struct itemLista lista_dummy[quant_listas][100];

  for (int ql=0; ql<quant_listas; ql++){
    entrada_dados(valores_entrada[ql], &tam);

    listas_entrada[ql] = cria_lista();

    for (int i=0; i<tam; i++){
      lista_dummy[ql][i].codigo = valores_entrada[ql][i];
      insere_item_ordenado(listas_entrada[ql], &lista_dummy[ql][i]);
    }
  }

  //*lista_merge = merge_ordenadas(listas_entrada[0], listas_entrada[1]);
  //imprime_lista(lista_merge);
  //Lista* lista_merge2 = cria_lista();
  Lista* lista_merge2 = listas_entrada[0];
  //imprime_lista(lista_merge2);
  lista_merge2 = merge_ordenadas2(listas_entrada[0], listas_entrada[1]);

//  for (int ql=0; ql<quant_listas; ql++){
//    printf("ql = %d\n", ql);
//    *lista_merge2 = merge_ordenadas2(lista_merge2, listas_entrada[ql]);
//    //imprime_lista(lista_merge);
    //printf("AQUI.\n");
//  }
  imprime_lista(listas_entrada[0]);
  printf("De volta para main()\n");


/*
  imprime_lista(lista1);
  imprime_lista(listas_entrada[0]);

  imprime_lista(lista2);
  imprime_lista(listas_entrada[1]);

  imprime_lista(lista_merge);
  imprime_lista(lista_merge2);
  return 0;
  */

} //end-main


/*
cgg -Wall -c main.c -o main.o
gcc main.o LojaVirtual.c -o program
*/
