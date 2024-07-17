# 성적 처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# CRUD기능을 지원하는 성적처리프로그램 재작성하기
# 메뉴 UI 추가
# 즉, 성적입력, 조회, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당
# 성적 데이터는 리스트, 튜플, 딕셔너리로 작성


import sys

# 프로그램 메뉴 정의
main_menu = '''
================== 
 성적 프로그램 v4
==================
 1. 추가
 2. 조회
 3. 상세조회
 4. 수정
 5. 삭제 
 0. 종료
==================
'''
# 메뉴 출력 및 메뉴 별 처리


sjs =[['일지매',99,87,65,251,83.7,'우']]



while True:
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')

    if menu == '1':
        print('성적 데이터 추가')
        sj = []
        cnt = len(sjs)
        sj.append  (input(f"{cnt}번학생 이름을 입력하세요: "))
        sj.append  (int(input(f"{cnt}학생 국어 점수를 입력하세요: ")))
        sj.append (int(input(f"{cnt}번학생 영어 점수를 입력하세요: ")))
        sj.append (int(input(f"{cnt}번학생 수학 점수를 입력하세요: ")))
        sj.append(sj[1] + sj[2] + sj[3])
        sj.append(sj[4] / 3)
        grd =     '수' if (sj[5] >= 90) else \
                  '우' if (sj[5] >= 90) else \
                  '미' if (sj[5] >= 90) else \
                  '양' if (sj[5] >= 90) else '가'
        grd.append(grd)
        sjs.append(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        for sj in sjs:
            print(f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}')

    elif menu == '3':
            print('성적 데이터 상세조회')
            pass
    elif menu == '4':
            print('성적 데이터 수정')
            pass
    elif menu == '5':
            print('성적 데이터 삭제')
            pass
    elif menu == '0':
            print('프로그램 종료')
            sys.exit(0)
    else:
            print('메뉴를 잘못 선택하셨습니다!!')














#
import sys

# 프로그램 메뉴 정의
main_menu = '''
================== 
 성적 프로그램 v4
==================
 1. 추가
 2. 조회
 3. 상세조회
 4. 수정
 5. 삭제 
 0. 종료
==================
'''

# 초기 데이터 설정
students = {
    '일지매': {'kor': 99, 'eng': 87, 'mat': 65, 'tot': 251, 'avg': 83.7, 'grd': '우'}
}

def calculate_grade(avg):
    if avg >= 90:
        return '수'
    elif avg >= 80:
        return '우'
    elif avg >= 70:
        return '미'
    elif avg >= 60:
        return '양'
    else:
        return '가'

def add_student():
    name = input("학생 이름을 입력하세요: ")
    kor = int(input(f"{name} 학생 국어 점수를 입력하세요: "))
    eng = int(input(f"{name} 학생 영어 점수를 입력하세요: "))
    mat = int(input(f"{name} 학생 수학 점수를 입력하세요: "))

    tot = kor + eng + mat
    avg = tot / 3
    grd = calculate_grade(avg)

    students[name] = {'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}
    print(f"{name} 학생의 성적이 추가되었습니다.")

def view_all_students():
    for name, data in students.items():
        print(f"이름: {name}, 국어: {data['kor']}, 영어: {data['eng']}, 수학: {data['mat']}, 총점: {data['tot']}, 평균: {data['avg']:.2f}, 등급: {data['grd']}")

def view_student_detail():
    name = input("조회할 학생의 이름을 입력하세요: ")
    if name in students:
        data = students[name]
        print(f"이름: {name}, 국어: {data['kor']}, 영어: {data['eng']}, 수학: {data['mat']}, 총점: {data['tot']}, 평균: {data['avg']:.2f}, 등급: {data['grd']}")
    else:
        print(f"{name} 학생의 데이터가 존재하지 않습니다.")

def modify_student():
    name = input("수정할 학생의 이름을 입력하세요: ")
    if name in students:
        kor = int(input(f"{name} 학생 국어 점수를 입력하세요: "))
        eng = int(input(f"{name} 학생 영어 점수를 입력하세요: "))
        mat = int(input(f"{name} 학생 수학 점수를 입력하세요: "))

        tot = kor + eng + mat
        avg = tot / 3
        grd = calculate_grade(avg)

        students[name] = {'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}
        print(f"{name} 학생의 성적이 수정되었습니다.")
    else:
        print(f"{name} 학생의 데이터가 존재하지 않습니다.")

def delete_student():
    name = input("삭제할 학생의 이름을 입력하세요: ")
    if name in students:
        del students[name]
        print(f"{name} 학생의 데이터가 삭제되었습니다.")
    else:
        print(f"{name} 학생의 데이터가 존재하지 않습니다.")

# 메뉴 출력 및 메뉴 별 처리
while True:
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')

    if menu == '1':
        add_student()
    elif menu == '2':
        view_all_students()
    elif menu == '3':
        view_student_detail()
    elif menu == '4':
        modify_student()
    elif menu == '5':
        delete_student()
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')

