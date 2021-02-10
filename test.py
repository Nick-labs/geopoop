import pygame
import sys

size = 640, 480

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

img = pygame.image.load('img.jpg')
img = pygame.transform.scale(img, size)
size = img.get_size()

img_rect = img.get_rect(bottomright=size)
screen.blit(img, img_rect)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

pygame.time.delay(20)
