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
  rmDesc += "Destination choices are: \n Coruscant, Tatooine, Alderaan, or X for exit.\n"
  printNow (rmDesc)
  if(gameState[0]==true and gameState[1]==true): #has plans and princess
    printNow("\nCongratulations, You Have Rescued the Princess and brought her to safety")
    printNow("May the Force be with you!!!")
    check = false
  if(gameState[3]==1 and gameState[0]== false and gameState[1] == false):# found plan room
    printNow("\nYou have found the plan room, please take plans to save the Princess!")
    picPln = requestString("Do you want to pick up the plans? yes or no")
    picPln = picPln.lower()
    if picPln == "yes":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
  if(gameState[4]==1 and gameState[0]== true and gameState[1] == false): # found deathstar and already has plans
    printNow("\nYou have found the DeathStar, please save the Princess!!!")
    svPrncs = requestString("Do you want to rescue the Princess? yes or no")
    svPrncs = svPrncs.lower()
    if svPrncs == "yes": # if they want to save princess
      gameState[1] = true
      printNow("\nYou have the Princess, \nhead for the exit, \nMay The Force be With You!")
  # destination choice loop
  while check == true:
    chc = requestString("What is the number of your next destination choice? or type exit to quit")
    chc = chc.lower()
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
      printNow("You cannot get to destination "+ chc +" from here, try Coruscant, Tatooine, or Alderaan.")
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
  rmDesc += "Destination choices are: \nNaboo, Alderaan, Hoth, Dagobah, or exit to quit.\n"
  printNow(rmDesc)
  if(gameState[0]==true and gameState[1]==true): #has plans and princess
    gameState[2] -= 1 # this is not exit so subtract 1
    if gameState[2]<=0:
      exit()
      check = false
  if(gameState[3]==2 and gameState[1]== false and gameState[1] == false):# found plan room
    printNow("\nYou have found the plan room, please take plans to save the Princess")
    picPln = requestString("Do you want to pick up the plans? yes or no")
    picPln = picPln.lower()
    if picPln == "yes":
      gameState[0] = true
      printNow("\nYou have the plans, May The Force be With You!\n")
  if(gameState[4]==2 and gameState[0]== true and gameState[1] == false): # found deathstar and already has plans
    printNow("\nYou have found the DeathStar, please save the Princess!!!")
    svPrncs = requestString("Do you want to rescue the Princess? yes or no")
    svPrncs = svPrncs.lower()
    if svPrncs == "yes": # if they want to save princess
      gameState[1] = true
      printNow("\nYou have the Princess, \nhead for the exit, \nMay The Force be With You!")
  # destination choice loop
  while check == true:
    chc = requestString("What is the number of your next destination choice? or type exit to quit")
    chc = chc.lower()
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
      printNow("You cannot get to destination "+ chc +" from here, try Alderaan, Hoth, or Dagobah.")
      check = true

#################################################
# room 4 (Alderaan) function
#################################################
def alderaan(gameState):
  check = true
  roomDescrip = "\n--------------- Alderaan Spaceport ---------------\n"
  roomDescrip += "You have arrived at the Spaceport on the lush, \n"
  roomDescrip += "mountainous planet of Alderaan, one of the hubs of the Rebel \n"
  roomDescrip += "alliance.  After exchanging information with \n"
  roomDescrip += "some local rebels, you learn that your destination options\n"
  roomDescrip += "are Naboo, Coruscant, Cloud City, and Endor.\n"
  
  choiceDescrip = "What do you want to do?\n"
  choiceDescrip += "Type \"Naboo\" to jump to Naboo\n"
  choiceDescrip += "Type \"Coruscant\" to jump to Coruscant\n"
  choiceDescrip += "Type \"Cloud City\" to jump to Cloud City\n"
  choiceDescrip += "Type \"Endor\" to jump to Endor\n"
  
  #if this planet has the plans and you don't already have them, notify
  if gameState[0] == false and gameState[3] == 4:
    roomDescrip += "\nHowever, before you take off, His Highness, Prince Bail Organa\n"
    roomDescrip += "catches up to tell you that he has obtained a copy of the \n"
    roomDescrip += "plans of the layout of the Death Star.  He begs you to take them to\n"
    roomDescrip += "use in your mission to rescue his daughter, Princess Leia.\n\n"
    
    choiceDescrip += "Type \"Pickup Plans\" to pick up the plans from the Prince\n"
    
  #if you have the plans, no princess, and this is the planet with the Death Star orbiting, notify
  if gameState[0] == true and gameState[1] == false and gameState[4] == 4:
    roomDescrip += "\nHowever, you notice that everyone has become extremely nervous\n"
    roomDescrip += "and you ask why. It turns out that the Death Star has been \n"
    roomDescrip += "orbiting for the past several hours. You can finally\n"
    roomDescrip += "rescue Princess Leia!\n\n"
    
    choiceDescrip += "Type \"Save Princess\" to jump to the Death Star and rescue Leia\n"
  
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
  
  choiceDescrip += "Type \"quit\" to exit the game\n"
  printNow(roomDescrip)
  
  while check == true:
    choice = requestString(choiceDescrip).lower()
    
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
    elif choice == "pickup plans" and gameState[0] == false and gameState[3] == 4:
      printNow("You now have all the pieces you need to rescue Princess Leia! ")
      printNow("The next step is to find the Death Star.")
      gameState[0] = true
      alderaan(gameState)
      check = false
    elif choice == "save princess" and gameState[0] == true and gameState[1] == false and gameState[4] == 4:
      deathStar(gameState)
      check = false
    elif choice == "quit":
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
      check = false
    else:
      printNow("The nav computer could not interpret your choice. Please try again.")

