# 접근방법
# 입력값들을 리스트로 저장
# 빈자리가 있을 경우에는 임시 값을 넣어줌
# 각 리스트에 담긴 인덱스들을 합함
# 임시값을 제거해줌

# 입력값들을 받음
A = list(map(str, input()))
B = list(map(str, input()))
C = list(map(str, input()))
D = list(map(str, input()))
E = list(map(str, input()))
result = ""
result_list = []

# 문자열의 길이만큼 for문 설정
# 길이가 짧은 경우 임시값 T를 넣어줌
for i in range(15):
    A.append("T")
    B.append("T")
    C.append("T")
    D.append("T")
    E.append("T")

# 각 인덱스의 값들을 result값에 더함
for j in range(0, 20):
    result += (A[j]+B[j]+C[j]+D[j]+E[j])

# result값에 T값이 없는 경우에만 result_list에 append
for k in result:
    if k != "T":
        result_list.append(k)

# q값을 일렬로 출력
for q in result_list:
    print(q, end="")
