import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input();
if answer == number1 + number2: # This is example of a semantic error. The code does not fail to run (proper syntax). It also does not crash (functional runtime).
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))
