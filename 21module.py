# 모듈
# 매우 복잡하고 긴 코드을 하나의 파일에
# 모두 작성하는것은 비효율적일 수 있음 - 유지보수힘듬
# 또한, 여러 사람들과 함께 개발하는 경우
# 작업분담, 작업결과물 통합 역시 어려움
import sunSfeed.hello
# 모듈 방식의 개발을 이용하면
# 사용용도에 따라 파일별로 나눠 작성 가능
# 타인이 만들어 둔 코드를 자신의 프로그램에서 활용가능
# 딸랄서, 모듈은 변수/함수/클래스들을 모아둔 파일

# 모듈은 현재 디렉토리에 있는 파일이나
# 파이썬 라이브러리 디렉토리에 있는 파일을 불러올 수 있음
# 사용자/venu/py310/Lib/site-packages
# C:\Users\cloud6a\venv\py310\Lib\site-packages

# 모듈 불러오기
# import 명령을 이용해서 불러올수있음
# 모듈내 정의된 함수/클래스를 사용할려면
# 모듈명.함수명, 모듈명.클래스 형식으로 코드 작성

# 모듈(디렉토리 경로 폴더) 만들기
# 모듈 디렉토리 만들기
# 안에 파일 만들기
# 안에 함수 만들기

# 모듈 호출 시
# 디렉토리명.파일명.함수

import sunSfeed.hello
sunSfeed.hello.sayHello()

from sunSfeed import hello
hello.sayHello()

from sunSfeed import hello2
hello2.sayHello2()

# 모듈 사용하기 1 - 모듈명.함수명
import sunSfeed.calc
val = sunSfeed.calc.add(10,5)
print(val)

# 모듈 사용하기 1 - 함수명

from sunSfeed.calc import add
val = add(10,5)
print(val)

# 모듈 사용하기 3 - 함수명

from sunSfeed.calc import *
val = mul(10,5)
print(val)

# 모듈 사용하기 4 - 별칭
import sunSfeed.calc as zc
vla = zc.add(10,20)
print(val)

# 외부 모듈 사용하기
# 내장모듈이나 사용자 정의 모듈 이외에
# 다른 조직/기관이나 개인이 만든 모듈을 사용하려면
# pip install 모듈명으로 설치하면 됨
# pip install scikit-learn
# pip install pymysql
# pip install fastapi


# sunSfeed.example


# 단위환산(convert/readUnit/printUnit)

def convertUnit(mm):
    # mm 단위를 다양한 단위로 변환
    conversions = {
        'cm': mm / 10,
        'm': mm / 1000,
        'inch': mm / 25.4,
        'ft': mm / 304.8
    }
    return conversions

def readUnit():
    while True:
        try:
            mm = float(input("길이(mm)를 입력하세요: "))
            if mm >= 0:
                return mm
            else:
                print("양수를 입력하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

def printUnit():
    mm = readUnit()
    conversions = convertUnit(mm)
    for unit, value in conversions.items():
        print(f"{mm} mm --> {value} {unit}")

# 프로그램 실행
printUnit()






# 할인된 상품 가격표 출력(discountPrice/readDiscount,printPrices)
def discountPrice(prices, discount_rate):
    # 할인율에 따라 할인된 가격을 계산
    discounted_prices = {}
    for item, price in prices.items():
        discounted_prices[item] = price * (1 - discount_rate / 100)
    return discounted_prices

def readDiscount():
    while True:
        try:
            discount_rate = float(input("오늘의 할인율을 입력하세요: "))
            if 0 <= discount_rate <= 100:
                return discount_rate
            else:
                print("할인율은 0에서 100 사이의 값이어야 합니다.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

def printPrices():
    # 상품 가격표
    prices = {
        '쌀': 9900,
        '상추': 1900,
        '고추': 2900,
        '마늘': 8900,
        '통닭': 5600,
        '햄': 6900,
        '치즈': 3900
    }

    # 할인율 입력
    discount_rate = readDiscount()

    # 할인된 가격 계산
    discounted_prices = discountPrice(prices, discount_rate)

    # 결과 출력
    print("\n-- 한빛마트 오늘의 할인 가격표 출력 시스템 --")
    for item, original_price in prices.items():
        discounted_price = discounted_prices[item]
        print(f"{item} : {original_price} 원 -> {discounted_price:.0f} 원 ({discount_rate}% DC)")

# 프로그램 실행
printPrices()


# 주번 유효성 체크(cheakJumin/readJumin/printJumin)
# 주민등록번호는 13자리로 이루어져 있으며, 앞 6자리는 생년월일, 뒤 7자리 중 첫 번째 숫자는 성별 코드, 나머지 6자리는 지역 및 순서 코드를 의미합니다. 유효한 주민등록번호인지 확인하기 위해서는 다음과 같은 규칙을 따릅니다.
#
# 주민등록번호 길이가 13자리인지 확인합니다.
# 뒤 7자리 중 첫 번째 숫자가 1, 2, 3, 4 중 하나인지 확인합니다. (1, 3은 남자, 2, 4는 여자를 의미)
# 뒤 7자리 중 첫 번째 숫자를 제외한 나머지 6자리가 유효한 값인지 확인합니다. (000001 ~ 899999 사이의 값)
# 주민등록번호 유효성 검사 공식에 따라 계산한 결과가 맞는지 확인합니다.
# 이 때 주민등록번호 유효성 검사 공식은 다음과 같습니다.
#
# 주민등록번호 앞 12자리에 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 곱한 값을 모두 더합니다.
# 그 결과값을 11로 나눈 나머지를 11에서 뺍니다.
# 계산 결과값이 주민등록번호 마지막 자리 숫자와 일치하면 유효한 주민등록번호입니다.
# 위 규칙에 따라 주민등록번호 유효성을 검사하는 프로그램을 작성해 보세요.
# main.py

# main.py
from sunSfeed.example_module import print_jumin_validation,read_jumin,check_jumin

# 프로그램 실행
print_jumin_validation()
