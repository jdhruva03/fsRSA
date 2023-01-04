'''
Description: Encryption Module for RSA encryption system
Author: Jainam Dhruva
'''
import RSA.HelperFunctions as HelperFunctions

# Function to Encrypt the message
def encrypt(message, n, e):
    c = HelperFunctions.modular_exp(message,e,n)
    return c


# =========================================
# ============= Driver Code ===============
message = HelperFunctions.readMessage("message.txt")
message = int(message)

n,e = HelperFunctions.readPublicKey("public_key.txt")
n = int(n)
e = int(e)

ciphertext = encrypt(message,n,e)

ciphertext = str(ciphertext)
HelperFunctions.writeText("ciphertext.txt", ciphertext)


'''
# Encrypt.py CHECKS
print("message:", message)
print("n:", n)
print("e:", e)
print("ciphertext:", ciphertext)
'''