from collections import Counter
from math import gcd, sqrt
from collections import defaultdict
from functools import reduce

alphabet = "abcdefghijklmnopqrstuvwxyz"

ciphertext_a = "max gxmaxketgwl bl ahfx mh fhkx ubvrvexl matg ixhiex"
ciphertext_b = "eocecwami kz acrp fkso avg gpeww qm hjs naveq afgs hhbgj pg poeioi vv qgbertp cur ucfta eolfkql tai hpfuh puksrlopg eo xreviphpr vlqjcnoee pitl hjs dptrkzv glalhvgyg yvz vbwkasf hse tqgyweod ig xjl lxweh vipaitm ehxc dycwust veehc uspdl fcjy vc dptmp dvgfp taia hrfso snkcy opr gagmnso vc xadi ka aqfp ptpcaodzp thhcf qjcnoeevl wu cye hj vos ocdt vspzioso agh nvjgr qohhu pb vvp whvnk wv qzmxw ku acbj vtvklhksd feexvfu oyd llcwsu oyd bw wzsf tzr uempbi qzodmpn opr riyxkuu"

frequency_english = {
    "a": 8.2,
    "b": 1.5,
    "c": 2.8,
    "d": 4.2,
    "e": 12.7,
    "f": 2.2,
    "g": 2.0,
    "h": 6.1,
    "i": 7.0,
    "j": 0.1,
    "k": 0.8,
    "l": 4.0,
    "m": 2.4,
    "n": 6.7,
    "o": 7.5,
    "p": 1.0,
    "q": 0.1,
    "r": 6.0,
    "s": 6.3,
    "t": 9.0,
    "u": 2.8,
    "v": 1.0,
    "w": 2.4,
    "x": 0.1,
    "y": 2.0,
    "z": 0.1,
}


# checks if number is prime
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


# return a dictionary containing alphabet letters as keys and their relative frequencies in the given string as values
def frequency(string):
    freq = dict()

    length = len(string)
    counts = Counter(string)
    for c in alphabet:
        freq[c] = round((counts[c] / length) * 100, 1)
    return freq


def stat_dist(freq):
    stat_dist = 0
    sum = 0
    for v1, v2 in zip(frequency_english.values(), freq.values()):
        sum += abs(v1 - v2)

    stat_dist = round(sum / 2, 1)
    return stat_dist


# given a ciphertext string and key, returns the plaintext
def vigenere_cipher(string):
    ciphertext = string
    string = string.replace(" ", "")
    key_length = kasiski_test(string)
    nth_chars = list()
    key = ""
    for n in range(key_length):
        nth_chars.append(string[n::key_length])

    for s in nth_chars:
        stat_dists = dict()
        for k in range(26):
            freq = frequency(s)
            stat_dists[k] = stat_dist(freq)
            s = decrypt_shift(s, 1)

        key += alphabet[(min(stat_dists.items(), key=lambda x: x[1])[0])]

    plaintext = ""
    index = 0
    for c in ciphertext:
        if c.isalpha():
            plaintext += decrypt_char(c, key[index])
            index = (index + 1) % key_length
        else:
            plaintext += c

    print("Ciphertext: " + ciphertext)
    print("Plaintext: " + plaintext)
    print("Key: " + key)


def kasiski_test(string):
    # find repeating sequences of three or more characters and their spacings
    seq_spacings = defaultdict(list)
    for seq_len in range(3, 11):  # considering sequences of length 3 to 10
        for i in range(0, len(string) - seq_len):
            seq = string[i : i + seq_len]
            next_seq_index = string.find(seq, i + seq_len)
            if next_seq_index != -1:
                seq_spacings[seq].append(next_seq_index - i)

    # get all the distances we found between sequences
    distances = []
    for seq, spacings in seq_spacings.items():
        distances.extend(spacings)

    freq_distances = Counter(distances)
    distances = set(distances)

    # find all primes in the set of distances
    # they are not useful in estimating the key length
    primes = set()
    for n in distances:
        if is_prime(n):
            primes.add(n)

    # remove all primes from distances
    distances -= primes
    # find gcds of all remaining combinations
    gcds = list()
    for i in distances:
        for j in distances:
            gcds.append(gcd(i, j))
    # remove gcds of 1 and 2
    for n in range(1, 3):
        gcds = [i for i in gcds if i != n]

    # get the most commonly occuring gcd as key length
    key_length = max(Counter(gcds).items(), key=lambda x: x[1])[0]

    return key_length


# given a ciphertext string, computes the key using statistical distance and prints plaintext
def shift_cipher(string):
    stat_dists = dict()
    ciphertext = string

    for k in range(26):
        freq = frequency(string)
        stat_dists[k] = stat_dist(freq)
        string = decrypt_shift(string, 1)
    key = min(stat_dists.items(), key=lambda x: x[1])[0]
    print("Ciphertext: " + ciphertext)
    print("Plaintext: " + decrypt_shift(ciphertext, key))
    print("Key: " + str(key) + "\n")


# given a ciphertext string and key, returns the plaintext
def decrypt_shift(string, key):
    result = ""
    for c in string:
        if c.isalpha():
            result += alphabet[(alphabet.find(c) - key) % 26]
        else:
            result += c
    return result


# given a character and a key, returns the character shifted by that key
def decrypt_char(char, key):
    return alphabet[(alphabet.index(char) - alphabet.index(key)) % 26]


def main():
    shift_cipher(ciphertext_a)
    vigenere_cipher(ciphertext_b)


if __name__ == "__main__":
    main()
