'''
Description: Key Setup module for RSA encryption system
Author: Jainam Dhruva
'''
import random
import RSA.HelperFunctions as HelperFunctions


# Miller Rabin test helper function
def MillerRabin_Helper(a,s,d,n):       
    if (HelperFunctions.modular_exp(a, d, n) == 1):
        return False
    else:
        for r in range(s):
            if (HelperFunctions.modular_exp(a, (2**r)*d, n) == (n-1)):
                return False
    
    return True


# Function implementing Miller Rabin test for Primality
def MillerRabin(n, k=10):
    
    # Factor n-1 as ((2^s)*d)
    d = n - 1
    s = 0 
    while (d%2 == 0): 
        d>>=1
        s+=1
    
        
    for i in range(k):
        a = random.randrange(2, n)
        if (MillerRabin_Helper(a,s,d,n)):
            return False
    
    return True


# Function to check if a number is prime
def isPrime(x):
    
    if x!=int(x):
        return False
    x=int(x)
    
    if (x == 2):
        return True
    elif (x%2 == 0):
        return False
    else: 
        return MillerRabin(x)


# Function to Generate a Prime number between range [x,y]
# 2**350 ~ 106 digits; 2**500 ~ 151 digits
def generatePrime(x=(2**350), y=(2**500)):
    diff = abs(x-y)
    
    while(diff > 0):
        a = random.randrange(x,y)
        if (isPrime(a)):
            return a
        diff = (diff - 1)

    print("There probably does not exist a prime in the range[x, y].")
    return (-1)


# Function to Extended Eculidean Algorithm. Returns gcd and ordered coefficients
def EEA(x, y):
    if x == 0:
        return y, 0, 1
    else:
        gcd, a, b = EEA(y % x, x)
        return gcd, b - (y // x) * a, a


# Function to Generate Public Key (n, e)
def generatePublicKey():
    p = generatePrime()
    q = generatePrime()
    while(abs(q-p)<(10**95)):
        q = generatePrime()
    
    n=p*q

    e = 65537
    
    phi_n = (p-1)*(q-1)
    gcd_e_and_phi_n = EEA(e, phi_n)[0]
    
    if (gcd_e_and_phi_n != 1):
        while (gcd_e_and_phi_n != 1):
            e = generatePrime(10000,1000000)
            gcd_e_and_phi_n = EEA(e, phi_n)[0]

    return n,e,p,q


# Functiong Generate Private Key (d)
def generatePrivateKey(n,e,p,q):
    
    phi_n = (p-1)*(q-1)
    gcd,d,y = EEA(e,phi_n)
    while(d<0):
        d+=phi_n
 
    return d


# =========================================
# ============= Driver Code ===============

n,e,p,q = generatePublicKey()
d = generatePrivateKey(n,e,p,q)

public_f = open("public_key.txt", "w")
public_f.write(str(n))
public_f.write("\n")
public_f.write(str(e))
public_f.close()

private_f = open("private_key.txt","w")
private_f.write(str(d))
private_f.close()


'''
# KeySetup.py CHECKS
print(isPrime(1158398533632707750915405056251646513513288822820233629002517574278725302642684377984721026358365997))
print("n=",n)
print("e=",e)
print("d=",d)
print(HelperFunctions.modular_exp(e*d,1,(p-1)*(q-1)))
'''