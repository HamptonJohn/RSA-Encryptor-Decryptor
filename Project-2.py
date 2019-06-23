#Brandon Phipps, John Hampton, Jon-Paul Casias
#RSA encrypter and decrypter

import random 


#main driver function 
def main():

    answer = '' #determines whether user wants to encrypt or decrypt
    reRun = '' #determines whether user wants to encrypt or decrypt another message 
    t = True

    while (t== True):

        answer = input('\nTell us what you would like to do. To cipher enter c or to decypher enter d. \n\n')

        if answer == 'c': #encrypts

            RandomPrime()

        if answer == 'd': #decrypts 

            decipher()

        reRun = input('\nWould you like to cipher or decypher anything else? Enter y or n. \n\n' )

        if reRun == 'y': #encrypt/decrypt another message

            t = True

        if reRun == 'n': #end program
            t = False


     
 
 
        
def RandomPrime():

    #initialize variables
    PrimeNo1 = 0
    PrimeNo2 = 0
    Fermatp1=0
    Fermatp2=0

    while ( Fermatp1  < 1): #while Fermat test for first number is false
        
        PrimeNo1 = random.randint(50, 150) #generate random integer from 50 to 150
        
        for i in range(20): #conduct Fermat test 20 times to ensure primality of number
            
            Fermatp1 =FermatTest(PrimeNo1)  #conduct Fermat test on 1st random int, sets Fermatp1 to 0 or 1
            
            if Fermatp1 == 0: #if the number fails the Fermat test, break loop and select another random integer
                
                break;
            
    while ( Fermatp2  < 1): #while Fermat test for second number is false
        
        PrimeNo2 = random.randint(50, 150) #generate random integer from 50 to 150
        
        for i in range(20): #conduct Fermat test 20 times to ensure primality of number
            
            Fermatp2 = FermatTest(PrimeNo2) #conduct Fermat test on 2nd random int, sets Fermatp2 to 0 or 1
            
            if Fermatp2 == 0: #if the number fails the Fermat test, break loop and select another random integer
                
                break;

    print ("\nPrime Number 1 ", PrimeNo1)
    print ("\nPrime Number 2 " ,PrimeNo2)
    RSA(PrimeNo1 , PrimeNo2) #Call RSA function with 2 random prime numbers
 

#Fermat Primality Test
def FermatTest(n):

    prime = 0 #returns false, not prime
    
    if pow(2, n-1, n) == 1:
        
      prime = 1 #returns true, most likely prime
      
    return prime
      
def RSA(PrimeNo1 , PrimeNo2):
    
    #initialize Keys
    publicKey = []
    privateKey = 0
    
    n = (PrimeNo1 * PrimeNo2) #n equals prime number 1 multiplied by prime number 2, i.e. (53 * 71)
    
    publicKey.append(n)
    
    fn = (PrimeNo1 - 1) * (PrimeNo2 - 1) #fn equals ((prime number) 1 - 1) * ((prime number 2) - 1), i.e. (52 * 70)
    
    while True:
        
        e = random.randint(2, fn - 1) #assigns e as random integer from 2 to (fn-1) 
     
        if RelativePrime(e,fn): #determines relative primality of e 
            break
        
    publicKey.append(e) #append e to public key

    #print values for encryption/decryption
    print ("\ne: ",e)
    d = MultiplicativeInverse(e,fn)
    print ("\nd: ",d)
    
    privateKey = d
    
    print('\nn:',n)
    print('\nfn:',fn)
    
    print('\nPublic Key: ',publicKey)
    print('\nPrivate Key: ', privateKey)
    
    cipher(e, n) #call encrypt function 

#returns inverse of e
def MultiplicativeInverse(e,fn):
    
    for x in range(1,fn): #from 1 to (fn - 1)
        
        if ((e*x) % fn) == 1:  # d == ((1 % fn) / e )
            
            return x

#determines relative primality
def RelativePrime(a,b):
    
    return gcd(a,b) == 1

# Euclid's algorithm for finding greatest common divisor  
def gcd(a=1, b=1):
    
    if a < b: #swaps values if a is not divisble by b
        
        a, b = b, a
        
    if b == 0: #base case
        
        return a
    
    else: #recursive case
        
        return gcd(b, a%b)
    

#encrypting function     
def cipher(e, n):
    
    message = input('\nEnter the message you would like to encrypt. \n')
    st = '\nHere is you encryption: \n'

    
    for x in message:
        
        x = pow(ord(x),e,n) #convert character in string to integer, then raise to e power, modulus n
        
        st+= chr(x) #convert integer to character, then append character to string.
        
    print(st) #print encrypted string 


#decrypting function   
def decipher():
    
    message= input('\nEnter the message you would like to decrypt. \n')
    n = int(input('\nWhat would you like n to be? \n'),10) #convert n input to integer, base 10
    privateKey2 = int(input('\nWhat is your private key? \n'),10) #convert private key input to integer, base 10
    st = '\nHere is you decryption: '

    for x in message:
        
        x = pow(ord(x),privateKey2,n) #convert character in string to integer, then raise to power of private key (d), modulus n
        
        st+= chr(x) #convert integer to character, then append character to string
        
    print(st)#print decrypted string
