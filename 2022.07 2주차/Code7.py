# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

numbers = [0, 20, 100]
if numbers[0] > numbers[1]:
    if numbers[1] > numbers[2]:
        print(numbers[2])
    else:
        print(numbers[1])
elif numbers[1] > numbers[2]:
    print(numbers[2])
else:
    print(numbers[0])
