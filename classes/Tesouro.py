import os
import pygame


class Tesouro:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 2  # velocidade do movimento do tesouro para a esquerda
        self.largura = 5  # largura da imagem do tesouro
        self.altura = 5  # altura da imagem do tesouro
        self.coletado = False  # se o tesouro já foi coletado pelo jogador ou nao

        # carrega a imagem do tesouro
        caminho_tesouro = os.path.join("assets", "images", "tesouro", "moeda.png")
        imagem = pygame.image.load(caminho_tesouro)
        self.imagem = pygame.transform.scale(imagem, (self.largura, self.altura))

    # move o tesouro da direita pra esquerda
    def mover(self):
        self.x -= self.velocidade

    # mostra o tesouro somente se ainda não foi coletado
    def mostrar(self, janela):
        if self.coletado == False:
            janela.blit(self.imagem, (self.x, self.y))

    # funcao que retorna a area de colisão do tesouro pra verificar se o jogador encostou 
    def detectar_impactos(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
