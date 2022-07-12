# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]
if numbers[0] < numbers[1]:
    if numbers[1] < numbers[2]:
        print(numbers[1])
    else:
        print(numbers[2])
elif numbers[1] < numbers[2]:
    print(numbers[1])
