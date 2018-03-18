class ExpCalc:

    #Dictionaries giving monsters by CR:
    global monsters; monsters = {'Bat':'.1', 'Toad':'.1', 'Rat':'.125', 'Tiny Monstrous Centipede':'.125',
    'Donkey':'.16', 'Lizard':'.16', 'Monkey':'.16', 'Raven':'.16', 'Cat':'.25', 'Kobold':'.25',
    'Owl':'.25', 'Pony':'.25', 'Small Monstrous Centipede':'.25', 'Tiny Monstrous Scorpion':'.25',
    'Tiny Monstrous Spider':'.25', 'Weasel':'.25', 'Dire Rat':'.33', 'Dog':'.33',
    'Giant Fire Beetle':'.33', 'Goblin':'.33', 'Hawk':'.33', 'Skeleton':'.33',
    'Tiny Viper':'.33', 'Aasimar':'.5', 'Baboon':'.5', 'Badger':'.5', 'Brain Mole':'.5',
    'Dromite':'.5', 'Dwarf':'.5', 'Eagle':'.5', 'Elan':'.5', 'Elf':'.5', 'Formian Worker':'.5',
    'Gnome':'.5', 'Halfling':'.5', 'Hobgoblin':'.5', 'Human':'.5',
    'Zombie':'.5', 'Kobold Zombie':'.5', 'Locathah':'.5', 'Maenad':'.5',
    'Medium Monstrous Centipede':'.5', 'Merfolk':'.5', 'Orc':'.5', 'Porpoise':'.5',
    'Small Monstrous Scorpion':'.5', 'Small Monstrous Spider':'.5', 'Small Viper':'.5',
    'Stirge':'.5', 'Teoryran Human':'.5', 'Tiefling':'.5', 'Tiny Animated Object':'.5',
    'War Pony':'.5', 'Xeph':'.5', 'Blue':'1', 'Camel':'1', 'Darkmantle':'1', 'Drow':'1',
    'Duergar':'1', 'Dwarf':'1', 'Ghoul':'1', 'Giant Ant Worker':'1', 'Giant Bee':'1',
    'Gnoll':'1', 'Grig':'1', 'Grimlock':'1', 'Half-Giant':'1', 'Heavy Horse':'1',
    'Homunculus':'1', 'Hyena':'1', 'Krenshar':'1', 'Lacedon':'1', 'Large Monstrous Centipede':'1',
    'Lemure':'1', 'Light Horse':'1', 'Light Warhorse':'1', 'Lizardfolk':'1', 'Manta Ray':'1',
    'Medium Monstrous Scorpion':'1', 'Medium Monstrous Spider':'1', 'Medium Shark':'1',
    'Medium Viper':'1', 'Mule':'1', 'Nixie':'1', 'Octopus':'1', 'Pseudodragon':'1',
    'Puppeteer':'1', 'Riding Dog':'1', 'Shrieker':'1', 'Small Air Elemental':'1',
    'Small Animated Object':'1', 'Small Earth Elemental':'1', 'Small Fire Elemental':'1',
    'Small Water Elemental':'1', 'Spider Swarm':'1', 'Squid':'1', 'Svirfneblin':'1',
    'Troglodyte':'1', 'Troglodyte Zombie':'1', 'Wolf':'1', 'Wolf Skeleton':'1',
    'Ape':'2', 'Azer':'2', 'Bat Swarm':'2', 'Bison':'2', 'Black Bear':'2', 'Blink Dog':'2',
    'Boar':'2', 'Bugbear':'2', 'Bugbear Zombie':'2', 'Cheetah':'2', 'Choker':'2',
    'Constrictor Snake':'2', 'Crocodile':'2', 'Dire Badger':'2', 'Dire Bat':'2',
    'Dire Weasel':'2', 'Dretch':'2', 'Flesh Harrower Puppeteer':'2', 'Folugub':'2',
    'Giant Ant Queen':'2', 'Giant Ant Soldier':'2', 'Giant Bombardier Beetle':'2',
    'Heavy Warhorse':'2', 'Hippogriff':'2', 'Huge Monstrous Centipede':'2', 'Imp':'2',
    'Lantern Archon':'2', 'Large Monstrous Spider':'2', 'Large Shark':'2', 'Large Viper':'2',
    'Leopard':'2', 'Medium Animated Object':'2', 'Monitor Lizard':'2', 'Owlbear Skeleton':'2',
    'Quasit':'2', 'Rat Swarm':'2', 'Sahuagin':'2', 'Satyr':'2', 'Shocker Lizard':'2', 'Skum':'2',
    'Thoqqua':'2', 'Thought Eater':'2', 'Triton':'2', 'Vargouille':'2', 'Wererat':'2', 'White Dragon':'2',
    'Wolverine':'2', 'Worg':'2', 'Air Mephit':'3', 'Allip':'3', 'Ankheg':'3', 'Assassin Vine':'3',
    'Black Dragon':'3', 'Blue Dragon':'3', 'Brass Dragon':'3', 'Bronze Dragon':'3', 'Centaur':'3',
    'Cockatrice':'3', 'Copper Dragon':'3', 'Crysmal':'3', 'Deinonychus':'3', 'Derro':'3',
    'Dire Ape':'3', 'Dire Wolf':'3', 'Doppelganger':'3', 'Dryad':'3', 'Dust Mephit':'3',
    'Earth Mephit':'3', 'Ethereal Filcher':'3', 'Ethereal Marauder':'3', 'Ettercap':'3',
    'Fire Mephit':'3', 'Flamebrother Salamander':'3',
    'Formian Warrior':'3', 'Gelatinous Cube':'3', 'Ghast':'3', 'Giant Eagle':'3', 'Giant Owl':'3',
    'Giant Praying Mantis':'3', 'Giant Wasp':'3', 'Green Dragon':'3', 'Grick':'3', 'Hell Hound':'3',
    'Howler':'3', 'Huge Viper':'3', 'Ice Mephit':'3', 'Juvenile Arrowhawk':'3', 'Juvenile Tojanida':'3',
    'Large Animated Object':'3', 'Large Monstrous Scorpion':'3', 'Lion':'3', 'Locust Swarm':'3',
    'Magma Mephit':'3', 'Magmin':'3', 'Medium Air Elemental':'3', 'Medium Earth Elemental':'3',
    'Medium Fire Elemental':'3', 'Medium Water Elemental':'3', 'Merrow':'3', 'Minor Xorn':'3',
    'Ogre':'3', 'Ogre Zombie':'3', 'Ooze Mephit':'3', 'Pegasus':'3', 'Phantom Fungus':'3',
    'Rust Monster':'3', 'Salt Mephit':'3', 'Shadow':'3', 'Steam Mephit':'3', 'Temporal Filcher':'3',
    'Troll Skeleton':'3', 'Unicorn':'3', 'Violet Fungus':'3', 'Water Mephit':'3', 'Werewolf':'3',
    'White Dragon':'3', 'Wight':'3', 'Yeth Hound':'3', 'Aranea':'4', 'Barghest':'4',
    'Black Dragon':'4', 'Blue Dragon':'4', 'Brass Dragon':'4', 'Brown Bear':'4',
    'Centipede Swarm':'4', 'Chimera Skeleton':'4', 'Dire Boar':'4', 'Dire Wolverine':'4',
    'Five-Headed Hydra':'4', 'Gargoyle':'4', 'Giant Crocodile':'4', 'Giant Stag Beetle':'4',
    'Gray Ooze':'4', 'Green Dragon':'4', 'Griffon':'4', 'Harpy':'4', 'Hound Archon':'4',
    'Huge Shark':'4', 'Janni':'4', 'Kapoacinth':'4', 'Mimic':'4', 'Minotaur':'4',
    'Minotaur Zombie':'4', 'Otyugh':'4', 'Owlbear':'4', 'Pixie':'4', 'Polar Bear':'4',
    'Red Dragon':'4', 'Rhinoceros':'4', 'Satyr':'4', 'Sea Cat':'4', 'Sea Hag':'4',
    'Silver Dragon':'4', 'Tiger':'4', 'Vampire Spawn':'4', 'Wereboar':'4', 'White Dragon':'4',
    'Wyvern Zombie':'4', 'Achaierai':'5', 'Adult Arrowhawk':'5', 'Adult Tojanida':'5',
    'Basilisk':'5', 'Bearded Devil':'5', 'Black Dragon':'5', 'Bronze Dragon':'5', 'Cloaker':'5',
    'Copper Dragon':'5', 'Dire Lion':'5', 'Djinni':'5', 'Ettin Skeleton':'5', 'Giant Constrictor Snake':'5',
    'Gibbering Mouther':'5', 'Gold Dragon':'5', 'Greater Barghest':'5', 'Green Dragon':'5',
    'Green Hag':'5', 'Hieracosphinx':'5', 'Huge Animated Object':'5', 'Huge Monstrous Spider':'5',
    'Large Air Elemental':'5', 'Large Earth Elemental':'5', 'Large Fire Elemental':'5',
    'Large Water Elemental':'5', 'Manticore':'5', 'Mercane':'5', 'Mummy':'5', 'Nightmare':'5', 'Ochre Jelly':'5',
    'Orca':'5', 'Phase Spider':'5', 'Phrenic Creature':'5', 'Pixie':'5', 'Rast':'5',
    'Ravid':'5', 'Red Dragon':'5', 'Scrag':'5', 'Shadow Mastiff':'5', 'Silver Dragon':'5',
    'Six-Headed Hydra':'5', 'Spider Eater':'5', 'Troll':'5', 'Udoroot':'5', 'Unbodied':'5',
    'Werebear':'5', 'Weretiger':'5', 'Winter Wolf':'5', 'Wraith':'5',
    'Advanced Megaraptor Skeleton':'6', 'Annis':'6', 'Average Salamander':'6',
    'Average Xorn':'6', 'Babau':'6', 'Baleen Whale':'6', 'Belker':'6', 'Blue Dragon':'6',
    'Bralani':'6', 'Brass Dragon':'6', 'Chain Devil':'6', 'Digester':'6', 'Ettin':'6',
    'Five-Headed Hydra':'6', 'Gargantuan Monstrous Centipede':'6', 'Girallon':'6',
    'Gray Render Zombie':'6', 'Lamia':'6', 'Megaraptor':'6', 'Phthisic':'6', 'Seven-Headed Hydra':'6',
    'Shambling Mound':'6', 'Tendriculos':'6', 'White Dragon':'6', 'Will-O\'-Wisp':'6',
    'Wyvern':'6', 'Xill':'6', 'Aboleth':'7', 'Black Dragon':'7', 'Black Pudding':'7',
    'Bronze Dragon':'7', 'Bulette':'7', 'Cachalot Whale':'7', 'Chaos Beast':'7', 'Chimera':'7',
    'Chuul':'7', 'Cloud Giant Skeleton':'7', 'Copper Dragon':'7', 'Criosphinx':'7', 'Dire Bear':'7',
    'Dragonne':'7', 'Drider':'7', 'Eight-Headed Hydra':'7', 'Elasmosaurus':'7',
    'Elephant':'7', 'Flesh Golem':'7', 'Formian Taskmaster':'7', 'Gargantuan Animated Object':'7',
    'Gold Dragon':'7', 'Gray Glutton':'7', 'Hellcat':'7', 'Hill Giant':'7', 'Huge Air Elemental':'7',
    'Huge Earth Elemental':'7', 'Huge Fire Elemental':'7', 'Huge Monstrous Scorpion':'7',
    'Huge Water Elemental':'7', 'Intellect Devourer':'7', 'Invisible Stalker':'7', 'Lillend':'7',
    'Medusa':'7', 'Nymph':'7', 'Ogre Barbarian':'7', 'Phasm':'7', 'Psionic Aboleth':'7', 'Red Dragon':'7',
    'Remorhaz':'7', 'Silver Dragon':'7', 'Six-Headed Hydra':'7', 'Spectre':'7', 'Succubus':'7',
    'Water Naga':'7', 'Advanced Mummy':'8', 'Athach':'8', 'Behir':'8', 'Blue Dragon':'8',
    'Bodak':'8', 'Brass Dragon':'8', 'Dark Naga':'8', 'Destrachan':'8', 'Dire Tiger':'8',
    'Efreeti':'8', 'Elder Arrowhawk':'8', 'Elder Xorn':'8', 'Erinyes':'8', 'Gargantuan Monstrous Spider':'8',
    'Giant Octopus':'8', 'Gorgon':'8', 'Gray Render':'8', 'Greater Shadow':'8', 'Green Dragon':'8', 'Gynosphinx':'8',
    'Hellwasp Swarm':'8', 'Lammasu':'8', 'Mohrg':'8', 'Nine-Headed Hydra':'8', 'Noble Djinni':'8',
    'Ogre Mage':'8', 'Seven-Headed Hydra':'8', 'Shield Guardian':'8', 'Stone Giant':'8', 'Treant':'8',
    'Tyrannosaurus':'8', 'White Dragon':'8', 'Young Adult Red Dragon Skeleton':'8',
    'Androsphinx':'9', 'Avoral':'9', 'Black Dragon':'9', 'Bone Devil':'9', 'Bronze Dragon':'9',
    'Caller In Darkness':'9', 'Colossal Monstrous Centipede':'9', 'Copper Dragon':'9',
    'Delver':'9', 'Dire Shark':'9', 'Dragon Turtle':'9', 'Eight-Headed Hydra':'9',
    'Elder Tojanida':'9', 'Frost Giant':'9', 'Giant Squid':'9', 'Gold Dragon':'9',
    'Greater Air Elemental':'9', 'Greater Earth Elemental':'9', 'Greater Fire Elemental':'9',
    'Greater Water Elemental':'9', 'Hoary Steed':'9', 'Legendary Bear':'9', 'Nessian Warhound':'9',
    'Night Hag':'9', 'Roc':'9', 'Spirit Naga':'9', 'Stone Giant Elder':'9', 'Ten-Headed Hydra':'9',
    'Triceratops':'9', 'Vrock':'9', 'Yrthak':'9', 'Zelekhut':'9',
    'Bebilith':'10', 'Brass Dragon':'10', 'Cerebrilith':'10', 'Clay Golem':'10', 'Colossal Animated Object':'10',
    'Couatl':'10', 'Eleven-Headed Hydra':'10', 'Fire Giant':'10', 'Formian Myrmarch':'10',
    'Gargantuan Monstrous Scorpion':'10', 'Guardian Naga':'10', 'Legendary Tiger':'10',
    'Nine-Headed Hydra':'10', 'Noble Salamander':'10', 'Psionic Couatl':'10', 'Rakshasa':'10',
    'Red Dragon':'10', 'Silver Dragon':'10', 'White Dragon':'10', 'Barbed Devil':'11',
    'Black Dragon':'11', 'Blue Dragon':'11', 'Cauchemar Nightmare':'11', 'Cloud Giant':'11',
    'Colossal Monstrous Spider':'11', 'Copper Dragon':'11', 'Devourer':'11', 'Dread Wraith':'11',
    'Elder Air Elemental':'11', 'Elder Earth Elemental':'11', 'Elder Fire Elemental':'11',
    'Elder Water Elemental':'11', 'Gold Dragon':'11', 'Green Dragon':'11', 'Harpy Archer':'11',
    'Hezrou':'11', 'Hill Giant Dire Wereboar':'11', 'Retriever':'11', 'Stone Golem':'11',
    'Ten-Headed Hydra':'11', 'Troll Hunter':'11', 'Twelve-Headed Hydra':'11',
    'Abyssal Greater Basilisk':'12', 'Brass Dragon':'12', 'Bronze Dragon':'12', 'Colossal Monstrous Scorpion':'12',
    'Elder Black Pudding':'12', 'Eleven-Headed Hydra':'12', 'Frost Worm':'12', 'Kolyarut':'12',
    'Kraken':'12', 'Leonal':'12', 'Psion-Killer':'12', 'Purple Worm':'12', 'Roper':'12', 'White Dragon':'12',
    'Celestial Charger':'13', 'Force Dragon':'13', 'Ghaele':'13', 'Glabrezu':'13',
    'Golden Protector':'13', 'Green Dragon':'13', 'Ice Devil':'13', 'Iron Golem':'13',
    'Red Dragon':'13', 'Silver Dragon':'13', 'Storm Giant':'13', 'Thought Slayer':'13',
    'Twelve-Headed Hydra':'13', 'Astral Deva':'14', 'Black Dragon':'14', 'Blue Dragon':'14',
    'Copper Dragon':'14', 'Gold Dragon':'14', 'Nalfeshnee':'14', 'Nightwing':'14', 'Prismatic Dragon':'14',
    'Trumpet Archon':'14', 'Werewolf Lord':'14', 'Brass Dragon':'15', 'Bronze Dragon':'15',
    'Marut':'15', 'Mummy Lord':'15', 'Neothelid':'15', 'Red Dragon':'15', 'Silver Dragon':'15',
    'White Dragon':'15', 'Black Dragon':'16', 'Blue Dragon':'16', 'Copper Dragon':'16',
    'Gold Dragon':'16', 'Greater Stone Golem':'16', 'Green Dragon':'16', 'Horned Devil':'16',
    'Hound Archon Hero':'16', 'Nightwalker':'16', 'Planetar':'16', 'Prismatic Dragon':'16',
    'Aboleth Mage':'17', 'Brass Dragon':'17', 'Bronze Dragon':'17', 'Formian Queen':'17',
    'Frost Giant Jarl':'17', 'Marilith':'17', 'White Dragon':'17',
    'Behemoth Eagle':'18', 'Black Dragon':'18', 'Blue Dragon':'18', 'Green Dragon':'18',
    'Nightcrawler':'18', 'Red Dragon':'18', 'Silver Dragon':'18', 'White Dragon':'18',
    'Behemoth Gorilla':'19', 'Black Dragon':'19', 'Blue Dragon':'19', 'Brass Dragon':'19',
    'Bronze Dragon':'19', 'Copper Dragon':'19', 'Force Dragon':'19', 'Gold Dragon':'19',
    'Green Dragon':'19', 'White Dragon':'19', 'Balor':'20', 'Black Dragon':'20',
    'Brass Dragon':'20', 'Bronze Dragon':'20', 'Copper Dragon':'20', 'Pit Fiend':'20',
    'Red Dragon':'20', 'Silver Dragon':'20', 'Tarrasque':'20'}
    #Source: http://www.dandwiki.com/wiki/SRD:Creatures_by_CR
    #Dictionaries for CRs
    #Lvl:exp
    global cr1;cr1 = {1:300, 2:300, 3:300, 4:300, 5:300, 6:300, 7:263, 8:200}
    global cr2; cr2 = {1:600, 2:600, 3:600, 4:600, 5:500, 6:450, 7:350, 8:300, 9:225}
    global cr3; cr3 = {1:900, 2:900, 3:900, 4:800, 5:750, 6:600, 7:525, 8:400, 9:388, 10:250}
    global cr4; cr4 = {1:1350, 2:1350, 3:1350, 4:1200, 5:1000, 6:900, 7:700, 8:600, 9:450, 10:375, 11:275}
    global cr5; cr5 = {1:1800, 2:1800, 3:1800, 4:1600, 5:1500, 6:1200, 7:1050, 8:800, 9:675, 10:500, 11:413, 12:300}
    global cr6; cr6 = {1:2700, 2:2700, 3:2700, 4:2400, 5:2250, 6:1800, 7:1400, 8:1200, 9:900, 10:750, 11:550, 12:450, 13:325}
    global cr7; cr7 = {1:3600, 2:3600, 3:3600, 4:3200, 5:3000, 6:2700, 7:2100, 8:1600, 9:1350, 10:1000, 11:825, 12:600, 13:488, 14:350}
    global cr8; cr8 = {1:5400, 2:5400, 3:5400, 4:4800, 5:4500, 6:3600, 7:3150, 8:2400, 9:1800, 10:1500, 11:1100, 12:900, 13:650, 14:525, 15:375}
    global cr9; cr9 = {1:7200, 2:7200, 3:7200, 4:6400, 5:6000, 6:5400, 7:4200, 8:3600, 9:2700, 10:2000, 11:1650, 12:1200, 13:975, 14:788, 15:563, 16:400}
    global cr10; cr10 = {1:10800, 2:10800, 3:10800, 4:9600, 5:9000, 6:7200, 7:6300, 8:4800, 9:4050, 10:3000, 11:2200, 12:1800, 13:1300, 14:1050, 15:844, 16:600, 17:425}
    global cr11; cr11 = {4: 12800, 5:12000, 6:10800, 7:8400, 8:7200, 9:5400, 10:4500, 11:3300, 12:2400, 13:1950, 14:1400, 15:125, 16:800, 17:638, 18:450}
    global cr12; cr12 = {5:18000, 6:14400, 7:12600, 8:9600, 9:8100, 10:6000, 11:4950, 12:3600, 13:2600, 14:2100, 15:1500, 16:1200, 17:850, 18:675, 19:475}
    global cr13; cr13 = {6:21600, 7:16800, 8:14400, 9:10800, 10:9000, 11:6600, 12:5400, 13:3900, 14:2800, 15:2250, 16:1600, 17:1275, 18:900, 19:713, 20:500}
    global cr14; cr14 = {7:25200, 8:19200, 9:16200, 10:1200, 11:9900, 12:7200, 13:5850, 14:4200, 15:3000, 16:2400, 17:1700, 18:1350, 19:950, 20:750}
    global cr15; cr15 = {8:28800, 9:21600, 10:18000, 11:13200, 12:10800, 13:7800, 14:6300, 15:450, 16:3200, 17:2550, 18:1800, 19:1425, 20:1000}
    global cr16; cr16 = {9:32400, 10:24000, 11:19800, 12:14400, 13:11700, 14:8400, 15:6750, 16:4800, 17:3400, 18:2700, 19:1900, 20:1500}
    global cr17; cr17 = {10:36000, 11:26400, 12:21600, 13:15600, 14:12600, 15:9000, 16:7200, 17:5100, 18:3600, 19:2850, 20:2000}
    global cr18; cr18 = {11:39600, 12:28800, 13:23400, 14:16800, 15:13500, 16:9600, 17:7650, 18:5400, 19:3800, 20:3000}
    global cr19; cr19 = {12:43200, 13:31200, 14:25200, 15:18000, 16:14400, 17:10200, 18:8100, 19:5700, 20:4000}
    global cr20; cr20 = {13:46800, 14:33600, 15:27000, 16:19200, 17:15300, 18:10800, 19:8550, 20:6000}
    global crExp; crExp = {1:cr1, 2:cr2, 3:cr3, 4:cr4, 5:cr5, 6:cr6, 7:cr7, 8:cr8, 9:cr9, 10:cr10, 11:cr11, 12:cr12, 13:cr13, 14:cr14, 15:cr15, 16:cr16, 17:cr17, 18:cr18, 19:cr19, 20:cr20}

    def calcExp(monster, partyLvl, partyNum):
        partyLvl = int(partyLvl)
        partyNum = int(partyNum)
        m = monster
        if m in monsters:
            cr = monsters.get(m, "Unknown")
            cr = float(cr)
            if cr > 1:
                if partyLvl > (cr + 7):
                    print("Error: level difference too great")
                    finalExp = 0
                else:
                    crDict = crExp.get(cr, "error") #maybe add what to on "error"?
                    totalExp = crDict.get(partyLvl, 0)
                    finalExp = totalExp / partyNum
                    print("EXP per player is " + str(finalExp))
            elif cr < 1:
                if partyLvl > 8:
                    print("Error: level difference too great")
                    finalExp = 0
                else:
                    crDict = cr1
                    totalExp = crDict.get(partyLvl, 0) * cr
                    finalExp = totalExp / partyNum
        else:
            print("I don't know that monster.  Try a manual override (expmanual)")
        return finalExp
