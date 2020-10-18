"""
Use the Enigma Cipher Service like this:

ec = EnigmaCipher(my_public_key, peer_public_key, key, message,)
    my_public_key needs to be an integer
    peer_public_key needs to be an integer
    key needs to be an integer
    message needs to be a String
    pb needs to be a dictionary with 5 values

With the Service you can:
    encrypt messages:
    ec.encrypt()

    decrypt messages:
    ec.decrypt()
"""

class EnigmaCipher():
    def __init__(self, my_public_key, peer_public_key, key, message, pb):
        self.r1 = my_public_key % 26
        self.r2 = peer_public_key % 26
        self.r3 = key % 26
        self.message = message
    
    def encrypt(self):
        result = ''
        for letter in self.message:
            if ord(letter) < 65 or ord(letter) > 90 and ord(letter) < 97 or ord(letter) > 122:
                result += letter
            else:
                letter = letter.lower()
                step0 = ord(letter) - 97
                step1 = (step0 + self.r1 + self.r2 + self.r3 + 32 +self.r3 + self.r2 + self.r1) % 26
                result += chr(step1) + 97
                self.r1 + 1
                if self.r1 == 26:
                    self.r1 = 0
                    self.r2 + 1
                    if self.r2 == 26:
                        self.r2 = 0
                        self.r3 + 1
                        if self.r3 == 26:
                            self.r3 = 0
        return result

    def decrypt(self):
        result = ''
        for letter in self.message:
            if ord(letter) < 65 or ord(letter) > 90 and ord(letter) < 97 or ord(letter) > 122:
                result += letter
            elif letter.isupper():
                result += chr((ord(letter) + self.shift - 65) % 26 + 65)
            else:
                result += chr((ord(letter) + self.shift - 97) % 26 + 97)
        return result