import random

for i in range(random.randint(1,3)):
            consonants="bcdfghjklmnpqrstvwxyz"
            vowels="aeiou"
            random_text = "".join(random.choice((consonants,vowels)[i%2]) for i in range(10))
            print(random_text)