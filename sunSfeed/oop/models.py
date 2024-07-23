# 성적 클래스
class SungJuk:
    def __init__(self, sjno, name, kor, eng, mat):
        self.sjno = sjno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = kor + eng + mat
        self.avg = self.tot / 3
        self.grd = self.calculate_grade()


    def calculate_grade(self):
        if self.avg >= 90:
            return '수'
        elif self.avg >= 80:
            return '우'
        elif self.avg >= 70:
            return '미'
        elif self.avg >= 60:
            return '양'
        else:
            return '가'