"""Fixed XOR.
"""


def buffers_xor(buffer1, buffer2):
    """buffer1, buffer2: byte-like objects.
    """
    try:
        return bytes(b1 ^ b2 for b1, b2 in zip(buffer1, buffer2))
    except TypeError:
        print("Function 'buffers_xor' takes byte-like"
              "objects as an arguments.")


if __name__ == '__main__':
    print(buffers_xor(bytes.fromhex('1c0111001f010100061a024b53535009181c'),
                      bytes.fromhex('686974207468652062756c6c277320657965')))
    print(bytes.fromhex('746865206b696420646f6e277420706c6179'))
