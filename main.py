import os
from random import randint

names = []
scores = []
words = ["deal","power","shape","eaten","drank","apple","grind","it\'s"]
players = int(input('player count? (2 to 8)'))
word_chain = ''
last_word = words[randint(0,7)]

def clear_console():
 os.system('cls' if os.name == 'nt' else 'clear')

def fancy_exit(reason):
 input(f'{reason}\npress enter to exit the program.')
 exit()

if players < 2 or players > 8:
 fancy_exit('invaild player count')
rounds = round(16/players)

for i in range (players):
 clear_console()
 scores.append(0)
 names.append(input(f'player {i+1}\'s name?'))

for i in range (players*rounds):
 points = 0
 clear_console()
 word_chain = word_chain + last_word
 player_up = i % players
 print(f'{names[player_up]} is up!')
 print(f'round {i//players + 1} out of {rounds}')
 word = input(last_word)
 for j in range (players):
  if not(j == player_up):
   like = input(f'{names[j]}, do you like it? (y/n):')
   points += int(1 if like == 'y' else -1)
 scores[player_up] += points
 last_word = word if points > -1 else words[randint(0,7)]

clear_console()
print('winners:')
highest = -99
for j in range (players):
 highest = scores[j] if scores[j] > highest else highest
for j in range (players):
 if scores[j] == highest:
  print(names[j])

print(f'\nhighest score: {highest}')
fancy_exit(f'the word chain you all made:\n\n{word_chain}')