# A program that returns the numbers of vowels contained in a word
u_word = input('Enter a Sentence: ').lower()

vowelcounts = {}

for vowel in "aeiou":
    count = u_word.count(vowel)
    vowelcounts[vowel] = count

print(vowelcounts)
