import pygame
from random import randint

pygame.init()
relogio = pygame.time.Clock()

tamanhoTela = (1280, 720)
tela = pygame.display.set_mode(tamanhoTela)

pygame.display.set_caption("War Zombie ")
dt = 0

folhaSpritesSoldierIdle = pygame.image.load("assets/Soldier_1/Idle.png").convert_alpha()
folhaSpritesSoldierWalk = pygame.image.load("assets/Soldier_1/Walk.png").convert_alpha()
folhaSpritesSoldierRun = pygame.image.load("assets/Soldier_1/Run.png").convert_alpha()
folhaSpritesSoldierAttack = pygame.image.load("assets/Soldier_1/Attack.png").convert_alpha()
folhaSpritesSoldierShot = pygame.image.load("assets/Soldier_1/Shot_2.png").convert_alpha()
folhaSpritesSoldierDead = pygame.image.load("assets/Soldier_1/Dead.png").convert_alpha()
folhaSpritesSoldierHurt = pygame.image.load("assets/soldier_1/Hurt.png").convert_alpha()
folhaSpritesSoldierRecharge = pygame.image.load("assets/soldier_1/Recharge.png").convert_alpha()
folhaSpritesSoldierGrenade = pygame.image.load("assets/soldier_1/Grenade.png").convert_alpha()
folhaSpritesSoldierExplosion = pygame.image.load("assets/soldier_1/Explosion.png").convert_alpha()

folhaSpritesZombieIdle = pygame.image.load("assets/Zombie Man/Idle.png").convert_alpha()
folhaSpritesZombieWalk = pygame.image.load("assets/Zombie Man/Walk.png").convert_alpha()
folhaSpritesZombieRun = pygame.image.load("assets/Zombie Man/Run.png").convert_alpha()
folhaSpritesZombieAttack = pygame.image.load("assets/Zombie Man/Attack_2.png").convert_alpha()
folhaSpritesZombieDead = pygame.image.load("assets/Zombie Man/Dead.png").convert_alpha()
folhaSpritesZombieHurt = pygame.image.load("assets/Zombie Man/Hurt.png").convert_alpha()

listaFramesSoldierIdle = []
listaFramesSoldierWalk = []
listaFramesSoldierRun = []
listaFrmaesSoldierAttack = []
listaFramesSoldierShot = []
listaFrmaesSoldierDead = []
listaFramesSoldierHurt = []
listaFramesSoldierRecharge = []
listaFramesSoldierGrenade = []
listaFramesSoldierExplosion = []

listaFramesZombieIdle = []
listaFramesZombieWalk = []
listaFramesZombieRun = []
listaFramesZombieAttack = []
listaFramesZombieDead = []
listaFramesZombieHurt = []

for i in range(7):
    frame = folhaSpritesSoldierIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierIdle.append(frame)

for i in range(7):
    frame = folhaSpritesSoldierWalk.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierWalk.append(frame)

for i in range(8):
    frame = folhaSpritesSoldierRun.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierRun.append(frame)

for i in range(3):
    frame = folhaSpritesSoldierAttack.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFrmaesSoldierAttack.append(frame)

for i in range(4):
    frame = folhaSpritesSoldierShot.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierShot.append(frame)

for i in range(4):
    frame = folhaSpritesSoldierDead.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFrmaesSoldierDead.append(frame)

for i in range(3):
    frame = folhaSpritesSoldierHurt.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierHurt.append(frame)

for i in range(13):
    frame = folhaSpritesSoldierRecharge.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierRecharge.append(frame)

for i in range(9):
    frame = folhaSpritesSoldierGrenade.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierGrenade.append(frame)

for i in range(9):
    frame = folhaSpritesSoldierExplosion.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesSoldierExplosion.append(frame)

for i in range(8):
    frame = folhaSpritesZombieIdle.subsurface(i * 96, 0, 96, 96)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesZombieIdle.append(frame)

for i in range(8):
    frame = folhaSpritesZombieWalk.subsurface(i * 96, 0, 96, 96)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesZombieWalk.append(frame)

for i in range(7):
    frame = folhaSpritesZombieRun.subsurface(i * 96, 0, 96, 96)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesZombieRun.append(frame)

for i in range(4):
    frame = folhaSpritesZombieAttack.subsurface(i * 96, 0, 96, 96)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesZombieAttack.append(frame)

for i in range(5):
    frame = folhaSpritesZombieDead.subsurface(i * 96, 0, 96, 96)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesZombieDead.append(frame)

for i in range(3):
    frame = folhaSpritesZombieHurt.subsurface(i * 96, 0, 96, 96)
    frame = pygame.transform.scale(frame, (256, 256))
    listaFramesZombieHurt.append(frame)

gravidade = 1
direcaoPersonagem = 1
estaAndando = False

listBgImages = [
    pygame.image.load("assets/War4/Pale/sky.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/moon.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/houses4.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/houses3.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/houses2.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/houses1.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/wall.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/road.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/wheels.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/wheels2.png").convert_alpha(),
    pygame.image.load("assets/War4/Pale/wheels3.png").convert_alpha(),
]

listBgVelocidades = [1, 3, 7, 9, 10, 15, 20]

ListaBgPosicoes = [0 for _ in range(len(listBgImages))]
for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], tamanhoTela)

iconeVida = pygame.image.load("assets/Icon/Icon12.png").convert_alpha()
iconeVida = pygame.transform.scale2x(iconeVida)

ALTURA_CHAO = 550
velocidadePersonagem = 30

vidas = 3
GameOver = False
tempoJogo = 0


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))

    for i in range(len(listBgImages)):

        tela.blit(listBgImages[i], (ListaBgPosicoes[i], 0))

        tela.blit(listBgImages[i], (ListaBgPosicoes[i] + tamanhoTela[0], 0))

        tela.blit(listBgImages[i], (ListaBgPosicoes[i] + -tamanhoTela[0], 0 ))

    tela.blit(listaFramesSoldierIdle[0], (tamanhoTela[0] / 2, tamanhoTela[1] / 2))

    tela.blit(listaFramesZombieIdle[0], (tamanhoTela[0] / 2, tamanhoTela[1] / 2))

    pygame.display.update()

    dt = relogio.tick(60) / 1000