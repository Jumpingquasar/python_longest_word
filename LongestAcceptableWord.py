import re


words_file = open("words_alpha.txt", "r")
words = words_file.read().splitlines()
words_file.close()
longest_word="null"
longest_words = []

for word in words:
    x = re.findall("[gkmqvwxzio]", word)
    if x == []:
        if len(word) >= len(longest_word):
            longest_word = word
            longest_words.append(word)

print (longest_words)
