import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600),pygame.RESIZABLE)
pygame.display.set_caption("tajna")
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
