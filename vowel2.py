u_word = input('Enter a Sentence: ').lower()
#count = 0
#for letter in u_word:
 #   if letter in 'aeiou':
  #      count += 1
vowel_list = [letter for letter in  u_word if letter in "aeiou"]
print(f'The number of vowels in [{u_word}] is {len(vowel_list)}')
