import os
from random import randint

names = []
scores = []
words = ["deal","power","shape","eaten","drank","apple","grind","it\'s"]
points = -1
players = int(input('player count? (2 to 8)'))
rounds = round(16/players)
word_chain = ''

def clear_console():
 os.system('cls' if os.name == 'nt' else 'clear')

def fancy_exit(reason):
 input(f'{reason}\npress enter to exit the program.')
 exit()

if players < 2 or players > 8:
 fancy_exit('invaild player count')
 
for i in range (players):
 scores.append(0)
 names.append(input(f'player {i+1}\'s name?'))
 clear_console()

for i in range (players*rounds):
 last_word = word if points > -1 else words[randint(0,7)]
 word_chain.join(last_word)
 player_up = i % players
 print(f'{names[player_up]} is up!')
 print(f'round {i//players + 1} out of {rounds}')
 word = input(last_word)
 for j in range (players):
  if not(j == player_up):
   like = input(f'{names[j]}, do you like it? (y/n):')
   points =+ (1 if like == 'y' else -1)
 scores[player_up] += points
 clear_console()

highest = -99
for j in range (players):
 highest = scores[j] if scores[j] > highest else highest
for j in range (players):
 print(names[j] if scores[j] == highest else '')

print(f'highest score: {highest}')
fancy_exit(f'the word chain you all made:\n{word_chain}')