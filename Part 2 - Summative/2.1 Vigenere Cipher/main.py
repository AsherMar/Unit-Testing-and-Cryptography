# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  new_str = ""
  keyword_list = []
  for letter in text:
    index = alpha.find(letter)
    #print(index)
    for let in keyword:
      move = 0
      keyword_list.append(let)
      index2 = alpha.find(keyword_list[move])
      move += 1

    print(index2)




def vig_decode(text, keyword):
  return ""


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
#dec = vig_decode(enc, vig_key)
print(enc)
#print(dec)
# If this worked, dec should be the same as test!