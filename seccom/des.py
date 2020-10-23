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

key_compression_premutation_matrix = [
    # from Applied Cryptography, Bruce Schneier, Table 12.4
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]


block_expansion_permutation_matrix = [
    # from Applied Cryptography, Bruce Schneier, Table 12.5
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]


block_substitution_boxes = [
    # from Applied Cryptography, Bruce Schneier, Table 12.6
    [
        # S-box 1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        # S-box 3
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        # S-box 3
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        # S-box 4
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        # S-box 5
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        # S-box 6
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        # S-box 7
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        # S-box 8
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]


block_p_box = [
    # from Applied Cryptography, Bruce Schneier, Table 12.7
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]


block_final_premutation_matrix = [
    # from Applied Cryptography, Bruce Schneier, Table 12.8
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]


# actions
encrypt = 1
decrypt = 0


class DESCipher():
    """
    Use the DES Cipher Service like this:

    des = DESCipher(key)
        key needs to be 64 bits long

    With the Service you can:
        encrypt messages:
        des.encrypt(plain_text)

        decrypt messages:
        des.decrypt(cypher_text)
    """

    def __init__(self, key):
        if len(key) < 8:
            raise Warning("The key should be 64 bits long")
        elif len(key) > 8:
            # If key size is above 64 bits, cut it to 64 bits
            print("INFO: Key was cut to 64bits in length.")
            key = key[:8]

        self.password = key

    def encrypt(self, plain_text):
        return self._main(plain_text, encrypt)

    def decrypt(self, cypher_text):
        return self._main(cypher_text, decrypt)

    def _main(self, text, action):
        self.text = text

        # The Key Transformation
        self._generate_subkeys()

        # splitting the text in blocks of 64 bits
        text_blocks = self._nsplit(self.text, 8)

        result = []
        for block in text_blocks:
            # convert input
            block = self._get_bit_list(block)

            # The Initial Permutation
            block = self._permutate_or_expand(
                block, block_initial_premutation_matrix)
            left, right = self._nsplit(block, 32)

            tmp = None
            rounds = range(16)
            for round in rounds:
                # The Expansion Permutation
                right_expanded = self._permutate_or_expand(
                    right, block_expansion_permutation_matrix)

                # deside which key to use
                if action == encrypt:
                    round_key = self.keys[round]
                else:
                    # if decrypt start with the last key
                    round_key = self.keys[15-round]

                # XOR round_key with right_expanded
                xored_list = self._xor_list(round_key, right_expanded)

                # The S-Box Substitution
                substituted_block = self._substitute(xored_list)

                # The P-Box Permutation
                premutated_block = self._permutate_or_expand(
                    substituted_block, block_p_box)

                block = self._xor_list(left, premutated_block)
                left = right
                right = block

            # The Final Permutation
            block = self._permutate_or_expand(
                right+left, block_final_premutation_matrix)

            # add to the other text blocks
            result += block

        # convertign the blocks into a string
        final_res = self._get_string(result)

        return final_res

    def _substitute(self, right_expanded):
        """substitute the bit list using the S-boxes"""

        # split the right block into sublist of 6 bits
        sub_blocks = self._nsplit(right_expanded, 6)

        result = []
        for round in range(len(sub_blocks)):
            # get block
            block = sub_blocks[round]

            # get row with from first and last bit
            first_bit = str(block[0])
            last_bit = str(block[5])
            row = int(first_bit + last_bit, 2)

            # get the column (the 2,3,4,5 bits)
            second_to_fifth_bits = block[1:][:-1]
            second_to_fifth_bits_as_strings = [
                str(bit) for bit in second_to_fifth_bits]
            second_to_fifth_bits_as_one_string = ''.join(
                second_to_fifth_bits_as_strings)
            column = int(second_to_fifth_bits_as_one_string, 2)

            # get the right S-Box value with round, row and column
            value = block_substitution_boxes[round][row][column]

            # convert the value to binary
            bin = self._get_bin_value(value, 4)

            # separate the bits
            bits_list = [int(bit) for bit in bin]

            # add to result list
            result += bits_list
        return result

    def _permutate_or_expand(self, block, matrix):
        """premutates or expands (works exactly the same) the given block using the given matrix"""
        new_block = [
            block[position - 1]
            for position in matrix
        ]
        return new_block

    def _xor_list(self, first_list, second_list):
        tuples = zip(first_list, second_list)
        xored = [first_value ^ second_value for first_value,
                 second_value in tuples]
        return xored

    def _generate_subkeys(self):
        """Generates all 16 keys."""
        self.keys = []
        key = self._get_bit_list(self.password)
        # Apply the initial permutate on the key
        key = self._permutate_or_expand(key, key_initial_premutation_matrix)

        left, right = self._nsplit(key, 28)
        rounds = range(16)
        for round in rounds:
            shift_amount = key_shift_matrix[round]
            left_shifted = self._shift(left, shift_amount)
            right_shifted = self._shift(right, shift_amount)
            shifted = left_shifted + right_shifted

            premutated = self._permutate_or_expand(
                shifted, key_compression_premutation_matrix)
            self.keys.append(premutated)

    def _shift(self, the_list, shift_amount):
        """shift a list to the left a certain amount"""
        the_list_shifted = the_list[shift_amount:] + the_list[:shift_amount]
        return the_list_shifted

    def _get_bit_list(self, text):
        """converts a string into a list of bits

        it's the reverse function of self._get_string()
        """
        bit_list = []
        for char in text:
            bin_val = self._get_bin_value(char, 8)

            # Add the char bits to bit_list
            char_bits = [int(bit) for bit in list(bin_val)]
            bit_list.extend(char_bits)
        return bit_list

    def _get_string(self, the_list):
        """converts a bit list into a string

        it's the reverse function of self._get_bit_list()
        """
        byte_bits_list = self._nsplit(the_list, 8)

        bytes_list = []
        for bit_list in byte_bits_list:
            bit_list_as_strings = [str(bit) for bit in bit_list]
            byte = "".join(bit_list_as_strings)
            bytes_list.append(byte)

        chars = ""
        for byte in bytes_list:
            ascii_nr = int(byte, 2)
            char = chr(ascii_nr)
            chars += char

        return chars

    def _get_bin_value(self, value, bit_size):
        """returns the binary value as a string"""
        # converting value into binary
        if isinstance(value, int):
            bits = bin(value)
            bin_val = bits[2:]  # removing the "0b"
        else:
            unicode_nr = ord(value)
            bits = bin(unicode_nr)
            bin_val = bits[2:]  # removing the "0b"

        # check if binary value is larger than the expected bit size
        if len(bin_val) > bit_size:
            raise Warning("binary value is larger than the expected bit size")

        # add as many 0 as needed to get the wanted size
        while len(bin_val) < bit_size:
            bin_val = "0"+bin_val

        return bin_val

    def _nsplit(self, full_list, size_n):
        """splits a list into sublists of size n"""
        list_range = range(0, len(full_list), size_n)
        sub_lists = [
            full_list[part:part+size_n]
            for part in list_range
        ]
        return sub_lists


if __name__ == '__main__':
    key = "qwe_fgäs"
    message = "sodifjoisdjfoisdjfoisjdfoijsdfoijsdofijsoidfjosdifjosidjfoisdjfo"

    DESService = DESCipher(key)
    cypher_text = DESService.encrypt(message)
    plain_text = DESService.decrypt(cypher_text)

    if message == plain_text:
        print("Works!")
    else:
        print("Doesn't work :/")
