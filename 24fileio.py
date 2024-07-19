# 1. # 파일 읽기
# with open(경로, 방식, 'r') as 파일객체변수
#   파일객체변수.read()

# 파일 기록 방식
# r (읽기)

# 2. # 파일읽을때 사용하는 함수
# read      : 파일의 내용을 모두 읽음
# readline  : 파일의 내용을 한 줄씩 읽음 (반복문 필요)
# readlines : 파일의 내용을 한 줄씩 모두 읽음 (반복문 필요)

# 3. # 파일에서 회원정보 읽어오기
with open('c:/Java/member.dat', 'r', encoding='UTF-8') as f:
    print(f.read())

# 4. # 파일에서 회원정보 읽어오기  - 행단위 처리1
with open('c:/Java/member.dat', 'r', encoding='UTF-8') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())         # 3줄짜리 파일 모두 읽을려면 3번 찍어야 함

# 4-1. # 파일에서 회원정보 읽어오기  - 행단위 처리 2 (반복문 while)
with open('c:/Java/member.dat', 'r', encoding='UTF-8') as f:
    while True:
        line = f.readline()     # 먼저 한 줄 읽기
        if not line:
            break               # 읽은 내용이 없으면 중단
        print(line.strip())     # 각 줄 출력 (끝의 개행 문자 제거)

# 4-2. # 파일에서 회원정보 읽어오기  - 행단위 처리 3 (반복문 for)
with open('c:/Java/member.dat', 'r', encoding='UTF-8') as f:
    lines = f.readline()        # 각행 단위로 모두 읽어서 리스트에 저장

for line in lines:              # 이터러블 형식으로 반복처리 (꺼내먹는)
    print(line)

# 5.# 회원정보 데이터파일에서
# 이름과 이메일만 출력
# 스플릿트 함수(슬래쉬를 구분해서 나눔)
with open ('c:/Java/member.dat', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
# 5-1. #스플릿트 구분자: 문자열변수.스플릿트 특정문자로 문자열을 나눠 리스트에 저장
for line in lines:
    member =line.split('/')
    print(member[2], member[3])


# 5-2. # GPT (오류이유: 아까 쓰기나 더하기 할때 공백이 있어서 읽지 못 함- 공백 지워서 해결)
with open('c:/Java/member.dat', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

# 각 줄을 '/' 구분자로 나누어 이름과 이메일을 출력
for line in lines:
    member = line.strip().split('/')  # 각 줄에서 끝의 개행 문자를 제거하고 '/'로 분리
    print(member[2], member[3])  # 이름과 이메일 출력



# 5-3. # 앞 예제에서 파일로 저장한 성적데이터를
# 다음과 같은 형태로 화면에 출력
# 이름:abc, 국어:99, 영어:87, 수학:66
# 파일을 읽기 모드로 열기
with open('c:/Java/sungjuk.dat', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

# 각 줄을 ',' 구분자로 나누어 형식에 맞게 출력
for line in lines:
    line = line.strip()  # 공백 제거
    if not line:
        continue  # 빈 줄 건너뛰기

    student = line.split(',')
    if len(student) != 4:
        continue  # 잘못된 형식의 데이터 건너뛰기

    name, korean, english, math = student
    print(f"이름: {name}, 국어: {korean}, 영어: {english}, 수학: {math}")
