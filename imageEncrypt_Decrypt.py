def Encrypt(filename, key):
    file = open(filename, 'rb')
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("ENC-"+filename, 'wb')
    file.write(data)
    file.close()
   

def Decrypt(filename, key):
    file = open(filename, 'rb')
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, 'wb')
    file.write(data)
    file.close()

a=True
while a==True:
    key = int(input("Shkruani nje celes ne intervalin 1-255: "))
    if key <=255 & key>=1:
        filename = input("Shkruani emrin e file: ")
        Encrypt(filename, key)
        a=False
    else:
        key = int(input("Ju lutemi shkruani nje celes ne intervalin 1-255: "))
        a=True

    
