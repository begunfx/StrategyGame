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
#Look for the secret plans to the Death Star
#Find the Princess (Who is locked up on the Death Star
#Escape before you run our of turns!

#Put all imports here please
import random

# Star Wars game function
def starWars():
  randomRooms = randomizeRooms()
  # gameState[0] = hasPlans (true, false)
  # gameState[1] = hasPrincess (true, false)
  # gameState[2] = numTurnsLeft (6, 5, ... , 1, 0)
  # gameState[3] = plansRoom (2, 3, ... , 8) random
  # gameState[4] = deathStarRoom (2, 3, ... , 8) random
  gameState = [false, false, 6, randomRooms[0], randomRooms[1]]
  naboo(gameState)
             
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

# exit function
def exit():
  printNow("Loser, The Force was not with you!!!")
  return

# end function
def end():
  return false

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
  if(gameState[0]==true and gameState[1]==true): ########## has plans and princess and has reached exit, game is won #############
    printNow("\nCongratulations, You Have Rescued the Princess and brought her to safety")
    printNow("\nHis Highness, Prince Bail Organa thanks you for saving the Princess!!!")
    printNow("\nThe Force is with with you!!!\n")
    check = end()
  ############## this scenario is unlikely since Naboo is the entrance/exit planet (added for possible future change) #############
  if(gameState[3]==1 and gameState[0]== false and gameState[1] == false):# found plan room
    fndPlns = "\nHowever, before you take off, Valenthyne Farfalla\n"
    fndPlns += "catches up to tell you that the Bothans have succeeded in\n"
    fndPlns += "bribing a high-ranking Imperial officer into allowing them\n"
    fndPlns += "to infiltrate a slicer droid into the Coruscant computer network\n"
    fndPlns += "and have located and copied the plans of the Death Star layout.\n"
    fndPlns += "He has just arrived at Naboo to give you the plans personally.\n"
    fndPlns += "He asks you to take them to use in your mission to rescue Princess Leia.\n\n"
    printNow(fndPlns)
    picPln = requestString("Type \"Pickup Plans\" to pick up the plans from the Jedi Master\n")
    picPln = picPln.lower()
    if picPln == "pickup plans":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
    else:
      printNow("\nYou have failed to pickup the plans.\nReturn later and try again.\n")
  ############## this scenario is unlikely since Naboo is the entrance/exit planet (added for possible future change) #############
  if(gameState[4]==1 and gameState[0]== true and gameState[1] == false): # found deathstar and already has plans
    dthStrFnd = "\nHowever, you notice that everyone has become extremely nervous\n"
    dthStrFnd += "and you ask why. It turns out that the Death Star has been \n"
    dthStrFnd += "orbiting for the past several hours. You can finally\n"
    dthStrFnd += "rescue Princess Leia!\n\n"
    printNow(dthStrFnd)    
    svPrncs = requestString("Type \"Save Princess\" to jump to the Death Star and rescue Leia\n")
    svPrncs = svPrncs.lower()
    if svPrncs == "save princess": # if they want to save princess
      deathStar(gameState)
    else:
      printNow("\nYou have failed to save the Princess.\nReturn later and try again.\n")
  # destination choice loop
  while check == true:
    dstChc = "What is your destination choice?\n"
    dstChc += "Type \"Coruscant\" to jump to Coruscant\n"
    dstChc += "Type \"Tatooine\" to jump to Tatooine\n"
    dstChc += "Type \"Alderaan\" to jump to Alderaan\n"
    dstChc += "or just Type \"EXIT\" to quit."
    chc = requestString(dstChc)
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
    elif chc == "exit":
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
  if(gameState[0]==true and gameState[1]==true): #has plans and princess, this is not the exit, keep trying if you can.
    gameState[2] -= 1
    if gameState[2] > 1:
      printNow("\nBe Careful! You only have " + str(gameState[2]) + " spacejumps left to outrun the Empire to Naboo!\n")
    elif gameState[2] == 1:
      printNow("\nBe Careful! You only have 1 spacejump left to outrun the Empire to Naboo!\n")
    if gameState[2] == 0:
      printNow("Imperial troops caught up with you en route to Coruscant. You lose.")
      printNow("The Force is not with you.")
      return
  if(gameState[3]==2 and gameState[0]== false and gameState[1] == false):# found plan room
    fndPlns = "\nHowever, before you take off, Valenthyne Farfalla\n"
    fndPlns += "catches up to tell you that the Bothans have succeeded in\n"
    fndPlns += "bribing a high-ranking Imperial officer into allowing them\n"
    fndPlns += "to infiltrate a slicer droid into the Coruscant computer network\n"
    fndPlns += "and have located and copied the plans of the Death Star layout.\n"
    fndPlns += "He asks you to take them to use in your mission to rescue Princess Leia.\n\n"
    printNow(fndPlns)
    picPln = requestString("Type \"Pickup Plans\" to pick up the plans from the Jedi Master\n")
    picPln = picPln.lower()
    if picPln == "pickup plans":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
    else:
      printNow("\nYou have failed to pickup the plans.\nReturn later and try again.\n")
  if(gameState[4]==2 and gameState[0]== true and gameState[1] == false): # found deathstar and already has plans
    dthStrFnd = "\nHowever, you notice that everyone has become extremely nervous\n"
    dthStrFnd += "and you ask why. It turns out that the Death Star has been \n"
    dthStrFnd += "orbiting for the past several hours. You can finally\n"
    dthStrFnd += "rescue Princess Leia!\n\n"
    printNow(dthStrFnd)    
    svPrncs = requestString("Type \"Save Princess\" to jump to the Death Star and rescue Leia\n")
    svPrncs = svPrncs.lower()
    if svPrncs == "save princess": # if they want to save princess
      deathStar(gameState)
    else:
      printNow("\nYou have failed to save the Princess.\nReturn later and try again.\n")
  # destination choice loop
  while check == true:
    dstChc = "What is your destination choice?\n"
    dstChc += "Type \"Naboo\" to jump to Naboo\n"
    dstChc += "Type \"Alderaan\" to jump to Alderaan\n"
    dstChc += "Type \"Hoth\" to jump to Hoth\n"
    dstChc += "Type \"Dagobah\" to jump to Dagobah\n"
    dstChc += "or just Type \"EXIT\" to quit."
    chc = requestString(dstChc)
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
    elif chc == "exit":
      exit()
      check = false
    else:
      printNow("You cannot get to "+ chc +" from here,\ntry Naboo, Alderaan, Hoth, Dagobah, or type EXIT to quit..")
      check = true

