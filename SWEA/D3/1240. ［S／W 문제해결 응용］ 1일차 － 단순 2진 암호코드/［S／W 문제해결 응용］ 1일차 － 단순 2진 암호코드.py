def find_cord():
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] != '0':
                return arr[i][j-55:j+1]

num_dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
            '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    s = find_cord()
    ans = 0
    cnt = 0
    for i in range(0, 56, 7):
        if i%2:
            cnt += num_dict[s[i:i+7]]
            ans += num_dict[s[i:i+7]]
        else:
            cnt += num_dict[s[i:i + 7]]*3
            ans += num_dict[s[i:i + 7]]

    if cnt % 10:
        ans = 0

    print(f'#{testcase} {ans}')