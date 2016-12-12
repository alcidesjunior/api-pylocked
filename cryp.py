import base64

def enc(str):
    crypt = base64
    str = crypt.b64encode(str+"6a4120be23c814f8")
    return crypt.b64encode(str)
def dec(str):
    crypt = base64
    str = (crypt.b64decode(str))
    return crypt.b64decode(str)
def encode(str):
    str = str[::-1]
    return enc(str)
def decode(str):
    return (dec(str)).replace("6a4120be23c814f8","")[::-1]

# texto = encode("web280215#@+")
# print texto
# print decode(texto)
