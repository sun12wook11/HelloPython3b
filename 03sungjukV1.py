# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 이름 : 홍길동, 국어: 99, 영어: 98, 수학 99
# 총점 : 297, 평균 99.9, 학점:수


# 1. 성적 데이터 입력

# 2. 성적 처리

# 3. 결과 출력

# 성적 처리 프로그램 v1

# 1. 성적 데이터 입력
name = input("이름을 입력하세요: ")
korean = int(input("국어 점수를 입력하세요: "))
english = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))

# 2. 성적 처리
total = korean + english + math
average = total / 3

# 학점 계산
if average >= 90:
    grade = "수"
elif average >= 80:
    grade = "우"
elif average >= 70:
    grade = "미"
elif average >= 60:
    grade = "양"
else:
    grade = "가"

# 3. 결과 출력
print(f"이름: {name}")
print(f"국어: {korean}, 영어: {english}, 수학: {math}")
print(f"총점: {total}, 평균: {average:.1f}, 학점: {grade}")

