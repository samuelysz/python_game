import pygame

class Ship():
    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('image/ship.png')
        self.image_size = (100, 100)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom  
        self.moving_right = False

    def update(self):
        if self.moving_rigth:
            self.rect.center +=1

    def blitme(self):

        self.screen.blit(self.image, self.rect)