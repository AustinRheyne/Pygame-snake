import pygame
import random

class Cherry:
    def __init__(self, screen):
        self.image = pygame.image.load("Images/Cherry.png")
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 200
        self.screen = screen

    def eat_me(self, player):
        if self.x == player.x and self.y == player.y:
            player.new_node()
            newPos = (random.randint(0,9)*50, random.randint(0,9)*50)
            while newPos in player.get_positions():
                newPos = (random.randint(0,9)*50, random.randint(0,9)*50)
            self.x, self.y = newPos
            return True


    def blit_me(self):
        self.rect.x, self.rect.y = self.x, self.y
        self.screen.blit(self.image, self.rect)