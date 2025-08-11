from time import sleep

c = {'sem_cor': '\033[m', 'azul': '\033[1;34m', 'amarelo': '\033[33m', 'vermelho': '\033[31;1m', 'verde': '\033[1;32m','branco': '\033[1;37m'}
equipes = []
matrizpont = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
cla = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
modalidade = ['surf', 'futevôlei', 'remo', 'vôlei']

def titulo(msg, cor = '\033[m'):
    print(f'{cor}='*47, c['sem_cor'])
    print(f'{c['branco']}{msg.center(47)}{c["sem_cor"]}')
    print(f'{cor}='*47, c['sem_cor'])

def menu():
    titulo('MENU INTERATIVO', '\033[1;37;44m')
    print(f'{c["branco"]}Digite o número da opção que deseja:\n1 -{c["sem_cor"]}{c["azul"]} Cadastrar Equipes \n{c["branco"]}2 - {c["azul"]}Ver dados \n{c["branco"]}3 - {c["azul"]}Modificar dados \n{c["branco"]}4 - {c["azul"]}Classificação \n{c["branco"]}5 - {c["azul"]}Sair do sistema{c["sem_cor"]}')
    print('\033[1;37;44m='*47, c['sem_cor'])

    while True:
        opc = input(f'{c["branco"]}Sua opção: {c["sem_cor"]}')
        if opc.isnumeric():
            opc = int(opc)
            if 1 <= opc <= 5:
                return opc
        print(f'{c["vermelho"]}Opção inválida, tente novamente!{c["sem_cor"]}')

    


def cadastro():
    titulo('CADASTRAR EQUIPES', '\033[1;37;44m')
    if equipes:
        titulo('TABELA DE PONTUAÇÕES', '\033[1;37;44m')
        print(f'{c["amarelo"]}Já tem equipes cadastradas!{c["sem_cor"]}')
        sleep(2)
        return

    for i in range(1,4):
        eqp=input(f'{c["branco"]}Digite o nome da {i}° equipe: {c["sem_cor"]}').lower()
        if eqp.isalpha():
            equipes.append(eqp)
        else:
            while True:
                print(f'{c["vermelho"]}Nome inválido, só é permitido letras{c["sem_cor"]}')
                eqp=input(f'{c["amarelo"]}Digite o nome da {i}° equipe: {c["sem_cor"]}').lower()
                if eqp.isalpha():
                    equipes.append(eqp)
                    break
    
    pontuacoes()

        
def pontuacoes():   
    for i in range(3):
        if i == 0:
            titulo('Iniciando cadastro das pontuações', '\033[1;37;44m')
            print(f'{c["amarelo"]}Carregando',end='')
        sleep(1)
        print('.', end='', flush=True)
    print('\033[m')

    for i in range(3):
        while True:
            surf = input(f"{c['branco']}Informe a pontuação da equipe {equipes[i]} no surf: {c['sem_cor']}")
            surf = surf.replace(',', '.')
            try:
                surf = float(surf)
                matrizpont[i][0] = surf
                break
            except ValueError:
                print(f'{c["vermelho"]}Valor inválido! Digite um número.{c["sem_cor"]}')

    for i in range(3):
        while True:
            fute = input(f"{c['branco']}Informe a pontuação da equipe {equipes[i]} no futevôlei: {c['sem_cor']}")
            fute = fute.replace(',', '.')
            try:
                fute = float(fute)
                matrizpont[i][1] = fute
                break
            except ValueError:
                print(f'{c["vermelho"]}Valor inválido! Digite um número.{c["sem_cor"]}')

    for i in range(3):
        while True:
            remo = input(f"{c['branco']}Informe a pontuação da equipe {equipes[i]} no remo: {c['sem_cor']}")
            remo = remo.replace(',', '.')
            try:
                remo = float(remo)
                matrizpont[i][2] = remo
                break
            except ValueError:
                print(f'{c["vermelho"]}Valor inválido! Digite um número.{c["sem_cor"]}')

    for i in range(3):
        while True:
            volei = input(f"{c['branco']}Informe a pontuação da equipe {equipes[i]} no vôlei de praia: {c['sem_cor']}")
            volei = volei.replace(',', '.')
            try:
                volei = float(volei)
                matrizpont[i][3] = volei
                break
            except ValueError:
                print(f'{c["vermelho"]}Valor inválido! Digite um número.{c["sem_cor"]}')
    
    


