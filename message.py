from Crypto.Cipher import AES 
import base64


def pad(entry):
    padded =  entry + (16-len(entry)%16)*'['
    return padded

def EncryptText(key_ecb):
    #Getting text from user to encrypt
    plain_text = input("Shkruani tekstin qe po deshironi t'a enkriptoni: ")
    plain_text = pad(plain_text)
    plain_text = plain_text.encode('UTF-8')

    #Encryption with AES(mode ecb)
    cipher_ecb = AES.new(key_ecb, AES.MODE_ECB)
    ciphertext = cipher_ecb.encrypt(plain_text)
    return base64.b64encode(ciphertext).decode('UTF-8')

def DecryptText(key_ecb, ciphertext):
    #decryption with aes mode ecb
    cipher_ecb = AES.new(key_ecb, AES.MODE_ECB)
    data = cipher_ecb.decrypt(base64.b64decode(ciphertext.encode('utf-8')))
    unpad = data.find('['.encode('utf-8'))
    data = data[:unpad]
    return data.decode('utf-8')

#key generation
key_ecb=input("Jepni celesin qe do ta perdorni per enkriptim/dekriptim: ")
key_ecb=pad(key_ecb)
key_ecb=key_ecb.encode('UTF-8')

encrypt_or_decrypt=input("\nA po deshironi te enkriptoni apo te dekriptoni tekst\n Shtyp E(Enkriptim) ose D(Dekriptim): ").lower()

if encrypt_or_decrypt=='e':
    #Function call
    encrypted_message = EncryptText(key_ecb)
    print(encrypted_message)

elif encrypt_or_decrypt=='d':
    a=True
    continue_decrypt = input("\nA po deshironi te vazhoni me dekriptim: [p/j] ").lower()

    #Checking if user wants to decrypt or not
    while a == True:
        if continue_decrypt=="p":
            try:
                Decrypt_Text = input("\nShkruani textin qe po deshironi ta dekriptoni: ")
                decript_msg = DecryptText(key_ecb,Decrypt_Text)
                print(decript_msg)
                a=False
            except:
                print("E dhena duhet te jete e enkriptuar me modin ECB")

        elif continue_decrypt=="j":
            print("Programi ka perfunduar!")
            a=False

        else:
            continue_decrypt = input("\nA po deshironi te dekriptoni:\nJu lutemi shtypni j (per jo) ose p (per po):")
