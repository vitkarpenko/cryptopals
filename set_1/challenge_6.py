"""Break repeating-key XOR.
"""

import base64
from collections import Counter
import os


KEY_LENGTH_DELTA = 0.1


def compute_coincidence_index(buffer):
    """buffer: byte-like object."""
    frequency_distribution = Counter(
        b for b in buffer
    )
    N = len(buffer)
    return sum(
        v * (v - 1) / (N * (N - 1) / len(frequency_distribution))
        for k, v in frequency_distribution.items()
    )


def compute_cipher_key_IC(buffer, key_length):
    """IC stands for 'index of coincidence'.
    https://en.wikipedia.org/wiki/Index_of_coincidence
    """
    columns = [
        buffer[i::key_length]
        for i in range(key_length)
    ]
    return sum(
        compute_coincidence_index(column) / len(columns)
        for column in columns
    )


def find_best_cipher_key_lengths(buffer):
    """For english optimal IC is ~1.73."""
    key_ICs = dict()
    for key_length in range(2, 40):
        key_ICs[key_length] = compute_cipher_key_IC(buffer, key_length)
    return [
        key_length
        for key_length, key_IC in key_ICs.items()
        if abs(key_IC - 1.73) / 1.73 < KEY_LENGTH_DELTA
    ]


def main():
    with open(os.path.join('data', 'challenge_6.txt')) as data:
        data = base64.b64decode(data.read())
    print(find_best_cipher_key_lengths(data))


if __name__ == '__main__':
    main()
