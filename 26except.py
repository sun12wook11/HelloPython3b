# 예외except처리
# 프로그램 실행중 발생할 수 있는 예기치 않은 상황이나
# 오류를 관리하고 처리하는 프로그래밍 기법
# 에러: 시스템에서 발생하는 심각한 문제 (메모리 부족, 네트워크 통신 불가)
# -> 복구불가 -> 프로그래머 처리불가
# 예외 : 프로그램 실행중에 발생하는 예측가능한 오류
# -> 복구가능 -> 프로그래머 처리 가능


# 예외처리를 통해 프로그램의 안정성과 신뢰성 보장
# 오류 발생시 적절한 대응 및 비정상적인 종료(블루스크린,전원off등)를 방지
# 파이썬에서는 try ~ except ~ else ~ finally로 예외처리 구현

# 프로그램 실행 1
print('프로그램 실행 시작')
print(10/5)
print('프로그램 실행 끝') # 정상종료

# 프로그램 실행 2

print('프로그램 실행 시작')
print(10/0)
print('프로그램 실행 끝') # 중간 오류로 인한 비정상 종료

# 프로그램 실행 3

print('프로그램 실행 시작')
nums = [1,2,3]
print(nums[3])
print('프로그램 실행 끝') # 중간 오류로 인한 비정상 종료

# 발생한 오류를 예외처리하기
# try:
#     오류가 발생할만한 코드
# except:
#     오류가 발생시 처리할 코드


# 프로그램 실행 4
print('프로그램 실행 시작')
try:                    # 실행은 여기서부터
    print(10/0)         # ~
except:                 # 여기까지
    print('0으로 나누면 안되요!!') # 오류 뜨면 이거 호출
print('프로그램 실행 끝') # 중간 오류로 인한 except 호출

# 프로그램 실행 5

print('프로그램 실행 시작')
try:                      # 실행은 여기서부터
    nums = [1,2,3]
    print(nums[3])        # ~
except:                   # 여기까지
    print('오류: 리스트 넘버 확인!!') # 오류 뜨면 이거 호출
print('프로그램 실행 끝') # 중간 오류로 인한 비정상 종료

# 프로그램 실행 6 - 예외처리가 포괄적임
nums = [1,10,20,50]

try:
    idx = int(input('nums에서 사용할 값의 인덱스는? '))
    divr = int(input('받은 값을 나눌 정수는? '))
    print(nums[idx]/divr)
except:
    print('오류:발생')


# 프로그램 실행 7 - 예외처리 유형별로 세분화
# try:
#     오류가 발생할만한 코드
# except 예외유형1:
#     오류1 발생시 처리할 코드
# except 예외유형2:
#     오류2 발생시 처리할 코드
# except:
#     그외 기타오류 발생시 처리할 코드
nums = [1,10,20,50]
try:
    idx = int(input('nums에서 사용할 값의 인덱스는? '))
    divr = int(input('받은 값을 나눌 정수는? '))
    print(nums[idx]/divr)
except IndexError:
    print('리스트 인덱스가 너무 커')
except ZeroDivisionError:
    print('0으로 나누면 안돼!!')
except ValueError:
    print('숫자만 입력해!!')
except:
    print('알수없는 오류발생 - 관리자에게 문의!!')


# 프로그램 실행 8 - FileNotFoundError
try:
    with open('abc123.xyz') as f:
        f.read()
except FileNotFoundError:
    print('파일이나 디렉토리가 없어요!!')