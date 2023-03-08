def solution(n):
    answer = 0
    a = bin(n)[2:].count('1')
    while True:
        n += 1
        if bin(n)[2:].count('1') == a:
            answer = n
            break
    return answer