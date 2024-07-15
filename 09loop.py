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