#################################################
# room 4 (Alderaan) function
#################################################
def alderaan(gameState):
  check = true
  choiceDescrip = ""
  roomDescrip = "\n--------------- Alderaan Spaceport ---------------\n"
  roomDescrip += "You are at the Spaceport on the lush, \n"
  roomDescrip += "mountainous planet of Alderaan, one of the hubs of the \n"
  roomDescrip += "Rebel Alliance.  You spend some time talking to some rebels\n"
  roomDescrip += "about the best ways to avoid the Empire. Your destination options\n"
  roomDescrip += "are Naboo, Coruscant, Cloud City, and Endor.\n"
  
  cDescrip = "What do you want to do?\n"
  cDescrip += "Type \"Naboo\" to jump to Naboo\n"
  cDescrip += "Type \"Coruscant\" to jump to Coruscant\n"
  cDescrip += "Type \"Cloud City\" to jump to Cloud City\n"
  cDescrip += "Type \"Endor\" to jump to Endor\n"
  
  #if this planet has the plans and you don't already have them, notify
  if gameState[0] == false and gameState[3] == 4:
    roomDescrip += "\nHowever, before you take off, you recieve a transmission\n"
    roomDescrip += "from His Highness, Prince Bail Organa.  He requests to meet\n"
    roomDescrip += "with you immediately in his private quarters.\n"
    
    choiceDescrip = "Type \"Meet Prince\" to see what the Prince has to say\n"
    
  #if you have the plans, no princess, and this is the planet with the Death Star orbiting, notify
  if gameState[0] == true and gameState[1] == false and gameState[4] == 4:
    roomDescrip += "\nHowever, you notice that everyone has become extremely nervous\n"
    roomDescrip += "and you ask why. It turns out that the Death Star has been \n"
    roomDescrip += "orbiting for the past several hours. You can finally\n"
    roomDescrip += "rescue Princess Leia!\n"
    
    choiceDescrip = "Type \"Save Princess\" to jump to the Death Star and rescue Leia\n"
  
  #if you have the plans and princess, notify and deduct turns left
  if gameState[0] == true and gameState[1] == true:
    gameState[2] -= 1
    if gameState[2] > 1:
      roomDescrip += "\nBe Careful! You only have " + str(gameState[2]) + " spacejumps left to outrun the Empire to Naboo!\n"
    elif gameState[2] == 1:
      roomDescrip += "\nBe Careful! You only have 1 spacejump left to outrun the Empire to Naboo!\n"
    if gameState[2] == 0:
      printNow("Imperial troops caught up with you en route to Endor. You lose.")
      printNow("The Force is not with you.")
      return
  
  choiceDescrip = cDescrip + choiceDescrip + "Type \"Exit\" to exit the game\n"
  cDescrip += "Type \"Exit\" to exit the game\n"
  
  printNow(roomDescrip)
  choice = requestString(choiceDescrip)
  
  while check == true:
    if choice == None:
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
      check = false
    else:
      choice = choice.lower()
    if choice == "naboo":
      naboo(gameState)
      check = false
    elif choice == "coruscant":
      coruscant(gameState)
      check = false
    elif choice == "cloud city":
      cloudCity(gameState)
      check = false
    elif choice == "endor":
      endor(gameState)
      check = false
    elif choice == "meet prince" and gameState[0] == false and gameState[3] == 4: #talk to prince
      hasPlans = talkToPrince()
      if hasPlans == 1:
        gameState[0] = true
        printNow("You travel back to the spaceport with all the pieces you need to ")
        printNow("rescue Princess Leia. The next step is to find the Death Star.")
        choice = requestString(cDescrip)
      elif hasPlans == 0:
        printNow("Are you sure you don't want to take the plans?  They would be")
        printNow("very useful!")
        choice = requestString(choiceDescrip)
      else:
        return
    elif choice == "save princess" and gameState[0] == true and gameState[1] == false and gameState[4] == 4:
      deathStar(gameState) #go to death star
      check = false
    elif choice == "exit":
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
      check = false
    else:
      printNow("The nav computer could not interpret your choice. Please try again.")
      choice = requestString(choiceDescrip)
      
