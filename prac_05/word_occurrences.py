

text = input("Text:")
unique_words = {}
words = text.split()

for word in words:
    word_count = unique_words.get(word, 0)
    unique_words[word] = word_count + 1

words = list(unique_words.keys())
words.sort()

max_length = max((len(word)for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))
