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
        self.fonte_normal = pygame.font.SysFont("Georgia", 20, bold=True)

        # definicao das cores dos textos exibidos
        self.cor_titulo = (38, 113, 65)
        self.cor_texto = (255, 255, 255)
        self.cor_botao = (255, 255, 255)
        self.cor_contorno = (255, 255, 255)

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
        # titulo centralizado na tela
        x_treasure = self.largura // 2 - self.fonte_titulo.size("Treasure")[0] // 2
        x_hunter = self.largura // 2 - self.fonte_titulo.size("Hunter")[0] // 2
        self.texto_com_contorno("Treasure", self.fonte_titulo, self.cor_titulo, x_treasure, 80)
        self.texto_com_contorno("Hunter", self.fonte_titulo, self.cor_titulo, x_hunter, 160)

        # exibe os controles na tela
        controles = [
            ("A / Esquerda", "Mover para esquerda"),
            ("D / Direita", "Mover para direita"),
            ("W / Cima", "Pular"),
            ("Espaço", "Atirar"),
        ]

        # centraliza as linhas de controle
        for i, (tecla, acao) in enumerate(controles):
            linha = tecla + "  -  " + acao
            texto = self.fonte_normal.render(linha, True, self.cor_texto)
            x = self.largura // 2 - texto.get_width() // 2
            self.janela.blit(texto, (x, 310 + i * 35))

        # botao de jogar
        x_botao = self.largura // 2 - self.fonte_normal.size("ENTER - Jogar")[0] // 2
        self.janela.blit(self.fonte_normal.render("ENTER - Jogar", True, self.cor_botao), (x_botao, 480))

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
