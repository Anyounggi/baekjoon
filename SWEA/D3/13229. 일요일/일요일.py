week_dict = {
    'MON' : 1, 'TUE' : 2, 'WED' : 3,
    'THU' : 4, 'FRI' : 5, 'SAT' : 6, 'SUN' : 7
}


T = int(input())
for testcase in range(1, T+1):
    s = input()
    ans = 7 - week_dict[s]
    if ans == 0:
        ans += 7
    print(f'#{testcase} {ans}')