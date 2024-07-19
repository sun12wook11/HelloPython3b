import sqlite3

# 데이터베이스 파일 경로
db_file = 'db/python.db'

# 1. 테이블 생성
def create_table():

    conn = sqlite3.connect(db_file)
    # 데이터베이스 커서 생성
    cursor = conn.cursor()

    # 실행할 SQL 작성
    sql = '''CREATE TABLE IF NOT EXISTS member (
                userid VARCHAR(18) NOT NULL PRIMARY KEY,
                passwd VARCHAR(18) NOT NULL,
                name VARCHAR(10) NOT NULL,
                email VARCHAR(35) NOT NULL)'''

    # 작성한 sql을 실행
    cursor.execute(sql)
    conn.commit()

    # 작업 마무리
    cursor.close()
    conn.close()

# 2. 데이터 추가
def add_member(user_id, password, name, email):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    sql = 'INSERT INTO member (userid, passwd, name, email) VALUES (?, ?, ?, ?)'
    cursor.execute(sql, (user_id, password, name, email))
    conn.commit()
    cursor.close()
    conn.close()

# 메인 코드
create_table()

user_id = input("아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")
name = input("이름을 입력하세요: ")
email = input("이메일을 입력하세요: ")

add_member(user_id, password, name, email)
print("회원 정보가 성공적으로 저장되었습니다.")
