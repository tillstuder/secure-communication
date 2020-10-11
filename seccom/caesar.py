"""
Use the Ceasar Cipher Service like this:

cc = CaesarCipher(m, i)
    m needs to be a Message
    i needs to be an integer

With the Service you can:
    encrypt messages:
    cc.encrypt(m,i)

    decrypt messages:
    cc.decrypt(m,i)
"""

class CaesarCipher():
    def __init__(self, message, shift):
        self.message = message
        self.shift = shift

    def encrypt(self):
        result = ''
        for letter in self.message:
            if ord(letter) < 65 or ord(letter) > 90 and ord(letter) < 97 or ord(letter) > 122:
                result += letter
            elif letter.isupper():
                result += chr((ord(letter) + self.shift - 65) % 26 + 65)
            else:
                result += chr((ord(letter) + self.shift - 97) % 26 + 97)
        return result
    
    def decrypt(self):
        result = ''
        for letter in self.message:
            if ord(letter) < 65 or ord(letter) > 90 and ord(letter) < 97 or ord(letter) > 122:
                result += letter
            elif letter.isupper():
                result += chr((ord(letter) - self.shift - 65) % 26 + 65)
            else:
                result += chr((ord(letter) - self.shift - 97) % 26 + 97)
        return result



# insert following into main.py

message = input("Please enter your Text: ") #encrypted or decrypted message
shift = int(input("Enter a shift number: ")) # Must be the same on both sites

encrypt = "encrypt"
decrypt = "decrypt"
mode = input("Please select the mode [{}/{}]: ".format(encrypt, decrypt))
assert mode == encrypt or mode == decrypt  # Validting the user input

cc = CaesarCipher(message,shift)

if mode == encrypt:
    print ("Klartext: " + message)
    print ("Verschlüsselter Text: " + cc.encrypt())
else:
    print ("Verschlüsselter Text: " + message)
    print ("klartext: " + cc.decrypt())

