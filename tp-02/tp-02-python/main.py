import lista_encadeada
import string

lista = lista_encadeada.ListaEncadeada()


tipo_entrada = input()
#print(tipo_entrada)
num_listas = input()
#print(num_listas)
lista_listas = []
for n in range(int(num_listas)):
    entrada_str = input()
    entrada = entrada_str.split(',')
    entrada.pop()
    lista = [float(x) for x in entrada]
    lista_listas.append(lista)

def merge_ordenadas(l1, l2):
    tam_1 = len(l1)
    tam_2 = len(l2)
    print("merge de ")
    print(l1, l2)
    resultado = []
    i, j = 0, 0
    while i < tam_1 and j < tam_2:
        if l1[i] < l2[j]:
            resultado.append(l1[i])
            i += 1
        else:
            resultado.append(l2[j])
            j += 1
    print('merge ordenado: ', resultado)
    return resultado

def concatenar_listas_ord(lista_listas):
    resutado = lista_listas[0]
    for l in range(1, len(lista_listas)):
        #print(resutado)
        #print(lista_listas[l])
        resultado = merge_ordenadas(resutado, lista_listas[l])
        print(resultado)
    return resultado


if tipo_entrada == '1':
    #print('oi')
    resultado = concatenar_listas_ord(lista_listas)
    print(resultado)
