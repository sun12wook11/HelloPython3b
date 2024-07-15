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



# 3과 8의 공배수
i=1
while i < 100+1:
    i += 1
    if (i % 3==0 and i % 8 == 0):
        print(i, end=' ')

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


# 삼각형 너비

w = 1
h = 1
while w * h < 300:
    print('삼각형의 넓이: ', w * h, end=' ')
    w *= 2
    h *= 3
