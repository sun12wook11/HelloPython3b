# 모듈
# 특정기능을 수행하는 코드들의 모음
# 코드 재사용 : 한번 작성한 코드를 여러번 사용 가능
# 코드 관리 : 큰 프로젝트를 작은 모듈로 나누어 관리가능
# 협업: 여러 개발자가 각각 모듈을 개발하고 함께사용
# 표준모듈 : 파이썬에서 기본적으로 제공하는 모듈
# 외부모듈 : 다른 조직, 개발자가 만든 모듈, 별도 설치 필요
# 사용자 정의 모듈: 직접 만든 모듈

# 모듈 사용방법
# import 모듈명
# import 모듈명 as 별칭
# from 모듈명 import 함수명 as 별칭

# 난수 생성
#import random
# 줄여 쓰기
import random as rnd
# randint 함수만 가져오기
#from random import randint

# 1~10까지 임의의 난수생성
#print(random.randint(1,10))
print(rnd.randint(1,10))
#print(randint(1,10))

# 이건 중복 추출 가능
print(rnd.randint(1,45))

# 특정 범위의 숫자들 중에서 하나 추출 (표본추출)
# range(n,m) : n ~ m-1 사이의 정수들
print(rnd.sample(range(1,46), 6))

# 날짜 시간 처리
import datetime as dt

print(dt.datetime.now())
print(dt.date.today())
print(dt.datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))

# 긴급재난 지원금 대상자 판별
incom = int(input('월 소득을 입력하세요: '))
diff = int(input('타 지원금 수급 여부 수급1, 미수급2 :  '))

# print ('수급대상자') if (incom <= 4000000) & (diff > 1) else print ('수급대상자 아님')
result = '수급대상자' if (incom <= 4000000) & (diff > 1) else '수급대상자 아님'

print (result)

# 긴급재난 지원금 대상자 판별 (operator, 성능이 더 좋음)

import operator as op
incom = int(input('월 소득을 입력하세요: '))
diff = int(input('타 지원금 수급 여부 수급1, 미수급2 :  '))
tgIncome = 4_000_000

result = '수급대상자' if op.and_(
            op.le(incom, tgIncome),
            op.eq(diff, 2)) else '수급대상자 아님'

print (result)


# 수온 계산기

deeps = float(input('수심(m)은? '))
tem = 20 - deeps * 0.07
print(f'수심이 {deeps}m 일때 수온의 온도는 {tem}℃ 입니다.')

# 수온 계산기(op)
import operator as op
deeps = float(input('수심(m)은? '))
tem = 20 - deeps * 0.07
print(f'수심이 {deeps}m 일때 수온의 온도는 {tem}℃ 입니다.')


# 자동차 주행거리 계산
import operator as op
speed = float(input('주행속도는? '))
rtime = int(input('주행시간은? '))

# dist = speed * rtime
dist = op.mul(speed,rtime)

print(f'{dist} km')


# 컴퓨터 업무 수량 파악
worktime = int(input('근무시간은? '))
needpc = 0
if (24 % worktime) == 0:
   needpc = 24 // worktime
elif (24 % worktime) >= 0:
    needpc = 24 // worktime + 1

print(f'필요한 컴퓨터: {needpc}')

worktime = int(input('근무시간은? '))
comp = 3 * 8 // worktime
etccomp = 1 if (3 * 8 % worktime) > 0 else 0
print(f'필요한 컴퓨터: {comp + etccomp}')


# 컴퓨터 업무 수량 파악 (operator)
import operator as op
worktime = int(input('근무시간은? '))

cal1 = op.mul(3,8)
comp = op.floordiv(cal1, worktime)
etccomp = 1 if (op.mod(cal1,worktime) > 0) else 0

print(f'필요한 컴퓨터: {comp + etccomp}')
