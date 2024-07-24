# 성적 처리 프로그램 v8b
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# CRUD기능을 지원하는 성적처리프로그램 재작성하기
# 메뉴 UI 추가
# 즉, 성적입력, 조회, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당
#클래스 기반으로 프로그램 작성

# pache
# v8b 데이터베이스는 마리아 디비 10.6으로 변경


# main consol


import sys
from sunSfeed.oop.services import SungJukService as sjv8
import sunSfeed.sungjukv8DAO as sjv8dao
import sunSfeed.sungjukv8

# 메뉴출력 및 메뉴별 처리
while True:
    menu = sjv8.display_menu()

    if menu == '1':
        print('성적 데이터 추가')
        sjv8.add_sungjuk()

    elif menu == '2':
        print('성적 데이터 조회')
        sjv8.show_sungjuk()

    elif menu == '3':
        print('성적 데이터 상세조회')
        sjv8.showone_sungjuk()

    elif menu == '4':
        print('성적 데이터 수정')
        sjv8.modify_sungjuk()

    elif menu == '5':
        print('성적 데이터 삭제')
        sjv8.remove_sungjuk()

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다!!')

