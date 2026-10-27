import pygame
pygame.init()
from configure import *
from gameMechanics.spellCasting import SpellCastingMechanic as SCM
from Sprites.player import Player
from Sprites.opponent import Opponent
from gameMechanics.battle import Battle


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

cameraX = 0
cameraY = 0

global player; player = Player(window)
global opponent; opponent = Opponent(window, "fire, water")
global spellCaster; spellCaster = SCM(window)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #removes window
            exit() #terminates the program


        if event.type == pygame.KEYDOWN:
            #collect spellCasting.state, open or close spellCastingInteface accordingly
            if spellCaster.state == "open":
                spellCaster.open(event)
            elif spellCaster.state == "closed":
                spellCaster.wait(event)

            print(event.key, repr(event.unicode))      

        

    

    window.fill((0,0,0))


    player.draw(window, cameraX, cameraY)  
    opponent.draw(window, cameraX, cameraY)


    spellCaster.drawLetters((50,50), (255,255,255), spellCaster.letters)
    spellCaster.drawLetters ((200, 50), (255,0,0), spellCaster.spell)
    player.drawLetterInfo((50,100), (0,255,0), ("Player Health: " + str(player.health)))
    opponent.drawLetterInfo((750,100), (255,0,0), ("Opponent Health: " + str(opponent.health)))


    pygame.display.update()
    clock.tick(60)