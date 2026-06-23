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

        self.jogador = Jogador(-50, 400) # cria o jogador na sua posicao inicial
        self.obstaculos = []
        self.tesouros = []
        self.tesouros_coletados = 0  # contador de tesouros que serao coletados
        self.estado = "jogando"  # estado atual do jogo

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
        self.intervalo_troca = 10000  # troca de fundo a cada 10 segundos

        # controle de tempo para gerar obstaculos e tesouros
        self.tempo_obstaculo = pygame.time.get_ticks()
        self.intervalo_obstaculo = 3500

        self.tempo_tesouro = pygame.time.get_ticks()
        self.intervalo_tesouro = 2500

    def atualizar(self, teclas):
        self.jogador.mover(teclas)
        self.jogador.gravidade()
        self.fundo_posicao -= 1.5

        # troca o fundo a cada 10 segundos
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_troca >= self.intervalo_troca:
            self.fundo_atual += 1
            if self.fundo_atual >= 4:
                self.fundo_atual = 0
            self.fundo = self.fundos[self.fundo_atual]
            self.tempo_troca = tempo_atual

        if self.fundo_posicao <= -self.largura:
            self.fundo_posicao = 0

        # gera um obstaculo a cada 3,5 segundos
        if tempo_atual - self.tempo_obstaculo >= self.intervalo_obstaculo:
            self.obstaculos.append(Obstaculo(800, 355))
            self.tempo_obstaculo = tempo_atual

        # gera um tesouro a cada 2.5 segundos
        if tempo_atual - self.tempo_tesouro >= self.intervalo_tesouro:
            self.tesouros.append(Tesouro(800, 320))
            self.tempo_tesouro = tempo_atual

        # move todos os obstaculos para a esquerda
        for obstaculo in self.obstaculos:
            obstaculo.mover()

        # move todos os tesouros para a esquerda
        for tesouro in self.tesouros:
            tesouro.mover()

        # verifica se o jogador encostou em algum obstaculo
        for obstaculo in self.obstaculos:
            if self.jogador.detectar_impactos().colliderect(obstaculo.detectar_impactos()):
                self.estado = "derrota"

        # verifica se o jogador coletou algum tesouro
        for tesouro in self.tesouros:
            if tesouro.coletado == False:
                if self.jogador.detectar_impactos().colliderect(tesouro.detectar_impactos()):
                    tesouro.coletado = True
                    self.tesouros_coletados += 1

        # verifica a condicao de vitoria
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

        # exibe na tela o contador dos tesouros
        fonte = pygame.font.SysFont("Arial", 18, bold=True)
        texto = fonte.render(f"TESOUROS: {self.tesouros_coletados} / 10", True, (255, 255, 255))
        self.janela.blit(texto, (10, 10))
        pygame.display.flip()  # atualiza a tela

    def tela_vitoria(self):
        # exibe na tela a mensagem de vitória
        fonte = pygame.font.SysFont("Georgia", 60, bold=True)
        texto = fonte.render("VITÓRIA!", True, (255, 255, 255))
        x = self.largura // 2 - texto.get_width() // 2
        y = self.altura // 2 - texto.get_height() // 2
        self.janela.blit(texto, (x, y))
        pygame.display.flip()

    def tela_derrota(self):
        # exibe na tela a mensagem de derrota
        fonte = pygame.font.SysFont("Georgia", 60, bold=True)
        texto = fonte.render("VOCÊ PERDEU", True, (255, 255, 255))
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

        pygame.time.wait(2000)  # espera 2 segundos antes de voltar p menu
        return "menu"
