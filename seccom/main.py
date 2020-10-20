# Python Reference: https://docs.python.org/3.4/library/
from seccom.diffiehellman import DiffieHellman
from seccom.caesar import CaesarCipher

# Mode selection loop until mode valid
while True:
    modelist = ['real', 'demo'] # Define mode list
    mode = input("Please select the mode [Real, Demo]: ").lower() # Get User prefered mode
    
    # Check if mode is valid
    if mode in modelist:
        break
    else:
        print ("mode unknown!")

if mode == "real":
    # Key Exchange
    dh = DiffieHellman()

    my_public_key = dh.get_public_key()
    print("My Public Key:\n--------------\n{}\n--------------\n".format(my_public_key))

    peer_public_key = input("My Peer's public Key: ")
    key = dh.get_shared_key(peer_public_key)
    print("Our Shared Key:\n--------------\n{}\n--------------\n".format(key))
    
    # WIP...

#Run if mode is "demo"
if mode == "demo":
    my_dh = DiffieHellman()
    partner_dh = DiffieHellman()

    #Creating Keys
    my_public_key = my_dh.get_public_key()
    print("My Public Key:\n--------------\n{}\n--------------\n".format(my_public_key))

    peer_public_key = partner_dh.get_public_key()
    key = my_dh.get_shared_key(peer_public_key)
    print("Our Shared Key:\n--------------\n{}\n--------------\n".format(key))

#infinite Loop While Session is Running
while True:
    #Define Cypher mode
    while True:
        cypherlist = ['1', '2', '3', 'x'] # Define cypher list
        print ("1: Caesar Cypher\n2: Enigma Cypher\n3: RSA Cypher\nx: End Session") # Print Cypher modes
        cypher = input("Please select your mode [1, 2, 3, x]: ") # Get User Cypher

        # Check if mode is valid
        if cypher in cypherlist:
            break
        else:
            print ("Cypher unknown!")

    #exit code if cypher is 'x'
    if cypher == 'x':
        print("session closed")
        if mode == "real":
            print("Please tell your Partner to end the session")
        break

    #Define Type
    while True:
        crypttypelist = ['1', '2'] # Define type list
        print ("1: Encrypt Message\n2: Decrypt Message") # Print Types
        crypttype = input("Please select your mode [1, 2]: ") # Get Type

        # Check if Type is valid
        if crypttype in crypttypelist:
            break
        else:
            print ("Type unknown!")

    #Define Message
    message = input("Please enter your Message here:\n")

    #Run Caesar Cypher
    if cypher == '1':
        cc = CaesarCipher(message, key)
        if crypttype == '1':
            text = cc.encrypt()
            print ("Deine verschlüsselte Nachricht:\n-----------\nCaesar Cypher:\n{}\n-----------\nBitte sende diesen Text an deinen Partner".format(text))
        else:
            text = cc.decrypt()
            print ("Deine entschlüsselte Nachricht:\n-----------\n{}\n-----------\n".format(text))

    if cypher == '2':
        cc = CaesarCipher(message, key)
        if crypttype == '1':
            text = cc.encrypt()
            print ("Deine verschlüsselte Nachricht:\n-----------\nCaesar Cypher:\n{}\n-----------\nBitte sende diesen Text an deinen Partner".format(text))
        else:
            text = cc.decrypt()
            print ("Deine entschlüsselte Nachricht:\n-----------\n{}\n-----------\n".format(text))
