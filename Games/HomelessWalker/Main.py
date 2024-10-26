import pygame
from random import randint

pygame.init()
relogio = pygame.time.Clock()

tamanhoTela = (1280, 720)
tela = pygame.display.set_mode(tamanhoTela)

pygame.display.set_caption("Homeless Walker ")
dt = 0

fonteTempo = pygame.font.Font("assets/Fonts/EnergyStation.ttf", 80)

folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle_2.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()
folhaSpritesJump = pygame.image.load("assets/Homeless_1/Jump.png").convert_alpha()
folhaSpritesRunn = pygame.image.load("assets/Homeless_1/Run.png").convert_alpha()

framesIdle = []
framesWalk = []
framesJump = []
framesRunn = []
listaObstaculos = []

for i in range(6):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesIdle.append(frame)

for i in range(8):
    frame = folhaSpritesWalk.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesWalk.append(frame)

for i in range(9):
    frame = folhaSpritesJump.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesJump.append(frame)

for i in range(8):
    frame = folhaSpritesRunn.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesRunn.append(frame)

indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 5

indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJumo = 3

indexFrameRunn = 0
tempoAnimacaoRunn = 0.0
velocidadeAnimacaoRunn = 10

personagemRect = framesIdle[0].get_rect(midbottom = (250, 480))
pesrsonagemColisaoRect = pygame.Rect(personagemRect.x, personagemRect.y, 80, 120)


gravidade = 1
direcaoPersonagem = 1
estaAndando = False

listBgImages = [
    pygame.image.load("assets/Apocalipse/Apocalypce3/Pale/sky.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce3/Pale/moon.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce3/Pale/sand_back.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce3/Pale/sand&objects3.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce3/Pale/sand&objects2.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce3/Pale/sand&objects1.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypce3/Pale/sand.png").convert_alpha(),
]


listBgVelocidades = [1, 3, 7, 9, 10, 15, 20]

ListaBgPosicoes = [0 for _ in range(len(listBgImages))]
for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], tamanhoTela)

listBgWapons = [
   pygame.image.load(f"assets/Obstaculos/icon28_{i:02d}.png").convert_alpha() for i in range(1, 40)
]
    
for i in range(len(listBgWapons)):
    listBgWapons[i] = pygame.transform.scale(listBgWapons[i], (50, 50))
    listBgWapons[i] = pygame.transform.flip(listBgWapons[i], True, False)
    listBgWapons[i] = pygame.transform.rotate(listBgWapons[i], 35)

iconeVida = pygame.image.load("assets/Icons/Icon12.png").convert_alpha()
iconeVida = pygame.transform.scale2x(iconeVida)

#TAMANHO_CHAO = 580
ALTURA_CHAO = 550
# VELOCIDADE_PERSONAGEM = 10
velocidadePersonagem = 30

vidas = 3
GameOver = False
tempoJogo = 0

listaObstaculos = []

AUMENTA_DIFICULDADE = pygame.USEREVENT + 1

ADICIONA_OBSTACULOS = pygame.USEREVENT + 1

pygame.time.set_timer(AUMENTA_DIFICULDADE, 10000)

pygame.time.set_timer(ADICIONA_OBSTACULOS, 1500)

tempoMaximoEntreObstaculos = 3000

