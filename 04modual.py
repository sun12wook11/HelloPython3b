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

# 수온 계산기

# 자동차 주행거리 계산