#################################################
# room 8 (Endor) function
#################################################
def endor(gameState):
  check = true
  roomDescrip = "\n--------------- Endor Spaceport ---------------\n"
  roomDescrip += "You have arrived at the Spaceport on the forest moon\n"
  roomDescrip += "of Endor. After the Ewoks have refueled the Millenium\n"
  roomDescrip += "Falcon, you're ready to continue your journey.\n"
  roomDescrip += "They tell you that the only planets within range\n"
  roomDescrip += "are Alderaan and Hoth.\n"
  
  choiceDescrip = "What do you want to do?\n"
  choiceDescrip += "Type \"Alderaan\" to jump to Alderaan\n"
  choiceDescrip += "Type \"Hoth\" to jump to Hoth\n"
  
  #if this planet has the plans and you don't already have them, notify
  if gameState[0] == false and gameState[3] == 8:
    roomDescrip += "\nMore importantly, you notice a blue astromech droid\n"
    roomDescrip += "rolling toward you and beeping.  The gold protocol droid\n"
    roomDescrip += "next to him informs you that they have the plans for\n"
    roomDescrip += "the layout of the Death Star.\n\n"
    
    choiceDescrip += "Type \"Pickup Plans\" to pick up the plans from the droids\n"
    
  #if you have the plans, no princess, and this is the planet with the Death Star orbiting, notify
  if gameState[0] == true and gameState[1] == false and gameState[4] == 8:
    roomDescrip += "\nHowever, you notice that everyone has become extremely nervous\n"
    roomDescrip += "and you ask why. It turns out that the Death Star has been \n"
    roomDescrip += "orbiting for the past several hours. You can finally\n"
    roomDescrip += "rescue Princess Leia!\n\n"
    
    choiceDescrip += "Type \"Save Princess\" to jump to the Death Star and rescue Leia\n"
  
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
  
  choiceDescrip += "Type \"quit\" to exit the game\n"
  printNow(roomDescrip)
  
  while check == true:
    choice = requestString(choiceDescrip).lower()
    
    if choice == "alderaan":
      alderaan(gameState)
      check = false
    elif choice == "hoth":
      hoth(gameState)
      check = false
    elif choice == "pickup plans" and gameState[0] == false and gameState[3] == 8:
      printNow("You now have all the pieces you need to rescue Princess Leia! ")
      printNow("The next step is to find the Death Star.")
      gameState[0] = true
      endor(gameState)
      check = false
    elif choice == "save princess" and gameState[0] == true and gameState[1] == false and gameState[4] == 8:
      deathStar(gameState)
      check = false
    elif choice == "quit":
      printNow("\nYou're quitting, you nerf herder?  Too bad, she has a lot of money.\n")
      return
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
  choiceDescrip += "Type \"continue\" to keep your promise and finish the mission\n"
  choiceDescrip += "Type \"quit\" to desert the princess and exit the game\n"
  
  gameState[1] = true
  printNow(roomDescrip)
  
  while check == true:
    choice = requestString(choiceDescrip).lower()
    
    if choice == "quit":
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
        printNow("your off to Dagobah...wooosh!")
        choiceStat = true
        return('dagobah')
      elif userInput == 'cloudcity' and roomState == 'tatooine':
        printNow("your off to Cloud City...woosh!")
        choiceStat = true
        return('cloudcity')
      elif userInput == 'cantina' and roomState == 'tatooine':
        printNow("I'm thursty, let's go check out the cantina.")
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
        printNow("your off to save the Princess on the Death Star...woosh!")
        choiceStat = true
        return('deathstar')
      else:
        printNow("The nav computer could not interpret your choice. Please try again.")
        choiceStat = false
        
