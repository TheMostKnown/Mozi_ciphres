def vizh_encode(phrase, alphabet, key):
    while(len(key) < len(phrase)):
        key += key
    ans = ''
    for i in range(len(phrase)):
        ch_num = alphabet.find(phrase[i]) + alphabet.find(key[i])
        ch_num %= len(alphabet)
        ans += alphabet[ch_num]
    return ans

def vizh_decode(phrase, alphabet, key):
    while(len(key) < len(phrase)):
        key += key
    ans = ''
    for i in range(len(phrase)):
        ch_num = alphabet.find(phrase[i]) - alphabet.find(key[i])
        ch_num %= len(alphabet)
        ans += alphabet[ch_num]
    return ans

def vizh_open_encode(phrase, alphabet, key):
    if len(key) != 1:
        raise TypeError("Invalid key (len)")
    key += phrase
    ans = vizh_encode(phrase, alphabet, key)
    return ans

def vizh_open_decode(phrase, alphabet, key):
    if len(key) != 1:
        raise TypeError("Invalid key (len)")
    ans = ''
    ch_num = alphabet.find(phrase[0]) - alphabet.find(key[0])
    ch_num %= len(alphabet)
    key += alphabet[ch_num]
    ans += alphabet[ch_num]
    for i in range(len(phrase) - 1):
        ch_num = alphabet.find(phrase[i+1]) - alphabet.find(key[-1])
        ch_num %= len(alphabet)
        key += alphabet[ch_num]
        ans += alphabet[ch_num]
    return ans

def vizh_cipher_encode(phrase, alphabet, key):
    if len(key) != 1:
        raise TypeError("Invalid key (len)")
    ans = ''
    ch_num = alphabet.find(phrase[0]) + alphabet.find(key[0])
    ch_num %= len(alphabet)
    key += alphabet[ch_num]
    ans += alphabet[ch_num]
    for i in range(len(phrase) - 1):
        ch_num = alphabet.find(phrase[i+1]) + alphabet.find(key[-1])
        ch_num %= len(alphabet)
        key += alphabet[ch_num]
        ans += alphabet[ch_num]
    return ans

def vizh_cipher_decode(phrase, alphabet, key):
    if len(key) != 1:
        raise TypeError("Invalid key (len)")
    key += phrase
    ans = vizh_decode(phrase, alphabet, key)
    return ans

def main():
    print('Choose cipher:')
    print('0 -- Vizhener cipher')
    print('1 -- Vizhener on opentext cipher')
    print('2 -- Vizhener on ciphertext cipher')
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

    print('Use extended? -- y/n? (adds space, comma, etc...)')
    ext = str(input())
    if ext == 'y' or ext == 'Y' or ext == '1':
        alphabet += ' .,?!'
        print('You have chosen YES')
    else:
        print('You have chosen NO')

    print('Cipher/Decipher? -- 0/1')
    cipher_mode = int(input())
    if cipher_mode < 0 or cipher_mode > 1:
        raise TypeError('Unknown mode')

    print('Input phrase:')
    phrase = str(input())
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) == -1 :
            raise TypeError('Invalid phrase (symbols)')

    print('Input key:')
    key = str(input())
    for i in range(len(key)):
        if alphabet.find(key[i]) == -1 :
            raise TypeError('Invalid key (symbols)')


    if cipher_type == 0:
        if cipher_mode == 0:
            print(vizh_encode(phrase, alphabet, key))
        else:
            print(vizh_decode(phrase, alphabet, key))
    elif cipher_type == 1:
        if cipher_mode == 0:
            print(vizh_open_encode(phrase, alphabet, key))
        else:
            print(vizh_open_decode(phrase, alphabet, key))
    else:
        if cipher_mode == 0:
            print(vizh_cipher_encode(phrase, alphabet, key))
        else:
            print(vizh_cipher_decode(phrase, alphabet, key))

if __name__ == '__main__':
    main()
