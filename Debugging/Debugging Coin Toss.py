import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss_N = random.randint(0, 1)

if toss_N==0:
    toss = "heads"
else:
    toss = "tails"


if toss == guess:                   ##Equating string with an integer
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()                 ##Spelling of guess
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
