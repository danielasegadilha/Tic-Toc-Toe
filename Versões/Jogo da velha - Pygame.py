import pygame
import numpy
import math

pygame.display.set_caption('Jogo da velha')

# cores em RGB
FUNDO = (64, 64, 64)
COR_DA_LINHA = (215, 216, 215)
COR_X = (233, 80, 79)
COR_O = (53, 148, 159)
BUTTON_COLOR = (128, 128, 128)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_LIGHT_BORDER = (192, 192, 192)  # cinza claro
BUTTON_DARK_BORDER = (48, 48, 48)  # cinza escuro
LINE_BORDER = 2

# constantes
TELA_X = 1000
TELA_Y = 600
TABULEIRO = 360
LINHA = 15
CIRCULO_DIAMETRO = 35
CIRCULO = LINHA - LINHA//3
ESPACO = 30
LINHA_X = LINHA
QUADRADO = TABULEIRO//3
AJUSTE_X = (TELA_X - TABULEIRO)//2
AJUSTE_Y = (TELA_Y - TABULEIRO)//2
BUTTON_X = 240
BUTTON_Y = 60

# relógio
clock = pygame.time.Clock()

# fonte do jogo
pygame.font.init()
fonte = pygame.font.SysFont('Arial', 30, bold=True)

# tela do jogo
tela = pygame.display.set_mode((TELA_X, TELA_Y))
tela.fill(FUNDO)

# tabuleiro
tab = numpy.zeros((3, 3))

# funções


def linhas_do_jogo():
    pygame.draw.line(tela, COR_DA_LINHA, (AJUSTE_X + QUADRADO, AJUSTE_Y), (AJUSTE_X + QUADRADO, AJUSTE_Y + TABULEIRO),
                     LINHA)
    pygame.draw.line(tela, COR_DA_LINHA, (AJUSTE_X + (QUADRADO * 2), AJUSTE_Y),
                     (AJUSTE_X + (QUADRADO * 2), AJUSTE_Y + TABULEIRO), LINHA)
    pygame.draw.line(tela, COR_DA_LINHA, (AJUSTE_X, AJUSTE_Y + QUADRADO), (AJUSTE_X + TABULEIRO, AJUSTE_Y + QUADRADO),
                     LINHA)
    pygame.draw.line(tela, COR_DA_LINHA, (AJUSTE_X, AJUSTE_Y + (QUADRADO * 2)),
                     (AJUSTE_X + TABULEIRO, AJUSTE_Y + (QUADRADO * 2)), LINHA)


def tabuleiro_hover(round):
    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0:
                pygame.draw.rect(tela, FUNDO, (AJUSTE_X + i * QUADRADO, AJUSTE_Y + j * QUADRADO, QUADRADO, QUADRADO))
    if 0 <= x < 3 and 0 <= y < 3 and tab[x][y] == 0:
        if jogada(round) == 1:
            pygame.draw.rect(tela, COR_X, (AJUSTE_X + x * QUADRADO, AJUSTE_Y + y * QUADRADO, QUADRADO, QUADRADO))
        else:
            pygame.draw.rect(tela, COR_O, (AJUSTE_X + x * QUADRADO, AJUSTE_Y + y * QUADRADO, QUADRADO, QUADRADO))


def jogada(round):
    if round % 2 != 0:
        player = 1
    else:
        player = 2
    return player


