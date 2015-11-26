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

# get choice function
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
#Also use to determine what room leads to secret room
#Hard coded range: 2-8
def randomizeRoom():
  randomNum = random.randint(2, 8)
  return (randomNum)
