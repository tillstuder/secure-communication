# Python Reference: https://docs.python.org/3.4/library/
from seccom.diffiehellman import DiffieHellman
import random

# Mode selection
real = "real"
simulation = "simulation"

mode = input("Please select the mode [{}/{}]: ".format(real, simulation))
assert mode == real or mode == simulation  # Validting the user input


if mode == real:
    # Key Exchange
    dh = DiffieHellman()

    my_public_key = dh.get_public_key()
    print("My Public Key:\n--------------\n{}\n--------------\n".format(my_public_key))

    peer_public_key = input("My Peer's public Key: ")
    key = dh.get_shared_key(peer_public_key)
    print("Our Shared Key:\n--------------\n{}\n--------------\n".format(key))


    # Send and receive messages
    # ...

if mode == simulation:
    print("WORK IN PROGRESS")
    pass
