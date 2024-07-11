# 조건문
# 주어진 상황에 따라서 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨

# 파이썬에서 조건문 작성시 반드시 올바른 들여쓰기에 따라 코드를 작성

# 파이썬의 코드 블록
# 특정한 동작을 위해 관련된 코드를 한곳에 모아둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함!

# if 문
# if 문 조건식:
#       조건참일때 수행할 문장(들)

# 삼항연산자
# 참일때/조건/거짓일때

# : 뒤에는 들여쓰기
# 들여쓰기 파이썬 tab은 4칸


# 짝수 판별하기
num = int(input('숫자는? '))

if (num % 2 == 0):
    print('짝수입니다')


if (num % 2 == 0): print('짝수입니다') # 코드간략화

# if ~ else
# if문은 조건이 참일 경우에만 지정한 코드를 실행하는데 비해
# if ~ else 문은 조건이 참일때와 거짓일때 각각 지정한 코드를
# 실행한다는 것이 다름
# if 조건식:
#    수행할 문장1
# else:
#    수행할 문장2

# 짝수/홀수 출력프로그램

num = int(input('숫자는? '))

if (num % 2 == 0):
    print('짝수입니다')
else:
    print('홀수입니다')



# pass
# 조건문/반복문/함수/클래스나 다른문에서 실행문이 정해지지않은 경우
# 임시로 작성하는 명령문

if num % 2 == 0:
    pass
else:
    pass

# 마일리지 사용하기
mileage = 1200

# if mileage >= 1000:
#     print('마일리지 사용가능!')
# else:
#     print('마일리지 사용불가!')



# # 입력받기
# mileage = 1200
#
# # 처리
# result = ''
# if mileage >= 1000:
#     result='마일리지 사용가능!'
# else:
#     result='마일리지 사용불가!'
#
# # 결과 출력
# print(result)


# 입력받기
mileage = 1200

# 처리
result = '마일리지 사용불가!'
if mileage >= 1000:
    result = '마일리지 사용가능!'

# 결과 출력
print(result)




# 중첩 if 문
# if문 속에 또 다른 if 문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을때 사용 - 복잡함

# 평균 점수에 따라 ABCDRF 학점을 처리하는 조건문 작성
# 처리하는 조건문 작성
avg = 73.5
grade = 'F'
if avg >= 90:
    grade = 'A'
else:
    if avg >= 80:
        grade = 'B'
    else:
        if avg >= 70:
         grade = 'C'
        else:
            if avg >= 60:
             grade = 'D'

print(grade)

# 다중 if 문
# 중첩 if 문을 작성하는 경우, 조건이 많으면 다소 복잡함
# 이러한 중첩 if 문을 단순하게 작성할수있는 조건문
# if 조건1:
#   실행할 코드1
# elif 조건2:
#   실행할 코드 2
# elif 조건3:
#   실행할 코드 3
# else:
#   실행할 코드 4

avg = 85.5

grade = 'F'
if avg >= 90:
    grade = 'A'
elif avg>= 80:
    grade = 'B'
elif avg>= 70:
    grade = 'C'
elif avg>= 60:
    grade = 'D'

print(grade)

# if 조건문 대체 1 - switch 모방
# 조건이 많아지는 경유, 다중 조건문 역시 복잡해짐
# 이럴 경우, dict 자료 구조를 이용하면 간단하게 작성 가능

# if 조건문 대체2
#py 3.10부터switch와 비슷한 match ~ case 문 도입
# match 값:
#  case 값범위1: 실행문1
#  case 값범위2: 실행문2
#  default: 실행문 2

# 주민번호 성별코드에 따른 성별 출력
# 1: 남자 (2000년 이전 출생)
# 2: 여자 (2000년 이전 출생)
# 3: 남자 (2000년 이후 출생)
# 4: 여자 (2000년 이후 출생)

code = int(input('성별코드는?'))

result = ''
match code:
    case 1: result = '남자 (2000년 이전 출생)'
    case 2: result = '여자 (2000년 이전 출생)'
    case 3: result = '남자 (2000년 이후 출생)'
    case 4: result = '여자 (2000년 이후 출생)'
    case _: result = '외국인 이군!'
print(result)




# if 문으로 작성한 학점계산 코드를
# match case로 바꿔 작성하세요
avg = 85.5

grade = 'F'
if avg >= 90:
    grade = 'A'
elif avg>= 80:
    grade = 'B'
elif avg>= 70:
    grade = 'C'
elif avg>= 60:
    grade = 'D'

print(grade)

# match case를 사용한 학점 계산 코드

avg = int(input('점수는?'))

match avg:
    case avg if avg >= 90:
        grade = 'A'
    case avg if avg >= 80:
        grade = 'B'
    case avg if avg >= 70:
        grade = 'C'
    case avg if avg >= 60:
        grade = 'D'
    case _:
        grade = 'F'

print(grade)

#

avg = int(input('점수는?'))

match avg // 10:
    case 10 | 9:
        grade = 'A'
    case 8:
        grade = 'B'
    case 7:
        grade = 'C'
    case 6:
        grade = 'D'
    case _:
        grade = 'F'

print(grade)



# 속도 위반 경고
# 자동 온도 조절 장치
# 자동 주문 시스템
# 국가 재난 지원금 수령
# 개선된 BMI 지수 출력 프로그램
# 버스 전용차로 단속
# 마스크 구매 가능 요일 출력
# 차량 2부제
# 생존율 출력
# 전기 요금 계산기