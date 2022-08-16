# 해빈이가 드디어 면허를 땄다! 해빈이의 부모님은 기뻐하며 해빈이에게 첫 차로 몬스터 트럭을 사 주셨다. 해빈이는 자신의 첫 차가 강남 대로의 모든 차를 부수면서 러시 아워조차 자신을 막을 수 없다는 것을 깨닫고 기뻐했지만, 차가 다른 차들의 네 배 크기이기 때문에 주차하는 데 애를 먹고 있었다.

# 그걸 본 준규는 마침 강남에서 공영 주차장 아르바이트를 하고 있기 때문에 정기적으로 해빈이에게 강남 주차장 지도를 보내주기로 했다. 지도는 R행 C열의 표로 이뤄져 있다. 표의 각 칸은 빌딩('#'), 주차 된 차('X'), 또는 빈 주차 공간('.')이다. 해빈이의 차는 꽤 커서 정확히 2행 2열의 칸을 차지한다.

# 해빈이를 도와 가능한 주차 공간을 해빈이가 부숴야 하는 차의 수대로 모아서 보여주자. 이때 주차하기 위해 부숴야 하는 차만 고려한다. (주차 하러 가는 길에 부수는 차는 신경쓰지 않는다.) 단, 아무리 몬스터 트럭이라도 빌딩을 부술 수는 없기 때문에 빌딩이 있는 자리에는 주차를 할 수 없다.
import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())

parking_lot = []
for _ in range(R):
    parking_lot.append(input())
# parking_lot = ['#..#',
#                '..X.',
#                '..X.',
#                '#XX#']

crush_zero = 0
crush_one = 0
crush_two = 0
crush_three = 0
crush_four = 0

for r in range(R):
    for c in range(C):
        if r+1 == R or c+1 == C:
            break
        w = parking_lot[r][c]
        x = parking_lot[r][c+1]
        y = parking_lot[r+1][c]
        z = parking_lot[r+1][c+1]

        temp = w+x+y+z

        if "#" in temp:
            continue
        else:
            monster_car = temp.count("X")
            if monster_car == 0:
                crush_zero += 1
            elif monster_car == 1:
                crush_one += 1
            elif monster_car == 2:
                crush_two += 1
            elif monster_car == 3:
                crush_three += 1
            elif monster_car == 4:
                crush_four += 1
print(crush_zero)
print(crush_one)
print(crush_two)
print(crush_three)
print(crush_four)
