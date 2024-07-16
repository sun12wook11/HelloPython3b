# 중첩 반복문
# 2개이상의 반복문을 이용해서 반복실행할수도 있음
# 하나의 반복문안에 다른 반복문을 포함시킨 것을 의미
# 이것을 통해 좀 더 복잡한 반복패턴을 구현할수있음
# 2차원 배열처리나 행렬 등 가능

# 별출력 5*5
for i in range (1,5+1):         # 행
    for j in range (1, 5+1):    # 열
        print('*', end ='')     # 세로로 나열
    print()                     # 줄바꿈


# 별출력 12345 1열1개 2열2개
for i in range (1,5+1):         # 행
    for j in range (i):    # 열
        print('*', end ='')     # 세로로 나열
    print()                     # 줄바꿈

# 별출력 54321
for i in range (1,5+1):         # 행
    for j in range (6 - i):    # 열
        print('*', end ='')     # 세로로 나열
    print()                     # 줄바꿈


# 구구단
for i in range(1,9+1):
    for j in range(1,9+1):
        print(f'{j:2d} * {i} = {i*j:2d}', end='   ')
    print( )

# 19단
for i in range(1,19+1):
    for j in range(1,19+1):
        print(f'{j:2d} * {i:2d} = {i*j:3d}', end='   ')
    print( )


