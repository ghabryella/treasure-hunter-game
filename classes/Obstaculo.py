import pygame
import os


class Obstaculo:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 1  # velocidade do movimento para a esquerda
        self.largura = 10  # largura da imagem do obstaculo
        self.altura = 10  # altura da imagem do obstaculo

        # carrega a imagem do obstaculo
        caminho_obstaculo = os.path.join("assets", "images", "obstaculo", "obstaculo.png")
        imagem = pygame.image.load(caminho_obstaculo)
        self.imagem = pygame.transform.scale(imagem, (self.largura, self.altura))

    # move o obstaculo para a esquerda
    def mover(self):
        self.x -= self.velocidade

    # mostra o obstaculo na tela
    def mostrar(self, janela):
        janela.blit(self.imagem, (self.x, self.y))

    # retangulo de colisao do obstaculo ao encostar no jogador
    def detectar_impactos(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