def whereAmI(roomState, currentRoom):
  options = ""
  roomDescrip = ""
  action = ""
  
  options = """
  
    Type help to re-display this introduction.
    Type exit or cancel the dialog box to quit at any time.
    """
  if roomState == 'tatooine':
    roomDescrip = """\nYou have arrived at Mos Isley Spaceport on Tatooine.  There are space transports currently available to take you
      to Dagobah or Cloud City and a cantina nearby.
      """
    if gameState[1] == true:
      action = """\nSince you found the princess, you'd better hurry to get her home!  You have a limited amount of turns to do it.  So get moving!
        """
    elif gameState[0] == true and gameState[1] == false:
      action = """\nYou have the secret plans, but you might want to check out the Cantina, and see if anyone can help you find the Death Star.
      """
    elif gameState[0] == false and gameState[1] == false:
      action = """\nSince your mission is to find the secret plans for the Death star, you might want to ask around a little bit and see if anyone can help 
      you.
      """
    action = action + "\nEnter Dagobah or CloudCity to move on to another planet or type Cantina to go into the bar nearby and talk to some locals"
  elif roomState == 'cantina':
    roomDescrip = """\nYou've entered the local cantina.  Strangely enough, the bar is virtually empty.  At the moment, only the barkeep is around
      cleaning drink glasses with a scorn look on his face. 
      """
    if gameState[1] == true:
      action = """\nThe princess is looking really pissed at the moment, since you seemed more concerned with hanging out at a bar than getting her to safety.
        """
    elif gameState[0] == true and gameState[1] == false:
      action = """\nYou might want to ask the barkeep if he knows how to get to the Death Star.
      """
    elif gameState[0] == false and gameState[1] == false:
      action = """\nHe's staring right at you.  Now is your chance to ask him for some help.
      """
    action = action + "\nEnter chat to ask the barkeep a question or type leave to exit the cantina."    
  elif roomState == 'chat':
    roomDescrip = "\nYou say jokingly: \"Hey barkeep, you happen see any secret Death Star plans around here?\"\n"
    if gameState[1] == true:
      action = """\nHe replies: \"Moron, you've got them in your hand, and the princess is right at your side.  If I were you I would get the hell
      out of here and take her home as quick as possible.\"  Completely disgusted with you, the barkeep goes back to cleaning glasses.\n
        """
    elif gameState[0] == true and gameState[1] == false:
      action = """\nHe replies: \"Moron, you've got them in your hand.\"  You reply with a look of embarrassment on your face: \"Sorry, I mean do you know of a way to get to
      the Death Star?\"\n
      """
      if gameState[4] == currentRoom and gameState[1] == false:
        action = action + """\n\"You might want to try the exit at the back behind the bar.  It\'s a secret launch pad.  Should take you directly there.  Now leave me alone!\""""
      else:
        action = action + """\n\"Nope, nothing like that 'round here.  Don\'t ask me stupid questions.  Now leave me alone!\""""
      
    elif gameState[0] == false and gameState[1] == false:
      if gameState[3] == currentRoom and gameState[0] == false:
        action = action + """\n\"You mean these worthless maps?  Some old guy with a lightsaber traded them for a drink.  I took pitty on the old drunk and agreed on the trade.  
        You can have them if you want.  There just collecting dust back here.\"  He hands you the plans.  What luck!"""
        gameState[1] = true
      else:
        action = """\n\"Nope, nothing like that around here.  You may want to check out one of the nearby systems.  Might have better luck.\"
        """
    if gameState[4] == currentRoom and gameState[1] != true:
      action = action + "\n\nType DeathStar to use the secret launchpad or type leave to exit the bar"
    elif gameState[4] != currentRoom or gameState[1] == true: 
      action = action + "\nType leave to exit the bar"
    elif gameState[3] != currentRoom or gameState[0] == true: 
      action = action + "\nType leave to exit the bar"  
  return(options, roomDescrip, action, gameState)
  
  
def dialog(roomState, gameState, currentRoom):

  printNow("\n--------------- Tatooine ---------------")
  if gameState[1] == 1:
    printNow("You have %d of 6 turns remaining\n" % gameState[2])
    
  options = whereAmI(roomState, currentRoom)[0]
  roomDescrip = whereAmI(roomState, currentRoom)[1]
  action = whereAmI(roomState, currentRoom)[2]
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
    if userResult == 'dagobah':
      return
    elif userResult == 'cloudcity':
      return
    elif userResult == 'deathstar':
      return
    