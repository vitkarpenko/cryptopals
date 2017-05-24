"""Single-byte XOR cipher.
"""

from collections import Counter
import os


ENCODED_STRING = ('1b37373331363f78151b7f2b783431333d'
                  '78397828372d363c78373e783a393b3736')


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
        )

most_frequent_book_letters = set(
    entry[0]
    for entry in book_counter.most_common(10)
)

cipher_key_ranking = dict()
for cipher_key in range(256):
    decrypted_string = generate_decrypted_string(cipher_key)
    decrypted_string_counter = Counter(decrypted_string)
    most_frequent_string_letters = set(
        entry[0]
        for entry in decrypted_string_counter.most_common(10)
    )
    cipher_key_ranking[cipher_key] = len(
        most_frequent_book_letters & most_frequent_string_letters
    )

maximum_frequency_likeness = max(cipher_key_ranking.values())

best_cipher_keys = [
    key
    for key, value in cipher_key_ranking.items()
    if value == maximum_frequency_likeness
]

for key in best_cipher_keys:
    print(generate_decrypted_string(key))
