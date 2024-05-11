import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
import serial
import threading


def game_do_peixinho(tempo, dificuldade, forca, porta, frequencia):

    tempo_jogo = tempo
    dificuldade_jogo = dificuldade
    forca_do_paciente = forca
    porta_arduino = porta
    frequencia_arduino = frequencia

    # Função para lidar com a comunicação serial
    def serial_communication(forca, porta, frequencia, callback):
        try:
            arduino = serial.Serial(porta, frequencia)
            while True:
                linha = arduino.readline().decode().strip()
                valor_altura_maxima = int(linha)
                if valor_altura_maxima >= forca and not esta_pulando:
                    print(valor_altura_maxima)
                    callback(valor_altura_maxima)
        except Exception as e:
            print("Erro na comunicação serial:", e)

    # Função de callback para lidar com os dados recebidos
    def handle_jump(valor_altura_maxima):
        global esta_pulando
        esta_pulando = True 
        return valor_altura_maxima

    # Inicialização
    esta_pulando = False

    # Iniciando a comunicação serial em uma thread separada
    thread = threading.Thread(target=serial_communication, args=(forca_do_paciente, porta_arduino, frequencia_arduino, handle_jump))
    thread.daemon = True
    thread.start()

    def dificuldade_do_jogo(dificuldade):
        if dificuldade == 'Fácil': 
            return 5;  
        elif dificuldade == 'Médio':
            return 10
        elif dificuldade == 'Difícil':
            return 15
        else:
            raise ValueError("Dificuldade inválida: deve ser 'Fácil', 'Médio' ou 'Difícil'")

    '''
    arduino = serial.Serial(porta, frequencia)

    while True:
        linha = arduino.readline().decode().strip()
        valor_altura_maxima = int(linha) 
        esta_pulando = False
        
        if valor_altura_maxima >= 200:  
            print(valor_altura_maxima )
            esta_pulando = True
        if tempo == 200:
            break
    '''

    pygame.init()
    pygame.mixer.init()

    #Pegando os aquivos do jogo (para que funcione em qualquer PC)
    diretorio_principal = os.path.dirname(__file__)
    diretorio_imagens = os.path.join(diretorio_principal, 'imagens')


    #Tamando da tela
    LARGURA = 1040
    ALTURA = 700


    #Cor da tela
    BRANCO = (255, 255, 255)


    #configuracões da tela
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Game peixinho')


    #pegando as imagens
    sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()


    #configuracão imagem dino
    class Dino(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            #Pegando so 3 primeiros frames
            self.imagens_dinossauro = []
            #pegando a posicão das imagens  | posicao | tamanho x e y -- Primeiro frame
            for i in range (3):
                img = sprite_sheet.subsurface((i * 32,0), (32, 32))
                img = pygame.transform.scale(img,(32*3, 32*3))
                self.imagens_dinossauro.append(img)

            self.index_lista = 0
            self.image = self.imagens_dinossauro[self.index_lista]
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            #posicão dinossauro na tela de acordo com o tamando da mesma
            self.pos_y_inicial = ALTURA - 64 - 96//2
            self.rect.center = (100, ALTURA - 64)
            self.esta_pulando = False  #mudei de self.pulo ---> self.esta_pulando

        def pular(self):
            self.esta_pulando = True   #Original = True | esta_pulando


        #velocidade da mudanca de quadros
        def update(self):

            #pulo do player
            if self.esta_pulando == True: #Original = True | esta_pulando

                #quando chegar em determina posicão, ele para de subir
                if self.rect.y <= 470: #==== PAINEL DE CONTROLE ======= (padrão = 500)
                    self.esta_pulando = False

                #toda vez que alterar o espaco, a posicão Y do dino ira diminuir (pular)
                self.rect.y -= 20 #==== PAINEL DE CONTROLE ======= GRAVIDADE PRA CIMA (PRA CIMA) (padrão = 20)
            else:

                #se o player estiver na altuta maxima, ele vai descer (se nao estiver encostado no chão)
                if self.rect.y < self.pos_y_inicial:
                    self.rect.y += 10 #==== PAINEL DE CONTROLE ======= GRAVIDADE (PRA BAIXO) | (padrão = 20)

                #se o dinossauro ja estiver encostado no chão
                else:
                    self.rect.y = self.pos_y_inicial

            if self.index_lista > 2:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_dinossauro[int(self.index_lista)]


    #configuracão imagem nuvens
    class Nuvens(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = sprite_sheet.subsurface((7*32, 0), (32, 32))

            #aumentando tamando da nuvem ------------------- X . 3 | y. 3
            self.image = pygame.transform.scale(self.image, (32*3, 32*3))

            #posicioando nuvem com quadrado em volta para mapear a posicão da nuvem
            self.rect = self.image.get_rect()

            #posicao aleatoria das nuvems em X e Y| intervalo inicial, final e o passo
            self.rect.y = randrange(50, 200, 50)
            self.rect.x = LARGURA - randrange(30, 300, 90)


        #movimentacão das nuvens
        def update(self):
            if self.rect.topright[0] < 0:          #se ultrapassar a borda esquerda da tela:
                self.rect.x = LARGURA
                self.rect.y = randrange(50, 200, 50)              
            self.rect.x -= dificuldade_do_jogo(dificuldade_jogo)


    #configuracão de chão
    class Chao(pygame.sprite.Sprite):
        def __init__(self, pos_x):
            pygame.sprite.Sprite.__init__(self)
            # ----------------------------------- V o numero 6 representa a posicão do chão na sprit
            self.image = sprite_sheet.subsurface((6*32, 0), (32, 32))
            self.image = pygame.transform.scale(self.image, (32*2, 32*2))
            self.rect = self.image.get_rect()                                    
            self.rect.y = ALTURA - 64
            self.rect.x = pos_x * 64
        
        #movimentacão do chão
        def update(self):
            if self.rect.topright[0] < 0:      
                self.rect.x = LARGURA  
            self.rect.x -= dificuldade_do_jogo(dificuldade_jogo)  


    #configuracão de inimigos
    class Inimigo(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = sprite_sheet.subsurface((5*32, 0), (32, 32))
            self.image = pygame.transform.scale(self.image, (32*2, 32*2))
            self.rect =  self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.center = (LARGURA, ALTURA - 64)

        def update(self):
            if self.rect.topright[0] < 0:          #se ultrapassar a borda esquerda da tela:
                self.rect.x = LARGURA       
            self.rect.x -= dificuldade_do_jogo(dificuldade_jogo)


    todas_as_sprites = pygame.sprite.Group()
    dino = Dino()
    todas_as_sprites.add(dino)


    #fazendo varias nuvens aparecerem
    for i in range(4):
        nuvem = Nuvens()
        todas_as_sprites.add(nuvem)


    #criando varios "chaos"
    for i in range(LARGURA*2//64):
        chao = Chao(i)
        todas_as_sprites.add(chao)

    #intanciando o inimigo na tela
    inimigo = Inimigo()
    todas_as_sprites.add(inimigo)


    grupo_obstaculos = pygame.sprite.Group()
    grupo_obstaculos.add(inimigo)


    relogio = pygame.time.Clock()
    #parte de eventos do jogo
    while True:
        relogio.tick(30)
        tela.fill(BRANCO)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        #evento do pulo -- PARTE DE FOCO 000
        if event.type == KEYDOWN: 
            #se a tecla apertada for igual a "espaço"

            if event.key == K_SPACE: #TROCAR POR UMA VARIAVEL QUE SEJA TRUE OU FALSE

                #se o player ainda estiver no ar
                if dino.rect.y != dino.pos_y_inicial:
                    pass
                else:
                #chamando metodo de pular
                    dino.pular()


        #verificando de houve colisão
        colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)

        todas_as_sprites.draw(tela)

        #se colidir o game vai parar
        todas_as_sprites.update()
        '''
        if colisoes:
            pass
        else:
            pass
            todas_as_sprites.update()
        '''
        pygame.display.flip()
