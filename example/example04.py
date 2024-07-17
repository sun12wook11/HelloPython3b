# 51 구구단
# 리스트 초기화
results = [[] for _ in range(9)]
# 각 구구단의 결과 계산하여 리스트에 추가
print('            Multiplication Table      ')
print('        1   2   3   4   5   6   7   8   9        ')
print('-----------------------------------------  ')
for i in range(1, 10): # i,j는 반복문이 실행될때만 살아있다
    for j in range(1, 10):
        result = i * j
        results[i-1].append(result)

# 각 단을 가로로 출력
for row in range(9):
    line = f"{row+1} |  "
    for col in range(9):
        line += f" {results[row][col]:3d}"  # 각 결과를 2자리 정수 형태로 출력
    print(line)



# 달력


# 33
cardno = input('카드번호는? ')

result = '잘못된 카드 번호입니다'
if cardno[0:1] == '3':
    if cardno == '356317': result = 'JCB NH농협카드'
    elif cardno == '356901': result = 'JCB 신한카드'
    elif cardno == '356912': result = 'JCB KB국민카드'
elif cardno[0:1] == '4':
    if cardno == '404825': result = '비자카드 비씨카드'
    elif cardno == '438676': result = '비자카드 신한카드'
    elif cardno == '404825': result = '비자카드 KB국민카드'
elif cardno[0:1] == '5':
    if cardno == '515594': result = '마스터카드 신한카드'
    elif cardno == '524353': result = '마스터카드 외환카드'
    elif cardno == '540926': result = '마스터카드 KB국민카드'

print(f'{cardno} / {result}')



# 16 거스름돈 계산하기 리스트/반복문/함수을 이용해서 개선하기
money = int(input('받은돈: '))
price = int(input('상품금액: '))
charge1 = money - price
charge = money - price

w50000 = charge//50000
# charge = charge - w50000 * 50000
charge &= 50000

w10000 = charge//10000
# charge = charge - w10000 * 0000
charge &= 10000

w5000 = charge//5000
# charge = charge - w5000 * 5000
charge &= 5000

w1000 = charge//1000
# charge = charge - w1000 * 1000
charge &= 1000

w500 = charge//500
# charge = charge - w500 * 000
charge &= 500

w100 = charge//100
# charge = charge - w100 * 100
charge &= 100

w50 = charge//50
# charge = charge - w50 * 50
charge &= 50

w10 = charge//10
# charge = charge - w10 * 10
charge &= 10


print(f'거스름돈은 {charge1} 입니다.')
print (f'여기 50000원권 {w50000}장') if w50000 >= 1 else print('')
print (f'여기 10000원권 {w10000}장') if w10000 >= 1 else print('')
print (f'여기 5000원권 {w5000}장') if w5000 >= 1 else print('')
print (f'여기 1000원권 {w1000}장') if w1000 >= 1 else print('')
print (f'여기 500원 {w500}개') if w500 >= 1 else print('')
print (f'여기 100원 {w100}개') if w100 >= 1 else print('')
print (f'여기 50원 {w50}개') if w50 >= 1 else print('')
print (f'여기 10원 {w10}개') if w10 >= 1 else print('')
print('드리겠습니다.')



money = int(input('받은돈: '))
price = int(input('상품금액: '))

charge = money - price
charge1 = charge

# 화폐 단위 리스트 (큰 단위부터 작은 단위 순서로)
currency_units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
currency_counts = {}

# 각 화폐 단위에 대한 개수를 계산
for unit in currency_units:
    currency_counts[unit] = charge // unit
    charge %= unit

print(f'거스름돈은 {charge1} 입니다.')
for unit in currency_units:
    count = currency_counts[unit]
    if count > 0:
        print(f'여기 {unit}원권 {count}장') if unit >= 1000 else print(f'여기 {unit}원 {count}개')
print('드리겠습니다.')







# 거스름돈 개선 GPT

def compute_charge(money, price):
    # 화폐 단위 리스트 (큰 단위부터 작은 단위 순서로)
    currency_units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    currency_counts = {}
    # 각 화폐 단위에 대한 개수를 계산
    charge = money - price
    for unit in currency_units:
        currency_counts[unit] = charge // unit
        charge %= unit

    return money - price, currency_counts

def print_change(charge1, currency_counts):
    print(f'거스름돈은 {charge1} 입니다.')
    for unit, count in currency_counts.items():
        if count > 0:
            print(f'여기 {unit}원권 {count}장') if unit >= 1000 else print(f'여기 {unit}원 {count}개')
    print('드리겠습니다.')

def main():
    money = int(input('받은돈: '))
    price = int(input('상품금액: '))
    charge1, currency_counts = compute_charge(money, price)
    print_change(charge1, currency_counts)

# if __name__ == "__main__":
    main()


# # 하나의 코드 스크립트로 정리된 mymodule.py와 import_script.py
#
# def main():
#     print("This is the main function.")
#
# def other_function():
#     print("This is another function.")
#
# print("This will always be printed.")
#
# if __name__ == "__main__":
#     print("This will only be printed if mymodule.py is run directly.")
#     main()
#
# def run_import_script():
#     import mymodule
#
#     print("Importing mymodule...")
#     mymodule.other_function()
#
# if __name__ == "__main__":
#     run_import_script()
#
# # 실행 결과
#
# # mymodule.py를 직접 실행한 경우
# print("=== Running mymodule.py directly ===")
# main()
#
# # import_script.py를 실행한 경우
# print("\n=== Running import_script.py ===")
# run_import_script()
