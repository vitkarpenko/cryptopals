"""Break repeating-key XOR.
"""

import base64
from collections import Counter
import os
import string


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
    columns = [
        buffer[i::key_length]
        for i in range(key_length)
    ]
    return sum(
        compute_coincidence_index(column) / len(columns)
        for column in columns
    )


with open(os.path.join('data', 'challenge_6.txt')) as data:
    data = base64.b64decode(data.read())
for k in range(2, 40):
    print(compute_cipher_key_IC(data, k))
