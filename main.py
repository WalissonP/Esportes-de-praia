from funcoes import *
from time import sleep

print('\033[1;93m-'*47, '\033[m')
print('\033[1;93mDESENVOLVEDORES: Walisson, Davi Rangel e Cauã\033[m')
titulo('CAMPEONATO DE ESPORTES DE PRAIA', '\033[1;46m')
print('\033[1;94m-'*47, '\033[m')

while True:
    calcular_classificacao()
    sleep(1)
    opc = menu()

    if opc == 1:
        cadastro()
    elif opc == 2:
        ver_dados()
    elif opc == 3:
        modificar_dados()
    elif opc == 4:
        mostrar_classificacao()
    else:
        for i in range(3):
            if i == 0:
                print(f'{c["amarelo"]}Encerrando',end='')
            sleep(1)
            print('.', end='', flush=True)
        print('\033[m')
        break