import pygame
pygame.init()
tamanho = (900 , 500)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Hello Games! ")
relogio = pygame.time.Clock()
posicaoBola = pygame.Vector2(450, 250)
dt = 0
direcaoY = 1
direcaoX = 1
while True:
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit()
    tela.fill((40, 200, 100))
    pygame.draw.circle(tela, (10, 255, 200), posicaoBola, 50)
    posicaoBola.y += 100 * direcaoY * dt
    posicaoBola.x += 100 * direcaoX * dt
    if posicaoBola.y >= 450:
        direcaoY = -1
    elif posicaoBola.y <= 50:
        direcaoY = 1
    elif posicaoBola.x >= 850:
        direcaoX = -1
    elif posicaoBola.x <= 50:
        direcaoX = 1
    
    
    dt = relogio.tick(60) / 1000
    pygame.display.update()    