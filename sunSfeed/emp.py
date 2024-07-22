# 3 LAYER
# 28sungjukV7   -> main
# sungjuk7      -> service
# sungjukv7DAO  -> DAO

# Employees 데이터베이스화(sql)

import sunSfeed.empDAO as eda

# main UI 창 만들기
def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
    ================== 
     사원 전산 시스템
    ==================
     1. 사원 데이터 추가
     2. 사원 데이터 조회
     3. 사원 데이터 상세 조회
     4. 사원 데이터 수정
     5. 사원 데이터 삭제 
     0. 프로그램 종료
    ==================
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')
    return menu

# 직원 데이터 리스트 입력 받기
def readEmployees():
    ep = []
    cnt = eda.getTotalEmp() + 1
    print(f"현재 직원 수: {cnt-1}, 다음 직원 ID는 {cnt+99}입니다.")
    ep.append(input(f"{cnt+99}번 직원 FIRST_NAME을 입력하세요: "))
    ep.append(input(f"{cnt+99}번 직원 LAST_NAME을 입력하세요: "))
    ep.append(input(f"{cnt+99}번 직원 EMAIL을 입력하세요: "))
    ep.append(input(f"{cnt+99}번 직원 PHONE_NUMBER를 입력하세요: "))
    ep.append(input(f"{cnt+99}번 직원 HIRE_DATE를 입력하세요 (YYYY-MM-DD): "))
    ep.append(input(f"{cnt+99}번 직원 JOB_ID를 입력하세요: "))
    ep.append(input(f"{cnt+99}번 직원 SALARY를 입력하세요: "))
    ep.append(input(f"{cnt+99}번 직원 COMMISSION_PCT를 입력하세요 (소수점 포함, 없으면 0): "))
    ep.append(input(f"{cnt+99}번 직원 MANAGER_ID를 입력하세요: (없으면 0)"))
    ep.append(input(f"{cnt+99}번 직원 DEPARTMENT_ID를 입력하세요: (없으면 0)"))
    return ep

# 입력받은 직원 리스트 데이터 저장
# 입력박은 것들중 일부는 적절한 형변환이 필요
def addEmployees(ep):
    # 점수 계산 학점 출력 함수
    # computeEmployees(ep)
    # 기존 입력받은 데이터 + 계산된 데이터 합쳐서 DB 업로드
    emp = readEmployees()
    emp[8] = float(emp[8]) if emp[8] != 0 else None
    emp[9] = float(emp[9]) if emp[9] != 0 else None
    emp[10] = float(emp[10]) if emp[10] != 0 else None

# 리스트에 저장된 직원 데이터 조회
def showEmployees():
    result =''
    eps = eda.readAllEmployees()
    for ep in eps:
        result += f'empid: {ep[0]}, fname: {ep[1]}, lname: {ep[2]}, email: {ep[3]}, deptid: {ep[4]}\n'
    print(result)

# 직원 번호(empid)로 해당 직원 데이터 전체 출력
def showOneEmployees():
    # name = input('조회할 학생 이름은?')
    empid = input('조회할 직원 번호는?')
    result ='데이터가 존재하지 않아요!!'
    ep = eda.readOneEmployees(empid)
    if ep: # 조회할 데이터가 존재한다면
        result = f'empid: {ep[0]}, fname: {ep[1]}, lname: {ep[2]}, email: {ep[3]}, phone: {ep[4]},\n \
        hdate: {ep[5]}, jobid: {ep[6]}, sal: {ep[7]}, comm: {ep[8]}, mgrid: {ep[9]}, deptid: {ep[10]}'
    print(result)

    # ------------------------------

    # # 입력 받은거 성적처리 계산 -> 총점 평균 학점 계산(compute)
    # def computeEmployees(ep):
    #     ep.append(sj[1] + sj[2] + sj[3])
    #     sj.append(sj[4] / 3)
    #     grd =   '수' if sj[5] >= 90 else \
    #             '우' if sj[5] >= 80 else \
    #             '미' if sj[5] >= 70 else \
    #             '양' if sj[5] >= 60 else '가'
    #     sj.append(grd)


#
def removeEmp():
    empid = input('삭제할 사원의 사원번호는? ')
    result = '데이터가 존재하지 않아요!!'
    cnt = eda.deleteEmp(empid)
    if cnt > 0:
        result = f'{cnt}건의 데이터가 삭제됨!!'
    print(cnt, '건의 데이터가 삭제됨!!')
