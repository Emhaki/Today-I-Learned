# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 숫자 N 입력
N = int(input())

# 가장 작은 생성자를 저장할 변수
answer = 0
# 1부터 N 사이의 모든 수의 분해합을 탐색
for number in range(1, N):
    # 분해합 저장 변수
    split_sum = 0

    # 각 자리수의 합
    for digit in str(number):
        split_sum = split_sum + int(digit)

    # 각 자리수의 합 + 수의 합 => 분해합
    split_sum = split_sum + number

    # 구한 분해합과 입력 N이 같으면
    # number는 N의 생성자
    if N == split_sum:
        print(number)

        break  # 가장 작은 생성자를 탐색

# for-else
# break를 만나지 않으면
else:
    print(0)
