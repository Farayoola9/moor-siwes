# A scrabble game
import random

print("Welcome to this Game :)")

word_list = ["welcome", "nice", "something", "tranquility", "honesty", "value"]

for i in word_list:
    word = ''.join([random.choice(i) for x in i])

    print("Rearrange the words correctly \n")

    user_input = input(f"{word} : ")

    if user_input == i:
        print("Congratulations!!! :) You are a Genius")
    else:
        print("You Suck!:(")

#def scatter_word(word):
    #scatter_word = ""
   # memo = ""

    #while len(scatter_word) < len(word):
        #rand_word = random.choice(word)

        #if rand_word in memo:
         #   continue

       # memo += rand_word
       # scatter_word += rand_word

   # return scatter_word


