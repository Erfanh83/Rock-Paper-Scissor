#Packages
from random import random
import math

#Root(Base) variables and prints
choices = ("rock","paper","scissor")
computer_choice = choices[math.floor(random() * 3)]

print(f"--------- Welcome to our (Rock, Paper, Scissor) game ---------")

ready = input("Are you ready to start (y/n) ? ")
