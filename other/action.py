import os
print('hello')
print('hello')
print('hello')
print('hello')
clear = lambda: os.system("cls")
print('hello')

from replit import clear
from os import system, name 
#HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)

name = input("What is your name?")
price = input("What is your bid price?")

bids = {
  name:price
}

other = input("is there other users who want to bid?")

if other == 'yes':
  clear()