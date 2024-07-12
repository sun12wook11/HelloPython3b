# 성적 처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 단, 학생 3명에 대해 성적처리를 진행함

# 이름 : 민지, 국어: 99, 영어: 98, 수학 99
# 이름 : 혜린, 국어: 88, 영어: 77, 수학 66
# 이름 : 다니엘, 국어: 55, 영어: 77, 수학 99

# 1. 성적 데이터 입력
# 2. 성적 처리
# 3. 결과 출력

# 1. 성적 데이터 입력
name1 = input("1번학생 이름을 입력하세요: ")
korean1 = int(input("1번학생 국어 점수를 입력하세요: "))
english1 = int(input("1번학생 영어 점수를 입력하세요: "))
math1 = int(input("1번학생 수학 점수를 입력하세요: "))
# 1. 성적 데이터 입력
name2 = input("2번학생 이름을 입력하세요: ")
korean2 = int(input("2번학생 국어 점수를 입력하세요: "))
english2 = int(input("2번학생 영어 점수를 입력하세요: "))
math2 = int(input("2번학생 수학 점수를 입력하세요: "))
# 1. 성적 데이터 입력
name3 = input("3번학생 이름을 입력하세요: ")
korean3 = int(input("3학생 국어 점수를 입력하세요: "))
english3 = int(input("3번학생 영어 점수를 입력하세요: "))
math3= int(input("3번학생 수학 점수를 입력하세요: "))

# 2. 성적 처리
total1 = korean1 + english1 + math1
average1 = total1 / 3
# 2. 성적 처리
total2 = korean2 + english2 + math2
average2 = total2 / 3
# 2. 성적 처리
total3 = korean3 + english3 + math3
average3 = total3 / 3

# 학점 계산
if average1 >= 90:
    grade1 = "수"
elif average1 >= 80:
    grade1 = "우"
elif average1 >= 70:
    grade1 = "미"
elif average1 >= 60:
    grade1 = "양"
else:
    grade1 = "가"
# 학점 계산
if average2 >= 90:
    grade2 = "수"
elif average2 >= 80:
    grade2 = "우"
elif average2 >= 70:
    grade2 = "미"
elif average2 >= 60:
    grade2 = "양"
else:
    grade2 = "가"
# 학점 계산
if average3 >= 90:
    grade3 = "수"
elif average3 >= 80:
    grade3 = "우"
elif average3 >= 70:
    grade3 = "미"
elif average3 >= 60:
    grade3 = "양"
else:
    grade3 = "가"



# 3. 결과 출력
print(f"이름: {name1}")
print(f"국어: {korean1}, 영어: {english1}, 수학: {math1}")
print(f"총점: {total1}, 평균: {average1:.1f}, 학점: {grade1}")
# 3. 결과 출력
print(f"이름: {name2}")
print(f"국어: {korean2}, 영어: {english2}, 수학: {math2}")
print(f"총점: {total2}, 평균: {average2:.1f}, 학점: {grade2}")
# 3. 결과 출력
print(f"이름: {name3}")
print(f"국어: {korean3}, 영어: {english3}, 수학: {math3}")
print(f"총점: {total3}, 평균: {average3:.1f}, 학점: {grade3}")

