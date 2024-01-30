import random

max_range = int(input('configure max number[range is from 1 to your number] '))

number = random.choice(range(1, max_range + 1))
print(number)

chances = int(input('how many chances you want to have?'))
while True:
    guess = int(input(f'guess the number, from 1 to {max_range} \n'))
    if guess == number:
        print('you guessed correctly. Congratulations')
        break
    elif guess > number:
        print('Bad guess. The number you guessed is too high \n')
        chances = chances - 1
        print(f'you have {chances} chances left')
    elif guess < number:
        print('Bad guess. The number you guessed is too low \n')
        chances = chances - 1
        print(f'you have {chances} chances left')
    if chances == 0:
        print(f'you lost because you ran out of the chances :/ number was {number}')
        break
    