-- # 사원데이터 기반 CRUD 기능이 제공되는 프로그램
-- # 사원 - empid, fname, lname,email,phone,
-- #       hdate,jobid,sal,comm,mgrid,deptid
-- # 조회 - 사원번호,이름,이메일,부서번호
-- # 상세조회 -특정 사원번호 대상 모든 칼럼 출력
--
-- # 3 LAYER - <emp table>
-- # 28sungjukV7   -> main     -> 30EMP
-- # sungjuk7      -> service  -> emp
-- # sungjukv7DAO  -> DAO      -> empDAO
--
-- 1. 테이블 만들고 데이터 넣고
-- 2. 3 레이어 구축 - <30EMP/emp/emoDAO>
-- 3. 적절하게 수정

-- emo 테이블 만들기
create table EMPLOYEES
(
    empid  integer     not null
        primary key autoincrement,
    fname  varchar(2)  not null,
    lname  varchar(20) not null,
    email  varchar(20) not null,
    phone  varchar(20) not null,
    hdate  date        not null,
    jobid  varchar(20) not null,
    sal    int         not null,
    comm   float,
    mgrid  int,
    deptid int
);

-- emo 테이블 삭제
drop table EMPLOYEES;

-- emo 데이터 추가 (파일 불러오기)

-- emo 데이터 검색
select * from sungjuk;

-- emo 데이터 중 사원번호,이름,이메일,부서번호 만 조회
select empid, fname, lname, email, deptid from EMPLOYEES;

-- 성적 데이터 중 학생번호로 검색해서 모두 조회
select * from EMPLOYEES where empid = 100;


