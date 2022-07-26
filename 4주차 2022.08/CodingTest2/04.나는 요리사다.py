# "나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.

# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

# 점수 입력
player1 = []
player2 = []
player3 = []
player4 = []
player5 = []
n = 0
while n != 5:
    a, b, c, d = map(int, input().split())
    if n == 0:
        player1.append(a)
        player1.append(b)
        player1.append(c)
        player1.append(d)
    elif n == 1:
        player2.append(a)
        player2.append(b)
        player2.append(c)
        player2.append(d)
    elif n == 2:
        player3.append(a)
        player3.append(b)
        player3.append(c)
        player3.append(d)
    elif n == 3:
        player4.append(a)
        player4.append(b)
        player4.append(c)
        player4.append(d)
    elif n == 4:
        player5.append(a)
        player5.append(b)
        player5.append(c)
        player5.append(d)
    n += 1

# player1 = [5, 4, 4, 5]
# player2 = [5, 4, 4, 4]
# player3 = [5, 5, 4, 4]
# player4 = [5, 5, 5, 4]
# player5 = [4, 4, 4, 5]

# 가장 큰 점수
# 점수가 큰 플레이어

# winner_list를 생성
winner_list = []
# winner_list에 append를 통해 player들의 점수 입력
winner_list.append(sum(player1))
winner_list.append(sum(player2))
winner_list.append(sum(player3))
winner_list.append(sum(player4))
winner_list.append(sum(player5))

# winner_list = [18, 17, 18, 19, 17]

# winner_list에서 가장 큰 값의 index + 1과 max 점수를 출력
print((winner_list.index(max(winner_list))+1), max(winner_list))
