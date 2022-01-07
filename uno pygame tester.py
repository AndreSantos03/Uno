import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
run = True

WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))


while run:
    clock.tick(30)

    event_list = pygame.event.get()
    for event in event_list:
        if event.type ==  pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                run = False

    SCREEN.fill((255,255,255))    

    pygame.draw.rect(SCREEN,(0,0,0,10),pygame.Rect(0,0,WIDTH,HEIGHT))
    pygame.draw.rect(SCREEN,(255,255,255),pygame.Rect(WIDTH/4,HEIGHT/4,WIDTH/2,HEIGHT/2))
    font = pygame.font.SysFont('Comic Sans', 50)
    font_color = (0,0,0)
    font_background = (255,255,255)
    text_rect = pygame.Rect(WIDTH/4,HEIGHT/4,WIDTH/2,HEIGHT/2)
    text_rect = text_rect.move(WIDTH/6.5,HEIGHT/25)
    text = font.render("Choose a color", True, font_color, font_background)
    center_red = (WIDTH / 3.2, HEIGHT / 1.8)
    center_blue = (WIDTH / 2.3, HEIGHT / 1.8)
    center_green = (WIDTH / 1.8, HEIGHT / 1.8)
    center_yellow = (WIDTH / 1.5, HEIGHT / 1.8)
    radius = HEIGHT / 12
    pygame.draw.circle(SCREEN,(255,0,0),center_red,radius)
    pygame.draw.circle(SCREEN,(0,0,255),center_blue,radius)
    pygame.draw.circle(SCREEN,(0,255,0),center_green,radius)
    pygame.draw.circle(SCREEN,(255,255,0),center_yellow,radius)
    SCREEN.blit(text,text_rect)
    pygame.display.flip()

pygame.quit()
sys.exit(0)