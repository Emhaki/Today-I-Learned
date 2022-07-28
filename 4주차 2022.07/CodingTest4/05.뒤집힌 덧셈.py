# 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.

# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

# 두 양의 정수 X와 Y값 입력
X, Y = input().split()

# X와 Y를 각각 뒤집고 더한 값을 뒤집어야 하기 때문에 함수를 정의


def solution(X):
    # 숫자들을 담을 리스트
    num_list = []
    # 입력된 X를 str로 변환해서 for문을 이용
    for i in str(X):
        # num_list에 i값을 append
        num_list.append(i)
        # num_list = [-,1,2,3]
        result = num_list[::-1]
        # result 값에 num_list를 거꾸로 변환
        # result = [3,2,1,-]

    # 만약에 음수 값이 들어온다면 -값을 앞으로 넣어줘야 함
    for j in result:
        # 만약 j랑 -랑 같다면(있다면)
        if j == '-':
            # result 첫번째 인덱스에 result 마지막 인덱스 '-' 삽입.
            result.insert(0, result[-1])
            # [-,3,2,1,-]
            # pop을 통해 마지막 값을 뺌
            result.pop()
            # [-,3,2,1]
            # 결과값을 result2에 저장
            result2 = result
        else:
            # if문이 아니라면 양수이기 때문에 바로 result2에 저장
            result2 = result

    # result2에 result가 나눠진 부분을 합친 값을 저장
    result2 = "".join(result)
    # 저장된 값을 float으로 형변환하고, round를 통해 소수점 탈락
    return round(float(result2))


print(solution(solution(X) + solution(Y)))
