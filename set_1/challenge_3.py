"""Single-byte XOR cipher.
"""

from collections import Counter
import operator
import os
import string


ENCODED_STRING = ('1b37373331363f78151b7f2b783431333d'
                  '78397828372d363c78373e783a393b3736')


def calculate_frequency_likeness(counter1, counter2):
    """Finds how many most frequent keys match.
    """
    return sum(1 for c1, c2 in zip(counter1.most_common(),
                                   counter2.most_common()) if c1[0] == c2[0])


def generate_decrypted_string(cipher_key):
    try:
        return bytes(b1 ^ cipher_key
                     for b1 in bytes.fromhex(ENCODED_STRING)).decode().lower()
    except UnicodeDecodeError:
        pass


book_counter = Counter()
with open(os.path.join('data', 'book.txt')) as book:
    for line in book:
        book_counter.update(
            character.lower() for character in line
            if character in string.ascii_letters
        )

cipher_key_ranking = dict()
for cipher_key in range(256):
    decrypted_string = generate_decrypted_string(cipher_key)
    decrypted_string_counter = Counter(decrypted_string)
    cipher_key_ranking[cipher_key] = calculate_frequency_likeness(
        book_counter, decrypted_string_counter
    )

best_cipher_key = max(cipher_key_ranking.items(),
                      key=operator.itemgetter(1))[0]

print(generate_decrypted_string(best_cipher_key))
