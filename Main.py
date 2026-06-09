import pygame
import sys
from classes.Menu import Menu

pygame.init()
pygame.mixer.init()

largura = 800
altura = 600

janela = pygame.display.set_mode((largura, altura))

menu = Menu(janela)

while True:
    menu.desenhar()
    resultado = menu.tratar_eventos()
    if resultado == "jogar":
        break
    elif resultado == "sair":
        pygame.quit()
        sys.exit()
