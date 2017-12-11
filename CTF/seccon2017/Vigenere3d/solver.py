
def _l(idx, s):
    return s[idx:] + s[:idx]


def decrypt(cipher, k1, k2):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]

    i1 = 0
    i2 = 0
    plain = ""
    for c in cipher:
        for i in range(len(s)):
            if t[i][s.find(k1[i1])][s.find(k2[i2])] == c:
                plain += s[i]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return plain


if __name__ == '__main__':
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]

    cipher = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
    pp = "SECCON{"
    
    k1_half = ""
    k2_half = ""
    for a, b in zip(pp, cipher):
        # print("--- '{}' ---".format(a))
        # print("{0} : {1}".format(s[0], s[t[s.find(a)][0].find(b)]));
        k1_half += s[0]
        k2_half += s[t[s.find(a)][0].find(b)]
    
    k1 = k1_half + k2_half[::-1]
    k2 = k2_half + k1_half[::-1]
    # print(k1)
    # print(k2)
    plain = decrypt(cipher, k1, k2)
    print(plain)



