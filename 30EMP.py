# -- # 사원데이터 기반 CRUD 기능이 제공되는 프로그램
# -- # 사원 - empid, fname, lname,email,phone,
# -- #       hdate,jobid,sal,comm,mgrid,deptid
# -- # 조회 - 사원번호,이름,이메일,부서번호
# -- # 상세조회 -특정 사원번호 대상 모든 칼럼 출력
# --
# -- # 3 LAYER - <emp table>
# -- # 28sungjukV7   -> main     -> 30EMP
# -- # sungjuk7      -> service  -> emp
# -- # sungjukv7DAO  -> DAO      -> empDAO

import sys
import sunSfeed.empDAO as eda
import sunSfeed.emp as emp

# 메뉴출력 및 메뉴별 처리
while True:
    menu = emp.displayMenu()

    if menu == '1':
        print('직원 데이터 추가')
        ep = emp.readEmployees()
        emp.addEmployees(ep)

    elif menu == '2':
        print('직원 데이터 조회')
        emp.showEmployees()

    elif menu == '3':
        print('직원 데이터 상세조회')
        emp.showOneEmployees()

    elif menu == '4':
        print('직원 데이터 수정')
        # 수정 로직 추가 필요
        pass

    elif menu == '5':
        print('직원 데이터 삭제')
        emp.removeEmp

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다!!')

