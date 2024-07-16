# 51 구구단

# 각 구구단의 결과를 저장할 리스트 초기화
results = [[] for _ in range(9)]

# 각 구구단의 결과 계산하여 리스트에 추가
print('            Multiplication Table      ')
print('        1   2   3   4   5   6   7   8   9        ')
print('-----------------------------------------  ')
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        results[i-1].append(result)

# 각 단을 가로로 출력
for row in range(9):
    line = f"{row+1} |  "
    for col in range(9):
        line += f" {results[row][col]:3d}"  # 각 결과를 2자리 정수 형태로 출력
    print(line)



# 달력