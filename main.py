import pygame
import random

num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption('Я по твоему тупой?')
pygame.mouse.set_visible(False) 
screen = pygame.display.set_mode((W, H))

bg = pygame.image.load('Image/room.png')
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load('Image/cat.png')
cat_rect = cat.get_rect(center=(70, 220))
dog = pygame.image.load('Image/dog.png')
dog_rect = dog.get_rect(center=(410, 220))
owl = pygame.image.load('Image/owl.png')
owl_rect = owl.get_rect(center=(210, 120))
dialog = pygame.image.load('Image/dialog.png')
dialog_rect = dialog.get_rect()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    pygame.display.update()
