words = "The quick brown fox jumped over the lazy dog"

print(words)
print(words.upper())
print(len(words))
print(words.replace("brown", "black"))

if words.isupper():
    print("The words are uppercase")
else:
    print("The words are not upper case")

zip = "5474o08"

if zip.isnumeric():
    print("The zip is numeric")
else:
    print("The zip is mixed")
