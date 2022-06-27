import random
import os
from turtle import clear
import time
import sys

coins = 0

#shop
def changecharacter(): 
    global coins
    os.system('clear')
    print("coins: $", coins)
    chosen = int(input("you reach a tavern and you can change your character [name, shield, health, damage, heal] \n 1 = $500 Jack, 0, 100, 20, 10 \n 2 = $500 Billy, 0, 100, 10, 15 \n 3= $500 Wizas, 0, 75, 15, 20 \n or exit = 0 \n"))

    if chosen == 1:
        if coins < 500:
            print("not enough coins")
            time.sleep(1)
            changecharacter()
        else:
            print("")
            delay_print("you chose Jack")
            player = Player("Jack", 0, 100, 20, 10)
            coins -= 500
            print("")
            print("coins: $", coins)
            time.sleep(2)
        
            

    elif chosen == 2:
        if coins < 500:
            print("not enough coins")
            time.sleep(1)
            changecharacter()
        else:
            print("")
            delay_print("you chose Billy")
            player = Player("Billy", 0, 100, 10, 15)
            coins -= 500
            print("")
            print("coins: $", coins)
            time.sleep(2)

    elif chosen ==  3:
        if coins < 500:
            print("not enough coins")
            time.sleep(1)
            changecharacter()           
        else:
            print("")
            delay_print("you chose Wizas")
            player = Player("Wizas", 0, 75, 15, 20)
            coins -= 500
            print("")
            print("coins: $", coins)
            time.sleep(2)
    
    elif chosen == 0:
        print("exited")
        time.sleep(3)
    
    else:
        print("invalid input")
        time.sleep(1)
        changecharacter()
    os.system('clear')

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

class Player:
    def __init__(self, name, shield, health, damage, heal):
        self.name = name
        self.shield = shield
        self.health = health
        self.damage = damage
        self.heal = heal
        
class Opponent: 
    def __init__(self, name, shield, health, damage, heal):
        self.name = name
        self.shield = shield
        self.health = health
        self.damage = damage
        self.heal = heal


def battle(Player, Opponent):

    while Player.health and Opponent.health > 0:
        print("")
        time.sleep(1)
        os.system('clear')
        delay_print (f"Your health: {Player.health} \nOpponent health: {Opponent.health}")
        print("")
        enemy_move = random.randint(1,2)
        round_attack = int(input("Pick your move, \n 1 = Punch \n 2 = Heal \n-> "))

        if round_attack == 1:
            if enemy_move == 1:
                delay_print ("You chose punch \nOpponent chose punch ")
                Opponent.health -= player.damage
                Player.health -= opponent.damage
                print("")
        
            elif enemy_move == 2: 
                delay_print ("You chose punch \nOpponent chose heal")
                Opponent.health += opponent.heal
                Opponent.health -= player.damage
        
        elif round_attack == 2:
            if enemy_move == 1:
                delay_print ("You chose healing \nOppponent chose punch ")
                Player.health += player.heal
                Player.health += opponent.damage
            
            elif enemy_move == 2:
                delay_print ("You chose healing \nOpponent chose healing")
                Player.health += player.heal
                Opponent.health += opponent.heal
        else:
            print('invalid number, please choose "1" for punch or "2" for heal ')
    if Player.health <= 0:
        print("")
        delay_print ("You have been defeated, the game is over")
        print("")
        retry = input("retry (Y/N)?")
        if retry == "Y":
            battle(Player, Opponent)
        elif retry == "N":
            exit
    elif Opponent.health <= 0:
        print("")
        delay_print ("You have won the match, moving on...")
        coins =+ 500
    elif Opponent.health and Player.health <= 0:
        print("")
        delay_print ("It's a draw, you have been defeated, the game is over")
        print("")
        retry = input("retry (Y/N)?")
        if retry == "Y":
            battle(Player, Opponent)
        elif retry == "N":
            exit

    
#Beginning of the game 
os.system('clear')
time.sleep(0.5)
delay_print ("Welcome to 'The Adventure'! \n")
time.sleep(1)

#Choosing Character -- 

character = random.randint(1,3)

if character == 1:
    delay_print ("You have landed with Jack, he specialises in damage"); 
    player = Player("Jack", 0, 100, 20, 10)
    
    
elif character == 2:
    delay_print ("You have landed with Billy, he specialises in shields"); 
    player = Player("Billy", 0, 100, 10, 15)
    

elif character == 3:
    delay_print ("You have landed with Wizas, he is an all-rounder"); 
    player = Player("Wizas", 0, 75, 15, 20)
   

#Choosing Enemy --

opponent = Opponent("Monster", 100, 100, 20, 10)
time.sleep(1)
print("")
print("You enter the forest")
firstDir = int(input("Do you want to take a left, or right, or go straight down the middle? \n 1 = Left, \n 2 = Right, \n 3 = Middle \n-> "))

if firstDir == 1:
    delay_print ("You turn towards the left, and see a monster in the corner of your eye")
    time.sleep(0.5)
    print("")
    print("It runs towards you!!!")

    battle(player, opponent)

elif firstDir == 2:
    delay_print ("You turn towards the right, and are greeted by a monster standing right in front of you")

    battle(player, opponent)

elif firstDir == 3:
    delay_print ("You go down the center")
    print("")
    delay_print ("You walk over the bridge and continue on")
    print("")
    print("NOT!!")
    delay_print ("you accidentally fall into the water and are attacked by a MONSTER")

    battle(player, opponent)

elif firstDir == 10:
    print("continuing")
    
print("")
delay_print("CONGRATULATIONS on completing your first battle")

changecharacter()
