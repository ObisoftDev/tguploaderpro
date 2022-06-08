import random


def crypt_char(char):
    map = '@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    for ch in map:
        if ch == char:
            return map[len(map) - 1 - i]
        i+=1
    return char

def encrypt(text):
    i = 0
    cryptText = ''
    for char in text:
        rnd = random.randrange(1,9,1)
        cryptText += crypt_char(char) + crypt_char(str(rnd))
        i+=1
    return cryptText

def decrypt(text):
    i = 0
    decryptText = ''
    while i < len(text):
        decryptText += crypt_char(text[i])
        i+=2
    return decryptText


def tokenize(args):
    token = ''
    i=0
    for item in args:
        end = ''
        if i<len(args)-1:
           end = '|'
        token += encrypt(str(item)+end)
        i+=1
    return token

def parsetoken(token):
    patoken = decrypt(token)
    return str(patoken).split('|')


#token = tokenize(['obysoft','Obysoft2001@'])
#url = 'https://tguploader.url/'+encrypt('https://moodle.uclv.edu.cu/draftfile.php/9918312/1323/file.txt')+'/'+token
#tokens = str('https://tguploader.url/uFiIiJmHjKRKXHXDpHnDnJyFqDeDYFzFhHsIBFeEYDeFyFhHYKzJhHXFyKkKBIwIiIwKtJqHeKYGmIuImKXJKKKGIIKEHHXGhIjIeHkDXJyGkDBJwKiHXJKGDEKKGHKEFDJELEFFXGwEtIqDeEOEIELKLEGDHGFFYKsHmEvD/BIAFyIBIkDtHeEqGYFgJpFMEbGaHCKDJLKGJJEDHLFGHFIHKFI*EJHLKJGKK').split('/')
#uri = tokens[-2]
#uri = decrypt(uri)
#userdata = parsetoken(tokens[-1])
#print(url)
#proxy = encrypt('152.206.201.33:4545')
#print(proxy)