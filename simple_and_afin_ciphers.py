import math


def simple_encode(phrase, alphabet, key):
    ans = ''
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) != -1:
            ans += key[alphabet.find(phrase[i])]
        else:
            ans += phrase[i]
    return ans


def simple_decode(phrase, alphabet, key):
    ans = ''
    for i in range(len(phrase)):
        if key.find(phrase[i]) != -1:
            ans += alphabet[key.find(phrase[i])]
        else:
            ans += phrase[i]
    return ans


def simple_key_check(key, alphabet):
    if (len(key) != len(alphabet)):
        raise TypeError('Invalid key (length)')
    for i in range(len(key)):
        if key.find(key[i]) != key.rfind(key[i]) or alphabet.find(key[i]) == -1:
            raise TypeError('Invalid key (symbols)')


def afin_encode(phrase, a, b, alphabet):
    ans = ''
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) != -1:
            ans += alphabet[(a*alphabet.find(phrase[i]) + b) % len(alphabet)]
        else:
            ans += phrase[i]
    return ans


def find_reverse(a, m):
    rev = 0
    while ((rev*a) % m != 1):
        rev += 1
    return rev


def afin_decode(phrase, a, b, alphabet):
    rev = find_reverse(a, len(alphabet))
    ans = ''
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) != -1:
            ans += alphabet[rev*(alphabet.find(phrase[i]) - b) % len(alphabet)]
        else:
            ans += phrase[i]
    return ans


def req_afin_encode(phrase, a1, a2, b1, b2, alphabet):
    ans = ''
    for i in range(len(phrase)):
        if i == 0:
            a = a1
            b = b1
        elif i == 1:
            a = a2
            b = b2
        else:
            a = (a1 * a2) % len(alphabet)
            b = (b1 + b2) % len(alphabet)
            a1, a2 = a2, a
            b1, b2 = b2, b

        if alphabet.find(phrase[i]) != -1:
            ans += alphabet[(a*alphabet.find(phrase[i]) + b) % len(alphabet)]
        else:
            ans += phrase[i]
    return ans


def req_afin_decode(phrase, a1, a2, b1, b2, alphabet):
    ans = ''
    for i in range(len(phrase)):
        if i == 0:
            a = a1
            b = b1
        elif i == 1:
            a = a2
            b = b2
        else:
            a = (a1 * a2) % len(alphabet)
            b = (b1 + b2) % len(alphabet)
            a1, a2 = a2, a
            b1, b2 = b2, b

        rev = find_reverse(a, len(alphabet))
        if alphabet.find(phrase[i]) != -1:
            ans += alphabet[rev*(alphabet.find(phrase[i]) - b) % len(alphabet)]
        else:
            ans += phrase[i]
    return ans


def main():

    print('Choose cipher:')
    print('0 -- Simple change cipher')
    print('1 -- Afin cipher')
    print('2 -- Afin recurrent cipher')
    cipher_type = int(input())
    if cipher_type < 0 or cipher_type > 2:
        raise TypeError('Unknown cipher')

    print('Choose language:')
    print('0 -- RUS')
    print('1 -- ENG')
    language = int(input())
    if language == 0:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    elif language == 1:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    else:
        raise TypeError('Unknown language')

    print('Encode/Decode? -- 0/1')
    cipher_mode = int(input())
    if cipher_mode < 0 or cipher_mode > 1:
        raise TypeError('Unknown mode')

    print('Input phrase:')
    phrase = str(input())

    if cipher_type == 0:
        print('Input key string:')
        key = str(input())  # example: yzabcdefghijklmnopqrstuvwx
        simple_key_check(key, alphabet)
        if (cipher_mode == 0):
            print(simple_encode(phrase, alphabet, key))
        else:
            print(simple_decode(phrase, alphabet, key))

    elif cipher_type == 1:
        print('Input key (a, b):')
        a, b = map(int, input().split())
        if math.gcd(a, len(alphabet)) != 1:
            raise TypeError('Invalid key')

        if cipher_mode == 0:
            print(afin_encode(phrase, a, b, alphabet))
        else:
            print(afin_decode(phrase, a, b, alphabet))
    else:
        print('Input key (a1, a2, b1, b2):')
        a1, a2, b1, b2 = map(int, input().split())
        if math.gcd(a1, len(alphabet)) != 1 or math.gcd(a2, len(alphabet)) != 1:
            raise TypeError('Invalid key')

        if cipher_mode == 0:
            print(req_afin_encode(phrase, a1, a2, b1, b2, alphabet))
        else:
            print(req_afin_decode(phrase, a1, a2, b1, b2, alphabet))


if __name__ == '__main__':
    main()
