alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

move = 0
def vig_encode(text, keyword):
  global index2
  new_str = ""
  keyword_list = []
  for let in keyword:
    global move
    keyword_list.append(let)
    index2 = alpha.find(keyword_list[move])
    move += 1
  for letter in text:
    index = alpha.find(letter)
    index3 = index + index2
    if index3 > len(alpha):
      index3 %= 26
      new_str += alpha[index3]
  return new_str

def vig_decode(text, keyword):
  return ""


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
#dec = vig_decode(enc, vig_key)
print(enc)
#print(dec)
# If this worked, dec should be the same as test!