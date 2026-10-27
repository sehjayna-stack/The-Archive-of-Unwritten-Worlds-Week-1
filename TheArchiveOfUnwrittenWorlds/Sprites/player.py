import pygame
import math
import random

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, image=None, ):
        #calls the Sprite constructor first
        super().__init__()

        self.screen = screen
        self.image = pygame.Surface((50,50))
        self.image.fill(((0,255,0))) #temp green player sprite.
        #self.image = pygame.image.load("player.png").convert alpha 

        #creates hitbox area of the image
        self.rect = self.image.get_rect(center = (400,300))
        self.rect.center = (400,300)
        #define speed
        self.speed = 5
        self.health = 100
        

    def updatePOS(self):
        #"handles player movement based on keyboar input"
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
            self.rect.x -= self.speed
        if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:   
            self.rect.x += self.speed
        if self.keys[pygame.K_UP] or self.keys[pygame.K_w]:
            self.rect.y -= self.speed
        if self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, surface, cameraX, cameraY):
        surface.blit(self.image, (self.rect.x - cameraX, self.rect.y - cameraY))
        

        
    def drawLetterInfo(self, pos, color, words=None):
        font = pygame.font.Font(None, 36)
        text = font.render(words, True, color)
        self.screen.blit(text, (pos))

