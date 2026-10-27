import pygame
pygame.init()


class Opponent(pygame.sprite.Sprite):
    def __init__(self,screen, usableSpells):
        self.health = 100
        self.usableSpells = usableSpells
        self.image  = pygame.Surface((50,50))
        self.image.fill(((255,0,0)))

        self.rect = self.image.get_rect(center = (900,300))
        self.rect.center = (900,300)
        self.target = ""
        self.speed = 5
        self.screen = screen


    def attack(self, target, spell):
        self.tartget = target
        self.spell = spell

    def draw(self, surface, cameraX, cameraY):
        surface.blit(self.image, (self.rect.x - cameraX, self.rect.y - cameraY))
        
    def drawLetterInfo(self, pos, color, words=None):
            font = pygame.font.Font(None, 36)
            text = font.render(words, True, color)
            self.screen.blit(text, (pos))


