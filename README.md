# The-Archive-of-Unwritten-Worlds-Week-1
You play as an Archivist, someone who enters unstable “Unwritten Worlds” to stabilize them before they collapse. Each world is a different genre (fantasy, sci‑fi, mystery, surreal dreamscape), but all are incomplete, so physics, characters, and rules glitch in creative ways.

Tried to create a battle system, failed. ship prep. Made some background art that will be transformed to digital soon
1h 24m
Oct 26, 2026
Attempted creating a battle class with help from AI. Failed. It's jus easier to learn it myself atp. Did some research, and I need to update the "architecture" of my folders and files. For now, though, will worry about ship prep.

Created an Opponent, Gave player health, and opponent health
2h 25m
Oct 25, 2026
Created an opponent for player, made the player's movement smooth, created a player health bar and opponent health bar. Next, will decrease the players health and announce what spell was casted by whom and how much health it decreases of player.

FIXED EVERY BUG!!!!
3h 38m
Oct 24, 2026
the spellDatabaseReader, the spellCasting mechanic (open, closed and draw letters system), the game class, the spellDatabase itself, the configure file problem, EVERYTHING I COULD FIND. The system works perfectly, and I learned the lesson to not let myself get too far into coding without running the game. Now, the spellCastingMechanic has its open and closed state, and it works; the spellDatabaseReader can read the json file properly, and return the list of usable spell sequences; it can match up the usable spell sequences to the existing letters; and return the spellsequence that is being cast!!!!! Next, i want to work on either returning the list of usableSpellSequences with a tuple (nameOfSpell, spellSeqeunce), add graphics, and work on making storyline classes.

fixed the spellsDatabaseReader, and expanded spellsDatabase
2h 27m
Oct 22, 2026
fixed the spellsDatabaseReader; it returns the usable spellSequence perfectly. Now, though, when I implement the findSpellCaster, it causes bugs and problems, and the code won't run. N

Updated the format for the spells database
1h 39m
Oct 21, 2026
Worked on the spellsDatabaseReader: it still won't return ALL the usable spells, but it will return some and that's a start compared to before's nothing. Next, will work on fixe the spellsDatabaseReader.

Worked on the spellsDatabase reader.
2h 1m
Oct 20, 2026
creating spell casting system. Turns out, the spellsDatabase needs to be complete otherwise the spellsDatabaseReader won't read it without bugging or crashing out.

logic: user types spell -- spell is stored -- spellsDatabaseReader reads spellsDatabase and filters it for usable spells and their type sequence-- spellCastingMechanic matches type sequence to what user typed -- spellCastingMechanic initiates spell.


