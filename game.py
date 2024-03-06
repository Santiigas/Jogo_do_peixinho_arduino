import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

#Pegando os aquivos do jogo (para que funcione em qualquer PC)
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')


#Tamando da tela
LARGURA = 1040
ALTURA = 780


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

        #posicão dinossauro na tela de acordo com o tamando da mesma
        self.rect.center = (100, ALTURA - 64)

    #velocidade da mudanca de quadros
    def update(self):
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
        self.rect.x -= 10                      #velocidade de movimentacão da nuven


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
    
    #movimentacão do ceu
    def update(self):
        if self.rect.topright[0] < 0:      
            self.rect.x = LARGURA      
        self.rect.x -= 10 




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


relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()