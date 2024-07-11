# 4

# 12
# 0,1 보다는 TF로 쓰면 if 문에서 조건 바로 적용가능함

# 14


# 16
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



