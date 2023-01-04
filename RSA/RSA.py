import RSA.HelperFunctions as HelperFunctions
import RSA.KeySetup as ks
from django.conf import settings
import os

def helloworld():
    print("hello world")


def encrypt(file_path):
    
    # Set up public and private keys
    n,e,p,q = ks.generatePublicKey()
    d = ks.generatePrivateKey(n,e,p,q)

    # Read Message
    message = HelperFunctions.readMessage(file_path)
    # TOD: Gotta update this for not int .txt files smh
    message = int(message)

    # Encrpyt
    ciphertext = HelperFunctions.modular_exp(message,e,n)
    ciphertext = str(ciphertext)

    # Write the encrypted text to a file
    ct_fname = "__encrypted__.txt"
    ct_path = os.path.join(settings.MEDIA_ROOT, ct_fname)
    HelperFunctions.writeText(ct_path, ciphertext)

    # Return filepath and the numbers
    return n,e,p,q,d,ct_fname


def decrypt(file_path,n,e,p,q,d):
    ciphertext = HelperFunctions.readMessage(file_path)
    ciphertext = int(ciphertext)

    original_message = HelperFunctions.modular_exp(ciphertext, d, n)
    original_message = str(original_message)

    # Write the encrypted text to a file
    ot_fname = "__decrypted__.txt"
    ot_path = os.path.join(settings.MEDIA_ROOT, ot_fname)
    HelperFunctions.writeText(ot_path, original_message)

    # Return File Path
    return ot_path
