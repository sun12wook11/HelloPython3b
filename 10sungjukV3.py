# 성적 처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 이름 : 민지, 국어: 99, 영어: 98, 수학 99
# 이름 : 혜린, 국어: 88, 영어: 77, 수학 66
# 이름 : 다니엘, 국어: 55, 영어: 77, 수학 99




names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []


# 성적 입력
for i in range(3):
    names.append  (input(f"{i+1}번학생 이름을 입력하세요: "))
    kors.append  (int(input(f"{i+1}학생 국어 점수를 입력하세요: ")))
    engs.append (int(input(f"{i+1}번학생 영어 점수를 입력하세요: ")))
    mats.append (int(input(f"{i+1}번학생 수학 점수를 입력하세요: ")))

# 성적 처리

for i in range(3):
    tot = kors[i] + engs[i] + mats[i]
    tots.append(tot)
    avg = tots[i] / 3
    avgs.append(avg)
    grd =   '수' if (avgs[i] >= 90) else \
            '우' if (avgs[i] >= 90) else \
            '미' if (avgs[i] >= 90) else \
            '양' if (avgs[i] >= 90) else '가'
    grds.append(grd)
    tots[i] = kors[i] + engs[i] + mats[i]
    avgs[i] = tots[i] / 3
    tots[i] = kors[i] + engs[i] + mats[i]
    avgs[i] = tots[i] / 3


# 결과 출력
result=('')

for i in range(3):
    result +=f'''이름: {names[0]},국어: {kors[0]}, 영어: {engs[0]}, 수학: {mats[0]}
                 총점: {tots[0]}, 평균: {avgs[0]:.1f}, 학점: {grds[0]}\n'''




# 구구단 출력하는 예제
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()