import random

mistakes_count = 0

guessed_word = str()
guessed_letter = []


word = input("Enter a word: ")

i = 0
while i < len(word):
    print(i)
    guessed_letter.append(False)
    guessed_word += '-'
    i+=1

for _ in range(2):
    l = random.random(0, len(word))
    guessed_letter[l] = True
    guessed_word[l] = word[l] 






print(f"The guessed word is: {guessed_word}")