def mostrar_tabela():
    if not equipes:
        titulo('TABELA DE PONTUAÇÕES', '\033[1;37;44m')
        print(f'{c["amarelo"]}Nenhuma equipe cadastrada ainda!{c["sem_cor"]}')
        sleep(2)
        return

    titulo('TABELA DE PONTUAÇÕES', '\033[1;37;44m')

    # Cabeçalho
    print(f'{c["branco"]}Equipe \033[m', end='')
    for mod in modalidade:
        print(f'{c["branco"]}\t{mod.title()}', end='')
    print()

    # Linha de separação
    print('-' * 47)

    # Conteúdo da tabela
    for i in range(len(equipes)):
        print(f'{c["branco"]}{equipes[i].capitalize():<10}\033[m', end='')
        for j in range(len(modalidade)):
            print(f'{c["azul"]}{matrizpont[i][j]:<10}\033[m', end='')
        print()


def ver_dados():
    titulo('VER DADOS', '\033[1;37;44m')
    print(f'{c["branco"]}1 - {c["azul"]}Tabela completa {c["branco"]}\n2 - {c["azul"]}Dado específico\033[m')
    while True:
        opc = input(f'{c["branco"]}Sua opção: \033[m')
        if opc.isnumeric():
            opc = int(opc)
            if 1 <= opc <= 2:
                break
        print(f'{c["vermelho"]}Opção inválida, tente novamente!{c["sem_cor"]}')
    
    if opc == 1:
        mostrar_tabela()
    else:
        busca()


def modificar_dados():
    if not equipes:
        titulo('MODIFICAR DADOS', '\033[1;37;44m')
        print(f'{c["amarelo"]}Não há dados a serem modificados no momento!{c["sem_cor"]}')
        sleep(2)
        return

    titulo('MODIFICAR DADOS', '\033[1;37;44m')

    # Mostrar equipes disponíveis
    print(f'{c["branco"]}Equipes disponíveis:\033[m')
    for eq in equipes:
        print(f'{c["azul"]}→ {eq}\033[m')
    print()

    # Mostrar modalidades disponíveis
    print(f'{c["branco"]}Modalidades disponíveis:\033[m')
    for mod in modalidade:
        print(f'{c["azul"]}→ {mod}\033[m')
    print()

    # Procurar equipe (forma tradicional)
    nome_eqp = input(f'{c["branco"]}Digite o nome da equipe: \033[m').strip().lower()
    linha = -1
    for i in range(len(equipes)):
        if equipes[i].lower() == nome_eqp:
            linha = i
            break

    if linha == -1:
        print(f'{c["vermelho"]}Equipe não encontrada!{c["sem_cor"]}')
        return

    # Procurar modalidade (forma tradicional)
    nome_mod = input(f'{c["branco"]}Digite a modalidade: \033[m').strip().lower()
    coluna = -1
    for j in range(len(modalidade)):
        if modalidade[j].lower() == nome_mod:
            coluna = j
            break

    if coluna == -1:
        print(f'{c["vermelho"]}Modalidade não encontrada!{c["sem_cor"]}')
        return

    # Exibir pontuação atual
    atual = matrizpont[linha][coluna]
    print(f'{c["branco"]}\nPontuação atual da equipe {c["azul"]}{equipes[linha].capitalize()}{c["branco"]} na modalidade {c["azul"]}{modalidade[coluna]}{c["branco"]}: {atual}')

    # Solicitar nova pontuação com validação
    while True:
        nova = input(f'{c["branco"]}Digite a nova pontuação: \033[m')
        nova = nova.replace(',', '.')
        try:
            nova = float(nova)
            matrizpont[linha][coluna] = nova
            print(f'\n{c["verde"]}Pontuação atualizada com sucesso!{c["sem_cor"]}')
            break
        except ValueError:
            print(f'{c["vermelho"]}Valor inválido! Digite um número.{c["sem_cor"]}')


