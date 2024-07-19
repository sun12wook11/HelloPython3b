# 파일 입출력
# 지금까지 프로그램을 실행할때 값을 입력받을려면
# 키보드를 사용하고
# 값을 출력하려면
# 모니터 화면에 표시하는 방식을 사용했음

# 하지만, 값을 입력받거나 출력하는 방법은 이게 다가 아님
# 파일을 통해 값을 입력/출력할 수 있고
# 심지어, 네트워크를 통해 값을 입력/출력할 수도 있음

# 프로그램 실행중 생성된 데이터(변수)들은
# 주로 메모리내에 존재하는데 프로그램 종료시 같이 소멸됨(휘발성)
# 이러한 데이터에 영속성(persistance)을 부여하려면
# 데이터를 저장장치에 보관해서
# 데이터가 소멸되지 않도록 하는것이 중요!

# 파일쓰기 : 데이터를 파일에 저장
# with open(경로, 방식) as 파일객체변수
#   파일객체변수.write(파일에 저장할 문자열)

# 파일 기록 방식 : 파일 작업 종류 지정
# w(쓰기), t(텍스트파일 쓰기)
# a(추가 쓰기), b(바이너리파일 쓰기)

# 1. 간단한 인삿말을 파일에 저장
# with open(경로, 방식) as 파일객체변수
with open('c:/Java/hello.txt','w') as f:
    f.write('hello world')

# 2. # Hello2.txt에 '안녕, 세상아!' 라는 한글 내용을 저장
with open('c:/Java/hello2.txt','w') as f:
    f.write('안녕, 세상아!')
# 인코딩 지정 누락 -> 기본 인코딩은 원도우 자체 인코딩을 따라감(cp949)


# 2-1.# with open(경로, 방식, 인코딩) as 파일객체변수
# 인코딩은 UTF-8로 지정/변경
with open('c:/Java/hello3.txt','w',encoding='UTF=8') as f:
    f.write('안녕, 세상아!')


# 3. # 회원정보를 입력받아 member.dat에 저장
# 저장대상 : 아이디, 비밀번호, 이름, 이메일
# 저장형식 : "아이디/비밀번호/이름/이메일" 형식으로 파일에 저장
# ex) abc123/987xyz/abc123/abc123@987xyz.co.kr

def save_member_info(filename):
    # 사용자로부터 입력받기
    user_id = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    email = input("이메일을 입력하세요: ")

    # "아이디/비밀번호/이름/이메일" 형식으로 데이터 생성
    member_info = f"{user_id}/{password}/{name}/{email}\n"

    # 파일에 저장 ('a'는 추가 'w'는 새로쓰기/덮어쓰기)
    with open('c:/Java/member.dat', 'a', encoding='UTF-8') as f:
        f.write(member_info)

# 파일 경로 지정
filename = 'c:/Java/member.dat'

# 사용자 정보 저장 함수 호출
save_member_info(filename)


# 4. # 학생으로부터 이름,국어,영어,수학 점수를 입력받아
# 파일에 저장하세요 (파일명 : sungjuk.dat)
# 단, 점수는 임의로, 파일에 저장하는 형식은
# "이름,국어,영어,수학" 순으로 작성함
# => 혜교,99,98,99 (csv 형식)

import csv

def sungjuk(filename):
    name = input("학생의 이름을 입력하세요: ")
    kor = input("국어 점수를 입력하세요: ")
    eng = input("영어 점수를 입력하세요: ")
    mat = input("수학 점수를 입력하세요: ")

    # "이름,국어,영어,수학" 형식으로 데이터 생성
    student_info = f"{name},{kor},{eng},{mat}\n"

    # 파일에 저장 (추가 모드로 열기)
    with open(filename, 'a', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, kor, eng, mat])
        f.write(student_info)

# 파일 경로 지정
filename = 'c:/Java/sungjuk.dat'

# 학생 정보 저장 함수 호출
sungjuk(filename)
