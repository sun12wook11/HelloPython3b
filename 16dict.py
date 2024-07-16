# 딕셔너리
# 이름(key)과 값(value)으로 구성된 연관배열의 일종
# 자료구조를 만들때는 {}를 사용하고
# 이름과 값은 :으로 구분해서 정의함
# 다른 언어인  JSON과 유사한구조
# 이름을 통해 자료를 찾는 헤시 테이블을 이용하므로 검색속도가 빠름
# 순서와 상관없기에 빠름

# 중간고사 성적을 dict로 선언
sj = {'C/C++':'A', 'Java':'B+', '네트워크':'C', '보안':'A+', '해킹':'F', '클라우드':'C+'}

print(sj)

# 회원정보를 dict로 선언
# key : 이름, 아이디, 비번, 이메일, 주소, 취미
member = {'name':'홍길동',
          'uid':'abc',
          'pw':'123',
          'em':'a@1',
          'addr':'here',
          'hobby':['운동','게임','여행']}
print(member)

# 딕셔너리 다루기
# 조회 : 변수명[키], 변수명.get(키)
print(member['uid'], member['pw'])
print(member.get('em'),member.get('addr'))
print(member.get('zipcode'))

# 새로운 항목 추가 : 변수명['새로운키'] = 값을 지정
member['zipcode'] = '12345'

# 기존 항목 수정 : 변수명['키'] = 수정할값
member['zipcode'] = '98765'
member['addr'] = 'there'

# 기존항목 삭제 : 변수명.pop(키)
member.pop('zipcode')
member.pop('addr')

# dict의 모든 키 조회 : 변수명.keys()
# dict의 모든 값 조회 : 변수명.values()

print(member.keys())
print(member.values())


# dict 전체항목 조회 출력
for k in member.keys():
    print(f'{member[k]}', end=' ')

# 열거형 enumerrate으로 dict 조회
for idx, k in enumerate(member):
    print(idx, k)

# key와 value를 한번에 출력 : 변수명.items
for k, v in member.items():
    print(k,v)




# 중간고사 성적관리
quizs = []
trueCount = 0
falseCount = 0
totalCount = 0
sj = {'C/C++':'A',
      'Java':'B+',
      '네트워크':'C',
      '보안':'A+',
      '해킹':'F',
      '클라우드':'C+'}
print(sj)

# 2개 조회
print(sj['Java'], sj['클라우드'])

# 삽입 변경
sj['Python'] = 'A'
sj['OS'] = 'A+'

# 수정
sj['Java'] = 'F'
sj['클라우드'] = 'A'

# 조회 출력
for k, v in sj.items():
    print(k,v)





# 로또 게임
import random

# 사용자로부터 6개의 숫자를 입력받기
user_numbers = []
print("1부터 45까지의 정수 6개를 입력하세요.")
for i in range(6):
    num = int(input(f"Number {i + 1} : "))
    user_numbers.append(num)

# 컴퓨터가 랜덤하게 6개의 숫자 생성
random_numbers = random.sample(range(1, 46), 6)

# 일치하는 숫자 찾기
matching_numbers = set(user_numbers) & set(random_numbers)

# 결과 출력
print(f"이번주 로또 번호 {sorted(random_numbers)}")
print(f"내가 선택한 번호 {sorted(user_numbers)}")
print(f"일치하는 숫자 {sorted(matching_numbers)}")







# 수학시험 프로그램
# 문제, 정답, 점수 데이터를 저장
questions = [
    {"question": "3+2", "answer": 5, "score": 3},
    {"question": "5÷2의 몫", "answer": 2, "score": 5},
    {"question": "10÷2", "answer": 5, "score": 3},
    {"question": "10^2×2", "answer": 200, "score": 5},
    {"question": "1-(10÷4의 나머지)", "answer": -1, "score": 5},
    {"question": "2⁴", "answer": 16, "score": 3},
    {"question": "4÷2", "answer": 2, "score": 3},
]

# 변수 초기화
correct_count = 0
total_score = 0

# 답을 입력받아 채점
for q in questions:
    user_answer = int(input(f"문제 : {q['question']} = "))
    if user_answer == q["answer"]:
        print("정답입니다!")
        correct_count += 1
        total_score += q["score"]
    else:
        print(f"틀렸습니다. 정답은 {q['answer']}입니다.")

# 결과 출력
print(f"\n정답 개수: {correct_count}")
print(f"오답 개수: {len(questions) - correct_count}")
print(f"Total Score: {total_score}")
