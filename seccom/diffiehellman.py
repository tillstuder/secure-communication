"""
Use the Diffie-Hellman Service like this:

dh = DiffieHellman(g, n)
    n needs to be a large prime number
    g needs to be primitive mod n

With the Service you can:
    generate private keys:
    dh.gen_private_key()

    generate public keys:
    dh.gen_public_key(my_private_key)

    generate the shared key:
    dh.gen_key(my_private_key, peer_public_key)
"""
import random


class DiffieHellman():
    def __init__(self, g, n):
        # "The number (n − l)/2 should also be a prime [1253]." Page 298 "Applied Cryptography" Bruce Schneier
        self.n = n
        self.g = g

    def gen_private_key(self):
        private_key = random.randint(5, 10)
        return private_key

    def gen_public_key(self, my_private_key):
        public_key = (self.g**my_private_key) % self.n
        return public_key

    def gen_key(self, my_private_key, peer_public_key):
        key = (int(peer_public_key)**int(my_private_key)) % self.n
        return key


def _theory():
    # Theory: https://www.youtube.com/watch?v=Yjrfm_oRO0w
    g = random.randint(0, 9)

    # "The number (n − l)/2 should also be a prime [1253]." Page 298 "Applied Cryptography" Bruce Schneier
    
    n = 1001000000000000

    alice_private_key = random.randint(5, 10)
    bob_private_key = random.randint(10, 20)

    alice_public_key = (g**alice_private_key) % n
    bob_public_key = (g**bob_private_key) % n

    k_alice = (bob_public_key**alice_private_key) % n
    k_bob = (alice_public_key**bob_private_key) % n

    assert k_alice == k_bob
    print(k_alice == k_bob)


