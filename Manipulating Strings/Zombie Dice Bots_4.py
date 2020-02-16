import zombiedice

class MyZombie:
    def __init__(self, name):
        
        self.name = name

    def turn(self, gameState):
       

        diceRollResults = zombiedice.roll() 
       
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun > 2 or len(diceRollResults['rolls'])>4:
                break
            else:
                diceRollResults = zombiedice.roll()
                

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
)

zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
