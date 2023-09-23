from collections import Counter

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
    string = string.replace(" ", "")
    min_key = 2
    max_key = 10
    keys_sd = dict()
    possible_keylengths = dict()

    print(string)
    for k in range(26):
        print("for k=" + str(k))
        for n in range(min_key, max_key):
            nth_chars = string[::n]
            freq = frequency(nth_chars)
            sd = stat_dist(freq)
            keys_sd[n] = sd
        string = decrypt_shift(string, 1)

        print(keys_sd)
        print(str(sum(keys_sd.values()) / len(keys_sd)) + "\n")


# given a ciphertext string, computes the key using statistical distance and prints plaintext
def shift_cipher(string):
    stat_dist_dict = dict()
    ciphertext = string

    for k in range(26):
        freq = frequency(string)
        stat_dist_dict[k] = stat_dist(freq)
        string = decrypt_shift(string, 1)
    key = min(stat_dist_dict.items(), key=lambda x: x[1])[0]
    print("Ciphertext: " + ciphertext)
    print("Plaintext: " + decrypt_shift(ciphertext, key))
    print("Key: " + str(key))


# given a ciphertext string and key, returns the plaintext
def decrypt_shift(string, key):
    result = ""
    for c in string:
        if c.isalpha():
            result += alphabet[(alphabet.find(c) - key) % 26]
        else:
            result += c
    return result


def main():
    shift_cipher(ciphertext_a)
    vigenere_cipher(ciphertext_b)


if __name__ == "__main__":
    main()
