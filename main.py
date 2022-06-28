import random
import os
from turtle import clear
import time
import sys

coins = 0
level = 0

#shops

def changecharacter1(): 
    global coins
    os.system('clear')
    print("Level:",level)
    print("coins: $", coins)
    chosen = int(input("you reach a tavern and you can change your character [name, shield, health, damage, heal] \n 1 = $500 Jack, 0, 100, 20, 10 \n 2 = $500 Billy, 0, 100, 10, 15 \n 3= $500 Wizas, 0, 75, 15, 20 \n or exit = 0 \n"))

    if chosen == 1:
        if coins < 500:
            print("not enough coins")
            time.sleep(1)
            changecharacter1()
        else:
            print("")
            delay_print("you chose Jack")
            player = Player("Jack", 0, 100, 20, 10)
            character = "Jack"
            coins -= 500
            print("")
            print("coins: $", coins)
            time.sleep(2)
        
            

    elif chosen == 2:
        if coins < 500:
            print("not enough coins")
            time.sleep(1)
            changecharacter1()
        else:
            print("")
            delay_print("you chose Billy")
            player = Player("Billy", 0, 100, 10, 15)
            character = "Billy"
            coins -= 500
            print("")
            print("coins: $", coins)
            time.sleep(2)

    elif chosen ==  3:
        if coins < 500:
            print("not enough coins")
            time.sleep(1)
            changecharacter1()           
        else:
            print("")
            delay_print("you chose Wizas")
            player = Player("Wizas", 0, 75, 15, 20)
            character = "Wizas"
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
        changecharacter1()
    os.system('clear')

def changecharacter2():
    global coins
    os.system('clear')
    print("Level:",level)
    print("coins: $", coins)
    chosen = int(input("you reach a tavern and you can change your character [name, shield, health, damage, heal] \n 1 = $1000 James, 0, 120, 30, 12 \n 2 = $1000 Bruno, 0, 140, 10, 25 \n 3= $1000 William, 0, 100, 20, 20 \n or exit (the shop) = 0 \n"))

    if chosen == 1:
        if coins < 1000:
            print("not enough coins")
            time.sleep(1)
            changecharacter2()
        else:
            print("")
            delay_print("you chose James")
            player = Player("James", 0, 120, 30, 11)
            character = "James"
            coins -= 1000
            print("")
            print("coins: $", coins)
            time.sleep(2)
        
            

    elif chosen == 2:
        if coins < 1000:
            print("not enough coins")
            time.sleep(1)
            changecharacter2()
        else:
            print("")
            delay_print("you chose Bruno")
            player = Player("Bruno", 0, 140, 10, 25)
            character = "Bruno"
            coins -= 1000
            print("")
            print("coins: $", coins)
            time.sleep(2)

    elif chosen ==  3:
        if coins < 1000:
            print("not enough coins")
            time.sleep(1)
            changecharacter2()           
        else:
            print("")
            delay_print("you chose William")
            player = Player("William", 0, 100, 20, 20)
            character = "William"
            coins -= 1000
            print("")
            print("coins: $", coins)
            time.sleep(2)
    
    elif chosen == 0:
        print("exited")
        time.sleep(3)
    
    else:
        print("invalid input")
        time.sleep(1)
        changecharacter2()
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
        if retry.upper() == "Y":
            battle(Player, Opponent)
        elif retry.upper() == "N":
            exit
    elif Opponent.health <= 0:
        print("")
        delay_print ("You have won the match, moving on...")
        coins =+ 500
        level =+ 0.5
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

changecharacter1()

secondDir = int(input("You leave the tavern and reach a fork in the road, the left leads to a cave and the right leads to a river \n 1 = left \n 2 = right \n"))

if secondDir == 1:
    os.system('clear')
    delay_print ("You turn left into the cave")
    print("")
    item = int(input("What item do you pick up? \n 1 = torch (increses health) \n 2 = pickaxe (increses damnage) \n"))
    if item == 1:
        delay_print ("you chose the torch...")
        tool = "torch"
        Player.health =+ 20
    
    if item == 2:
        delay_print ("you chose the picaxe...")
        tool = "picaxe"
        Player.damage =+ 10
    time.sleep(3)
    os.system('clear')
    delay_print ("you walk further down the cave when....")
    print("")
    print("A ROCK GOLEM RISES FROM THE GROUD AND GRABS YOUR FOOT!!!")
    opponent = Opponent("Rock_Golem", 150, 200, 25, 20)

    battle(player, opponent)
    os.system('clear')
    delay_print ("CONGRADULATIONS ON defeating the rock golem!!")
   
elif secondDir == 2:
    os.system('clear')
    delay_print ("You turn right towards the river")
    print("")
    item = int(input("What item do you pick up? \n 1 = water proof jacket (increses health) \n 2 = spear (increses damnage) \n"))
    if item == 1:
        delay_print ("you chose the water proof jacket...")
        tool = "water proof jacket"
        Player.health =+ 20
    
    if item == 2:
        delay_print ("you chose the spear...")
        tool = "spear"
        Player.damage =+ 10
    time.sleep(3)
    os.system('clear')
    delay_print("you walk towards the river when....")
    print("")
    print("SUDDENLY A SEA SERPENT comes out of the river and begins to fire boiling water at you")
    opponent = Opponent("Sea_Serpent", 100, 80, 35, 10)

    battle(player, opponent)
    

    os.system('clear')
    delay_print ("CONGRADULATIONS ON defeating the Sea Serpent!!")

coins =+ 500





    
    
