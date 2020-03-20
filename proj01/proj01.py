__author__ = "Bruno F. Bessa"
__email__ = "bruno.fernandes.oliveira@alumni.usp.br"

"""
Este codigo é o primeiro projeto da disciplina MAI5001.
"""

def main():

    numero = input()
    if float(numero) < 0:
        numero = -1
    print("Hello World " + str(numero))

if __name__ == "__main__":
    main()
