import pygame
import random
from .spellCasting import SpellCastingMechanic as SCM


class Battle:

    def __init__(self, screen):
        self.screen = screen

        self.turn = "opponent"
        self.round = 0
        self.battleMode = False

        self.opponents = []
        self.heroes = []

        self.fighters = []

        self.playerMove = SCM()

        self.infoLine1 = ""
        self.infoLine2 = ""

        self.winner = None


    def start(self, opponents, heroes):

        self.opponents = opponents
        self.heroes = heroes

        self.fighters = []

        for fighter in self.opponents:
            initiative = random.randrange(1, 101)
            self.fighters.append((fighter, initiative))

        for fighter in self.heroes:
            initiative = random.randrange(1, 101)
            self.fighters.append((fighter, initiative))

        self.fighters.sort(
            key=lambda fighter: fighter[1],
            reverse=True
        )

        self.fighters = [
            fighter[0]
            for fighter in self.fighters
        ]

        print("Turn Order: - battle.py:53")
        

        self.battleMode = True
        self.round = 1


    def update(self, event):

        if not self.battleMode:
            return

        if len(self.heroes) == 0:
            self.winner = "opponents"
            self.battleMode = False
            return

        if len(self.opponents) == 0:
            self.winner = "heroes"
            self.battleMode = False
            return

        if len(self.fighters) == 0:
            self.start(self.opponents, self.heroes)
            return

        fighter = self.fighters[0]

        #
        # PLAYER TURN
        #
        if fighter.name == "player":

            if self.playerMove.state == "open":
                self.playerMove.open(event)
            else:
                self.playerMove.wait(event)

            if self.playerMove.spell is not None:

                damage = random.randrange(1, 21)

                if len(self.opponents) > 0:

                    target = self.opponents[0]

                    target.health -= damage

                    self.infoLine1 = (
                        f"{fighter.name} uses "
                        f"{self.playerMove.spell}"
                    )

                    self.infoLine2 = (
                        f"It deals {damage} damage!"
                    )

                    if target.health <= 0:

                        self.opponents.remove(target)

                        if target in self.fighters:
                            self.fighters.remove(target)

                self.playerMove.spell = None

                self.fighters.pop(0)

        #
        # OPPONENT TURN
        #
        else:

            damage = random.randrange(1, 21)

            target = self.heroes[0]

            target.health -= damage

            self.infoLine1 = (
                f"{fighter.name} uses fire!"
            )

            self.infoLine2 = (
                f"It deals {damage} damage!"
            )

            if target.health <= 0:

                self.heroes.remove(target)

                if target in self.fighters:
                    self.fighters.remove(target)

            self.fighters.pop(0)


    def draw(self):

        self.drawLetterInfo(
            (750, 50),
            (0, 0, 255),
            self.infoLine1
        )

        self.drawLetterInfo(
            (750, 100),
            (0, 0, 255),
            self.infoLine2
        )


    def drawLetterInfo(self, pos, color, words=""):

        font = pygame.font.Font(None, 36)

        text = font.render(
            str(words),
            True,
            color
        )

        self.screen.blit(
            text,
            pos
        )