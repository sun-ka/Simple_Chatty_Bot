word_first = input()
word_second = input()

# How many letters does the longest word contain?

word_first_length = len(word_first)
word_second_length = len(word_second)

print(max(word_first_length, word_second_length))
