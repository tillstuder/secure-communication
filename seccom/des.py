class DESCipher():
    """
    Use the DES Cipher Service like this:

    des = DESCipher(message)
        message needs to be a String

    With the Service you can:
        encrypt messages:
        des.encrypt()

        decrypt messages:
        des.decrypt()
    """

    def __init__(self, message):
        self.message = message

    def encrypt(self):
        return result

    def decrypt(self):
        return result


block_initial_premutation_matrix = [
    # form Applied Cryptography, Bruce Schneier, Table 12.1
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

key_initial_premutation_matrix = [
    # form Applied Cryptography, Bruce Schneier, Table 12.2
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

key_shift_matrix = [
    # from Applied Cryptography, Bruce Schneier, Table 12.3
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

key_compression_premutation_map = {
    # from Applied Cryptography, Bruce Schneier, Table 12.4
    # old_position: new_position,
    14: 1, 17: 2, 11: 3, 24: 4, 1: 5, 5: 6, 3: 7, 28: 8, 15: 9, 6: 10, 21: 11, 10: 12,
    23: 13, 19: 14, 12: 15, 4: 16, 26: 17, 8: 18, 16: 19, 7: 20, 27: 21, 20: 22, 13: 23, 2: 24,
    41: 25, 52: 26, 31: 27, 37: 28, 47: 29, 55: 30, 30: 31, 40: 32, 51: 33, 45: 34, 33: 35, 48: 36,
    44: 37, 49: 38, 39: 39, 56: 40, 34: 41, 53: 42, 46: 43, 42: 44, 50: 45, 36: 46, 29: 47, 32: 48
}

def _function_f():
    # shift the key key_bits
    # select 48 key_bits of the key
    # expand right half to 48 bit via expansion premutation
    # combine with 48 key_bits of a shifted and permuted key via an XOR
    # send through 8 S-boxes producing 32 new key_bits
    # permuted again
    pass

def _shift(the_string, shift_amount):
    # shift a string to the left a certain amount of characters
    assert len(the_string) >= shift_amount
    return the_string[shift_amount:] + the_string[:shift_amount]

def _generate_sub_keys(key_bits):
    # divide key in the 28-bit halfs
    left_half, right_half = key_bits[:int(len(key_bits)/2)], key_bits[int(len(key_bits)/2):]

    # shift both halfs to left based on round and do compression premutation
    sub_keys = []
    for i in range(16):
        ## shifting
        shift_amount = key_shift_matrix[i]

        shifted_left_half = _shift(left_half, shift_amount)
        shifted_right_half = _shift(right_half, shift_amount)

        shifted_sub_key = shifted_left_half + shifted_right_half
        
        ## compression premutation
        ### create a map of which bit has to go to which position
        bit_pairs = {}
        bit_location = 0
        for bit in shifted_sub_key:
            bit_location += 1
            try:
                new_bit_location = key_compression_premutation_map[bit_location]
                bit_pairs.update({new_bit_location: bit})
            except KeyError:
                pass
        assert len(bit_pairs) == 48

        ### use the map to create the subkey
        sub_key = ""
        for i in range(48):
            sub_key += bit_pairs[i + 1]
        
        ## add the subkey to the subkeys list
        sub_keys.append(sub_key)

    return sub_keys


def _main(block, key):
    # check if block and key is 64bit
    if block.bit_length() != 64:
        raise "Block should be 64 bits long"
    if key.bit_length() != 64:
        raise "Key should be 64 bits long"

    # converting the key and block into a string of its bits
    key_bits = str(bin(key))
    key_bits = key_bits.lstrip('-0b')

    block_bits = str(bin(block))
    block_bits = block_bits.lstrip('-0b')

    # initial permutation of the block
    ## create a map of which bit has to go to which position 
    bit_pairs = {}
    bit_position = 0
    for bit in block_bits:
        bit_position += 1
        new_bit_position = block_initial_premutation_matrix[int(bit_position) - 1]
        bit_pairs.update({new_bit_position: bit})
    
    ## use the map to create the premutated block
    premutated_block = ""
    for i in range(48):
        premutated_block += bit_pairs[i + 1]

    # make input key (64bit) to 56bit (every 8th bit is ignored)
    bit_position = 0
    new_key_bits = ""
    for key_bit in key_bits:
        bit_position += 1
        if bit_position not in [8, 16, 24, 32, 40, 48, 56, 64]:
            new_key_bits += key_bit
        else:
            pass
    assert bit_position == 64  # checking if the last processed bit is the 64th bit
    assert len(new_key_bits) == 56  # checking if the new key is 56 bits long

    # generating the keys for each round
    sub_keys = _generate_sub_keys(new_key_bits)
    
    # split block into left and right half
    left_half_block, right_half_block = premutated_block[:int(len(premutated_block)/2)], premutated_block[int(len(premutated_block)/2):]

    # check if half's are 32 bit
    assert len(left_half_block) == 32
    assert len(right_half_block) == 32

    # E-box (Expansion Permutation)
    # ..... The Expansion Permutation, P.161

    # the 16 rounds
    rounds = 16
    for i in range(rounds):
        f_output = _function_f()
        # combine output with left half via XOR
        # the result of that XOR is the new right half and the old right half becomes the new left half

    # join left and right half
    # final permutation (the inverse of the initial permutation)


if __name__ == "__main__":
    _main(block=12312345612345645672, key=12345678912345678121)
