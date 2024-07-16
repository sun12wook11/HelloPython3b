# while 문
# 조건을 만족할때까지 반복 수행 - 반복 횟수는 모름

# 변수 = 초기값
# while 조건식:
# 반복할 문장
# 변수증가/감소

# 1~10 까지 정수 출력
i=1
while i <= 10:
    print(i, end=' ')
    i += 1



# 1~ 50 사이에 정수중 홀수만 출력
i=0
while i <= 50:
    i += 1
    if i % 2 == 1:
     print(i, end=' ')

# 1~ 50 사이에 정수중 9의 배수만 출력
i=0
while i <= 50:
    i += 1
    if i % 9 == 0:
        print(i, end=' ')

# 반복문 내 실행 중지 : break
# for, while 문 내에서 반복흐름을 벗어나기 위해 사용

# 1 ~ 10000사이 정수의 합을 출력
# 단, 정수의 합이 12345678 보다 크면 계산을 중지

i=0
sum=0
while sum <= 12345678:
    i += 1
    sum += i
print(sum,'+',i,'=', sum+i ,'(12345678보다 큼!)')
# 12347965 + 4969 = 12352934 (12345678보다 큼!)

i=1
sum=0
while i < 10000+1:
    if sum > 12345678: break #12347965
    sum += i
    i += 1

print(sum)





# 369게임 (while로 작성)
# 값 in str(문자열)
# '3' in str(36)
# '6' in str(36)
# '9' in str(39)

i = 1
while i<100+1:
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if '33' in str(i): jjak += ' 짝!'
    if '66' in str(i): jjak += ' 짝!'
    if '99' in str(i): jjak += ' 짝!'

    print(i,jjak)
    i += 1

# 3과 8의 공배수
i=1
while i < 100+1:
    i += 1
    if (i % 3==0 and i % 8 == 0):
        print(i, end=' ')

# 삼각형 너비

w = 1
h = 1
while w * h < 300:
    print(w,h,'삼각형의 넓이는 ', 1/2*(w * h),'입니다\n')
    w *= 2
    h *= 3


# 기차 시간
tA = 10
tB = 25
tC = 30
min = 1

while min < 541:
    if min % 5 ==0:
        if min % tA == 0 and min % tB == 0: # 50분 간격
            hour = 9+ min //60
            min = min % 60
            print(f'{hour}시{min}분 교차')
        elif min % 10 == 0 and min % 30 == 0: # 30분 간격
            hour = 9+ min //60
            min = min % 60
            print(f'{hour}시{min}분 교차')
        elif (min % 25 == 0) and (min % 30 == 0): # 150분 간격
            hour = 9+ min //60
            min = min % 60
            print(f'{hour}시{min}분 교차')
    min += 1


# 로그인 기능 만들기
attempts = 0
max_attempts = 5
correct_password = 'hanbitac'

while True:
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

# 반복문 내에 건너뛰기: continue
# for, while문 내에서 반복흐름을 일시적으로 넘기기 위해 사용
sum = 0
for i in range(1,10+1):
    if i%2 == 0 : continue
    sum += 1
print(sum)

# 1~100까지 정수 합
# 단 3이나 7의 배수는 뺌
sum = 0
i = 0
while i < 100:
    i += 1
    if i % 3 == 0 or i % 7 == 0:
        continue
    else:
        sum += i
print(sum)


sum = 0
for i in range(1 ,100+1):
    if i % 3 == 0 or i % 7 == 0:
        continue
    else:
        sum += i
print(sum)


total_sum = 0
for i in range(1, 101):
    if i % 3 != 0 and i % 7 != 0:
        total_sum += i

print(total_sum)