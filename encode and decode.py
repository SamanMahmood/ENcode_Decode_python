import string
import random


st = input("Enter message for process s: ")
words = st.split(" ")
coding = input("1 for EnCoding and 0 for Decoding : ")
coding = True if (coding == "1") else False
print(coding)
if (coding):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            r1 = ''.join(random.choices(string.ascii_uppercase, k=3))
            r2 = ''.join(random.choices(string.ascii_lowercase, k=3))
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
