import os
from random import choice

names = []
scores = []
words = ["deal","power","shape","eaten","drank","apple","grind","it\'s"]
j = int(input('player count? (2 to 8)'))
word_chain = ''
last_word = choice(words)

def clear_console():
 os.system('cls' if os.name == 'nt' else 'clear')

def fancy_exit(reason):
 input(f'{reason}\npress enter to exit the program.')
 exit()

if j < 2 or j > 8:
 fancy_exit('invaild player count')
rounds = round(16/j)

for i in range(j):
 clear_console()
 scores.append(0)
 names.append(input(f'player {i+1}\'s name?'))

for i in range(len(names)*rounds):
 points = 0
 clear_console()
 word_chain.join(last_word)
 player_up = i % len(names)
 print(f'{names[player_up]} is up!')
 print(f'round {i//len(names)+1} out of {rounds}')
 word = input(last_word)
 for j in range (len(names)):
  if not(j == player_up):
   like = input(f'{names[j]}, do you like it? (y/n):')
   points += 1 if like == 'y' else -1
 scores[player_up] += points
 last_word = word if points > -1 else choice(words)

clear_console()
print('winners:')

highest = max(scores)
for i in range (len(names)):
 if scores[i] == highest:
  print(names[i])
print(f'\nhighest score: {highest}')
fancy_exit(f'your word chain:\n\n{word_chain}')