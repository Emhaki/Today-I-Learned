
def solution(field, n):

    for r in range(len(field)):
        for c in range(len(field)):
            if r+1 == n or c+1 == n:
                break
            w = field[r][c]
            x = field[r][c+1]
            y = field[r+1][c]
            z = field[r+1][c+1]

            temp = w+x+y+z
            max_temp = 0

            if temp > max_temp:
                max_tamp = temp
    return max_tamp
