"""Implement repeating-key XOR.
"""

from itertools import cycle


KEY = bytes('TOTORO', 'utf-8')


def encrypt_repeating_key(buffer, key):
    if (not isinstance(buffer, (bytes, bytearray))
        or not isinstance(key, (bytes, bytearray))):
            raise ValueError('encrypt_repeating_key accepts only byte-like'
                             ' objects as an arguments!')

    return bytes(
        b1 ^ b2
        for b1, b2 in zip(buffer, cycle(key))
    )


def main():
    vulnerable_string = 'koolkackerpazzw0rD!#'
    print(encrypt_repeating_key(buffer=bytes(vulnerable_string, 'utf-8'),
                                key=KEY))


if __name__ == '__main__':
    main()
