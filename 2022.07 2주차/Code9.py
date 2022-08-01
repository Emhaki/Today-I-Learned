# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']


def get_name(x):
    return x.startswith('이영희')


results = [x for x in students if get_name(x)]  # <== list comprehension 방법
print(len(results))
