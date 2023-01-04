'''
Description: Helper Functions for RSA encryption system
Author: Jainam Dhruva
'''

# Function To read the message file
def readMessage(filename):
    file_handler = open(filename, "r")
    message = file_handler.read()
    file_handler.close()
    return message


# Function to read the Public Key file
def readPublicKey(filename):
    file_handler = open(filename, "r")
    n = file_handler.readline()
    e = file_handler.readline()
    file_handler.close()
    return n,e


# Function to write the encrypted message to file
def writeText(filename, ciphertext):
    file_handler = open(filename, "w")
    file_handler.write(ciphertext)
    file_handler.close()


# Function to read Private Key
def readPrivateKey(filename):
    file_handler =  open(filename, "r")
    d = file_handler.readline()
    file_handler.close()
    return d


# Function(Iterative) to compute and return (x^y)(mod n). Returns a number in the range [0, n-1]
def modular_exp(x, y, n):
    
    z = 1
    while(y > 0):
        
        if(( y&1 )==1): 
            z = (z*x)%n
        
        x = (x*x)%n
        y >>= 1
    
    return (z%n)

