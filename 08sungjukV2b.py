# 성적 처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 이름 : 민지, 국어: 99, 영어: 98, 수학 99
# 이름 : 혜린, 국어: 88, 영어: 77, 수학 66
# 이름 : 다니엘, 국어: 55, 영어: 77, 수학 99

# 1. 성적 데이터 입력
# 2. 성적 처리
# 3. 결과 출력


names = ['민지','혜린','다니엘']
kors = [88,77,66]
engs = [88,77,66]
mats = [55,77,99]
tots = []
avgs = []
grds = []

tots[0] = koreans[0] + englishs[0] + maths[0]
avgs[0] = tots[0] / 3

tots[1] = koreans[1] + englishs[1] + maths[1]
avgs[1] = tots[1] / 3

tots[2] = koreans[2] + englishs[2] + maths[2]
avgs[2] = tots[2] / 3




# 1. 성적 데이터 입력
names.append  (input("1번학생 이름을 입력하세요: "))
koreans.append ( int(input("1번학생 국어 점수를 입력하세요: ")))
englishs.append ( int(input("1번학생 영어 점수를 입력하세요: ")))
maths.append  (int(input("1번학생 수학 점수를 입력하세요: ")))
# 1. 성적 데이터 입력
names.append  (input("2번학생 이름을 입력하세요: "))
koreans.append  (int(input("2번학생 국어 점수를 입력하세요: ")))
englishs.append  (int(input("2번학생 영어 점수를 입력하세요: ")))
maths.append  (int(input("2번학생 수학 점수를 입력하세요: ")))
# 1. 성적 데이터 입력
names.append  (input("3번학생 이름을 입력하세요: "))
koreans.append  (int(input("3학생 국어 점수를 입력하세요: ")))
englishs.append (int(input("3번학생 영어 점수를 입력하세요: ")))
maths.append (int(input("3번학생 수학 점수를 입력하세요: ")))

# 2. 성적 처리

tot = kors[0] + engs[0] + mats[0]
tots.append(tot)
avg = tots[0] / 3
avgs.append(avg)
grd =   '수' if (avgs[2] >= 90) else \
        '수' if (avgs[2] >= 90) else \
        '수' if (avgs[2] >= 90) else \
        '수' if (avgs[2] >= 90) else '가'


grds.append(grd)
# 2. 성적 처리
total2 = kor2 + eng2 + mat2
average2 = total2 / 3
# 2. 성적 처리
total3 = kor3 + eng3 + mat3
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

