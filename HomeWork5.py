def usa_elections(records):
    qty = int(input('QTY records '))
    result = {}
    for candidate, voices in records:
        if candidate in result:
            result[candidate] += voices
        else:
            result[candidate] = voices

    for key, value in sorted(result.items()):
        print(key, value)


usa_elections([('Dobkin', 200),
               ('Bush', 100),
               ('Reagan', 500),
               ('Dobkin', 200),
               ('Bush', 400),
               ('Reagan', 600),
               ('Bush', 400),
               ('Reagan', 600),
               ('Bush', 400),
               ('Reagan', 600),
               ])


def most_frequent_word(records):
    qty = int(input('QTY records '))
    result = {}
    for words in records:
        words = words.split(' ')
        for word in words:
            if word == '':
                continue
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    max_count = max(result.values())
    freq_word = ''
    for word, count in result.items():
        if count == max_count:
            if freq_word == '' or word < freq_word:
                freq_word = word
    print(freq_word)


    # version 2
    # max_count = max(result.values())
    # words_list = [key for (key, value) in result.items() if value == max_count]
    # words_list.sort()
    # print(words_list[0])


most_frequent_word(['one basket apple orange banana christmas banana',
                    'one orange basket banana apple christmas banana',
                    'one banana orange basket apple banana christmas'
                    ])


def occurs_before(numb_string):
    numbers = numb_string.split(' ')
    numb_set = set()
    for number in numbers:
        if number in numb_set:
            print('YES')
        else:
            print('NO')
        numb_set.add(number)


occurs_before('2 5 3 2 3 7 7 8')
