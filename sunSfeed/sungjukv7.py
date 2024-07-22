# 사원데이터 기반 CRUD 기능이 제공되는 프로그램
# 사원 - empid, fname, lname,email,phone,
#       hdate,jobid,sal,comm,mgrid,deptid
# 조회 - 사원번호,이름,이메일,부서번호
# 상세조회 -특정 사원번호 대상 모든 칼럼 출력

# 3 LAYER - <emp table>
# 28sungjukV7   -> main     -> 30EMP
# sungjuk7      -> service  -> emp
# sungjukv7DAO  -> DAO      -> empDAO


# V7 데이터베이스화(sql)
import sqlite3


# main UI 창 만들기
def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
    ================== 
     성적 프로그램 v5
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

# 성적 데이터 리스트 입력 받기
def readSungJuk():
    sj = []
    cnt = getTotalSungJUk()
    sj.append(input(f"{cnt}번 학생 이름을 입력하세요: "))
    sj.append(int(input(f"{cnt}번 학생 국어 점수를 입력하세요: ")))
    sj.append(int(input(f"{cnt}번 학생 영어 점수를 입력하세요: ")))
    sj.append(int(input(f"{cnt}번 학생 수학 점수를 입력하세요: ")))
    return sj

# 입력받은 성적 리스트 입력 처리 -> 총점 평균 학점 계산 + DB 업로드
def addSungJuk(sj):
    # 점수 계산 학점 출력 함수
    computeSungJuk(sj)
    # 기존 입력받은 데이터 + 계산된 데이터 합쳐서 DB 업로드
    newSungJuk(sj)

# 리스트에 저장된 성적 데이터 조회
def showSungJuk():
    result =''
    sjs = readAllSungJuk()
    for sj in sjs:
        result += f'번호: {sj[0]}, 이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}, 등록일: {sj[5]}\n'
    print(result)

# 학생 번호(sjno)로 성적데이터 조회후 출력
def showOneSungJuk():
    # name = input('조회할 학생 이름은?')
    sjno = input('조회할 학생 번호는?')
    result ='데이터가 존재하지 않아요!!'
    sj = readOneSungJuk(sjno)
    if sj: # 조회할 데이터가 존재한다면
        result = (f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}\n'
                  f'총점: {sj[5]}, 평균: {sj[6]:.1f}, 등급: {sj[7]}, 등록일: {sj[8]}')
    print(result)


# ------------------------------


# 학생 번호(sjno)으로 성적데이터 총 갯수 조회
def getTotalSungJUk():
    sql = 'select count(sjno) + 1  total from sungjuk'
    cnt = 0
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    for r in rs:
        cnt = r[0]
    cursor.close()
    conn.close()
    return cnt

# 입력 받은거 성적처리 계산 -> 총점 평균 학점 계산(compute)
def computeSungJuk(sj):
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(sj[4] / 3)
    grd =   '수' if sj[5] >= 90 else \
            '우' if sj[5] >= 80 else \
            '미' if sj[5] >= 70 else \
            '양' if sj[5] >= 60 else '가'
    sj.append(grd)

# 처리된 성적데이터를 테이블에 저장
def newSungJuk(sj):
    sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd) \
            values (?,?,?,?, ?,?,?);'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sj[0],sj[1],sj[2],sj[3],sj[4],sj[5],sj[6])
    cursor.execute(sql,  params)
    print(cursor.rowcount, '건의 데이터 추가됨!')
    conn.commit()
    cursor.close()
    conn.close()

# 성적 데이터 전체 조회
def readAllSungJuk():
    sql = 'select sjno, name, kor, eng, mat,substr(regdate,0,11) regdate  from sungjuk'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    sjs = cursor.fetchall()
    cursor.close()
    conn.close()
    return sjs

# 학생 한명의 성적 상세 조회
def readOneSungJuk(sjno):
    sql = 'select * from sungjuk where sjno = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sjno,)
    cursor.execute(sql, params)
    sj = cursor.fetchone()
    cursor.close()
    conn.close()
    return sj