tab = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def imprimeTabuleiro():
    cont = 1
    for linha in range(3):
        print(f'   "posição {cont}"   |   "posição {cont + 1}"   |   "posição {cont + 2}"  ')
        print(f'                 |                 |                 ')
        print(f'        {tab[linha][0]}        |        {tab[linha][1]}        |        {tab[linha][2]}        ')
        print(f'                 |                 |                 ')
        if linha != 2:
            print(f'_________________|_________________|_________________')
        else:
            print(f'                 |                 |                 ')
        cont += 3

def jogada(round):
    if round % 2 != 0:
        player = 'X'
    else:
        player = 'O'
    return player


def conferePosicao(posicao):
    quebra = 0
    if 1 <= posicao <= 3 and tab[0][posicao - 1] == " ":
        tab[0][posicao - 1 ] = jogada(partida)
    elif 3 <= posicao <= 6 and tab[1][posicao - 4] == " ":
        tab[1][posicao - 4] = jogada(partida)
    elif 6 <= posicao <= 9 and tab[2][posicao - 7] == " ":
        tab[2][posicao - 7] = jogada(partida)
    else:
        print(f'\n Essa posição não está disponível, por favor, tente novamente \n')


def confereVencedor():
    for i in range(0, 3):
        if tab[i][0] == tab[i][1] == tab[i][2] != " " or tab[0][i] == tab[1][i] == tab[2][i] != " ":
            return False
    if tab[0][0] == tab[1][1] == tab[2][2] != " " or tab[0][2] == tab[1][1] == tab[2][0] != " ":
        return False
    return True


def resultado(rodadas):
    if rodadas != 9:
        print(f'Parabéns, você venceu!')
    else:
        print(f'Deu velha!')


partida = 0
print('\n Seja as seguintes posições no tabuleiro: \n ')
imprimeTabuleiro()
while confereVencedor() and partida < 9:
    partida += 1
    p = int(input(f"\n Jogador {jogada(partida)} é a sua vez, por favor, informe a posição da jogada:  " ))
    conferePosicao(p)
    imprimeTabuleiro()
resultado(partida)
