import pygame
import os


class Menu:
    def __init__(self, janela):
        self.janela = janela
        self.largura = janela.get_width()
        self.altura = janela.get_height()

        # carrega as imagens do fundo do menu
        caminho_fundo = os.path.join("assets", "images", "fundos", "background_menu.png")
        imagem_fundo_raw = pygame.image.load(caminho_fundo)
        self.imagem_fundo = pygame.transform.scale(imagem_fundo_raw, (self.largura, self.altura))

        # carrega a musica de fundo do menu
        caminho_musica = os.path.join("assets", "sounds", "menu", "music_menu.mp3")
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # definicao do estilo e tamanho das fontes
        self.fonte_titulo = pygame.font.SysFont("Georgia", 65, bold=True)
        self.fonte_normal = pygame.font.SysFont("Arial", 18, bold=True)
        self.fonte_nome = pygame.font.SysFont("Arial", 14)

        # definicao das cores dos textos exibidos
        self.cor_titulo = (94, 134, 76)
        self.cor_texto = (255, 255, 255)
        self.cor_botao = (255, 255, 255)
        self.cor_contorno = (255, 255, 255)
        self.cor_nome = (102, 102, 99)

    # texto com contorno em todos os lados para melhorar a leitura
    def texto_com_contorno(self, texto, fonte, cor, x, y):
        contorno = fonte.render(texto, True, self.cor_contorno)
        self.janela.blit(contorno, (x - 2, y))  # contorno na esquerda
        self.janela.blit(contorno, (x + 2, y))  # contorno na direita
        self.janela.blit(contorno, (x, y - 2))  # contorno em cima
        self.janela.blit(contorno, (x, y + 2))  # contorno em baixo
        principal = fonte.render(texto, True, cor)
        self.janela.blit(principal, (x, y))

    def desenhar(self):
        self.janela.blit(self.imagem_fundo, (0, 0))  # imagem do fundo cobrindo a tela inteira

        # meu nome no pergaminho
        nome = self.fonte_nome.render("DESENVOLVIDO POR GHABRYELLA", True, self.cor_nome)
        x_nome = self.largura // 2 - nome.get_width() // 2
        self.janela.blit(nome, (x_nome, 68))

        x_treasure = self.largura // 2 - self.fonte_titulo.size("TREASURE")[0] // 2
        x_hunter = self.largura // 2 - self.fonte_titulo.size("HUNTER")[0] // 2
        self.texto_com_contorno("TREASURE", self.fonte_titulo, self.cor_titulo, x_treasure, 130)
        self.texto_com_contorno("HUNTER", self.fonte_titulo, self.cor_titulo, x_hunter, 200)

        # exibe os controles na tela
        controles = [
            ("A / Esquerda", "Mover para esquerda"),
            ("D / Direita", "Mover para direita"),
            ("Espaço", "Pular"),
        ]

        # centraliza as linhas de controle
        for i, (tecla, acao) in enumerate(controles):
            linha = tecla + "  -  " + acao
            texto = self.fonte_normal.render(linha, True, self.cor_texto)
            x = self.largura // 2 - texto.get_width() // 2
            self.janela.blit(texto, (x, 290 + i * 25))

        # botao de jogar
        x_botao = self.largura // 2 - self.fonte_normal.size("ENTER - Jogar")[0] // 2
        self.janela.blit(self.fonte_normal.render("ENTER - Jogar", True, self.cor_botao), (x_botao, 368))

        # atualiza a tela
        pygame.display.flip()

    # funcao que verifica as teclas
    def tratar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return "jogar"
                if evento.key == pygame.K_ESCAPE:
                    return "sair"
        return "menu"
