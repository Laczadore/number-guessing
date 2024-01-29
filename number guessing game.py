import random

max_range = int(input('configure max number[range = 1 to your number]'))

number = random.choice(range(1, max_range + 1))
print(number)

chances = 3
while True:
    guess = int(input(f'guess the number, from 1 to {max_range} \n'))
    if guess == number:
        print('you guessed correctly. Congratulations')
        break
    elif guess > number:
        print('Bad guess. The number you guessed is too high \n')
    elif guess < number:
        print('Bad guess. The number you guessed is too low \n')