# talk to Prince to pick up plans, return 1 if plans picked up, 
#     0 if not picked up, -1 if exit
def talkToPrince():
  check = true
  roomDescrip = "You make your way to the palace and ask directions to His Higness.\n"
  roomDescrip += "He greets you in his private sitting room and locks the door before\n"
  roomDescrip += "pressing a hidden button and revealing a small data drive.  He informs\n"
  roomDescrip += "you that the drive contains the plans for the layout of the Death Star.\n"
  roomDescrip += "He begs you to take it and rescue his daughter, Leia.\n"
  
  choiceDescrip = "What do you want to do?\n"
  choiceDescrip += "Type \"Pickup Plans\" to take the plans from the Prince\n"
  choiceDescrip += "Type \"Ignore\" to ignore the Prince and leave without the plans\n"
  choiceDescrip += "Type \"Exit\" to exit the game\n"
  printNow(roomDescrip)
  
  while check == true:
    choice = requestString(choiceDescrip)
    
    if choice == None:
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return -1
      check = false
    else:
      choice = choice.lower()
    if choice == "ignore":
      return 0
      check = false
    elif choice == "pickup plans":
      return 1
      check = false
    elif choice == "exit":
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return -1
      check = false
    else:
      printNow("The nav computer could not interpret your choice. Please try again.")

#################################################
# room 8 (Endor) function
#################################################
def endor(gameState):
  check = true
  choiceDescrip = ""
  roomDescrip = "\n--------------- Endor Spaceport ---------------\n"
  roomDescrip += "You have arrived at the Spaceport on the forest moon\n"
  roomDescrip += "of Endor. After the Ewoks have refueled the Millenium\n"
  roomDescrip += "Falcon, you're ready to continue your journey.\n"
  roomDescrip += "They tell you that the only planets within range\n"
  roomDescrip += "are Alderaan and Hoth.\n"
  
  cDescrip = "What do you want to do?\n"
  cDescrip += "Type \"Alderaan\" to jump to Alderaan\n"
  cDescrip += "Type \"Hoth\" to jump to Hoth\n"
  
  #if this planet has the plans and you don't already have them, notify
  if gameState[0] == false and gameState[3] == 8:
    roomDescrip += "\nMore importantly, you notice a blue astromech droid\n"
    roomDescrip += "rolling toward you and beeping.  The gold protocol droid\n"
    roomDescrip += "next to him calls for you to wait.\n"
    
    choiceDescrip = cDescrip + "Type \"Droids\" to see what the droids have to say\n"
    
  #if you have the plans, no princess, and this is the planet with the Death Star orbiting, notify
  if gameState[0] == true and gameState[1] == false and gameState[4] == 8:
    roomDescrip += "\nHowever, you notice that everyone has become extremely nervous\n"
    roomDescrip += "and you ask why. It turns out that the Death Star has been \n"
    roomDescrip += "orbiting for the past several hours. You can finally\n"
    roomDescrip += "rescue Princess Leia!\n"
    
    choiceDescrip = cDescrip + "Type \"Save Princess\" to jump to the Death Star and rescue Leia\n"
  
  #if you have the plans and princess, notify and deduct turns left
  if gameState[0] == true and gameState[1] == true:
    gameState[2] -= 1
    if gameState[2] > 1:
      roomDescrip += "\nBe Careful! You only have " + str(gameState[2]) + " spacejumps left to outrun the Empire to Naboo!\n"
    elif gameState[2] == 1:
      roomDescrip += "\nBe Careful! You only have 1 spacejump left to outrun the Empire to Naboo!\n"
    if gameState[2] == 0:
      printNow("Imperial troops caught up with you en route to Endor. You lose.")
      printNow("The Force is not with you.")
      return
  
  choiceDescrip = cDescrip + choiceDescrip + "Type \"Exit\" to exit the game\n"
  cDescrip += "Type \"Exit\" to exit the game\n"
  printNow(roomDescrip)
  
  choice = requestString(choiceDescrip)
  
  while check == true:
    if choice == None:
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
      check = false
    else:
      choice = choice.lower()
    if choice == "alderaan":
      alderaan(gameState)
      check = false
    elif choice == "hoth":
      hoth(gameState)
      check = false
    elif choice == "droids" and gameState[0] == false and gameState[3] == 8: #talk to droids
      hasPlans = talkToDroids()
      if hasPlans == 1:
        gameState[0] = true
        printNow("You now have all the pieces you need to rescue Princess Leia! ")
        printNow("The next step is to find the Death Star.")
        choice = requestString(cDescrip)
      elif hasPlans == 0:
        printNow("Are you sure you don't want to take the plans?  They would be")
        printNow("very useful!")
        choice = requestString(choiceDescrip)
      else:
        return
    elif choice == "save princess" and gameState[0] == true and gameState[1] == false and gameState[4] == 8:
      deathStar(gameState)  #go to death star
      check = false
    elif choice == "exit":
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
      check = false
    else:
      printNow("The nav computer could not interpret your choice. Please try again.")
      choice = requestString(choiceDescrip)

# talk to droids to pick up plans, return 1 if plans picked up, 
#     0 if not picked up, -1 if exit
def talkToDroids():
  check = true
  roomDescrip = "You stop as the droids come up to you and introduce\n"
  roomDescrip += "themselves as R2-D2 and C-3PO.  C-3PO tells you that\n"
  roomDescrip += "they heard of your mission and that R2-D2 holds the plans \n"
  roomDescrip += "for the layout of the Death Star.  He offers them to you.\n"
  
  choiceDescrip = "What do you want to do?\n"
  choiceDescrip += "Type \"Pickup Plans\" to take the plans from the droids\n"
  choiceDescrip += "Type \"Ignore\" to ignore the droids and take off without the plans\n"
  choiceDescrip += "Type \"exit\" to exit the game\n"
  printNow(roomDescrip)
  
  while check == true:
    choice = requestString(choiceDescrip)
    
    if choice == None:
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return -1
      check = false
    else:
      choice = choice.lower()
    if choice == "ignore":
      return 0
      check = false
    elif choice == "pickup plans":
      return 1
      check = false
    elif choice == "exit":
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return -1
      check = false
    else:
      printNow("The nav computer could not interpret your choice. Please try again.")
      
#################################################
# room 9 (Death Star secret room) function
#################################################
def deathStar(gameState):
  check = true
  roomDescrip = "\n--------------- Death Star ---------------\n"
  roomDescrip += "You piggyback the Millenium Falcon to a Star Destroyer to get close \n"
  roomDescrip += "to the Death Star, slip inside through a trash chute, and leave\n"
  roomDescrip += "the Falcon in a deserted maintenance bay.  Then, you \n"
  roomDescrip += "follow the plans to cell block A661, disguised as a maintenance\n"
  roomDescrip += "worker. After stunning all the guards on duty, you throw open the cell\n"
  roomDescrip += "door, make hasty introductions to the startled Princess Leia, and pull\n"
  roomDescrip += "her toward the exit.  \n\nAs the two of you run back to the Falcon, she \n"
  roomDescrip += "tells you that the critical information she obtained during her time\n"
  roomDescrip += "as a prisoner must be given to an official on the planet of Naboo.\n"
  roomDescrip += "She hints at a large reward if you take her there, and you agree.\n\n"
  roomDescrip += "You safely take off aboard the Falcon, but as you clear the surface\n"
  roomDescrip += "of the Death Star, you receive a transmission. The messge\n"
  roomDescrip += "taunts you that although you have successfully escaped now,\n"
  roomDescrip += "the Empire has developed new technology that can track you down\n"
  roomDescrip += "after six spacejumps.  You look over to see the princess with a\n"
  roomDescrip += "grimly determined look on her face.\n"
  
  choiceDescrip = "What do you want to do?\n"
  choiceDescrip += "Type \"Continue\" to keep your promise and finish the mission\n"
  choiceDescrip += "Type \"Exit\" to desert the princess and exit the game\n"
  
  gameState[1] = true
  printNow(roomDescrip)
  
  while check == true:
    choice = requestString(choiceDescrip)
    if choice == None:
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
      check = false
    else:
      choice = choice.lower()
    if choice == "exit":
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
      check = false
    elif choice == "continue" and gameState[4] == 2:
      coruscant(gameState)
      check = false
    elif choice == "continue" and gameState[4] == 3:
      tatooine(gameState)
      check = false
    elif choice == "continue" and gameState[4] == 4:
      alderaan(gameState)
      check = false
    elif choice == "continue" and gameState[4] == 5:
      hoth(gameState)
      check = false
    elif choice == "continue" and gameState[4] == 6:
      dagobah(gameState)
      check = false
    elif choice == "continue" and gameState[4] == 7:
      cloudCity(gameState)
      check = false
    elif choice == "continue" and gameState[4] == 8:
      endor(gameState)
      check = false
    else:
      printNow("The nav computer could not interpret your choice. Please try again.")


#############################################
# room three (Tatooine) function ############
#############################################
def userChoice(roomState, gameState, currentRoom):
  choiceStat = false
  while choiceStat == false:
    userInput = requestString("Make your choice: ")
    if userInput == None:
      printNow("Okay, I guess you want to leave the game...Bye!")
      choiceStat = true
      exit()
    else:
      userInput = userInput.lower()
      if userInput == 'help':
        return('help')
        choiceStat = false
      elif userInput == 'exit':
        printNow("Time to leave.")
        choiceStat = true
        exit()
      elif userInput == 'dagobah' and roomState == 'tatooine':
        printNow("you're off to Dagobah...wooosh!")
        choiceStat = true
        return('dagobah')
      elif userInput == 'cloudcity' and roomState == 'tatooine':
        printNow("you're off to Cloud City...woosh!")
        choiceStat = true
        return('cloudcity')
      elif userInput == 'naboo' and roomState == 'tatooine':
        printNow("you're off to Naboo...woosh!")
        choiceStat = true
        return('naboo')
      elif userInput == 'cantina' and roomState == 'tatooine':
        printNow("I'm thirsty, let's go check out the cantina.")
        choiceStat = true
        return('cantina')
      elif userInput == 'chat' and roomState == 'cantina':
        choiceStat = true 
        return('chat')  
      elif userInput == 'leave' and roomState == 'cantina':
        printNow("\nYou've left the cantina.")
        choiceStat = true
        return('leave')
      elif gameState[4] == currentRoom and roomState == 'cantina':
        printNow("you're off to save the Princess on the Death Star...woosh!")
        choiceStat = true
        return('deathStar')
      else:
        printNow("The nav computer could not interpret your choice. Please try again.")
        choiceStat = false
        
def whereAmI(gameState, roomState, currentRoom):
  options = ""
  roomDescrip = ""
  action = ""
  
  options =  "\n Type help to re-display this introduction."
  options += "\nType exit or cancel the dialog box to quit at any time."
  
  if roomState == 'tatooine':
    roomDescrip =  "\nYou have arrived at Mos Isley Spaceport on Tatooine.  "  
    roomDescrip += "There are space transports currently available to take you to Dagobah, "
    roomDescrip += "Cloud City or Naboo and a cantina nearby."
    if gameState[1] == true:
      action =  "\nSince you found the princess, you'd better hurry to get her home!  "  
      action += "You have a limited amount of turns to do it.  So get moving!"
    elif gameState[0] == true and gameState[1] == false:
      action =  "\nYou have the secret plans, but you might want to check out the Cantina, "
      action += "and see if anyone can help you find the Death Star."
    elif gameState[0] == false and gameState[1] == false:
      action =  "\nSince your mission is to find the secret plans for the Death star, "
      action += "you might want to ask around a little bit and see if anyone can help you."
    action += "\nEnter Dagobah, CloudCity or Naboo to move on to another planet or type "
    action += "Cantina to go into the bar nearby and talk to some locals"
  elif roomState == 'cantina':
    roomDescrip =  "\nYou've entered the local cantina.  "
    roomDescrip += "Strangely enough, the bar is virtually empty.  "
    roomDescrip += "\nAt the moment, only the barkeep is around cleaning drink glasses "
    roomDescrip += "with a scornful look on his face."
    if gameState[1] == true:
      action =  "\nThe princess is looking really pissed at the moment, "
      action += "since you seemed more concerned with hanging out at a bar "
      action += "than getting her to safety."
    elif gameState[0] == true and gameState[1] == false:
      action = "\nYou might want to ask the barkeep if he knows how to get to the Death Star."
    elif gameState[0] == false and gameState[1] == false:
      action = "\nHe's staring right at you.  Now is your chance to ask him for some help."
    action += "\nEnter chat to ask the barkeep a question or type leave to exit the cantina."    
  elif roomState == 'chat':
    roomDescrip = "\nYou say jokingly: \"Hey barkeep, you happen see any secret "
    roomDescrip += "Death Star plans around here?\""
    if gameState[1] == true:
      action =  "\nHe replies: \"Moron, you've got them in your hand, and the "
      action += "princess is right at your side.  "
      action += "If I were you I would get the hell out of here and take her home "
      action += "as quick as possible.\""  
      action += "Completely disgusted with you, the barkeep goes back to cleaning glasses.\n"
    elif gameState[0] == true and gameState[1] == false:
      action =  "\nHe replies: \"Moron, you've got them in your hand.\"  "
      action += "You reply with a look of embarrassment on your face: \"Sorry, I mean "
      action += "do you know of a way to get to the Death Star?\""
      if gameState[4] == currentRoom and gameState[1] == false:
        action += "\n\"You might want to try the exit at the back behind the bar.  "
        action += "It\'s a secret launch pad.  Should take you directly there.  "
        action += "Now leave me alone!\""
      else:
        action += "\n\"Nope, nothing like that 'round here.  "
        action += "Don\'t ask me stupid questions.  Now leave me alone!\""
    elif gameState[0] == false and gameState[1] == false:
      if gameState[3] == currentRoom and gameState[0] == false:
        action += "\n\"You mean these worthless maps?  "
        action += "Some old guy with a lightsaber traded them for a drink.  "
        action += "I took pity on the old drunk and agreed on the trade.  "
        action += "You can have them if you want.  "
        action += "They're just collecting dust back here.\"  "
        action += "He hands you the plans.  What luck!"
      else:
        action =  "\n\"Nope, nothing like that around here.  "
        action += "You may want to check out one of the nearby systems.  "
        action += "Might have better luck.\""
    if gameState[4] == currentRoom and gameState[1] != true:
      action += "\n\nType DeathStar to use the secret launchpad "
      action += "or type leave to exit the bar"
    elif gameState[4] != currentRoom or gameState[1] == true: 
      action += "\nType leave to exit the bar"
    elif gameState[3] != currentRoom or gameState[0] == true: 
      action += "\nType leave to exit the bar"  
  return(options, roomDescrip, action, gameState)
  
  
def dialog(roomState, gameState, currentRoom):

  printNow("\n--------------- Tatooine ---------------")
  if gameState[1] == 1:
    gameState[2] -= 1
    printNow("You have %d of 6 turns remaining\n" % gameState[2])
    
  options = whereAmI(gameState, roomState, currentRoom)[0]
  roomDescrip = whereAmI(gameState, roomState, currentRoom)[1]
  action = whereAmI(gameState, roomState, currentRoom)[2]
  textDisplay =  roomDescrip + action + options
  
  printNow(textDisplay)  

def tatooine(gameState):

  currentRoom = 3
  roomState = 'tatooine'
  #plansRoom, deathStarRoom = randomizeRooms()
  
  dialog(roomState, gameState, currentRoom)
  userResult = userChoice(roomState, gameState, currentRoom)
  while userResult != 'exit' and userResult != None:
    if userResult == 'help':
      dialog(roomState, gameState, currentRoom)
      userResult = userChoice(roomState, gameState, currentRoom)
    if userResult == 'cantina':
      roomState = 'cantina'
      dialog(roomState, gameState, currentRoom)
      userResult = userChoice(roomState, gameState, currentRoom)
    if userResult == 'chat':
      dialog(userResult, gameState, currentRoom)
      userResult = userChoice(roomState, gameState, currentRoom)
    if userResult == 'leave':
      roomState = 'tatooine'
      dialog(roomState, gameState, currentRoom)
      userResult = userChoice(roomState, gameState, currentRoom)
    if userResult == 'chat' and gameState[3] == currentRoom:
      gameState[1] = true
    if userResult == 'dagobah':
      dagobah(gameState)
      userResult = 'exit'
    elif userResult == 'cloudcity':
      cloudCity(gameState)
      userResult = 'exit'
    elif userResult == 'naboo':
      naboo(gameState)
      userResult = 'exit'
    elif userResult == 'deathStar':
      deathStar(gameState)
      userResult = 'exit'
    
    
#############################################
# room seven (Cloud City) function ##########
#############################################
def userChoice2(roomState, gameState, currentRoom):
  choiceStat = false
  while choiceStat == false:
    userInput = requestString("Make your choice: ")
    if userInput == None:
      printNow("Okay, I guess you want to leave the game...Bye!")
      choiceStat = true
      exit()
    else:
      userInput = userInput.lower()
      if userInput == 'help':
        return('help')
        choiceStat = false
      elif userInput == 'exit':
        printNow("Time to leave.")
        choiceStat = true
        exit()
      elif userInput == 'tatooine' and roomState == 'cloudCity':
        printNow("your off to Tatooine...wooosh!")
        choiceStat = true
        return('tatooine')
      elif userInput == 'alderaan' and roomState == 'cloudCity':
        printNow("your off to Alderaan...woosh!")
        choiceStat = true
        return('alderaan')
      elif userInput == 'business' and roomState == 'cloudCity':
        printNow("I'm thursty, let's go check out the business.")
        choiceStat = true
        return('business')
      elif userInput == 'chat' and roomState == 'business':
        choiceStat = true 
        return('chat')  
      elif userInput == 'leave' and roomState == 'business':
        printNow("\nYou've left the business.")
        choiceStat = true
        return('leave')
      elif gameState[4] == currentRoom and roomState == 'business':
        printNow("your off to save the Princess on the Death Star...woosh!")
        choiceStat = true
        return('deathStar')
      else:
        printNow("The nav computer could not interpret your choice. Please try again.")
        choiceStat = false
        
def whereAmI2(gameState, roomState, currentRoom):
  options = ""
  roomDescrip = ""
  action = ""
  
  options =  "\n Type help to re-display this introduction."
  options += "\nType exit or cancel the dialog2 box to quit at any time."
  
  if roomState == 'cloudCity':
    roomDescrip =  "\nYou have arrived at the main space port on Cloud City.  "
    roomDescrip += "There are space transports currently available to take you "
    roomDescrip += "to Tatooine or Alderaan and the business district nearby."
    if gameState[1] == true:
      action =  "\nSince you found the princess, you'd better hurry to get her home!  "
      action += "You have a limited amount of turns to do it.  So get moving!"
    elif gameState[0] == true and gameState[1] == false:
      action =  "\nYou have the secret plans, but you might want to check "
      action += "out the local businesses, and see if anyone can help you "
      action += "find the Death Star."
    elif gameState[0] == false and gameState[1] == false:
      action =  "\nSince your mission is to find the secret plans "
      action += "for the Death star, you might want to ask around "
      action += "a little bit and see if anyone can help you."
    action += "\nEnter Tatooine or Alderaan to move on to another planet "
    action += "or type Business to go into the business center nearby "
    action += "and talk to some locals."
  elif roomState == 'business':
    roomDescrip =  "\nYou've entered the business district.  "
    roomDescrip += "It's off season, so the marketplace is virtually empty.  "
    roomDescrip += "At the moment, only a local merchant is around selling her wares."
    if gameState[1] == true:
      action =  "\nThe princess just charged up her blaster and is starting "
      action += "to point it your way, since you seemed more concerned with "
      action += "hanging out with old ladies."
    elif gameState[0] == true and gameState[1] == false:
      action =  "\nYou might want to ask the merchant if she knows "
      action += "how to get to the Death Star."
    elif gameState[0] == false and gameState[1] == false:
      action =  "\nShe's trying to ignore you, but since no one else "
      action += "seems to be around, why don\'t you ask her for some help."
    action += "\nEnter chat to talk to the merchant or type leave" 
    action += "to got back to the ship."    
  elif roomState == 'chat':
    roomDescrip =  "\nYou say jokingly: \"Hi there good lookin\', you "
    roomDescrip += "happen see any secret Death Star plans around here?\"\n"
    if gameState[1] == true:
      action =  "\nShe replies: \"Moron, you've got them in your hand, "
      action += "and the princess is right at your side.  "
      action += "If I were you I would get the hell "
      action += "out of here and take her home as quick as possible.\"  "
      action += "Completely disgusted with you, the merchant walks away.\n"
    elif gameState[0] == true and gameState[1] == false:
      action =  "\nShe replies: \"Moron, you've got them in your hand.\"  "
      action += "You reply with a look of embarrassment on your face: \"Sorry, "
      action += "I mean do you know of a way to get to the Death Star?\"\n"
      if gameState[4] == currentRoom and gameState[1] == false:
        action += "\n\"You might want to try the ship at the far end of the "
        action += "space port.  Should take you directly there.  Now leave me alone!\""
      else:
        action += "\n\"Nope, nothing like that 'round here.  Don\'t ask me "
        action += "stupid questions.  Now leave me alone!\""
    elif gameState[0] == false and gameState[1] == false:
      if gameState[3] == currentRoom and gameState[0] == false:
        action += "\n\"You mean these worthless maps?  Some old guy with a "
        action += "lightsaber traded them for a new pair of shoes.  I took pity "
        action += "on the old drunk and agreed on the trade.  I didn't know what "
        action += "to do with them, so I sewed them into this nice blanket.  "
        action += "You can have them if you want.  It\'s not selling anyway.\"  She "
        action += "hands you the plans.  What luck!"
      else:
        action =  "\n\"Nope, nothing like that around here.  You may want to check "
        action += "out one of the nearby systems.  Might have better luck.\""
    if gameState[4] == currentRoom and gameState[1] != true:
      action += "\n\nType DeathStar to use board the ship at the end of the "
      action += "space port or type leave to business district"
    elif gameState[4] != currentRoom or gameState[1] == true: 
      action = action + "\nType leave to exit business district"
    elif gameState[3] != currentRoom or gameState[0] == true: 
      action = action + "\nType leave to exit the business district"  
  return(options, roomDescrip, action, gameState)
  
  
def dialog2(roomState, gameState, currentRoom):

  printNow("\n--------------- Cloud City ---------------")
  if gameState[1] == 1:
  	gameState[2] -= 1
    printNow("You have %d of 6 turns remaining\n" % gameState[2])
    
  options = whereAmI2(gameState, roomState, currentRoom)[0]
  roomDescrip = whereAmI2(gameState, roomState, currentRoom)[1]
  action = whereAmI2(gameState, roomState, currentRoom)[2]
  textDisplay =  roomDescrip + action + options
  
  printNow(textDisplay)  

def cloudCity(gameState):

  currentRoom = 7
  roomState = 'cloudCity'
    
  dialog2(roomState, gameState, currentRoom)
  userResult = userChoice2(roomState, gameState, currentRoom)
  while userResult != 'exit' and userResult != None:
    if userResult == 'help':
      dialog2(roomState, gameState, currentRoom)
      userResult = userChoice2(roomState, gameState, currentRoom)
    if userResult == 'business':
      roomState = 'business'
      dialog2(roomState, gameState, currentRoom)
      userResult = userChoice2(roomState, gameState, currentRoom)
    if userResult == 'chat':
      dialog2(userResult, gameState, currentRoom)
      userResult = userChoice2(roomState, gameState, currentRoom)
    if userResult == 'leave':
      roomState = 'cloudCity'
      dialog2(roomState, gameState, currentRoom)
      userResult = userChoice2(roomState, gameState, currentRoom)
    if userResult == 'chat' and gameState[3] == currentRoom:
      gameState[1] = true  
    if userResult == 'tatooine':
    	tatooine(gameState)
    	userResult = 'exit'
    elif userResult == 'alderaan':
    	alderaan(gameState)
    	userResult = 'exit'
    elif userResult == 'deathStar':
    	deathStar(gameState)
    	userResult = 'exit'
    
     
##########HOTH FUNCTION (ROOM 5)#########################

def hoth(gameState): #room 5
  check = true
  roomDesc = "\n--------------- Hoth Spaceport ---------------\n"
  roomDesc += "Hoth is the sixth planet in the hoth system\n"
  roomDesc += "It is a frozen world covered in snow and ice.\n"
  roomDesc += "The wampa and the tauntaun are both native to hoth.\n"
  roomDesc += "A newly deceased tauntaun can be cut open to \n"
  roomDesc += "to make a great temporary refuge from the cold.\n"

  
  #if the player has the plans and princess, decrement turns, tell player how many turns
  if (gameState[0] == true and #hasPlans 
  gameState[1] == true): #hasPrincess
    gameState[2] = gameState[2] - 1
  if gameState[2] > 1:
    roomDesc += "\nYou have " + str(gameState[2]) + " turns left\n"
  elif gameState[2] == 1:
    roomDesc += "\nYou only have 1 turn left.\n" 
  elif gameState[2] == 0:
      roomDesc += "You did not exit in time.  You lose."
      return
  printNow(roomDesc)
  
  while check == true:
    option = "What is your choice?\n"
    # if the player doesn't have plans, and this is the planet with the plans, tell the player
    if (gameState[0] == false and #!hasPlans 
    gameState[3] == int(5)): #this planet has the plans
       option += "The plans are here!\n"
       option += "Type \"get plans\" to get the plans.\n"
    
    #if the player has plans, doesn't have princess, and the death star is near, tell the player
    if (gameState[0] == true and #hasPlans
    gameState[1] == false and #!hasPrincess
    gameState[4] == int(5)): #death star is near
      option += "Type \"Save Princess\" to jump to the Death Star and rescue the princess.\n"
  
    option += "Type \"Coruscant\" to jump to Coruscant.\n"
    option += "Type \"Endor\" to jump to Endor.\n"
    option += "Type \"Exit\" to quit."
        
    choice = requestString(option)
    choice = choice.lower()
    
    if choice == "coruscant":
      coruscant(gameState)
      check = false
    elif choice == "endor":
      endor(gameState)
      check = false
    elif (choice == "get plans" and
    gameState[0] == false and #player doesn't already have plans
    gameState[3] == int(5)):#this is the plans room
      printNow("You got the plans, now you can resuce the princess!")
      printNow("Go find the Death Star!")
      gameState[0] = true #hasPlans
      check = false
      dagobah(gameState)
    elif (choice == "save princess" and 
    gameState[0] == true and #hasPlans
    gameState[1] == false and #!hasPrincess
    gameState[4] == int(5)): #death star is near Dagobah
      deathStar(gameState)
      check = false
    elif choice == "exit":
      printNow("Bye Jar Jar")
      return
      check = false
    else:
      printNow("I don't recognize that statement.")
      
##########DAGOBAH FUNCTION (ROOM 6)#########################

def dagobah(gameState): #room 6
  check = true
  roomDesc = "\n--------------- Dagobah Spaceport ---------------\n"
  roomDesc += "Dagobah is a world of murky swamps,\n"
  roomDesc += "steaming bayous, and petrified forests.\n"
  roomDesc += "The great Jedi Yoda lives near a cave\n"
  roomDesc += "infused with the dark side of the Force\n"
  roomDesc += "which keeps Emperor Palpatine from detecting him.\n"

  
  #if the player has the plans and princess, 
  if (gameState[0] == true and #hasPlans 
  gameState[1] == true): #hasPrincess
    gameState[2] = gameState[2] - 1 #decrement turnsLeft
  if gameState[2] > 1: #tell player how many turns left
    roomDesc += "\nYou have " + str(gameState[2]) + " turns left\n"
  elif gameState[2] == 1:
    roomDesc += "\nYou only have 1 turn left.\n" 
  elif gameState[2] == 0:
      roomDesc += "You exit in time.  You lose."
      return
  printNow(roomDesc)
  
  while check == true:
    option = ""
    # if the player doesn't have plans, and this is the planet with the plans, tell the player
    if (gameState[0] == false and #!hasPlans 
    gameState[3] == int(6)): #this planet has the plans
      option += "\nThe plans are here!\n"
      option += "Type \"get plans\" to get the plans."
    
    #if the player has plans, doesn't have princess, and the death star is near, tell the player
    if (gameState[0] == true and #hasPlans
    gameState[1] == false and #!hasPrincess
    gameState[4] == int(6)): #death star is near
      option += "Type \"Save Princess\" to jump to the Death Star and rescue the princess.\n"
  
  
    option += "What is your choice?\n"
    option += "Type \"Coruscant\" to jump to Coruscant.\n"
    option += "Type \"Tatooine\" to jump to Tatooine.\n"
    option += "Type \"Exit\" to quit."
        
    choice = requestString(option)
    choice = choice.lower()
    
    if choice == "coruscant":
      coruscant(gameState)
      check = false
    elif choice == "tatooine":
      tatooine(gameState)
      check = false
    elif (choice == "get plans" and
    gameState[0] == false and #player doesn't already have plans
    gameState[3] == int(6)):#this is the plans room
      printNow("You got the plans, now you can resuce the princess!")
      printNow("Go find the Death Star!")
      gameState[0] = true #hasPlans
      check = false
      dagobah(gameState)
    elif (choice == "save princess" and 
    gameState[0] == true and #hasPlans
    gameState[1] == false and #!hasPrincess
    gameState[4] == int(6)): #death star is near Dagobah
      deathStar(gameState)
      check = false
    elif choice == "exit":
      printNow("Bye Jar Jar")
      return
      check = false
    else:
      printNow("I don't recognize that statement.")
