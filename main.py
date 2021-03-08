#Main file for program. Prompts the user if they'd like to do key generation, encryption or decryption
#loops until the user wants to stop

#imports
import KG
import ec
import dc

#variables
flag = False
loop = 'y'

#Start of the loop with prompts
while loop == 'y':
  print("\nPlease select the option you wish to choose for this public key cryptosystem.")
  print("1: key generation")
  print("2: encryption")
  print("3: decryption")
  response = int(input())

  #Loop for the input of which option you'd like
  #Loops while response is not 1, 2, or 3
  while flag == False:
    if response == 1:
      KG.keyGeneration()
      flag = True
    elif response == 2:
      ec.encryption()
      flag = True
    elif response == 3:
      dc.decryption()
      flag = True
    else:
      print("Please enter a valid number: ")
      response = int(input())
  
  #back to the other loop, asks user if they want to start again
  #if they do, clear the rest of the inputs
  print("\nWould you like to go again? y or n. ")
  loop = input()
  flag = False
  response = 0

