# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for i in word:
  if i == 'а' or i == 'А':
    count += 1
print(f'Букв А в слове Архангельск: {count}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
glasnie = set('ЁУЕЫАОЭЯИЮуеыаоэяиюё')
for letter in word:
  if letter in glasnie:
    count += 1
print(f"Количество глассных: {count}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
len_word_in_sentence = len(sentence.split())
print(f"Количество слов в предложении: {len_word_in_sentence}")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sent_split = sentence.split()
for letter in sent_split:
  print(letter[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split()
sum = 0
for word in sentence:
    sum += len(word)
avg = sum//len(sentence)
print(f"Усреднённая длина слова в предложении: {avg}")