"""Detect single-character XOR.
"""

import os

import challenge_3


def decrypt_all_strings(path):
    most_frequent_book_letters = challenge_3.find_most_frequent_letters_in_txt(
        os.path.join('data', 'book.txt')
    )

    with open(path) as data:
        for line in data:
            line = line.rstrip('\n')
            best_cipher_keys = challenge_3.find_best_cipher_keys(
                most_frequent_book_letters,
                line
            )
            for key in best_cipher_keys:
                print(challenge_3.generate_decrypted_string(key, line))


def main():
    decrypt_all_strings(os.path.join('data', 'challenge_4.txt'))


if __name__ == '__main__':
    main()
