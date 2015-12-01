#######Team 4 Strategy Game#######
#      William Gillihan          #
#      Christopher Dixon         #
#      Wendy Gray                #
#      Brian Begun               #
#                                #
#      ver 12.18.15              #
#      11_26_2015                #
##################################

#StrategyGame.py
#Main File
#Theme: Star Wars
#
#Object of the game:
#Travel from planet to planet
#Look for the secret plans to the Death Star
#Find the Princess (Who is locked up on the Death Star
#Escape before you run our of turns!

# #Put all imports here please
# import random

# Star Wars game function
def starWars():
  plansRoom = random.randint(2, 8)  
  gameState = [false, plansRoom]
  help()
  naboo(gameState)

# exit function
def exit():
  printNow("Loser, The Force was not with you!!!")
  return

  # help function
def help():
  printNow("A long time ago in a Galaxy far, far away...\n")
  printNow("It is a time of great unrest as the evil Galactic Empire")
  printNow("continues to conquer, ensalve and ravage the free planets of")
  printNow("the galaxy. However, small bands of rebels have banded together") 
  printNow("to fight the tyranny of the Empire and seek to restore the freedom and") 
  printNow("justice known under the Old Republic. Unbeknownst to all, on the planet")
  printNow("Naboo, a lone rebel seeks to obtain and deliver plans of a new, terrible") 
  printNow("weapon created to crush the last vestiges of hope in the galaxy...")
  printNow("Welcome to the Star Wars Galaxy.  You will be able to explore eight worlds in this galaxy.")  
  printNow("On each world, you may jump to other select worlds by typing in one of the choices given.")
  printNow("You need to pick up the plans, find the princess and return Naboo to win the game.\n")
  printNow("Type help at any time to redisplay this introduction.")
  printNow("Type exit to quit the game at any time.\n")

#############################################
# room one (Naboo) function #################
#############################################
def naboo(gameState):
  check = true
  ################### Introduction ####################
  rmDesc = "------------ Naboo Spaceport -----------\n"
  rmDesc += "You have arrived at the Naboo Spaceport.\n"
  rmDesc += "Naboo is a small pastoral world located\n"
  rmDesc += "near the border of the Outer Rim Territories.\n"
  rmDesc += "It is inhabited by two societies - an indigenous\n"
  rmDesc += "species of intelligent amphibians called the Gungans, and\n"
  rmDesc += "a group of peaceful humans who are referred to as the Naboo.\n" 
  rmDesc += "Destination choices are: \n Coruscant, Tatooine, Alderaan, or EXIT to quit.\n"
  printNow (rmDesc)
  ############## this scenario is unlikely since Naboo is the entrance/exit planet (added for possible future change) #############
  if(gameState[0]== false and gameState[1] == 1):# found plan room
    fndPlns = "\nHowever, before you take off, Valenthyne Farfalla\n"
    fndPlns += "catches up to tell you that the Bothans have succeeded in\n"
    fndPlns += "bribing a high-ranking Imperial officer into allowing them\n"
    fndPlns += "to infiltrate a slicer droid into the Coruscant computer network\n"
    fndPlns += "and have located and copied the plans of the Death Star layout.\n"
    fndPlns += "He has just arrived at Naboo to give you the plans personally.\n"
    fndPlns += "He asks you to take them to use in your mission to rescue Princess Leia.\n\n"
    printNow(fndPlns)
    pPln = "Type \"Pickup Plans\" to pick up the plans from the Jedi Master\n"
    pPln += "Type \"HELP\" for game info.\n"
    pPln += "or just Type \"EXIT\" to quit.\n"
    picPln = requestString(pPln)
    picPln = picPln.lower()
    if picPln == "help": # for game info
      help()
      picPln = requestString(pPln)
      picPln = picPln.lower()      
    if picPln == "pickup plans": # pickup plans
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
    elif picPln == "exit": # to exit
      exit()
      check = false
    else:
      printNow("\nYou have failed to pickup the plans.\nReturn later and try again.\n")
###################################################### Destination Choice Loop #################################################	  
  # destination choice loop
  while check == true:
    dstChc = "What is your destination choice?\n"
    dstChc += "Type \"Coruscant\" to jump to Coruscant\n"
    dstChc += "Type \"Tatooine\" to jump to Tatooine\n"
    dstChc += "Type \"Alderaan\" to jump to Alderaan\n"
    dstChc += "Type \"Help\" for game info.\n"
    dstChc += "or just Type \"EXIT\" to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "coruscant": # for Coruscant
      check = false
      coruscant(gameState)
    elif choice == "tatooine": # for Tatooine
      check = false
      tatooine(gameState)
    elif choice == "alderaan": # for Alderaan
      check = false
      alderaan(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    else:
      printNow("You cannot get to "+ chc +" from here,\ntry Coruscant, Tatooine, Alderaan, or type EXIT to quit.")
      check = true

#################################################
# room two (Coruscant) function #################
#################################################
def coruscant(gameState):
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
  rmDesc += "Destination choices are: \nNaboo, Alderaan, Hoth, Dagobah, or type EXIT to quit.\n"
  printNow(rmDesc)
################################################# found plan room #################################################
  if(gameState[0]== false and gameState[1] == 2):# found plan room
    fndPlns = "\nHowever, before you take off, Valenthyne Farfalla\n"
    fndPlns += "catches up to tell you that the Bothans have succeeded in\n"
    fndPlns += "bribing a high-ranking Imperial officer into allowing them\n"
    fndPlns += "to infiltrate a slicer droid into the Coruscant computer network\n"
    fndPlns += "and have located and copied the plans of the Death Star layout.\n"
    fndPlns += "He asks you to take them to use in your mission to rescue Princess Leia.\n\n"
    printNow(fndPlns)
    pPln = "Type \"Pickup Plans\" to pick up the plans from the Jedi Master\n"
    pPln += "Type \"HELP\" for game info.\n"
    pPln += "or just Type \"EXIT\" to quit.\n"
    picPln = requestString(pPln)
    picPln = picPln.lower()
    if picPln == "help": # for Help
      help()
      picPln = requestString(pPln)
      picPln = picPln.lower()      
    if picPln == "pickup plans":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
    elif picPln == "exit":
      exit()
      check = false
    else:
      printNow("\nYou have failed to pickup the plans.\nReturn later and try again.\n")
###################################################### Destination Choice Loop #################################################
  # destination choice loop
  while check == true:
    dstChc = "What is your destination choice?\n"
    dstChc += "Type \"Naboo\" to jump to Naboo\n"
    dstChc += "Type \"Alderaan\" to jump to Alderaan\n"
    dstChc += "Type \"Hoth\" to jump to Hoth\n"
    dstChc += "Type \"Dagobah\" to jump to Dagobah\n"
    dstChc += "Type \"Help\" for game info.\n"
    dstChc += "or just Type \"EXIT\" to quit."
    chc = requestString(dstChc)
    if (chc == None):
      chc = "exit"
    if chc.isdigit():
      chc = str(chc)
    choice = chc.lower()
    if choice == "naboo": # for Naboo
      check = false
      naboo(gameState)
    elif choice == "alderaan": # for Alderaan
      check = false
      alderaan(gameState)
    elif choice == "hoth": # for Hoth
      check = false
      hoth(gameState)
    elif choice == "dagobah": # for Dagobah
      check = false
      dagobah(gameState)
    elif choice == "help": # for game info
      help()
    elif chc == "exit": # to exit
      exit()
      check = false
    else:
      printNow("You cannot get to "+ chc +" from here,\ntry Naboo, Alderaan, Hoth, Dagobah, or type EXIT to quit..")
      check = true
