import pygame
from pygame.locals import *

WIDTH = 600
HEIGHT = 95
FPS = 30


class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('car.png')
        self.rect = self.image.get_rect()
        self.speed = 5

    def update(self):
        self.rect.x += self.speed

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Car Movement")
    clock = pygame.time.Clock()

    car = Car()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(car)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        all_sprites.update()

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
