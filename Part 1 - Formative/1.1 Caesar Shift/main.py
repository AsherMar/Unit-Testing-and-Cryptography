alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alpha_l = "abcdefghijklmnopqrstuvwxyz "


def caesar_encode(text, n):
    new_str = ""
    for let in text:
        if text == text.upper():
            index = alpha.index(let)
            new_str += alpha[(index + n) % 26]
        if text == text.lower():
            index2 = alpha_l.index(let)
            new_str += alpha_l[(index2 + n) % 26]
            if " " in text:
                space = text.find(" ", index2)

    return new_str

def caesar_decode(text, n):
    new_str = ""
    for let in text:
        index = alpha.index(let)
        new_str += alpha[(index - n) % 26]
        if text == text.lower():
            new_str += alpha_l[(index + n) % 26]
    return new_str


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
#print(enc)
#print(dec)
# If this worked, dec should be the same as test!
