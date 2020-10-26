# Python Reference: https://docs.python.org/3.4/library/
from seccom.diffiehellman import DiffieHellman
from seccom.caesar import CaesarCipher
from seccom.enigma import EnigmaCipher
from seccom.des import DESCipher

# Mode selection loop until mode valid
while True:
    modelist = ["real", "demo"]  # Define mode list
    # Get users preferred mode
    mode = input("Please select the mode [real, demo]: ").lower()

    # Check if mode is valid
    if mode in modelist:
        break
    else:
        print("mode unknown!")

# exchanging the keys
if mode == "real":
    # instantiating the DiffieHellman service
    dh = DiffieHellman()

    # Creating the keys
    my_public_key = dh.get_public_key()
    print("My Public Key:\n--------------\n{}\n--------------\n ".format(my_public_key))

    peer_public_key = int(input("My Peers public Key: "))
    key = dh.get_shared_key(peer_public_key)
    print("Our Shared Key:\n--------------\n{}\n--------------\n ".format(key))

if mode == "demo":
    # instantiating the DiffieHellman services
    my_dh = DiffieHellman()
    partner_dh = DiffieHellman()

    # Creating the keys
    my_public_key = my_dh.get_public_key()
    print("My Public Key:\n--------------\n{}\n--------------\n ".format(my_public_key))

    peer_public_key = partner_dh.get_public_key()
    print("Partner Public Key:\n--------------\n{}\n--------------\n ".format(peer_public_key))

    key = my_dh.get_shared_key(peer_public_key)
    print("Our Shared Key:\n--------------\n{}\n--------------\n ".format(key))


# infinite Loop While Session is Running
while True:
    # Define Cypher mode
    while True:
        cypherlist = ["1", "2", "3", "x"]  # Define cypher list
        # Print Cypher modes
        print("1: Caesar Cypher\n2: Enigma Cypher\n3: DES Cypher\nx: End Session")
        # Get users Cypher
        cypher = input("Please select your mode [1, 2, 3, x]: ")

        # Check if mode is valid
        if cypher in cypherlist:
            break
        else:
            print("Cypher unknown!")

    # exit code if cypher is "x"
    if cypher == "x":
        print("session closed")
        if mode == "real":
            print("Please tell your Partner to end the session too")
        break

    # Define Type
    while True:
        crypt_typelist = ["1", "2"]  # Define type list
        print("1: Encrypt Message\n2: Decrypt Message")  # Print Types
        crypt_type = input("Please select your mode [1, 2]: ")  # Get Type

        # Check if Type is valid
        if crypt_type in crypt_typelist:
            break
        else:
            print("Type unknown!")

    # Define Message
    print("Please enter your Message here:")
    message = input()

    # Run Caesar Cypher
    if cypher == "1":
        cc = CaesarCipher(message, key)
        if crypt_type == "1":
            text = cc.encrypt()
            print("Deine verschlüsselte Nachricht:\n-----------\nCaesar Cypher:\n{}\n-----------\nBitte sende diesen Text an deinen Partner".format(text))
        else:
            text = cc.decrypt()
            print(
                "Deine entschlüsselte Nachricht:\n-----------\n{}\n-----------\n ".format(text))

    # Run Enigma Cypher
    if cypher == "2":
        ec = EnigmaCipher(key, peer_public_key, my_public_key, message, mode)
        if crypt_type == "1":
            text = ec.encrypt()
            print("Deine verschlüsselte Nachricht:\n-----------\nEnigma Cypher:\n{}\n-----------\nBitte sende diesen Text an deinen Partner".format(text))
        else:
            text = ec.decrypt()
            print(
                "Deine entschlüsselte Nachricht:\n-----------\n{}\n-----------\n ".format(text))

    if cypher == "3":
        des = DESCipher(key)
        if crypt_type == "1":
            text = des.encrypt(message)

            # converting the cypher_text to bits, because not every shell can interpret unicode properly
            cypher_text_as_bit_list = des._get_bit_list(text)
            bits = ""
            for bit in cypher_text_as_bit_list:
                bits += str(bit)

            print("Deine verschlüsselte Nachricht:\n-----------\nDES Cypher:\n{}\n-----------\nBitte sende diesen Text an deinen Partner".format(bits))
        else:
            # converting the bits back to cypher_text
            ## splitting the bit stream to individual bits (as strings)
            bits_as_char = [char for char in message]

            ## converting the bits (as strings) to int's
            bits = [int(char) for char in bits_as_char]

            ## converting the bit list to the actual cypher_text
            new_message = des._get_string(bits)

            text = des.decrypt(new_message)
            print("Deine entschlüsselte Nachricht:\n-----------\n{}\n-----------\n ".format(text))
