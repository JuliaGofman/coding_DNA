s = input() + 's'
i = 0
c = 1
while i < len(s)-1:
    if s[i] == s[i+1]:
        i += 1
        c += 1
    else:
        print(s[i] + str(c), end='')
        i += 1
        c = 1