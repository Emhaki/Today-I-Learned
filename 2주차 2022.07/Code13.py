# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

x = str(input())


result = list(x)
print(result.pop()+result.pop()+result.pop()+result.pop()+result.pop())
