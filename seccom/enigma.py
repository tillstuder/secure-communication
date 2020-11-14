class EnigmaCipher():
    """
    Use the Enigma Cipher Service like this:

    ec = EnigmaCipher(key, peer_public_key, my_public_key, message, mode)
        key needs to be an integer
        peer_public_key needs to be an integer
        my_public_key needs to be an integer
        message needs to be a String
        mode needs to be either "real" or "demo"

    With the Service you can:
        encrypt messages:
        ec.encrypt()

        decrypt messages:
        ec.decrypt()
    """
    def __init__(self, key, peer_pkey, my_pkey, message, mode):
        #Define (shuffeled) Alphabets of the Rotors and Reflector
        self.alpha = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,!?()[]@#¢´`^+-*/'$_:;üÜäÄöÖéÉèÈáÁç&1234567890")
        self.r1alpha = ("C10:z?3fG(é)&eTI´;h7MKg]yjáÄA+5äo#Rr u@iÉ.ZmFSY*ÖDöaswÜ[N-¢nL4$ÁH,lEp68üVbPèqOçB/xÈkX!2JcdU'Q9`^tW_v")
        self.r2alpha = ("(L^q8gSçZ2hr?jKkYfzs$tCÖu/'+v9Wä*GJAHbOiénNáeöQ¢-0&@üXm3Uè5.7#]_4EÁDdcÜxplw!6[P;)B´,V` oFRMaIyTÄÉ1:È")
        self.r3alpha = (":(EiP0'a-Èx!)dztmR¢@äV?2G7áJfveW;yçOÄ5T1UXÖÁLég.4[uYcw&üSKÜ3#qNjBAQpDö]FÉ9´ è_l`8*+rbHhs^Mk,IZ$6nC/o")
        self.refalpha = ("]BW!-äreTQ8ÜS)hC ¢q[vam&Á*RJx59ZLUXèw3zbüPNDVáÉ0u1:g4@`´s6dlfA/kMÄt7#H2pEcçO$ÈÖjoöK_?,(F^;n+éY'IyG.i")
        #Source for Shuffeling the Alphabet: https://onlinerandomtools.com/shuffle-letters
        self.charamount = len(self.alpha)
        self.pos1 = key % self.charamount
        self.pos2 = peer_pkey % self.charamount
        self.pos3 = my_pkey % self.charamount
        self.ref = (key + peer_pkey + my_pkey) % self.charamount
        self.message = message
        self.mode = mode

    def encrypt(self):
        result = ""
        r1shift = self.pos1
        r2shift = self.pos2
        r3shift = self.pos3

        for letter in self.message:
            if letter not in self.alpha:
                result += letter  # adding Character to result if not in Alphabet list
            else:
                r1out = self.r1alpha[(self.alpha.index(letter)+r1shift) % self.charamount]  # Encryption of Rotor 1
                r2out = self.r2alpha[(self.alpha.index(r1out)+r2shift) % self.charamount]  # Encryption of Rotor 2
                r3out = self.r3alpha[(self.alpha.index(r2out)+r3shift) % self.charamount]  # Encryption of Rotor 3
                reflection = self.refalpha[(self.alpha.index(r3out)+self.ref) % self.charamount]  # Reflection into other direction
                r3in = self.r3alpha[(self.alpha.index(reflection)+r3shift) % self.charamount]  # Encryption of Rotor 3
                r2in = self.r2alpha[(self.alpha.index(r3in)+r2shift) % self.charamount]  # Encryption of Rotor 2
                r1in = self.r1alpha[(self.alpha.index(r2in)+r1shift) % self.charamount]  # Encryption of Rotor 1

                # Stepping to next rotation position
                r1shift += 1
                if r1shift == self.charamount:
                    r1shift = 0
                    r2shift += 1
                if r2shift == self.charamount:
                    r2shift = 0
                    r3shift += 1
                if r3shift == self.charamount:
                    r3shift = 0

                result += r1in
        return result

    def decrypt(self):
        result = ""
        if self.mode == "real":  # Checking mode for setting Rotor Positions
            r1shift = self.pos1
            r2shift = self.pos3
            r3shift = self.pos2
        else:
            r1shift = self.pos1
            r2shift = self.pos2
            r3shift = self.pos3

        for letter in self.message:
            if letter not in self.alpha:
                result += letter  # adding Character to result if not in Alphabet list
            else:
                r1out = self.alpha[self.r1alpha.index(letter)-r1shift]  # Encryption of Rotor 1
                r2out = self.alpha[self.r2alpha.index(r1out)-r2shift]  # Encryption of Rotor 2
                r3out = self.alpha[self.r3alpha.index(r2out)-r3shift]  # Encryption of Rotor 3
                reflection = self.alpha[self.refalpha.index(r3out)-self.ref]  # Reflection into other direction
                r3in = self.alpha[self.r3alpha.index(reflection)-r3shift]  # Encryption of Rotor 3
                r2in = self.alpha[self.r2alpha.index(r3in)-r2shift]  # Encryption of Rotor 2
                r1in = self.alpha[self.r1alpha.index(r2in)-r1shift]  # Encryption of Rotor 1

                # Stepping to next rotation position
                r1shift += 1
                if r1shift == self.charamount:
                    r1shift = 0
                    r2shift += 1
                if r2shift == self.charamount:
                    r2shift = 0
                    r3shift += 1
                if r3shift == self.charamount:
                    r3shift = 0

                result += r1in
        return result
