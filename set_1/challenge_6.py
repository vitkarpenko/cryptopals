"""Break repeating-key XOR.
"""

import base64
from collections import Counter
import itertools
import os

import challenge_3


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


def generate_decrypted_string(cipher_key, string):
    try:
        return bytes(b1 ^ cipher_key
                     for b1 in string).decode()
    except UnicodeDecodeError:
        pass
    except ValueError:
        pass


def find_cipher_candidates(buffer, key_length):

    columns = [
        buffer[i::key_length]
        for i in range(key_length)
    ]
    most_frequent_book_letters = challenge_3.find_most_frequent_letters_in_txt(
        os.path.join('data', 'book.txt')
    )

    cipher_candidates = []
    for column in columns:
        best_cipher_keys = challenge_3.find_best_cipher_keys(
            most_frequent_book_letters,
            column
        )
        cipher_candidates.append(best_cipher_keys)
    return [bytes(cc) for cc in itertools.product(*cipher_candidates)]


def decrypt_message(cipher, message):
    return bytes(
        b1 ^ b2
        for b1, b2 in zip(message, itertools.cycle(cipher))
    ).decode()


def main():
    # Some monkey patching.
    challenge_3.generate_decrypted_string = generate_decrypted_string

    with open(os.path.join('data', 'challenge_6.txt')) as data:
        data = base64.b64decode(data.read())

    with open('challenge_6_output.txt', 'w') as output:
        for key_length in find_best_cipher_key_lengths(data):
            for cipher_candidate in find_cipher_candidates(
                    data,
                    key_length):
                output.write(
                    f"For cipher {cipher_candidate}:\n" + 
                    decrypt_message(cipher_candidate, data) +
                    '\n{}\n'.format('='*120)
                )


if __name__ == '__main__':
    main()
