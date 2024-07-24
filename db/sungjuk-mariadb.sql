-- 마리아디비

-- 성적 테이블 삭제
drop table sungjuk;

-- 성적 테이블 만들기
create table sungjuk
(
    sjno    int auto_increment primary key,
    name    varchar(10) not null,
    kor     int         not null,
    eng     int         not null,
    mat     int         not null,
    tot     int         not null,
    avg     decimal(5, 1),
    grd     varchar(2),
    -- regdate datetime default now() -- UTC
    regdate datetime default current_timestamp -- UTC + 9
);

-- 성적 데이터 추가
insert into sungjuk (name, kor, eng, mat, tot, avg, grd)
values ('abc123',99,99,99,297,99.0,'수');


-- 성적 데이터 검색
select * from sungjuk;

-- 성적 데이터 중 이름,국어,영어,수학만 조회
select name, kor, eng, mat from sungjuk;

-- 성적 데이터 중 이름,국어,영어,수학, 등록일만 조회
select name, kor, eng, mat, substr(regdate,0,10) regdate
from sungjuk;

-- 성적 데이터 중 이름으로 검색해서 모두 조회
select * from sungjuk where name = 'abc123';

-- 성적 데이터 중 학생번호로 검색해서 모두 조회
select * from sungjuk where sjno = 1;
