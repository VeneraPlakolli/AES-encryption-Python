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


key = int(input("Shkruani nje celes ne intervalin 1-255: "))
filename = input("Shkruani emrin e file: ")
Encrypt(filename, key)
