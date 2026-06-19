import pygame
import os
from classes.Tesouro import Tesouro
from classes.Obstaculo import Obstaculo
from classes.Jogador import Jogador


class Jogo:

    def __init__(self, janela):
        self.janela = janela
        self.largura = janela.get_width()
        self.altura = janela.get_height()

        self.jogador = Jogador(-50, 400)
        self.obstaculos = []
        self.tesouros = []
        self.tesouros_coletados = 0
        self.estado = "jogando"

        # carrega os 4 fundos do jogo
        self.fundos = []
        caminho1 = os.path.join("assets", "images", "fundos", "background_1.png")
        imagem1 = pygame.image.load(caminho1)
        self.fundos.append(pygame.transform.scale(imagem1, (self.largura, self.altura)))

        caminho2 = os.path.join("assets", "images", "fundos", "background_2.png")
        imagem2 = pygame.image.load(caminho2)
        self.fundos.append(pygame.transform.scale(imagem2, (self.largura, self.altura)))

        caminho3 = os.path.join("assets", "images", "fundos", "background_3.png")
        imagem3 = pygame.image.load(caminho3)
        self.fundos.append(pygame.transform.scale(imagem3, (self.largura, self.altura)))

        caminho4 = os.path.join("assets", "images", "fundos", "background_4.png")
        imagem4 = pygame.image.load(caminho4)
        self.fundos.append(pygame.transform.scale(imagem4, (self.largura, self.altura)))

        self.fundo_atual = 0
        self.fundo = self.fundos[0]
        self.fundo_posicao = 0

        # controle de tempo para trocar de fundo
        self.tempo_troca = pygame.time.get_ticks()
        self.intervalo_troca = 10000

    def atualizar(self, teclas):
        self.jogador.mover(teclas)
        self.jogador.gravidade()
        self.fundo_posicao -= 1.5

        # troca o fundo a cada 5 segundos
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_troca >= self.intervalo_troca:
            self.fundo_atual += 1
            if self.fundo_atual >= 4:
                self.fundo_atual = 0
            self.fundo = self.fundos[self.fundo_atual]
            self.tempo_troca = tempo_atual

        if self.fundo_posicao <= -self.largura:
            self.fundo_posicao = 0

        for obstaculo in self.obstaculos:
            obstaculo.mover()

        for tesouro in self.tesouros:
            tesouro.mover()

        for obstaculo in self.obstaculos:
            if self.jogador.detectar_impactos().colliderect(obstaculo.detectar_impactos()):
                self.estado = "derrota"

        for tesouro in self.tesouros:
            if tesouro.coletado == False:
                if self.jogador.detectar_impactos().colliderect(tesouro.detectar_impactos()):
                    tesouro.coletado = True
                    self.tesouros_coletados += 1

        if self.tesouros_coletados >= 10:
            self.estado = "vitória"

    def exibir(self):
        self.janela.blit(self.fundo, (self.fundo_posicao, 0))
        self.janela.blit(self.fundo, (self.fundo_posicao + self.largura, 0))
        self.jogador.mostrar(self.janela)

        for obstaculo in self.obstaculos:
            obstaculo.mostrar(self.janela)

        for tesouro in self.tesouros:
            tesouro.mostrar(self.janela)

        fonte = pygame.font.SysFont("Arial", 18, bold=True)
        texto = fonte.render(f"TESOUROS: {self.tesouros_coletados} / 10", True, (255, 255, 255))
        self.janela.blit(texto, (10, 10))
        pygame.display.flip()

    def tela_vitoria(self):
        fonte = pygame.font.SysFont("Georgia", 60, bold=True)
        texto = fonte.render("VITÓRIA!", True, (255, 215, 0))
        x = self.largura // 2 - texto.get_width() // 2
        y = self.altura // 2 - texto.get_height() // 2
        self.janela.blit(texto, (x, y))
        pygame.display.flip()

    def tela_derrota(self):
        fonte = pygame.font.SysFont("Georgia", 60, bold=True)
        texto = fonte.render("VOCÊ PERDEU", True, (220, 50, 50))
        x = self.largura // 2 - texto.get_width() // 2
        y = self.altura // 2 - texto.get_height() // 2
        self.janela.blit(texto, (x, y))
        pygame.display.flip()

    def executar(self):
        relogio = pygame.time.Clock()

        while self.estado == "jogando":
            relogio.tick(60)
            teclas = pygame.key.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "sair"
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        self.jogador.pular()
                    if evento.key == pygame.K_ESCAPE:
                        return "menu"

            self.atualizar(teclas)
            self.exibir()

        if self.estado == "vitória":
            self.tela_vitoria()
        elif self.estado == "derrota":
            self.tela_derrota()

        pygame.time.wait(2000)
        return "menu"
