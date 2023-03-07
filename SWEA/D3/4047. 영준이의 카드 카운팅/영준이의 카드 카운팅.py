T = int(input())
for testcase in range(1, T+1):
    s = input()
    card1 = []
    card_dict = {'S' : 13, 'D' : 13, 'H' : 13, 'C' : 13} # 무늬별 카드 장수
    for i in range(0, len(s), 3):
        card1.append(s[i:i+3])
    card2 = list(set(card1))

    if len(card1) != len(card2):    # 중복된 카드가 있으면 에러
        print(f'#{testcase} ERROR')

    else:
        for card in card1:
            card_dict[card[0]] -= 1

        print(f'#{testcase} {card_dict["S"]} {card_dict["D"]} {card_dict["H"]} {card_dict["C"]}')
