# import sqlite3

#  밑에 터미널창에 pip install pymysqlfh 설치
import pymysql

# 데이터 베이스 연결 문자열
host = '52.78.137.248'  # 마리아디비 인스턴스 IP
dbname = 'clouds2024'   # 데이터베이스 이름
user = 'clouds2024'     # 데이터베이스 유저
passwd = 'clouds2024'   # 데이터베이스 비번

# 성적 DAO 클래스
class SungJukDAO:
    # 데이터베이스 연결객체와 커서 생성
    # 앞에 언더바쓰면 프라이빗하게 가능 (외부에서 이 함수 안보임)
    @staticmethod
    def _make_conn():
        """
        connect 연결과 cursor를 만드는 함수이다.
        :return: conn, cursor 값을 반환한다
        """
        conn = pymysql.connect(host=host, user=user,
                               password=passwd, database=dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    # 언더바쓰면 프라이빗하게 가능 (외부에서 이 함수 안보임)
    @staticmethod
    def _dis_conn(conn, cursor):
        """
        연결과 커서를 닫는 함수
        :param conn:
        :param cursor:
        :return:
        """
        cursor.close()
        conn.close()

    @staticmethod
    def insert_sungjuk(sj):
        """
        입력한 성적데이터를 sungjuk 테이블에 저장
        :param sj: 테이블에 저장할 성적데이터
        :return cnt: 테이블에 성공적으로 저장된 데이터 건수
        """
        sql = 'INSERT INTO sungjuk (name, kor, eng, mat, tot, avg, grd) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        """
        sungjuk 테이블에서 모든 성적 데이터(번호/이름/국어/영어/수학/등록일)를 읽어옴
        :return: 조회된 성적데이터 객체
        """
        sql = 'SELECT sjno, name, kor, eng, mat FROM sungjuk'
        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql)
        sjs = cursor.fetchall()
        SungJukDAO._dis_conn(conn, cursor)
        return sjs

    @staticmethod
    def selectone_sungjuk(sjno):
        """
        sungjuk 테이블에서 특정학생의 성적데이터를 읽어옴
        :param sjno: 조회할 학생의 학생번호
        :return: 조회된 학생의 성적데이터
        """
        sql = 'SELECT * FROM sungjuk WHERE sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql, (sjno,))
        sj = cursor.fetchone()
        SungJukDAO._dis_conn(conn, cursor)
        return sj

    @staticmethod
    def update_sungjuk(sj):
        """
        sungjuk 테이블 데이터 수정시 쓰는 함수
        :param sj: 테이블에 저장할 성적데이터
        :return: cnt: 테이블에 성공적으로 수정된 데이터 건수
        """
        sql = 'UPDATE sungjuk SET name = %s, kor = %s, eng = %s, mat = %s, tot = %s, avg = %s, grd = %s WHERE sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sj.sjno)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def delete_sungjuk(sjno):
        """
        sungjuk 테이블을 삭제하는 함수
        :param sjno: 조회할 학생의 학생번호
        :return:  테이블에 성공적으로 삭제된 데이터 건수
        """
        sql = 'DELETE FROM sungjuk WHERE sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql, (sjno,))
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt



from sunSfeed.oop.models import Employees

# 사원 DAO 클래스

# import pymysql
# host = '52.78.137.248'  # 마리아디비 인스턴스 IP
# dbname = 'clouds2024'   # 데이터베이스 이름
# user = 'clouds2024'     # 데이터베이스 유저
# passwd = 'clouds2024'   # 데이터베이스 비번

# 사원 DAO 클래스
class empDAO:
    @staticmethod
    def _make_conn():
        """
        connect 연결과 cursor를 만드는 함수이다.
        :return: conn, cursor 값을 반환한다
        """
        conn = pymysql.connect(host=host, user=user,
                               password=passwd, database=dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor


    @staticmethod
    def _dis_conn(conn, cursor):
        """
        연결과 커서를 닫는 함수
        :param conn:
        :param cursor:
        :return:
        """
        cursor.close()
        conn.close()


    @staticmethod
    def gettotal_emp():
        sql = 'select count(empid) + 99  total from EMPLOYEES'
        cnt = 0
        conn, cursor = empDAO._make_conn()
        cursor.execute(sql)
        rs = cursor.fetchall()
        for r in rs:
            cnt = r[0]
        empDAO._dis_conn(conn, cursor)
        return cnt


    # 처리된 성적데이터를 테이블에 저장
    @staticmethod
    def insert_emp(emp):
        sql =   "insert into EMPLOYEES values" \
                "(%s,%s,%s,%s, %s,%s,%s,%s, %s,%s,%s)"
        conn, cursor = empDAO._make_conn()
        params = (emp.empid,emp.fname,emp.lname,
                  emp.email,emp.phone,emp.hdate,
                  emp.jobid,emp.sal,emp.comm,emp.mgrid,emp.deptid)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        empDAO._dis_conn(conn, cursor)
        return cnt


    # 성적 데이터 중 empid,fname,lname,email,deptid 컬럼 전체 데이터 조회
    @staticmethod
    def select_emp():
        sql = 'SELECT empid, fname, lname, email, deptid FROM EMPLOYEES'
        conn, cursor = empDAO._make_conn()
        cursor.execute(sql)
        eps = cursor.fetchall()
        empDAO._dis_conn(conn, cursor)
        return eps


    # 직원 한명의 성적 상세 조회
    @staticmethod
    def selectone_emp(empid):
        sql = 'SELECT * FROM EMPLOYEES WHERE empid = %s'
        conn, cursor = empDAO._make_conn()
        params = (empid,)
        cursor.execute(sql, params)
        rs = cursor.fetchone()
        if rs:
            emp = Employees(rs[0],rs[1],rs[2],rs[3],rs[4],
                            rs[5],rs[6],rs[7],rs[8],rs[9],rs[10])
        else:
            emp = None

        empDAO._dis_conn(conn, cursor)
        return emp


    @staticmethod
    def delete_emp(empid):
        sql = 'DELETE FROM EMPLOYEES WHERE empid = %s'
        conn, cursor = empDAO._make_conn()
        params = (empid,)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        empDAO._dis_conn(conn, cursor)
        return cnt


    @staticmethod
    def update_emp(emp):
        sql = 'UPDATE EMPLOYEES SET email=%s, phone=%s, hdate=%s, jobid=%s, sal=%s, comm=%s, mgrid=%s, deptid=%s WHERE empid = %s'
        conn, cursor = empDAO._make_conn()
        params = (emp.email, emp.phone, emp.hdate, emp.jobid, emp.sal, emp.comm, emp.mgrid, emp.deptid, emp.empid)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        empDAO._dis_conn(conn, cursor)
        return cnt