# 반복문
# 특정 문장/코드를 지정한 횟수/조건만큼 반복 실행 하는 문장

# 간단한 메세지 한번 출력
print ('Hello, Python!')

# 메세지를 수정한다면 번거로움

# 파이썬의반복문
# for   : 지정한 횟수만큼 반복 수행
# while : 지정한 조건에 의해 반복 수행

# 횟수에 따른 반복 - for
# 반복횟수는 range() 함수로 유추가능 : 종료값 -1 - 시작값
# for 카운트 변수 in range(시작값, 종료값-1, 간격):
#     반복할 문장

# range 함수
# (시작값, 기입값+1(종료값), 사이간격) 연속된 정수 반환
print(list(range(1,101, 2)))

# for 사용 예
for i in range (1,10+1):
    print(i)

for i in range (1,3+1):
    print('h')

# 0부터 시작함 0,1,2
for i in range (3):
    print('h')


for _ in range (3):
    print('h')


sum = 0
for i in range(1, 101):
    sum= sum + i
print(sum)



# 메일발송
count = int(input('메일 발송 횟수를 입력하세요 : '))

for _ in range(count):
    print('메일발송!')


# 3의 배수 출력하기
result = ''

for i in range(1, 10+1):
    result += f'num = {i}\n'
    if i % 3 == 0:
        result += f'3의 배수!!\n'

print(result)


# 구구단 출력
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(f"{i} x {j} = {i * j}")
    print()

# 줄바꿈없이 출력하기(end='')
result=''
for i in range(1,9+1):
    # print(i, end='/')
    result += f'{i} '
print(result)


# 1~100사이 정수중 3과 7의 공배수와 최소공배수 구하기
result=''
for i in range(1, 100+1):
    if (i % 3 == 0) & (i % 7 == 0):
        result += f'{i}\n'
        result += f'ㄴ 3과 7의 공배수 !!\n'

print(result, f'최소공배수는 \n ㄴ {3 * 7}')


# range  함수 사용예


# 문자열을 for문에 사용하기
str = 'Hello, World!!'
for c in str:
    print(c, end=' ')



result = ''

for i in range(1, 100 + 1):
    result += f'{i} '
    clap = False

    # 숫자에 3, 6, 9가 포함되어 있는지 확인
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        clap = True

    clap= ''


    # 숫자가 3의 배수인지 확인
    if i % 3 == 0:
        clap = True

    if clap:
        result += 'Clap!\n'
    else:
        result += '\n'

print(result)


# 열차 교차 시간
print((540/10) == (540/25))



for min in range(1, 540+1):
    if (min % 10 == 0) & (min % 25 == 0): # 50분 간격
        hour = 9+ min //60
        min = min % 60
        print(f'{hour}시{min}분 교차')
    elif (min % 10 == 0) & (min % 30 == 0): # 30분 간격
        hour = 9+ min //60
        min = min % 60
        print(f'{hour}시{min}분 교차')
    elif (min % 25 == 0) & (min % 30 == 0): # 150분 간격
        hour = 9+ min //60
        min = min % 60
        print(f'{hour}시{min}분 교차')



# 로그인 프로그램
correct_password = 'hanbitac'
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    password = input("관리자 암호를 입력하세요: ")
    if password == correct_password:
        print("로그인 됐습니다.")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("암호를 다시 확인하세요!")
        else:
            print("로그인 실패!! 횟수 초과!!!")