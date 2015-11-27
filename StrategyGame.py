#######Team 4 Strategy Game#######
#      William Gillihan          #
#      Christopher Dixon         #
#      Wendy Gray                #
#      Brian Begun               #
#                                #
#      ver 1.0.0                 #
#      11_26_2015                #
##################################

#StrategyGame.py
#Main File
#Theme: Star Wars
#
#Object of the game:
#Travel from planet to planet
#Look for the secret plants to the Death Star
#Find the Princess (Who is locked up on the Death Star
#Escape before you run our of turns!

#Put all imports here please
import random

# get choice function - usersChoice = getChoice(1) for destination number ect
def getChoice(num):
  if num == 1:
    choice = requestString("What is the number of your next destination choice?")
  if num == 2:
    choice = requestString("Do you want to pick up the plans? y or n")
  if num == 3:
    choice = requestString("Do you want to rescue the Princess? y or n")
  if num == 4:
    choice = requestString("Do you want to quit the game? y or n")
  return choice          

              
#Randomize int numbers to pick room to hide plans in
#Hard coded range: 2-8
#IMPORTANT NOTE: To use this in your function put the following line of code in there
#plansRoom, deathStarRoom = randomizeRooms()
#then you can use each variable separately
def randomizeRooms():
  plansRoom = random.randint(2, 8)
  deathStarRoom = random.randint(2, 8)
  
  while plansRoom == deathStarRoom:
    deathStarRoom = random.randint(2, 8)
   
  return (plansRoom, deathStarRoom
