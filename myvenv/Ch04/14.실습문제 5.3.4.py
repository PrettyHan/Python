# 실습문제 5.3.4
# Learning Korean

# 한국어 리스트
korean_list = ["사랑해", "귀엽다", "고마워", "행복해"]

# 점수
score = 0

print("Let's learning Korean")

for korean in korean_list:
    print(korean)
    data = input()
    if data == korean: # 문제를 맞힌 경우
        score += 1

print("전체 문제 개수 : ", len(korean_list))        
print("맞힌 개수 : ", score)
print("틀린 개수 : ", len(korean_list) - score)

# 전체 문제 개수 : 4 개
# 맞힌 문제 개수 : 2 개
# 틀린 문제 개수 : 2 개
    