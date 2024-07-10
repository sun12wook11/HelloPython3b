
# 수식/표현식 expression
# 숫자 변수 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 산술연산자
# 자료형 승격 promotion

# 매출액 입력시 총합을 출력

# 문자열의 덧셈
# >> 'a' + 'b'
# >> 'ab'

# 문자열의 곱셈 (문자열 먼저)
# >> 'a' * 3
# >> 'aaa'
# >> 'a' * 0
# >> ''

# /나눗셈은 둘다 정수여도 부동소수점

# 0을 아무 숫자로 나누면 연산 결과는
# >> 0.0로 나옴

# 아무 숫자를 0으로 나누면
# 에러 : 0으로 나눌수 없음이 뜬다

# // 는 몫

# %는 나머지
# %2해서 홀짝구분 (나머지0,나머지1)

# **는 거듭제곱
# 2**3 = 2*2*2 = 8



# garo  = int(input ('가로의 길이는? '))
# sero  = int(input ('세로의 길이는? '))
# wi = int(garo * sero)
# print (f'''
#         넓이는 {wi} cm^2 입니다
# ''')

# print('bmi')
# we = int(input('몸무게(kg) : '))
# tall = float(input('신장(cm) ; '))
# bmi = round((we / (tall**2) *10000), 2)
# print (f'BMI : {bmi}')


print('홀짝 게임')
import random
ju = random.randint(1, 10)
print(f'{ju}')
jus = ju%2
print(f'{jus}')

# 파이썬 콘솔에서 실행
# (알트+쉬프트+E)

# 할당 연산자

# 논리연산자 단축식 평가

# 삼항 연산자
# 조건문을 한 줄로 표현할수있는 연산자
# 참일떄 값 if 조건식 else 거짓일때 값

myscore = 90
result = '합격!' if myscore >= 90 else '불합격!'

print(result)


# 복리계산기

year1_bok = 5_000_000
year1_ri = year1_bok * 0.05
year1 = year1_bok + year1_ri
print(year1)
year2 = year1 + year1 * 0.05
print(year2)
year3 = year2 + year2 * 0.05
print(year1)
year3 = year2 + year2 * 0.05
print(year1)
year3 = year2 + year2 * 0.05
print(year1)

# 범퍼카 탑승

# 범퍼카 탑승 판별

# 적자/흑자 판별