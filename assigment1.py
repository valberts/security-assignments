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


# given a ciphertext string and key, returns the plaintext
def viegenere_cipher(string):
    print("hi")


# given a ciphertext string, computes the key using statistical distance and prints plaintext
def shift_cipher(string):
    stat_dist = dict()
    ciphertext = string

    for k in range(26):
        sum = 0
        freq = frequency(string)

        for v1, v2 in zip(frequency_english.values(), freq.values()):
            sum += abs(v1 - v2)

        stat_dist[k] = round(sum / 2, 1)
        string = decrypt_shift(string, 1)
    key = min(stat_dist.items(), key=lambda x: x[1])[0]
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
    viegenere_cipher(ciphertext_b)


if __name__ == "__main__":
    main()
