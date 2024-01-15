
import csv
import string

translator = str.maketrans('', '', string.punctuation)

words_count = {}

with open('declaration.txt', 'r') as f:
    text = f.read()

words = text.split()

for word in words:
    word = word.translate(translator).lower()
    count = words_count.get(word, 0)
    count += 1
    words_count[word] = count


word_count_list = sorted(words_count, key=words_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, words_count[word])

with open('words.csv', 'w') as mycsv:
    writer = csv.writer(mycsv)
    writer.writerow(['word', 'count'])
    for word in word_count_list:
        writer.writerow([word, words_count[word]])
