# EMP 데이터베이스화(sql)
import sqlite3

# # empid로 성적데이터 총 갯수 조회
def getTotalEmp():
    sql = 'select count(empid) + 1  total from EMPLOYEES'
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

# 처리된 성적데이터를 테이블에 저장
def newEmployees(ep):
    sql = "insert into EMPLOYEES (fname,lname,email,phone,hdate,jobid,sal,comm,mgrid,deptid)  \
            values (?,?,?,?, ?,?,?,?, ?,?,?);"
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (ep[0],ep[1],ep[2],ep[3],ep[4],ep[5],ep[6],ep[7],ep[8],ep[9])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터 추가됨!')
    conn.commit()
    cursor.close()
    conn.close()

# 성적 데이터 중 empid,fname,lname,email,deptid 컬럼 전체 데이터 조회
def readAllEmployees():
    # SQL 쿼리 정의
    sql = 'select empid,fname,lname,email,deptid from Employees'
    # 데이터베이스 연결
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    # SQL 쿼리 실행
    cursor.execute(sql)
    # 조회 결과 가져오기
    eps = cursor.fetchall()
    # 커서와 연결 종료
    cursor.close()
    conn.close()
    # 조회 결과 반환
    return eps

# 직원 한명의 성적 상세 조회
def readOneEmployees(empid):
    sql = 'select * from Employees where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid,)
    cursor.execute(sql, params)
    ep = cursor.fetchone()
    cursor.close()
    conn.close()
    return ep

def deleteEmp(empid):
    sql = 'delete from Employees where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid, )
    cursor.execute(sql, params)
    cnt = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return cnt



def updateEmp(emp):
    sql = 'update EMPLOYEES set email=? ,phone=? ,hdate=? ,jobid=? ,sal=? ,comm=? ,mgrid=?, deptid=? \
            where empid = ?;'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (emp[3],emp[4],emp[5],emp[6],emp[7], emp[8],emp[9],emp[10],emp[0])
    cursor.execute(sql,  params)
    print(cursor.rowcount, '건의 데이터 수정됨!')
    conn.commit()
    cursor.close()
    conn.close()