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


# 33
cardno = input('카드번호는? ')

result = '잘못된 카드 번호입니다'
if cardno[0:1] == '3':
    if cardno == '356317': result = 'JCB NH농협카드'
    elif cardno == '356901': result = 'JCB 신한카드'
    elif cardno == '356912': result = 'JCB KB국민카드'
elif cardno[0:1] == '4':
    if cardno == '404825': result = '비자카드 비씨카드'
    elif cardno == '438676': result = '비자카드 신한카드'
    elif cardno == '404825': result = '비자카드 KB국민카드'
elif cardno[0:1] == '5':
    if cardno == '515594': result = '마스터카드 신한카드'
    elif cardno == '524353': result = '마스터카드 외환카드'
    elif cardno == '540926': result = '마스터카드 KB국민카드'

print(f'{cardno} / {result}')