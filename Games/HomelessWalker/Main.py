import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanhoTela = (1280, 720)
tela = pygame.display.set_mode(tamanhoTela)

pygame.display.set_caption("Homeless Walker ")
dt = 0

folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle_2.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()
folhaSpritesJump = pygame.image.load("assets/Homeless_1/Jump.png").convert_alpha()

framesIdle = []
framesWalk = []
framesJump = []

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

indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 5

indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJumo = 3

personagemRect = framesIdle[0].get_rect(midbottom = (250, 480))

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

listBgVelocidades = [1, 5, 9, 15, 16, 18, 20]

ListaBgPosicoes = [0 for _ in range(len(listBgImages))]
for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], tamanhoTela)
    

TAMANHO_CHAO = 580
VELOCIDADE_PERSONAGEM = 10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))

    for i in range(len(listBgImages)):
        if estaAndando:
            ListaBgPosicoes[i] -= listBgVelocidades[i] * VELOCIDADE_PERSONAGEM * dt * direcaoPersonagem

        if ListaBgPosicoes[i] <= -tamanhoTela[0]:
            ListaBgPosicoes[i] = 0

    for i in range(len(listBgImages)):

        tela.blit(listBgImages[i], (ListaBgPosicoes[i], 0))

        tela.blit(listBgImages[i], (ListaBgPosicoes[i] + tamanhoTela[0], 0))

        tela.blit(listBgImages[i], (ListaBgPosicoes[i] + -tamanhoTela[0], 0 ))

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

    estaAndando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        # personagemRect.x -= 200 * dt
        direcaoPersonagem = -1
        estaAndando = True 

    if teclas[pygame.K_RIGHT]:
        # personagemRect.x += 200 * dt
        direcaoPersonagem = 1
        estaAndando = True

    if teclas[pygame.K_SPACE]:
        if personagemRect.centery == TAMANHO_CHAO:
            gravidade = -30
    
    
    gravidade += 3

    personagemRect.y += gravidade

    if personagemRect.centery >= TAMANHO_CHAO:
        personagemRect.centery = TAMANHO_CHAO

    if gravidade < 0:
        frame = framesJump[indexFrameJump]
    else:
        if estaAndando:
            frame = framesWalk[indexFrameWalk]
        else:
            frame = framesIdle[indexFrameIdle]

    if direcaoPersonagem == -1:
        frame = pygame.transform.flip(frame, True, False)

    tela.blit(frame, personagemRect)

    # pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()

    dt = relogio.tick(60) / 1000