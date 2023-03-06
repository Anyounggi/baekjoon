T = int(input())
for testcase in range(1, T+1):
    arr = list(map(int, input().split()))
    lst = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                lst.append(arr[i] + arr[j] + arr[k])
    lst = list(set(lst))
    lst.sort(reverse=True)
    print(f'#{testcase}', lst[4])