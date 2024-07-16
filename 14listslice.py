# 슬라이싱
# 연속적인 객체-리스트 튜플 문자열에 범위를지정
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 객체명[시작 : 끝 -1 :스탭]
# 시퀀스 자료형에 지원되는 기능(순서를 기억)중에 하나


# 리스트 슬라이싱 예제
alpha = ['a','b','c','d','e','f']
print(alpha[2:5+1])
print(alpha[3:7+1], alpha[:4+1])
print(alpha[3:7+1])
print(alpha[5:9+1], alpha[5:])
print(alpha[:])
print(alpha[::2])
print(alpha[::-1]) # 역방향


# 문자열 슬라이싱 주민번호 추출
jumin = '123456-1234567'
print(jumin[0:6])
print(jumin[7:8]) #
