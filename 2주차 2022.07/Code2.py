# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.

# len() 함수를 바로 쓰기보다는 반복문을 활용하세요
word = str(input())
result = []
for i in word:
    result.append(len(word))
print(result.pop(-1))
