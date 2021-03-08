Name: Abbigail Utley
email: abbie.utley101@gmail.com

Public-key Cryptosystem
=======================

This is a public key cryptosystem, that uses block encryption and encrypts one block at a time. This mainly uses modular math 
and its properties to calculate the public key and private key. This is used for school, so the functionality will print to screen
as well as send it to external files, so keep in mind when running.

Public-key Cryptosystem uses a 33 bit prime and a 32 bit message, ensuring that the prime is always larger than the message.

This project will be in Python3

---

How to Build
------------

This section will describe how to build and use the program

1. In the directory, run the command `python3 main.py` and that will run the program
2. From here, you're prompted to choose an option for:
* Key Generation
* Encryption
* Decryption
3. If you want Key Generation, press 1, and hit enter. If you want Encryption, press 2 and hit enter. If you want Decryption press 3 and
hit enter. There are also directions prompted if you forget.
4. Once your desired segment runs, then it'll ask if you want to do it again. If yes, type y and hit enter. If no, then press any key and
hit enter, or just hit enter.

---

List of Files
-------------

This is a list of files and their descriptions that _must_ be included in the directory for the program to run.

* `main.py` : This file is the main file of the program. It has the prompts for which segment you'd like to run as well as the loop
              for convenience purposes. It imports each of the .py files.
* `KG.py` : This file holds the definition of Key Generation. I abbreviated its name so that I could call key generation from main without
            it looking too clunky. It calculates the public and private key and outputs the specified values to pubkey.txt and prikey.txt.
            It also outputs them to the shell for convenience purposes.
* `ec.py` : This file holds the definition of encryption. This reads in the key text files as well as the ptext file which contains the 
            plaintext. Here it uses the keys and the plaintext to encode. It outputs the plaintext and ciphertext to the shell for 
            convenience purposes as well as writes the binary representation of the ciphertext to a file called ctext.txt
* `dc.py` : This file holds the definition of decryption. This reads in the key text files as well as the ctext file which contains the 
            ciphertext. Here it uses the keys and the ciphertext to decode. It outputs the plaintext in ascii form to the shell for 
            convenience purposes as well as writes the ascii representation of the decrypted plaintext to a file called dtext.txt
* `ptext.txt` : This file holds the plaintext that encryption needs in order to run. Encryption only takes in 32 bits at a time, so keep 
                that in mind. 
* `mr.py` : This file holds the miller-rabin algorithm. The professor said we could look to outside sources for the miller-rabin code
            so this code is copied and pasted from http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes 

The rest of the files will be generated if you go in order of 1 - key generation, 2 - encryption and 3 - decryption.
