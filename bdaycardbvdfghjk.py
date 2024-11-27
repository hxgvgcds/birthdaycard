import pygame
import time

pygame.init()
pygame.font.init()

HEIGHT = 600
WIDTH = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("birthday greeting card")

image1 = pygame.image.load("images/box.jpg")
image2 = pygame.image.load("images/cake.jpg")
image3 = pygame.image.load("images/card.jpg")

img1 = pygame.transform.scale(image1, (WIDTH, HEIGHT))
img2 = pygame.transform.scale(image2, (WIDTH, HEIGHT))
img3 = pygame.transform.scale(image3, (WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    font = pygame.font.SysFont("Yatra One", 72)
    text1 = font.render("happybday", True, (0, 0, 0))
    screen.blit(text1, (200,150))
    screen.blit(img1,(0,0))
    pygame.display.update()
    time.sleep(2)

    font = pygame.font.SysFont("Yatra One", 72)
    text2 = font.render("tririertr", True, (0, 0, 0))
    screen.blit(text2, (200,150))
    screen.blit(img2,(0,0))
    pygame.display.update()
    time.sleep(2)

    font = pygame.font.SysFont("Yatra One", 72)
    text3 = font.render("happtrttrt", True, (0, 0, 0))
    screen.blit(text3, (200,150))
    screen.blit(img3,(0,0))
    pygame.display.update()
    time.sleep(2)