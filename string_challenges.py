# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
word_list = list(word.lower())
print(word_list)
count = 0
for letter in word_list:
    if letter == 'а':
        count += 1

print(count)

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vovels = ['ё', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
count = 0

for letter in word.lower():
    if letter in vovels:
        count += 1

print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???

sentence_list = sentence.split(' ')
print(sentence_list)
len_sentence_list = len(sentence_list)
print(len_sentence_list)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
words = sentence.split(' ')
# sentence_list_element_1 = sentence_list.pop(0)
# print(sentence_list_element_1[0])
# sentence_list_element_2 = sentence_list.pop(0)
# print(sentence_list_element_2[0])
# sentence_list_element_3 = sentence_list.pop(0)
# print(sentence_list_element_3[0])
# sentence_list_element_4 = sentence_list.pop(0)
# print(sentence_list_element_4[0])

for word in words:
    word_list = list(word)
    print(word_list[0])    
    

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???

words = sentence.split(' ')
print(words)

len_words = len(words)
print(len_words)

sum_len_word_2 = 0
# sum_len_word_1 = sum(words, str)
# print(sum_len_word_1)

for word in words:
    len_word = len(word)
    sum_len_word_2 += len_word
print(sum_len_word_2)

average_len_word = sum_len_word_2/len_words
print(average_len_word)


