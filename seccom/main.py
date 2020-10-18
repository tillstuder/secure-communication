# Python Reference: https://docs.python.org/3.4/library/
from seccom.diffiehellman import DiffieHellman
from seccom.caesar import CaesarCipher
import random

# Mode selection loop until mode valid
while True:
    modelist = ['real', 'demo'] # Define mode list
    mode = input("Please select the mode [Real, Demo]: ").lower() # Get User prefered mode
    
    # Check if mode is valid
    if mode in modelist:
        break
    else:
        print ("mode unknown!")

#Run if mode is "real"
if mode == "real":
    #Set Diffie Hellman Pre-settings
    g = int(input("Enter a pre-shared Integer between 0 and 9: "))
    # "The number (n − l)/2 should also be a prime [1253]." Page 298 "Applied Cryptography" Bruce Schneier
    n = 285542542228279613901563566102164008326164238644702889199247456602284400390600653875954571505539843239754513915896150297878399377056071435169747221107988791198200988477531339214282772016059009904586686254989084815735422480409022344297588352526004383890632616124076317387416881148592486188361873904175783145696016919574390765598280188599035578448591077683677175520434074287726578006266759615970759521327828555662781678385691581844436444812511562428136742490459363212810180276096088111401003377570363545725120924073646921576797146199387619296560302680261790118132925012323046444438622308877924609373773012481681672424493674474488537770155783006880852648161513067144814790288366664062257274665275787127374649231096375001170901890786263324619578795731425693805073056119677580338084333381987500902968831935913095269821311141322393356490178488728982288156282600813831296143663845945431144043753821542871277745606447858564159213328443580206422714694913091762716447041689678070096773590429808909616750452927258000843500344831628297089902728649981994387647234574276263729694848304750917174186181130688518792748622612293341368928056634384466646326572476167275660839105650528975713899320211121495795311427946254553305387067821067601768750977866100460014602138408448021225053689054793742003095722096732954750721718115531871310231057902608580607
    dh = DiffieHellman(g, n)

    #Creating Keys
    my_private_key = dh.gen_private_key()
    my_public_key = dh.gen_public_key(my_private_key)
    print("My Public Key: {}\nShare your Public Key with your partner".format(my_public_key))
    peer_public_key = int(input("My Peer's public Key: "))
    key = dh.gen_key(my_private_key, peer_public_key)

    #Print the Results
    print("\n\nMy Public Key:\n{}\n".format(my_public_key))
    print("My Peer's public Key:\n{}\n".format(peer_public_key))
    print("Shared Key:\n{}\n".format(key))

#Run if mode is "demo"
if mode == "demo":
    #Set Diffie Hellman Pre-settings
    g = random.randint(0, 9)
    # "The number (n − l)/2 should also be a prime [1253]." Page 298 "Applied Cryptography" Bruce Schneier
    n = 285542542228279613901563566102164008326164238644702889199247456602284400390600653875954571505539843239754513915896150297878399377056071435169747221107988791198200988477531339214282772016059009904586686254989084815735422480409022344297588352526004383890632616124076317387416881148592486188361873904175783145696016919574390765598280188599035578448591077683677175520434074287726578006266759615970759521327828555662781678385691581844436444812511562428136742490459363212810180276096088111401003377570363545725120924073646921576797146199387619296560302680261790118132925012323046444438622308877924609373773012481681672424493674474488537770155783006880852648161513067144814790288366664062257274665275787127374649231096375001170901890786263324619578795731425693805073056119677580338084333381987500902968831935913095269821311141322393356490178488728982288156282600813831296143663845945431144043753821542871277745606447858564159213328443580206422714694913091762716447041689678070096773590429808909616750452927258000843500344831628297089902728649981994387647234574276263729694848304750917174186181130688518792748622612293341368928056634384466646326572476167275660839105650528975713899320211121495795311427946254553305387067821067601768750977866100460014602138408448021225053689054793742003095722096732954750721718115531871310231057902608580607
    dh = DiffieHellman(g, n)

    #Creating Keys
    my_private_key = dh.gen_private_key()
    my_public_key = dh.gen_public_key(my_private_key)
    peer_public_key = random.randint(100, 1000000000000)
    key = dh.gen_key(my_private_key, peer_public_key)

    #Print the Results
    print("\n\nMy Public Key:\n{}\n".format(my_public_key))
    print("Shared Key:\n{}\n".format(key))

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
