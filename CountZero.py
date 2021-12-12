zero_count = 0
for i in range(int(input())):
    zero_count += 1 if int(input()) == 0 else 0
    # zero_count += int(input()) == 0
print(zero_count)
