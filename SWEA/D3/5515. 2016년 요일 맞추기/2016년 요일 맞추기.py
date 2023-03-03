month_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31,
              8:31, 9:30, 10:31, 11:30, 12:31}

week_dict = {0 : 4, 1 : 5, 2 : 6, 3 : 0, 4 : 1, 5 : 2, 6 : 3}

T = int(input())
for testcase in range(1, T+1):
    m, d = map(int, input().split())
    days = d-1
    for i in range(1, m):
        days += month_dict[i]
    print(f'#{testcase} {week_dict[days % 7]}')