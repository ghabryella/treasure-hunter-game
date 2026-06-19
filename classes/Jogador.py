import pygame
import os


class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 3  # velocidade do movimento na horizontal
        # tamanho do jogador
        self.largura = 300
        self.altura = 300
        self.velocidade_vertical = 0  # velocidade vertical usada na funcao pular e gravidade
        self.no_chao = False
        self.direcao_direita = True  # indica para qual lado o jogador está virado

        # carrega a imagem do jogador
        caminho_jogador = os.path.join("assets", "images", "jogador", "jogador.png")
        imagem_jogador = pygame.image.load(caminho_jogador)
        self.imagem_jogador = pygame.transform.scale(imagem_jogador, (self.largura, self.altura))

        # espelha a imagem do jogador quando ele andar pra esquerda
        self.imagem_jogador_esquerda = pygame.transform.flip(self.imagem_jogador, True, False)

    def mover(self, teclas):
        # move o jogador para a direita
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidade
            self.direcao_direita = True

        # move o jogador para a esquerda
        elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidade
            self.direcao_direita = False

    # funcao que permite que o jogador pule somente se estiver no chao
    def pular(self):
        if self.no_chao:
            self.velocidade_vertical = -15
            self.no_chao = False

    # funcao que faz com que a imagem correta do jogador seja exibida de acordo com a direção
    def mostrar(self, janela):
        if self.direcao_direita:
            janela.blit(self.imagem_jogador, (self.x, self.y))
        else:
            janela.blit(self.imagem_jogador_esquerda, (self.x, self.y))

    def gravidade(self):
        # aumenta a velocidade vertical
        self.velocidade_vertical += 1
        self.y += self.velocidade_vertical

        # chao
        if self.y >= 150:
            self.y = 150
            self.velocidade_vertical = 0
            self.no_chao = True

    # retorna o retangulo de impacto do jogador
    def detectar_impactos(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
