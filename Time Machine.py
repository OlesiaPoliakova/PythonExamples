import time
def countdown(given_sec):
    counter = (seconds for seconds in range(given_sec, -1, -1))
    return counter

for remaining_seconds in countdown(20):
    print(remaining_seconds)
    time.sleep(1)

