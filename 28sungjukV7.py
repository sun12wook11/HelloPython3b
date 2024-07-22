# 성적 처리 프로그램 v7
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# CRUD기능을 지원하는 성적처리프로그램 재작성하기
# 메뉴 UI 추가
# 즉, 성적입력, 조회, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당
# 성적 데이터는 리스트, 튜플, 딕셔너리로 작성

# V5 함수와 모듈 추가
# V6 리스트 형태로 저장된 파일을 sungjuk.dat(csv 형식 ',')에 저장
# V7 sql 데비터베이스

import sys
import sunSfeed.sungjukv7 as sjv7

# 메뉴출력 및 메뉴별 처리
while True:
    menu = sjv7.displayMenu()

    if menu == '1':
        print('성적 데이터 추가')
        sj = sjv7.readSungJuk()
        sjv7.addSungJuk(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        sjv7.showSungJuk()

    elif menu == '3':
        print('성적 데이터 상세조회')
        sjv7.showOneSungJuk()

    elif menu == '4':
        print('성적 데이터 수정')
        # 수정 로직 추가 필요
        pass

    elif menu == '5':
        print('성적 데이터 삭제')
        # 삭제 로직 추가 필요
        pass

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다!!')

