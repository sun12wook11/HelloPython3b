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
