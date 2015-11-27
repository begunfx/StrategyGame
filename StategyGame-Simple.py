## Team 4 Strategy Game Simple ###
#      William Gillihan          #
#      Christopher Dixon         #
#      Wendy Gray                #
#      Brian Begun               #
#                                #
#      ver 0.1.0                 #
#      11_26_2015                #
##################################
# call room1 to start
room1()
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
    choice = requestString("Do you want to quit the game? type X to quit")
  return choice
#############################################
# room one (Naboo) function #################
#############################################
def room1():
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
      room2()
    elif choice == 3: # for Tatooine
      check = false
      room3()
    elif choice == 4: # for Alderaan
      check = false
      room4()
    elif chc == "x":
      exit()
      check = false
    else:
      printNow("You cannot get to destination "+ chc +" from here, Try 2, 3, or 4.")
      check = true
#################################################
# room two (Coruscant) function #################
#################################################
def room2():
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
      room1()
    elif choice == 4: # for Alderaan
      check = false
      room4()
    elif choice == 5: # for Hoth
      check = false
      room5()
    elif choice == 6: # for Dagobah
      check = false
      room6()
    elif chc == "x":
      exit()
      check = false
    else:
      printNow("You cannot get to destination "+ chc +" from here, Try 2, 3, or 4.")
      check = true
