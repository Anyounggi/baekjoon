alphabet = 'abcdefghijklmnopqrstuvwxyz'

T = int(input())
for testcase in range(1, T+1):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == alphabet[i]:
            cnt += 1
        else:
            break
    print(f'#{testcase}', cnt)


