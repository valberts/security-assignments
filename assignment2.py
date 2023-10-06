def lfsr(c, s, n_bits):
    """
    This function implements a linear feedback shift register.
    :param c: The connection polynomial.
    :param s: The initial state.
    :param n_bits: The number of bits to generate.
    :return: The generated bits.
    """
    bits = []
    taps = [i for i, x in enumerate(c) if x == 1]

    for i in range(n_bits):
        bits.append(s[-1])
        next_bit = 0
        for tap in taps:
            next_bit = next_bit ^ s[tap]
        s = [next_bit] + s
        s = s[:-1]

    return bits


def main():
    n_bits = 20
    c = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
    s = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]
    bits = lfsr(c, s, n_bits)
    print(bits)


if __name__ == "__main__":
    main()
