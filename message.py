from Crypto.Cipher import AES 
import base64


def pad(entry):
    padded =  entry + (16-len(entry)%16)*'['
    return padded

def encrypt(key):
    #Getting text from user to encrypt
    plain_text = input("Shkruani tekstin qe po doni me e enkript: ")
    plain_text = pad(plain_text)
    plain_text = plain_text.encode('UTF-8')

    #Encryption with AES(mode ecb)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plain_text)
    return base64.b64encode(ciphertext).decode('UTF-8')

#key generation
key='12345'
key=pad(key)
key=key.encode('UTF-8')

#Function call
mesazhi_i_enkriptuar = encrypt(key)
print(mesazhi_i_enkriptuar)