import math  # for math.gcd()


def IsPrime(n):
    a = 2
    while a**2 <= n and n % a != 0:
        a += 1
    return a**2 > n


def get_keys(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)
    while True:
        print('Choose e prime to', fi, ':')
        e = int(input())
        if math.gcd(e, fi) != 1:
            print('Not prime. Try again.')
        else:
            break

    d = 1
    while (e * d) % fi != 1:
        d += 1

    return e, n, d


def encript(e, n, phrase):
    m_list = []
    for i in range(len(phrase)):
        if (ord(phrase[i]) >= n):
            raise TypeError('Invalid symbol. Try bigger n (p and q)')
        m_list.append(ord(phrase[i]))
    c_list = []
    for i in range(len(m_list)):
        c_list.append((m_list[i]**e) % n)
    return c_list


def decrypt(n, d, c_list):
    ans = []
    for i in range(len(c_list)):
        ans.append(chr((c_list[i]**d) % n))
    return ans


def main():
    print('Choose RSA System cipher-decipher performance:')
    print('0 -- Via using prime numbers (p, q, e)')
    print('1 -- Via using public and private keys')
    cipher_type = int(input())
    if cipher_type < 0 or cipher_type > 1:
        raise TypeError('Unknown cipher')

    print('Input phrase:')
    phrase = str(input())

    if cipher_type == 0:
        print('Enter prime p and q:')
        p, q = map(int, input().split())
        if not IsPrime(p):
            raise TypeError(f'{p} is not prime')
        if not IsPrime(q):
            raise TypeError(f'{q} is not prime')

        e, n, d = get_keys(p, q)

        print(f'Public key (e, n) is ({e}, {n})')
        print(f'PS. Your private key is {d}')

        c_list = encript(e, n, phrase)
        print(f'ciphered list is:\n {c_list}')
        ans = ''.join(decrypt(n, d, c_list))

        print(f'deciphered phrase is:\n {ans}')

    else:
        print('Enter e, n and d:')
        e, n, d = map(int, input().split())
        c_list = encript(e, n, phrase)
        print(f'ciphered list is:\n {c_list}')
        ans = ''.join(decrypt(n, d, c_list))

        print(f'deciphered phrase is:\n {ans}')


if __name__ == '__main__':
    main()
