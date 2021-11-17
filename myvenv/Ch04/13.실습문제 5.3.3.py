# 실습문제 5.3.3
# Learning Korean

korean_list = ["사랑해", "귀엽다", "고마워", "행복해"]

print("Let's learning Korean")

for korean in korean_list:
    print(korean)
    data = input()
    if data != korean:
        print("다시 입력해 주세요")
        break


# 전체 문제 개수 : 4 개
# 맞힌 문제 개수 : 2 개
# 틀린 문제 개수 : 2 개
    