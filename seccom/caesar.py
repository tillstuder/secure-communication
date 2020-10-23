class CaesarCipher():
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
    # Define Initial Settings
    def __init__(self, message, shift):
        self.message = message
        self.shift = shift
        

    def encrypt(self):
        result = ""
        for letter in self.message:
            if ord(letter) < 65 or ord(letter) > 90 and ord(letter) < 97 or ord(letter) > 122:  # Running if Char is not a Letter
                result += letter
            elif letter.isupper():  # Running if Char is a uppercase Letter
                result += chr((ord(letter) + self.shift - 65) % 26 + 65)  # Encrypting Letter
            else:  # Running if Char is a lowercase Letter
                result += chr((ord(letter) + self.shift - 97) % 26 + 97)  # Encrypting Letter
        return result  # Returning encryptet message
    
    def decrypt(self):
        result = ""
        for letter in self.message:
            if ord(letter) < 65 or ord(letter) > 90 and ord(letter) < 97 or ord(letter) > 122:  # Running if Char is not a Letter
                result += letter
            elif letter.isupper():  # Running if Char is a uppercase Letter
                result += chr((ord(letter) - self.shift - 65) % 26 + 65)  # Decrypting Letter
            else:  # Running if Char is a lowercase Letter
                result += chr((ord(letter) - self.shift - 97) % 26 + 97)  # Decrypting Letter
        return result  # Returning decryptet message
