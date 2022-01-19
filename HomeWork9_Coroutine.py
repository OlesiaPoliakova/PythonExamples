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

input_word = input(f"Enter your word here: ")

words_dict = {}
for word in words:
    letter = word[0]
    if letter in words_dict:
        words_dict[letter].append(word) #это список по определенной букве, если такой уже существует
    else:
        words_dict[letter] = [word]#это новый список по опередленной букве
# print(words_dict)#проверяем словарь из списков слов, на определенную букву

def return_word():
    # try:
               input_word = (yield) ##coroutine принимает значение, ждет ввода (но может и выводить)
               next_word = input_word #делаем его следующим словом
               yield next_word #генерируем  слово
               while True:
                   last_letter = next_word[-1]  # находим последнюю букву слова
                   if last_letter in words_dict:
                       specific_letter_list = words_dict[
                       last_letter]  # это список из слов, которые начинаются на последнюю букву
                # print(len(specific_letter_list))
                # print(specific_letter_list)
                       next_word = specific_letter_list.pop(
                       random.randint(0, len(specific_letter_list) - 1))  # удаляем и возвращаем рандомное слово
                       yield next_word
                       if not specific_letter_list:  # проверяем что список пустой
                           words_dict.pop(last_letter)  # удаляем букву из словаря {буква - список слов}
                   else:
                        break

coroutine = return_word()
next(coroutine)
coroutine.send(input_word)
for word in coroutine:
    print(word)
    # except:StopIteration as si:
    #     print(f"Exception: {StopIteration.__name__}\n")

