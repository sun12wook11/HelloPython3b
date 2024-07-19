# V6
import csv

# 메뉴입력
def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
    ================== 
     성적 프로그램 v6
    ==================
     1. 추가
     2. 조회
     3. 상세조회
     4. 수정
     5. 삭제 
     0. 종료
    ==================
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')
    return menu

# 기본 데이터 및 변수 선언
sjs = []

# 성적 데이터 리스트 입력 받기
def readSungJuk():
    sj = []
    cnt = len(sjs)
    sj.append(input(f"{cnt}번 학생 이름을 입력하세요: "))
    sj.append(int(input(f"{cnt}번 학생 국어 점수를 입력하세요: ")))
    sj.append(int(input(f"{cnt}번 학생 영어 점수를 입력하세요: ")))
    sj.append(int(input(f"{cnt}번 학생 수학 점수를 입력하세요: ")))
    return sj

# 입력받은 성적 리스트 입력 처리 -> 총점 평균 학점
def addSungJuk(sj):
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(sj[4] / 3)
    grd =   '수' if sj[5] >= 90 else \
            '우' if sj[5] >= 80 else \
            '미' if sj[5] >= 70 else \
            '양' if sj[5] >= 60 else '가'
    sj.append(grd)
    sjs.append(sj)

# 리스트에 저장된 성적 데이터 조회
def showSungJuk():
    result =''
    for sj in sjs:
        result += f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}, 총점: {sj[4]}, 평균: {sj[5]:.2f}, 등급: {sj[6]}\n'
    print(result)


# sungjuk.dat에 저장된 성적데이터를 읽기
def loadSungJuk():
    with open('C:/Users/cloud6a/Documents/projects2024/HelloPython3c/sunSfeed/sungjuk6.dat', encoding='utf-8') as f:
        rows = f.readlines()

    for row in rows:
        sj = []
        data = row.split(',')
        sj = [d for d in data]
        sjs.append(sj)



# 메모리에 생성된 sjs변수의 모든 성적 데이터를
# sungjukk.dat에 저장
def saveSungJuk(sjs):
    with open('./sunSfeed/sungjuk.dat', 'w', encoding='utf-8') as f:
        f.write()


# 데이터 초기화 함수 호출
loadSungJuk()


showSungJuk()