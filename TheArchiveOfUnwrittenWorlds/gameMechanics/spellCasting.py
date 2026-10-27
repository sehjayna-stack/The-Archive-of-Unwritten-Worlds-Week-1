import pygame
#from SaveFiles.editSave import SaveFile
pygame.init()
from .readSpellsDatabase import readSpellsDatabase as RSD

#global spellDB; spellDB = readSpellsDatabase()

'''
Spellcasting class: implements the spell-casting game mechanic
    .readKeys(key, list) -> reads the last 5 - 7 keys that user inputs and returns them
    .displayLettersInterface.store() -> display read letters (readKeys) for the user, also stores them in a list
    .displayLettersInterface.update() -> pushes the previously typed letters to the left, once list is 8 letters long, delete the first letter. 
    .displayLettersInterface.kill() -> kills the interface
    .displayLettersInterface.restrict() -> restrict the use of certain spells
    .displayLettersInterface.isolate(spellName) -> finds the value and index number of the letters that match a spell. 

    .findSpell ->  finds a spell that the user knows or find a spell when searched for
    .implementSpell -> initiates spell consequences and animation
    
    .glow() -> lights up the displayLettersInterface
'''


class SpellCastingMechanic(): #create outside of the game loop
    def __init__(self, screen=None):# change back
        #load the testbase image,
    
        self.letters = ""; self.state = "closed"
        self.font = pygame.font.Font(None, 60) #creates font
        self.screen = screen
        self.textSurface = self.font.render(self.letters, True, (255,255,255))
        self.database = RSD()
        self.usableSpells = []
        self.spell = ""
        self.target = ""


    def wait(self, event):
        if event.key == pygame.K_RETURN: #KEYDOWN
            self.state = "open"                

    def open(self, event): #use this in the game loop after the window and background are drawnand before pygame.display.update 
        self.usableSpells = self.database.getUsableSpellSequences("sequences")    
        if event.unicode.isalpha(): #KEYDOWN , checks if the inputs are lowercase 
            self.spell = ""
            self.letters += event.unicode.lower() # type: ignore
            if len(self.letters) > 7:
                self.letters = self.letters[1:]
            for spell in self.usableSpells:
                if spell in self.letters:
                    self.spell = spell
        elif event.key == pygame.K_RETURN: #KEYDOWN
            self.letters = ""
            self.state = "closed"
        else: pass
        

    def drawLetters(self, pos, color, words=None):
        font = pygame.font.Font(None, 36)
        text = font.render(words, True, color)
        self.screen.blit(text, (pos))

    
   
    def glow(self, spell):
        pass
