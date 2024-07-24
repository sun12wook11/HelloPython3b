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
        """
        학점 계산하는 함수
        :return: grd 학점
        """
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


# 사원 클래스
class Employees:
    def __init__(self, empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid):
        self.empid = empid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.hdate = hdate
        self.jobid= jobid
        self.sal = sal
        self.comm = comm
        self.mgrid = mgrid
        self.deptid = deptid