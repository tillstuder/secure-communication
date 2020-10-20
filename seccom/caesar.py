"""
Use the Ceasar Cipher Service like this:

cc = CaesarCipher(message, key)
    message needs to be a String
    key needs to be an integer

With the Service you can:
    encrypt messages:
    cc.encrypt()

    decrypt messages:
    cc.decrypt()
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