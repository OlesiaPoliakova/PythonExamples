def usa_elections(records):
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
               ('Reagan',500),
               ('Dobkin', 200),
               ('Bush', 400),
               ('Reagan', 600),
               ('Bush', 400),
               ('Reagan', 600),
               ('Bush', 400),
               ('Reagan', 600),
               ])