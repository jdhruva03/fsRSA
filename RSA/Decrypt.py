'''
Description: Decryption Module for RSA encryption system
Author: Jainam Dhruva
'''
import RSA.HelperFunctions as HelperFunctions


# Function to decrypt cipher text
def decrypt(ciphertext, d, n):
    m = HelperFunctions.modular_exp(ciphertext, d, n)
    return m


# =========================================
# ============= Driver Code ===============
ciphertext = HelperFunctions.readMessage("ciphertext.txt")
ciphertext = int(ciphertext)

n = HelperFunctions.readPublicKey("public_key.txt")[0]
n = int(n)

d = HelperFunctions.readPrivateKey("private_key.txt")
d = int(d)

original_message = decrypt(ciphertext, d, n)
original_message = str(original_message)

HelperFunctions.writeText("decrypted_message.txt", original_message)


'''
# Decrypt.py CHECKS
print("n:",n)
print("d:",d)
print("ciphertext:",ciphertext)
print("decrypted text:", original_message)
'''