import datetime

def check_jumin(jumin):
    if not jumin.isdigit() or len(jumin) != 13:
        return False

    gender_digit = int(jumin[6])
    if gender_digit not in [1, 2, 3, 4]:
        return False

    year = int("19" if gender_digit in [1, 2] else "20" + jumin[:2])
    month = int(jumin[2:4])
    day = int(jumin[4:6])

    try:
        datetime.date(year, month, day)
    except ValueError:
        return False

    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    checksum = sum(int(jumin[i]) * weights[i] for i in range(12))
    check_digit = (11 - (checksum % 11)) % 10

    return check_digit == int(jumin[12])

def read_jumin():
    while True:
        jumin = input("주민등록번호를 13자리로 입력하세요 (예: 1234561234567): ").strip()
        if len(jumin) == 13 and jumin.isdigit():
            return jumin
        print("잘못된 형식입니다. 다시 입력하세요.")

def get_gender(jumin):
    gender_digit = int(jumin[6])
    return "남자" if gender_digit in [1, 3] else "여자"

def get_birth_year(jumin):
    gender_digit = int(jumin[6])
    year = int(jumin[:2])
    return 1900 + year if gender_digit in [1, 2] else 2000 + year

def print_jumin_validation():
    jumin = read_jumin()
    if check_jumin(jumin):
        gender = get_gender(jumin)
        birth_year = get_birth_year(jumin)
        month, day = jumin[2:4], jumin[4:6]
        print(f"유효한 주민등록번호입니다. ({birth_year}년 {month}월 {day}일, {gender})")
    else:
        print("유효하지 않은 주민등록번호입니다.")

if __name__ == "__main__":
    print_jumin_validation()

