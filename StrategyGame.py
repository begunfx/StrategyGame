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
   
  return (plansRoom, deathStarRoom)
# initialize gameState array
plansRoom, deathStarRoom = randomizeRooms()
gameState = [false,false,6,plansRoom,deathStarRoom]
# start game
room1(gameState)
# exit function
def exit():
  printNow("Loser, The Force was not with you!!!")
  return
# get choice function
def getChoice(num):
  if num == 1:
    choice = requestString("What is the number of your next destination choice? ")
  if num == 2:
    choice = requestString("Do you want to pick up the plans? y or n")
  if num == 3:
    choice = requestString("Do you want to rescue the Princess? y or n")
  if num == 4:
    choice = requestString("Do you want to quit the game? Type X to quit")
  return choice
#############################################
# room one (Naboo) function #################
#############################################
def room1(gameState):
  check = true
  ################### Introduction ####################
  rmDesc = "------------ Naboo Spaceport -----------\n"
  rmDesc += "You have arrived at the Naboo Spaceport.\n"
  rmDesc += "Naboo is a small pastoral world located\n"
  rmDesc += "near the border of the Outer Rim Territories.\n"
  rmDesc += "It is inhabited by two societies - an indigenous\n"
  rmDesc += "species of intelligent amphibians called the Gungans, and\n"
  rmDesc += "a group of peaceful humans who are referred to as the Naboo.\n" 
  rmDesc += "Destination choices are: \n2 for Coruscant, 3 for Tatooine, 4 for Alderaan, or X for exit.\n"
  printNow (rmDesc)
  if(gameState[0]==true and gameState[1]==true): #has plans and princess
    printNow("\nCongratulations, You Have Rescued the Princess and brought her to safety")
    printNow("May the Force be with you!!!")
    check = false
  if(gameState[3]==1 and gameState[0]== false and gameState[1] == false):# found plan room
    printNow("\nYou have found the plan room, please take plans to save the Princess!")
    picPln = getChoice(2).lower()
    if picPln == "y":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
  if(gameState[4]==1 and gameState[0]== true and gameState[1] == false): # found deathstar and already has plans
    printNow("\nYou have found the DeathStar, please save the Princess!!!")
    svPrncs = getChoice(3).lower()
    if svPrncs == "y": # if they want to save princess
      gameState[1] = true
      printNow("\nYou have the Princess, \nhead for the exit, \nMay The Force be With You!")
  # destination choice loop
  while check == true:
    chc = getChoice(1)
    choice = 0
    if chc.isdigit():
      choice = int(chc)
    else:
      chc = chc.lower()
    if choice == 2: # for Coruscant
      check = false
      room2(gameState)
    elif choice == 3: # for Tatooine
      check = false
      room3(gameState)
    elif choice == 4: # for Alderan
      check = false
      room4(gameState)
    elif chc == "x":
      exit()
      check = false
    else:
      printNow("You cannot get to destination "+ chc +" from here, Try 2, 3, or 4.")
      check = true
#################################################
# room two (Coruscant) function #################
#################################################
def room2(gameState):
  check = true
  ################### Introduction ####################
  rmDesc = "------------ Coruscant Spaceport -----------\n"
  rmDesc += "You have arrived at the Coruscant Spaceport.\n"
  rmDesc += "Coruscant is the vibrant heart and capital of the galaxy.\n"
  rmDesc += "Coruscant was originally called Notron, also known\n"
  rmDesc += "as Imperial Center or the Queen of the Core.\n"
  rmDesc += "It is a planet located in the Galactic Core.\n"
  rmDesc += "It is generally agreed that Coruscant is\n"
  rmDesc += "the most politically important world in the galaxy.\n" 
  rmDesc += "Destination choices are: \n1 for Naboo, 4 for Alderaan, 5 for Hoth, 6 for Dagobah, or X for exit.\n"
  printNow (rmDesc)
  if(gameState[0]==true and gameState[1]==true): #has plans and princess
    gameState[2] -= 1 # this is not exit so subtract 1
    if gameState[2]<=0:
      exit()
      check = false
  if(gameState[3]==2 and gameState[1]== false and gameState[1] == false):# found plan room
    printNow("\nYou have found the plan room, please take plans to save the Princess")
    picPln = getChoice(2).lower()
    if picPln == "y":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
  if(gameState[4]==2 and gameState[0]== true and gameState[1] == false): # found deathstar and already has plans
    printNow("\nYou have found the DeathStar, please save the Princess!!!")
    svPrncs = getChoice(3).lower()
    if svPrncs == "y": # if they want to save princess
      gameState[1] = true
      printNow("\nYou have the Princess, \nhead for the exit, \nMay The Force be With You!")
  # destination choice loop
  while check == true:
    chc = getChoice(1)
    choice = 0
    if chc.isdigit():
      choice = int(chc)
    else:
      chc = chc.lower()
    if choice == 1: # for Naboo
      check = false
      room1(gameState)
    elif choice == 4: # for Alderan
      check = false
      room4(gameState)
    elif choice == 5: # for Hoth
      check = false
      room5(gameState)
    elif choice == 6: # for Dagobah
      check = false
      room6(gameState)
    elif chc == "x":
      exit()
      check = false
    else:
      printNow("You cannot get to destination "+ chc +" from here, Try 2, 3, or 4.")
      check = true
