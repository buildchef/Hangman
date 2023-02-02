import random
import os 
os.system('cls')

with open('random_words.txt', 'r') as file:
    list = file.read().split()
    var1 = random.choice(list)
   
print(var1)


if __name__ == '__main__':
    ...