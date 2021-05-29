import numpy as np
import math


def gcd_extended(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for gcd_extended equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)


def true_reverse(key, alphabet):
    key_true_rev = np.linalg.inv(key)
    det = round(np.linalg.det(key))
    key_true_rev = np.round(key_true_rev * det)
    x, y, a = gcd_extended(len(alphabet), round(det) % len(alphabet))
    key_true_rev *= y
    key_true_rev = np.round(key_true_rev) % len(alphabet)
    return key_true_rev


def hill_encode(phrase, alphabet, key):
    n = len(key)
    while(len(phrase) % n != 0):
        phrase += '.'
    ans = ''
    block = list()
    for i in range(len(phrase)):
        block.append(alphabet.find(phrase[i]))
        if i % n == n-1:
            block = np.array(block)
            block = block.dot(key)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
    return ans


def hill_decode(phrase, alphabet, key):
    key_true_rev = true_reverse(key, alphabet)
    n = len(key)
    if len(phrase) % n != 0:
        raise TypeError('Invalid phrase to decode')
    ans = ''
    block = list()
    for i in range(len(phrase)):
        block.append(alphabet.find(phrase[i]))
        if i % n == n-1:
            block = np.array(block)
            block = block.dot(key_true_rev)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
    return ans


def req_hill_encode(phrase, alphabet, key1, key2):
    n = len(key1)
    while(len(phrase) % n != 0):
        phrase += '.'
    ans = ''
    block_count = 0
    block = list()
    for i in range(len(phrase)):
        block.append(alphabet.find(phrase[i]))
        if i % n == n-1:
            block = np.array(block)
            if (block_count == 0):
                key = key1
            elif (block_count == 1):
                key = key2
            else:
                key = np.round(key2.dot(key1)) % len(alphabet)
                key1, key2 = key2, key
            block = block.dot(key)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
            block_count += 1
    return ans


def req_hill_decode(phrase, alphabet, key1, key2):
    n = len(key1)
    if len(phrase) % n != 0:
        raise TypeError('Invalid phrase to decode')
    ans = ''
    block_count = 0
    block = list()
    for i in range(len(phrase)):
        block.append(alphabet.find(phrase[i]))
        if i % n == n-1:
            block = np.array(block)
            if (block_count == 0):
                key = key1
            elif (block_count == 1):
                key = key2
            else:
                key = np.round(key2.dot(key1)) % len(alphabet)
                key1, key2 = key2, key
            key = true_reverse(key, alphabet)
            block = block.dot(key)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
            block_count += 1
    return ans


def main():
    print('Choose cipher:')
    print('0 -- Hill cipher')
    print('1 -- Hill recurrent cipher')
    cipher_type = int(input())
    if cipher_type < 0 or cipher_type > 1:
        raise TypeError('Unknown cipher')

    print('Choose language:')
    print('0 -- RUS(extended)')
    print('1 -- ENG(extended)')
    language = int(input())
    if language == 0:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?&'
    elif language == 1:
        alphabet = 'abcdefghijklmnopqrstuvwxyz.,?'
    else:
        raise TypeError('Unknown language')

    print('Cipher/Decipher? -- 0/1')
    cipher_mode = int(input())
    if cipher_mode < 0 or cipher_mode > 1:
        raise TypeError('Unknown mode')

    print('Input phrase:')
    phrase = str(input())

    print('Input size of key matrix:')
    n = int(input())

    print('Input key matrix:')
    key = list()
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            raise TypeError('Invalid size')
        key.append(row)
    key = np.array(key)
    key = np.round(key) % len(alphabet)
    if math.gcd(int(np.linalg.det(key)), len(alphabet)) != 1:
        raise TypeError('Invalid key')

    if cipher_type == 0:
        if cipher_mode == 0:
            print(hill_encode(phrase, alphabet, key))
        else:
            print(hill_decode(phrase, alphabet, key))

    elif cipher_type == 1:
        print('Input second key matrix:')
        key2 = list()
        for i in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                raise TypeError('Invalid size')
            key2.append(row)
        key2 = np.array(key2)
        key2 = np.round(key2) % len(alphabet)
        if math.gcd(int(np.linalg.det(key2)), len(alphabet)) != 1:
            raise TypeError('Invalid key')
        if (len(key) != len(key2)):
            raise TypeError('Invalid key len')

        if cipher_mode == 0:
            print(req_hill_encode(phrase, alphabet, key, key2))
        else:
            print(req_hill_decode(phrase, alphabet, key, key2))


if __name__ == '__main__':
    main()
