# 실습문제 6.1.3
# 로또 번호 추출기

import random

def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_num = []   # 리스트 만들어주기
count = 0  # 현재 뽑은 숫자 개수

while True:
    if count == 6: # 카운트 6 되면 
        break # 반복 중지
    number = get_random_number() # number 값 넣어줌
    if number not in lotto_num: # 중복이 아닐 때
        lotto_num.append(number) # 중복이 아닌수를 반복해서 넣어줌
        count += 1 # 카운트 +1 = > 6될 때까지 

lotto_num.sort() # 정렬 싹 해주고

for num in lotto_num: # 이쁘게 출력
    print(num, end= " ")