ADICIONA_OBSTACULO = pygame.USEREVENT + 2
pygame.time.set_timer(ADICIONA_OBSTACULO, randint(500, tempoMaximoEntreObstaculos))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not GameOver:

            if event.type == AUMENTA_DIFICULDADE:
                velocidadePersonagem += 4

                if tempoMaximoEntreObstaculos > 1100:
                    tempoMaximoEntreObstaculos -=300

                pygame.time.set_timer(ADICIONA_OBSTACULOS, randint(800, tempoMaximoEntreObstaculos))

            if event.type == ADICIONA_OBSTACULOS:
                obstaculoImage = listBgWapons[randint(0, len(listBgWapons) -1)]
                posicaoX = randint(1280, 1500)
                obstaculoRect = obstaculoImage.get_rect(midbottom=(posicaoX, 620))

                obstaculo = {
                    "rect": obstaculoRect,
                    "image": obstaculoImage
                }

                listaObstaculos.append(obstaculo)

    tela.fill((255, 255, 255))

    if vidas <= 0:
        GameOver = True

    for i in range(len(listBgImages)):
        if estaAndando:
            ListaBgPosicoes[i] -= listBgVelocidades[i] * velocidadePersonagem * dt * direcaoPersonagem

        if ListaBgPosicoes[i] <= -tamanhoTela[0]:
            ListaBgPosicoes[i] = 0

        if ListaBgPosicoes[i] >= tamanhoTela[0]:
            ListaBgPosicoes[i] = 0

    for i in range(len(listBgImages)):

        tela.blit(listBgImages[i], (ListaBgPosicoes[i], 0))

        tela.blit(listBgImages[i], (ListaBgPosicoes[i] + tamanhoTela[0], 0))

        tela.blit(listBgImages[i], (ListaBgPosicoes[i] + -tamanhoTela[0], 0 ))

    if not GameOver:
        tempoJogo += dt

    textoTempo = fonteTempo.render(str(int(tempoJogo)), False, (255, 255, 255))

    tela.blit(textoTempo, (tamanhoTela[0] / 2, 30))

    for i in range(vidas):
        tela.blit(iconeVida, (20 + i * iconeVida.get_width(), 20))

    if GameOver:
        textoGameOver = fonteTempo.render("VOCE PERDEU!", False, (255, 255, 255))
        textoReiniciar = fonteTempo.render("Aperte Enter para continuar", False, (255, 255, 255))

        tela.blit(textoGameOver, (484, 260))
        tela.blit(textoReiniciar, (84, 360))

    tempoAnimacaoIdle += dt

    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        indexFrameIdle = (indexFrameIdle + 1) % len(framesIdle)
        tempoAnimacaoIdle = 0.0

    tempoAnimacaoWalk += dt

    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        indexFrameWalk = (indexFrameWalk + 1) % len(framesWalk)
        tempoAnimacaoWalk = 0.0

    tempoAnimacaoJump += dt

    if tempoAnimacaoJump >= 1 / velocidadeAnimacaoJumo:
        indexFrameJump = (indexFrameJump + 1) % len(framesJump)
        tempoAnimacaoJump = 0.0

    tempoAnimacaoRunn += dt

    if tempoAnimacaoRunn >= 1 / velocidadeAnimacaoRunn:
        indexFrameRunn = (indexFrameRunn + 1) % len(framesRunn)
        tempoAnimacaoRunn = 0.0

    estaAndando = False

    teclas = pygame.key.get_pressed()

    if not GameOver:
   
        if teclas[pygame.K_LEFT]:
            # personagemRect.x -= 200 * dt
            direcaoPersonagem = -1
            estaAndando = True 

        if teclas[pygame.K_RIGHT]:
            # personagemRect.x += 200 * dt
            direcaoPersonagem = 1
            estaAndando = True

        if teclas[pygame.K_SPACE]:
            if personagemRect.centery == ALTURA_CHAO:
                gravidade = -30
                indexFrameJump = 0
    else:
        if teclas[pygame.K_RETURN]:
            vidas = 3
            GameOver = False
            tempoJogo = 0
            velocidadePersonagem = 30
            tempoMaximoEntreObstaculos = 3000
            listaObstaculos = []
    
    gravidade += 2

    personagemRect.y += gravidade

    if personagemRect.centery >= ALTURA_CHAO:
        personagemRect.centery = ALTURA_CHAO

    pesrsonagemColisaoRect.midbottom = personagemRect.midbottom

    if gravidade < 0:
        frame = framesJump[indexFrameJump]
    else:
        if estaAndando:
            #frame = framesWalk[indexFrameWalk]
            if velocidadePersonagem < 40:
                frame = framesWalk[indexFrameWalk]
            if velocidadePersonagem < 50:
                frame = framesRunn[indexFrameRunn]
            elif velocidadePersonagem < 70:
                velocidadeAnimacaoRunn = 30
                frame = framesRunn[indexFrameRunn]
            else:
                velocidadeAnimacaoRunn = 40
                frame = framesRunn[indexFrameRunn]
        else:
            frame = framesIdle[indexFrameIdle]

    if direcaoPersonagem == -1:
        frame = pygame.transform.flip(frame, True, False)

    tela.blit(frame, personagemRect)

    for obstaculo in listaObstaculos:
        obstaculo["rect"].x -= 30 * velocidadePersonagem * dt

        if obstaculo["rect"].right < 0:
            listaObstaculos.remove(obstaculo)

        tela.blit(obstaculo["image"], obstaculo["rect"])

        if pesrsonagemColisaoRect.colliderect(obstaculo["rect"]):
            listaObstaculos.remove(obstaculo)
            vidas -= 1

        #pygame.draw.rect(tela, (255, 0 , 255), obstaculo["rect"], 2)

    # pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()

    dt = relogio.tick(60) / 1000