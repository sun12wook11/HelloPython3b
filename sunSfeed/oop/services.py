# models의 SungJuk 가져오기
from sunSfeed.oop.models import SungJuk
# dao 가져오기
from sunSfeed.oop.dao import SungJukDAO as sjdao

# 성적 서비스 클래스
class SungJukService:
    # 데코레이터(@) : 함수에 추가 기능을 구현할때 사용
    # 프로그램 실행전 컴파일러에게 미리 내리는 지시
    @staticmethod   # 정적static 메서드: 객체화없이 바로 사용가능한 매서드
                    # 정적메서드로 정의된 함수는 self 매개변수 지정 할 필요없다.
                    # 호츨방법 : 클래스명.함수명
    def display_menu():
        """
        프로그램 메뉴 UI 호출 함수
        :return:
        """

        main_menu = '''
        ================== 
         성적 프로그램 v8
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

    @staticmethod
    def read_sungjuk():
        """
        학생 정보를 입력하는 함수
        :return:
        """
        sjno = input("새로운 학생 번호를 입력하세요: ")
        name = input(f"새로운 학생 이름을 입력하세요: ")
        kor = int(input(f"새로운 학생 국어 점수를 입력하세요: "))
        eng = int(input(f"새로운 학생 영어 점수를 입력하세요: "))
        mat = int(input(f"새로운 학생 수학 점수를 입력하세요: "))
        return SungJuk(sjno, name, kor, eng, mat)

    @staticmethod
    def add_sungjuk():
        """
        read_sungjuk으로 입력받은 데이터를 추가(저장)하는 함수
        :return:
        """
        sj = SungJukService.read_sungjuk()
        cnt = sjdao.insert_sungjuk(sj)
        result = f'{cnt}건의 데이터 추가 성공!!'
        print(result)

    @staticmethod
    def compute_sungjuk(sj):
        """
        계산하는 함수
        :param sj: 입력받은 함수
        :return: 계산된 값들
        """
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90): sj.grd = '수'
        elif (sj.avg >= 80): sj.grd = '우'
        elif (sj.avg >= 70): sj.grd = '미'
        elif (sj.avg >= 60): sj.grd = '양'

    @staticmethod
    def show_sungjuk():
        """
        모든 학생 데이터중 이름국어영어수학만 보여주는 함수
        :return:
        """
        result = ''
        sjs = sjdao.select_sungjuk()
        for sj in sjs:
            result += f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}\n'
        print(result)

    @staticmethod
    def showone_sungjuk():
        """
        상세정보를 보여주는 함수
        :return:
        """
        sjno = input('조회할 학생의 번호를 입력하세요: ')
        sj = sjdao.selectone_sungjuk(sjno)
        if sj:
            result = f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}, 총점: {sj[5]}, 평균: {sj[6]}, 학점: {sj[7]}\n'
            print(result)
        else:
            print('해당 번호의 학생이 없습니다.')

    @staticmethod
    def modify_sungjuk():
        """
        데이터를 수정하는 함수
        :return:
        """
        sjno = input('수정할 학생의 번호를 입력하세요: ')
        sj = sjdao.selectone_sungjuk(sjno)
        if sj:
            sj = SungJukService.read_sungjuk()
            sj.sjno = sjno
            cnt = sjdao.update_sungjuk(sj)
            result = f'{cnt}건의 데이터 수정 성공!!'
            print(result)
        else:
            print('해당 번호의 학생이 없습니다.')

    @staticmethod
    def remove_sungjuk():
        """ 데이터를 지우는 함수"""
        sjno = input('삭제할 학생의 번호를 입력하세요: ')
        cnt = sjdao.delete_sungjuk(sjno)
        result = f'{cnt}건의 데이터 삭제 성공!!'
        print(result)
