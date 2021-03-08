#Key Generation file. Takes in a random bit generated from the secrets library
#computes a pValue that's based on the p value
#calculates d and e2
#outputs p, e1, and e2 to pubkey.txt (e1 is just g - or just 2)
#outputs p, e1, and d to prikey.txt
#also prints them to shell for readability purposes

#imports
import mr
import random
import secrets

def keyGeneration():
  flag = False
  
  #while loop for primes. If the number is not prime it tries again, hence the continue
  #once all the conditions are met the flag is set to true and the loop is broken
  while flag == False:
    qValue = int(secrets.randbits(32))
    if (qValue // (2**31)) < 1:
      qValue += (2**31)
    if mr.miller_rabin(qValue, 40) == False:
      continue
    if (qValue % 12) != 5:
      continue
    else:
      pValue = (2*qValue) + 1
      if mr.miller_rabin(pValue, 40) == False:
        continue
      else:
        flag = True

#calculate e2
  dValue = random.randrange(1, pValue-2)
  e2Value = pow(2, dValue, pValue)

#send to file for public and private keys
  f = open("pubkey.txt", "w")
  f.write(str(pValue) + " 2 " + str(e2Value))
  f.close()

#print the values to the screen for grading convenience
  print("\nPUBLIC:\np: " + str(pValue) + "\ng: 2" + "\ne2: " + str(e2Value))

#write to the private key file
  f2 = open("prikey.txt", "w")
  f2.write(str(pValue) + " 2 " + str(dValue))
  f.close()
  
#print the values to the screen for grading convenience
  print("\nPRIVATE:\np: " + str(pValue) + "\ng: 2\nd: " + str(dValue))
