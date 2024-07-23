import sqlite3

# 성적 DAO 클래스
class SungJukDAO:

    # 데이터베이스 연결객체와 커서 생성
    # 언더바쓰면 프라이빗하게 가능 (외부에서 이 함수 안보임)
    @staticmethod
    def _make_conn():
        conn = sqlite3.connect('db/python.db')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    # 언더바쓰면 프라이빗하게 가능 (외부에서 이 함수 안보임)
    @staticmethod
    def _dis_conn(conn, cursor):
        cursor.close()
        conn.close()

    @staticmethod
    def insert_sungjuk(sj):
        sql = 'INSERT INTO sungjuk (sjno, name, kor, eng, mat, tot, avg, grd) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.sjno, sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        sql = 'SELECT sjno, name, kor, eng, mat FROM sungjuk'
        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql)
        sjs = cursor.fetchall()
        SungJukDAO._dis_conn(conn, cursor)
        return sjs

    @staticmethod
    def selectone_sungjuk(sjno):
        sql = 'SELECT * FROM sungjuk WHERE sjno = ?'
        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql, (sjno,))
        sj = cursor.fetchone()
        SungJukDAO._dis_conn(conn, cursor)
        return sj

    @staticmethod
    def update_sungjuk(sj):
        sql = 'UPDATE sungjuk SET name = ?, kor = ?, eng = ?, mat = ?, tot = ?, avg = ?, grd = ? WHERE sjno = ?'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sj.sjno)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def delete_sungjuk(sjno):
        sql = 'DELETE FROM sungjuk WHERE sjno = ?'
        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql, (sjno,))
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt