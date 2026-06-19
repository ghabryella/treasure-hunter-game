import pygame
import sys
from classes.Menu import Menu
from classes.Jogo import Jogo

# inicia o pygame e o mixer do audio
pygame.init()
pygame.mixer.init()

# tamanho da janela
largura = 800
altura = 600

janela = pygame.display.set_mode((largura, altura))  # criacao da janela
pygame.display.set_caption("Treasure Hunter")

estado = "menu"

while estado != "sair":
    if estado == "menu":
        menu = Menu(janela)
        while True:
            menu.desenhar()
            resultado = menu.tratar_eventos()
            if resultado == "jogar":
                estado = "jogando"
                break

            elif resultado == "sair":
                estado = "sair"
                break

    elif estado == "jogando":
        jogo = Jogo(janela)
        estado = jogo.executar()
pygame.quit()
sys.exit()
