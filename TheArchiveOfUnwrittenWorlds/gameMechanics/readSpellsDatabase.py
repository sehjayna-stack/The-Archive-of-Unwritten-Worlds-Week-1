import json

class readSpellsDatabase():

    def __init__(self):
        with open("SaveFiles/spellsDatabase.json", "r") as f: #try this late: {spellsDB}
            data = json.load(f)

        self.spells = data["spells"]

    def getUsableSpellSequences(self, format=None): #category must
        usableSpells = []

        for name, spell in self.spells.items():
            if spell["flags"]["usable"] == True:
                if spell["flags"]["learned"] == True:
                    if spell["flags"]["temp_forgotten"] == False:
                        if format == "sequences":
                            usableSpells.append((spell["traits"]["spellSequence"]))
                        else: usableSpells.append((name, spell["traits"]["spellSequence"]))
            else: continue

        return usableSpells

#    def getSpells(self):
 #       for spell in self.items():

        
a = readSpellsDatabase()
b = a.getUsableSpellSequences()

print(b)