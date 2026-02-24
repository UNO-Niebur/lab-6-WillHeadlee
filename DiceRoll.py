#DiceRoll.py
#Name: William Headlee
#Date: 2/24/26
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
  #find the sum total of the two dice
    sum = dice1 + dice2
    rolls[sum - 2] = rolls[sum - 2] + 1
  #print statictics for dice rolls
  dice = 2
  for r in rolls:
    print(dice, ":", rolls[dice - 2], "\t", rolls[dice - 2]*"|")
    dice += 1


if __name__ == '__main__':
  main()