def desenha_simbolo(x, y):
    if tab[x][y] == 1:
        pygame.draw.rect(tela, FUNDO, (AJUSTE_X + x * QUADRADO, AJUSTE_Y + y * QUADRADO, QUADRADO, QUADRADO))
        pygame.draw.line(tela, COR_X, (AJUSTE_X + x * QUADRADO + ESPACO, AJUSTE_Y + y * QUADRADO + QUADRADO - ESPACO),
                         (AJUSTE_X + x * QUADRADO + QUADRADO - ESPACO, AJUSTE_Y + y * QUADRADO + ESPACO), LINHA_X)
        pygame.draw.line(tela, COR_X, (AJUSTE_X + x * QUADRADO + ESPACO, AJUSTE_Y + y * QUADRADO + ESPACO),
                         (AJUSTE_X + x * QUADRADO + QUADRADO - ESPACO, AJUSTE_Y + y * QUADRADO + QUADRADO - ESPACO),
                         LINHA_X)

    elif tab[x][y] == 2:
        pygame.draw.rect(tela, FUNDO, (AJUSTE_X + x * QUADRADO, AJUSTE_Y + y * QUADRADO, QUADRADO, QUADRADO))
        pygame.draw.circle(tela, COR_O, (int(AJUSTE_X + x * QUADRADO + QUADRADO//2),
                                         int(AJUSTE_Y + y * QUADRADO + QUADRADO//2)), CIRCULO_DIAMETRO, CIRCULO)


def confere_vencedor(round):
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] != 0:
            desenha_vencedor_horizontal(i, round)
            return True
        elif tab[0][i] == tab[1][i] == tab[2][i] != 0:
            desenha_vencedor_vertical(i, round)
            return True
        if tab[0][0] == tab[1][1] == tab[2][2] != 0:
            desenha_vencedor_desc_diagonal(round)
            return True
        elif tab[0][2] == tab[1][1] == tab[2][0] != 0:
            desenha_vencedor_asc_diagonal(round)
            return True
    return False


def desenha_vencedor_horizontal(i, round):
    posX = i * QUADRADO + QUADRADO//2 + AJUSTE_X
    if jogada(round) != 1:
        pygame.draw.line(tela, COR_X, (posX, AJUSTE_Y + ESPACO//2), (posX, AJUSTE_Y + TABULEIRO - ESPACO//2), LINHA)
    else:
        pygame.draw.line(tela, COR_O, (posX, AJUSTE_Y + ESPACO // 2), (posX, AJUSTE_Y + TABULEIRO - ESPACO // 2),
                         LINHA)


def desenha_vencedor_vertical(i, round):
    posY = i * QUADRADO + QUADRADO//2 + AJUSTE_Y
    if jogada(round) != 1:
        pygame.draw.line(tela, COR_X, (AJUSTE_X + ESPACO//2, posY), (AJUSTE_X + TABULEIRO - ESPACO//2, posY), LINHA)
    else:
        pygame.draw.line(tela, COR_O, (AJUSTE_X + ESPACO // 2, posY), (AJUSTE_X + TABULEIRO - ESPACO // 2, posY), LINHA)


def desenha_vencedor_desc_diagonal(round):
    if jogada(round) != 1:
        pygame.draw.line(tela, COR_X, (AJUSTE_X + ESPACO//2, AJUSTE_Y + ESPACO//2),
                         (AJUSTE_X + TABULEIRO - ESPACO//2, AJUSTE_Y + TABULEIRO - ESPACO//2), LINHA)
    else:
        pygame.draw.line(tela, COR_O, (AJUSTE_X + ESPACO // 2, AJUSTE_Y + ESPACO // 2),
                         (AJUSTE_X + TABULEIRO - ESPACO // 2, AJUSTE_Y + TABULEIRO - ESPACO // 2), LINHA)


def desenha_vencedor_asc_diagonal(round):
    if jogada(round) != 1:
        pygame.draw.line(tela, COR_X, (AJUSTE_X + ESPACO//2, AJUSTE_Y + TABULEIRO - ESPACO//2),
                         (AJUSTE_X + TABULEIRO - ESPACO//2, AJUSTE_Y + ESPACO//2), LINHA)
    else:
        pygame.draw.line(tela, COR_X, (AJUSTE_X + ESPACO // 2, AJUSTE_Y + TABULEIRO - ESPACO // 2),
                         (AJUSTE_X + TABULEIRO - ESPACO // 2, AJUSTE_Y + ESPACO // 2), LINHA)


def restart_button(position, clicked):
    pygame.draw.rect(tela, BUTTON_COLOR, (380, 30, BUTTON_X, BUTTON_Y))

    if not clicked:
        pygame.draw.line(tela, BUTTON_LIGHT_BORDER, position.topleft, position.topright, LINE_BORDER)
        pygame.draw.line(tela, BUTTON_LIGHT_BORDER, position.topleft, position.bottomleft, LINE_BORDER)
        pygame.draw.line(tela, BUTTON_DARK_BORDER, position.bottomleft, position.bottomright, LINE_BORDER)
        pygame.draw.line(tela, BUTTON_DARK_BORDER, position.topright, position.bottomright, LINE_BORDER)
    else:
        pygame.draw.line(tela, BUTTON_DARK_BORDER, position.topleft, position.topright, LINE_BORDER)
        pygame.draw.line(tela, BUTTON_DARK_BORDER, position.topleft, position.bottomleft, LINE_BORDER)
        pygame.draw.line(tela, BUTTON_LIGHT_BORDER, position.bottomleft, position.bottomright, LINE_BORDER)
        pygame.draw.line(tela, BUTTON_LIGHT_BORDER, position.topright, position.bottomright, LINE_BORDER)

    text = fonte.render('Restart game', 1, BUTTON_TEXT_COLOR)
    tela.blit(text, (425, 40))

def restart_game():
    global game_over
    global partida
    tab = numpy.zeros((3, 3))
    game_over = False
    partida = 1
    pygame.draw.rect(tela, FUNDO, (380, 30, BUTTON_X + LINE_BORDER, BUTTON_Y + LINE_BORDER))
    return tab, game_over, partida

# mainloop
pygame.init()

partida = 1
game_over = False
restart_button_rect = pygame.Rect(380, 30, BUTTON_X, BUTTON_Y)
posicao_botao = pygame.Rect(380, 30, BUTTON_X, BUTTON_Y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    clock.tick(60)
    # mouse
    mouseX, mouseY = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if not game_over:

        # converte posicao x, y para index
        x = (math.ceil((mouseX - AJUSTE_X) / QUADRADO) - 1)
        y = (math.ceil((mouseY - AJUSTE_Y) / QUADRADO) - 1)

        if not confere_vencedor(partida) and partida < 10:
            tabuleiro_hover(partida)
            if 0 <= x < 3 and 0 <= y < 3:
                if click[0] and tab[x][y] == 0:
                    tab[x][y] = jogada(partida)
                    partida += 1
                desenha_simbolo(x, y)
            linhas_do_jogo()
        else:
            game_over = True
            clicked_button = False
            restart_button(posicao_botao, click[0])

    else:
        if click[0] and restart_button_rect.collidepoint(mouseX, mouseY):
            tab, game_over, partida = restart_game()
            clicked_button = True

    pygame.display.update()
