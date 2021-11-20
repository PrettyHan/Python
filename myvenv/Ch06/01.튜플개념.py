# 튜플
# : 읽기 전용 리스트
a = ()   # 소괄호로 만듬
b = 3, 4, 5 # 생략도 가능

c = (3)   # 틀림 / (3,) 는 가능
d = 3,

e = tuple([3, 4, 5])
f = list(range(10))
g = tuple(f)

h = 3, 4, 5
i = list(h)

# 튜플 관련 함수
x = 5, 6, 7, 8
print(max(x))
print(min(x))
print(sum(x))
print(x.count(6)) # 6의 개수
print(x.index(7)) # 7번째 리스트 값


# () = 함수를 정의, 호출
# [] = 리스트 정의, index 
# {} = f string, 딕셔너리

