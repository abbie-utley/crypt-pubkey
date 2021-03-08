#This is the encryption file: opens the pubkey.txt and prikey.txt and reads in the values
#opens ptext.txt and reads in the value. Prints to shell
#prints ciphertext to shell and writes it to a file called ctext.txt

#imports
import random

def encryption():

  #opens pubkey.txt and puts the value into toHold
  f = open("pubkey.txt", "r")
  toHold = f.read()
  f.close()

  #splits the string by spaces, makes them ints and puts it into another list
  listObj = toHold.split()
  numMap = map(int, listObj)
  numList =list(numMap)

  #stores the values needed in their respective files
  pValue = numList[0]
  e1Value = numList[1]
  e2Value = numList[2]

  #opens prikey.txt and reads in the string toHold2
  f2 = open("prikey.txt", "r")
  toHold2 = f2.read()
  f2.close()

  #does the same thing and parses the values
  listObj2 = toHold2.split()
  numMap2 = map(int, listObj2)
  numList2 = list(numMap2)

  #only dValue is new, so store that
  dValue = numList2[2]
  
  #opens ptext.txt and puts the string literal in hold2
  f3 = open("ptext.txt", "r")
  hold2 = f3.read()
  f3.close()
  
  #initializing a list called pTextL for the manipulation of plaintext
  pTextL = []

  #put the number version in the list then turn it into an 8bit number 
  for i in range(4):
    pTextL.append(ord(hold2[i]))
    pTextL[i] = format(pTextL[i], '08b')

  #join list into one string
  pText = "".join(pTextL)

  #take the binary string and convert to number
  pText = int(pText, 2)

  #r = random number from 1 to p-1
  #c1 = g^d mod p
  #c2 = (plaintext * e2^r) mod p
  randomR = random.randrange(1, pValue-1)
  c1 = pow(e1Value, randomR, pValue)
  c2 = pow((pow(pText, 1, pValue) * pow(e2Value, randomR, pValue)), 1, pValue)

  #need 33 bits for c1 and c2
  c1 = format(c1, '033b')
  c2 = format(c2, '033b')

  #cText = the concatenation of c1 and c2
  #print the number version to the shell for easier grading purposes
  cText = str(c1) + str(c2)
  cTextNum = str(int(c1, 2)) + str(int(c2, 2))
  print("\nplaintext: " + hold2 + "\ncipertext: " + cTextNum)
  
  #open ctext.txt and write the ciphertext to the file
  f4 = open("ctext.txt", "w")
  f4.write(cText)
  f4.close()
