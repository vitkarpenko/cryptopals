"""Single-byte XOR cipher.
"""

from collections import Counter
import os


ENCODED_STRING = ('1b37373331363f78151b7f2b783431333d'
                  '78397828372d363c78373e783a393b3736')


def generate_decrypted_string(cipher_key, string):
    try:
        return bytes(b1 ^ cipher_key
                     for b1 in bytes.fromhex(string)).decode()
    except UnicodeDecodeError as err:
        pass
    except ValueError as err:
        print(err)


def find_most_frequent_letters_in_txt(path):
    txt_counter = Counter()
    with open(path) as txt:
        for line in txt:
            txt_counter.update(
                character for character in line
            )
    return set(entry[0] for entry in txt_counter.most_common(10))


def find_best_cipher_keys(frequent_letters, string):
    cipher_key_ranking = dict()
    for cipher_key in range(256):
        decrypted_string = generate_decrypted_string(cipher_key,
                                                     string)
        decrypted_string_counter = Counter(decrypted_string)
        most_frequent_string_letters = set(
            entry[0]
            for entry in decrypted_string_counter.most_common(10)
        )
        cipher_key_ranking[cipher_key] = len(
            frequent_letters & most_frequent_string_letters
        )

    maximum_frequency_likeness = max(cipher_key_ranking.values())
    if maximum_frequency_likeness == 0:
        return []

    return [
        key
        for key, value in cipher_key_ranking.items()
        if value == maximum_frequency_likeness
    ]


def main():
    most_frequent_book_letters = find_most_frequent_letters_in_txt(
        os.path.join('data', 'book.txt')
    )

    best_cipher_keys = find_best_cipher_keys(most_frequent_book_letters,
                                             ENCODED_STRING)

    for key in best_cipher_keys:
        print(generate_decrypted_string(key, ENCODED_STRING))


if __name__ == '__main__':
    main()
