import sys

sys.setrecursionlimit(10000)

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def exgcd(m, n):
    if n == 0:
        assert m == 1
        return 1, 0
    else:
        x, y = exgcd(n, m % n)
        return y, x - m / n * y


def to_bytes(n):
    length = len(str(n))
    return ('%%0%dx' % (length << 1) % n).decode('hex')[-length:]


if __name__ == '__main__':
    n1 = 0x00cfcfbbeea7df143a8ac208b1aa1d2f86545ac4cb588c94a3fb1c14ad91a4f0b936157c5a4b869c18a8b864f4726bf8fcdc020cb41042bac96784ab7d03f9374947efb0bc3d665831974340159ffc3db7c8e74b6390fda6eec30b81c6ff624e8d3f5b17bfb7a5c7ffd8ecf4e6518b393abefddd0faeba4308746ba63f8106b59d7e058943a00131a7d4e538c464b270577647edbc478cc1ce9585efe877305b3a7c2e7c44db5475eddadc345a2c90a946771cac0a454cdbcb461f2840e7613c83e9cecc94037fa09bb9daa3f180562c01df0be6c51f0c06e8f0e2d6e1a5e50d0a28c3881140770a9f45934146b7f359b939ce23f0fa507a6f4e454571430952003c20f1d97a67140b6e5fcbfb3b376e4e24969aeb1d489cfc72af4f15a4788a1aa97c89756d1d4d94aa47e7cd3a81aecb92448cc92c77d2ef576aa0dbc1350862accddaddbce80357f0cd5b854dd0f8c4627fe4b718b24ecfe11ed24c3be22f00643bbed4ee5e345af176e5b76d23a2f80e0ec6f34e5718c62a70fe5570c28b807b44f22eadebd9b5ff906f6a85be88c0c8f6e5f880a51f17f84db1c2eefea8af34040444ced1a37df0e4f5f72cc3f50b7e427c8c2d8b6186ead762f0c444b3ca3a0103ed12a93bce9cae7479a229ebbc0a648eaa6f97e5051a66eb09ebd7348e92f75f125ebdc367e2a7d1da7759d41fae2e2635bf4b7a7f91becab3ac7d05bd

    n2 = 0x00bb33cc7fcc8ecaf3bf9ed95c583792e1ec6b80ee875ec2064dbcf07595c8344923bf536524d4e0a75574c7798c73b197dd2b1b42054b1e49cb45fbf04e6f114cf8a365c3df3645524f778268038a3fa26802e9d1edbfbb5edfb5a0c375370d7f10f57dabbd4f771dad3632f01b9bce10489966ee882dab17a33b786aa5f73165a54051300b1df9280392a3ede9d3fc9c4d8a6a06351f6ef3598e8de2b39d3b19af64a1716cd15826c3f24cb13deb722c3a03ef1d2be2d0a5a6e210ff5d018367be3bf99ea26ba006e5164a4dd55aabcd449de5ce1864825dc160e50d509eb0e6fe723ef182681eddb94084b83ec9e2e943e87cb87509ab0fd9b1ca22c1ceaff39fcacf6729fc0e0578670d87d7f0f9ccbe09cb3e12ceb895572a9979d10bfdbfafa260568d8db184be12b3e3193e07729ce3c1d9cd8283ed6983a06388036a0a70294f23392944778280e7de9f60163a8150e30ff4a4ea02792cbe8305baa2e99afe51e17dafc56be0d384147bcd38e9d12934ec712622217773a4b3851a9b0c6c7c3e01f6111a1e1a557f4e2ae4a247ce9b75ccccb1819825f3054aa1c055bd3e2340093ae2ef1d0fa5a176825efdf79507027f5104080009142f0d43e2f10cfad220813bbb9014d4f4325edac538fb5e82b753e2ad3b24607d7380aa64fcb98b59ea8b5a736b809383248cece0b17255ea559e90127f778af6d7e8a66dad91

    e = 65537
    p = gcd(n1, n2)
    q1 = n1 / p
    q2 = n2 / p
    # print q1, q2

    d1, _ = exgcd(e, (p-1)*(q1-1))
    d1 %= (p-1) * (q1-1)

    d2, _ = exgcd(e, (p-1)*(q2-1))
    d2 %= (p-1) * (q2-1)

    with open("cipher", "rb") as f:
        data = f.read()
        C = int(data.encode('hex'), 16)

    plain1 = pow(C, d1, n1)
    plain2 = pow(C, d2, n2)

    print to_bytes(plain1)
    print to_bytes(plain2)



