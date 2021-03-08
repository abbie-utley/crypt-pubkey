#Decryption in this file. Opens the ctext.txt file and decrypts it back into plaintext
#prints decrypted text to shell and stores it in dtext.txt file

def decryption():
  #opens the ctext.txt file and reads it into a value called cText
  f = open("ctext.txt", "r")
  cText = f.read()
  f.close()

  #c1 is the first half of the ciphertext and c2 is the second half
  c1 = cText[:33]
  c1 = int(c1, 2)
  c2 = cText[33:]
  c2 = int(c2, 2)

  #just like ec.py it opens the pubkey.txt file and reads in the string
  #then parses it to pValue, g, and e2
  f2 = open("pubkey.txt", "r")
  toHold = f2.read()
  f2.close()
  listObj = toHold.split()
  numMap = map(int, listObj)
  numList =list(numMap)
  pValue = numList[0]
  e1Value = numList[1]
  e2Value = numList[2]

  #just like ec.py it opens the prikey.txt file and reads in the string
  #then parses it into the dValue
  f3 = open("prikey.txt", "r")
  toHold2 = f3.read()
  f3.close()
  listObj2 = toHold2.split()
  numMap2 = map(int, listObj2)
  numList2 = list(numMap2)
  dValue = numList2[2]

  #hold = (c2 * c1^(p-1-d)) mod p
  hold = pow(pow(int(c2), 1, pValue) * pow(int(c1), (pValue - 1 - dValue), pValue), 1, pValue)
 
  #change hold to be a 32 bit number (including the 0)
  #split the value into 4 even chunks
  #turn the int into a base 2 int
  #then convert the value into a letter
  pTextL = []
  hold = format(hold, '032b')
  for i in range(4):
    pTextL.append(hold[:8])
    hold = hold[8:]
    pTextL[i] = int(pTextL[i], 2)
    pTextL[i] = chr(pTextL[i])

  #join the list of letters together to form a word
  pText = "".join(pTextL)
  print("plaintext decrypted: " + pText)

  #open the file dtext.txt and write the decrypted plaintext to it
  f4 = open("dtext.txt", "w")
  f4.write(pText)
  f4.close()
