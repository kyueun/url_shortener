CODEC = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def encode(index):
    result = []

    while index>0:
        index, mod = divmod(index, 62)
        result.insert(0, CODEC[mod])

    return ''.join(result)

def decode(url):
    result = 0
    str = reversed(url.split('/')[1])

    for i in range(len(str)):
        result += (pow(62, i)*CODEC.index(str[i]))

    return result