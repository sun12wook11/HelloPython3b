# 함수
# 특정 기능을 수행하는 코드블록 (모음)에 이름을 부여한 것
#  즉, 여러 곳에 반복적으로 사용할 가치가 있는 코드들을
# 한 뭉치로 묶고 (어떤 값을 입력하면) 결과가 반환되도록
# 작성한 것 - 재사용이 주 목적
# 이처럼 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목 요연하게 파악가능
# 다른 사람과의 협업시에 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈


# 함수 정의
# def 함수명(매개변수):
#     함수몸체




# 1. 단순 출력
print('오늘 날씨는 비옴!')

# 2. 반복 출력
for _ in range(3):
    print('오늘 날씨는 비옴!')



# 3. 반복 출력 모듈화
def say_weather():
    for _ in range(3):
        print('오늘 날씨는 비옴!')

        # 함수 호출1
        say_weather()

# 4. 반복 변수 함수
def say_weather2(info):
    for _ in range(1):
        print(f'오늘 날씨는 {info}!')

        # 함수 호출2(인자)
        say_weather2('나쁨')


# 5. 단위 변환 함수 만들기 (cm -> inch)
def convert_cm_to_inch(cm):
    inch = cm / 2.54
    return inch

# 센티미터 값 입력
cm = float(input("센티미터(cm) 값을 입력하세요: "))

# 인치로 변환 후 출력
inch = convert_cm_to_inch(cm)
print(f"{cm} 센티미터는 {inch:.2f} 인치입니다.")


# 6. 변수의 유효범위 scope
# scope: 변수가 접근가능한 범위를 의미
# 전역 scope: 프로그램의 최상위 레벨에서 정의된 변수
#            어느곳에서나 접근가능
#            함수내에서 전역변수로의 접근(사용) 가능
#            단, global이라는 키워드를 사용해서 전역변수에 접근가능

# 지역 scope: 반목문 내부 / 함수 내부에 정의된 변수
#            반복문이나 함수 내에서만 접근 가능
#            반복문 실행 종료나 함수 호출이 끝나면 자동 소멸


# 7. 함수 서순
x = 10 # 전역 변수
y = 10

def func1():
    x = 20
    print('func : ', x) # 함수내 지역변수 x 호출 (밖이랑 다름)

def func2():
    global y # 함수 내 전역 변수 가져오고 제어 - (눌러보면 색 같음)
    y = 20
    print('func : ', y) # 함수내 x 호출


print(x) # x 출력
func1() # x 함수 호출
print(x) # 함수 밖 x 출력

print(y) # y 출력 (함수 적용전)
func2() # y 함수 호출
print(y) # 함수 밖 y 출력 (함수 적용됨)


# 웹 사이트 방문 횟수 누적 프로그램
visits = 0
isFlag = True


def visits_count ():
    global visits, isFlag, menu
    while isFlag:
        menu = input('1. 웹사이트 방문 2. 종료 : ')
        if menu == '1': visits += 1
        elif menu == '2':
            print('방문을 종료합니다!')
            print('누적 방문횟수는 ',visits,'회 입니다')
            isFlag = False
            break

visits_count ()


#
totalPrice = 0
goodsCount = [5, 2, 10, 3]

def printReceipt():

    goods0Price = 1000
    goods1Price = 500
    goods2Price = 2000
    goods3Price = 1500

    global totalPrice  # Using global to modify totalPrice inside the function

    totalPrice += goods0Price * goodsCount[0]
    totalPrice += goods1Price * goodsCount[1]
    totalPrice += goods2Price * goodsCount[2]
    totalPrice += goods3Price * goodsCount[3]

    print('------printReceipt')
    print('totalPrice = ', totalPrice)

printReceipt()


#
goods = 1
goodsCount = [5, 2, 10, 3]

def printReceipt():
    total = 0
    total = 1000 * goodsCount[0] # 리스트는 참조 자료형이므로
                                 # 주소로 접근하기에 별다른 코드 없이 해당 변수 접근가능
    print(total)

    goodsCount[0] = 10
    total2 = 1000 * goodsCount[0]
    print(total2)
    # goodsCount = [99,99,99,99] # 전역변수 자체를 변경할려고 하면 오류발생
                                 # 글로벌 필수

    print(goodsCount[0])
    goodsCount[0] = 10           # 글로벌 없이 리스트 일부 변경 가능
    # print(goods)               # 변수는 글로벌해야됨
    # goods = 5


printReceipt()
print(goodsCount[0])
print(goods)