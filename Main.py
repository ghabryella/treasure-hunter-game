import pygame
import sys
from classes.Menu import Menu

# inicia o pygame e o mixer do audio
pygame.init()
pygame.mixer.init()

# tamanho da janela
largura = 800
altura = 600

janela = pygame.display.set_mode((largura, altura))  # criacao da janela

menu = Menu(janela)  # criacao do menu e o loop

while True:
    menu.desenhar()
    resultado = menu.tratar_eventos()
    if resultado == "jogar":
        break
    elif resultado == "sair":
        pygame.quit()
        sys.exit()
