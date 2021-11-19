import random

def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_num = []   # 리스트 만들어주기
count = 0  # 현재 뽑은 숫자 개수

while True:
    if count == 6:
        break
    number = get_random_number()
    if number not in lotto_num:
        lotto_num.append(number)
        count += 1

lotto_num.sort()

for num in lotto_num:
    print(num, end= " ")
