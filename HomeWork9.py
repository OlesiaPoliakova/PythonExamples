import requests
import random

words_with_punctuation = requests.get("https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt").text
# print(words_with_punctuation)
words_with_punctuation = words_with_punctuation.lower()

def split_to_words(text):
    filtered_text = text
    special_characters_list = ['\n', '"', '-', '.', ',', ':', '?', '!', '(', ')', ';', '/', '[', ']', '*',
     '\t', '=', '>', '#', '+', '�', '|', '&', '<', '$']
    for x in special_characters_list:
        filtered_text = filtered_text.replace(x, ' ')
    return filtered_text.split(' ')
# print(split_to_words(words_with_punctuation))

words = list(filter(lambda word: word not in ["","'"],split_to_words(words_with_punctuation)))
# print(words)

words_dict = {}
for word in words:
    letter = word[0]
    if letter in words_dict:
        words_dict[letter].append(word) #это список по определенной букве, если такой уже существует
    else:
        words_dict[letter] = [word]#это новый список по опередленной букве
# print(words_dict)#проверяем словарь из списков слов, на определенную букву

def match_letters_of_two_words():
    next_word = words.pop(random.randint(0, len(words)-1)) #Удаляет и возвращает слово с рандомным индексом
    yield next_word
    while True:
        last_letter = next_word[-1]#находим последнюю букву слова
        if last_letter in words_dict:
            specific_letter_list = words_dict[last_letter]#это список из слов, которые начинаются на последнюю букву
            # print(len(specific_letter_list))
            # print(specific_letter_list)
            next_word = specific_letter_list.pop(random.randint(0, len(specific_letter_list)-1))#удаляем и возвращаем рандомное слово
            yield next_word
            if not specific_letter_list: #проверяем что список пустой
                words_dict.pop(last_letter) #удаляем букву из словаря {буква - список слов}
        else:
            break

result = print(match_letters_of_two_words())
for word in match_letters_of_two_words():
    print(word)





