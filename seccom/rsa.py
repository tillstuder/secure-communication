"""
Use the RSA Cypher Service like this:

rsa = RSACypher(d, e, m, n)
    m needs to be a Message
    i needs to be an integer

With the Service you can:
    encrypt messages:
    cc.encrypt(m,i)

    decrypt messages:
    cc.decrypt(m,i)
"""