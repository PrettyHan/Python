# 실습문제 5.2.2

data = [] # 빈 리스트 생성

for i in range(1, 20):
    x = int(input("일차 턱걸이 횟수"))
    data.append(x)

# 코드가 너무 김 -> 반복문으로

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
avg = total / 7
print(int(avg))
# 나눗셈 연산으로 인해 float 표기
# int 형으로 바꿔줌