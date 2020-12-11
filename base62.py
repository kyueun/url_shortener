CODEC = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def encode(index):
    result = []

    while index>0:
        index, mod = divmod(index, 62)
        result.insert(0, CODEC[mod])

    # padding with 0 of base62
    return ''.join(result).rjust(8, CODEC[0])


def decode(url):
    result = 0
    # remove padding
    url = url.lstrip(CODEC[0])

    for i in range(len(url)):
        result += (pow(62, i)*CODEC.index(url))

    return result