def calcular_classificacao():
    for j in range(4):  # para cada modalidade (coluna)
        pontuacoes = []
        for i in range(3):  # para cada equipe (linha)
            pontuacoes.append((matrizpont[i][j], i))

        pontuacoes.sort(reverse=True)

        # Atribui a classificação: 1º lugar para o maior, 2º para o segundo, etc.
        for posicao in range(3):
            indice_equipe = pontuacoes[posicao][1]
            cla[indice_equipe][j] = posicao + 1
    
def mostrar_classificacao():
    if not equipes:
        titulo('CLASSIFICAÇÃO DAS EQUIPES')
        print(f'{c["amarelo"]}Nenhuma equipe cadastrada ainda.{c["sem_cor"]}')
        return

    titulo('CLASSIFICAÇÃO DAS EQUIPES', '\033[1;37;44m')

    # Cabeçalho
    print(f'{c["branco"]}Equipe\033[m', end='')
    for mod in modalidade:
        print(f'{c["branco"]}\t{mod.title()}\033[m', end='')
    print()
    print('-' * 47)

    # Linhas com os dados da matriz cla
    for i in range(3):
        print(f'{c["branco"]}{equipes[i].capitalize():<10}\033[m', end='')
        for j in range(4):
            print(f'{c["azul"]}{cla[i][j]}{"º":<10}{c["sem_cor"]}', end='')
        print()





def busca():
    titulo('CONSULTA DE DADOS', '\033[1;37;44m')

    if not equipes:
        print(f'{c["amarelo"]}Nenhuma equipe cadastrada ainda!{c["sem_cor"]}')
        return

    # Converte listas para minúsculo
    equipeslower = []
    for e in equipes:
        equipeslower.append(e.lower())

    modalidadelower = []
    for m in modalidade:
        modalidadelower.append(m.lower())

    # Entrada de nomes separados por vírgula
    equipes_input_raw = input(f'{c["branco"]}Digite o(s) nome(s) da(s) equipe(s) (separado por vírgulas): \033[m').lower()
    equipes_input = []
    for e in equipes_input_raw.split(','):
        e = e.strip()
        if e != '':
            equipes_input.append(e)

    modalidades_input_raw = input(f'{c["branco"]}Digite a(s) modalidade(s) (separado por vírgulas): \033[m').lower()
    modalidades_input = []
    for m in modalidades_input_raw.split(','):
        m = m.strip()
        if m != '':
            modalidades_input.append(m)

    # Pega os índices das equipes válidas
    indices_equip = []
    if equipes_input:
        for i in range(len(equipeslower)):
            if equipeslower[i] in equipes_input:
                indices_equip.append(i)
    else:
        for i in range(len(equipes)):
            indices_equip.append(i)

    # Pega os índices das modalidades válidas
    indices_modal = []
    if modalidades_input:
        for j in range(len(modalidadelower)):
            if modalidadelower[j] in modalidades_input:
                indices_modal.append(j)
    else:
        for j in range(len(modalidade)):
            indices_modal.append(j)

    # Validação final
    if not indices_equip or not indices_modal:
        print(f'{c["vermelho"]}Nenhuma equipe ou modalidade válida encontrada.{c["sem_cor"]}')
        return

    # Exibir tabela
    print()
    print(f'{c["branco"]}Equipe\033[m', end='')
    for j in indices_modal:
        print(f'{c["branco"]}\t{modalidade[j].title()}\033[m', end='')
    print()
    print('-' * 47)

    for i in indices_equip:
        print(f'{c["branco"]}{equipes[i].capitalize():<10}\033[m', end='')
        for j in indices_modal:
            print(f'{c["azul"]}{matrizpont[i][j]:<10}\033[m', end='')
        print()
