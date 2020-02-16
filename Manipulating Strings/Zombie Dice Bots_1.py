import zombiedice
import random
class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            a=random.randint(0,1)

            if a ==1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    
)


zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
