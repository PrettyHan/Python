# 1. 파일 쓰기
f = open("./myvenv/Ch09/data.txt", "w", encoding="utf8")
f.write("1. 스타트코딩과 함께 파이썬 공부")
f.close()

# 2. 파일 추가
f = open("./myvenv/Ch09/data.txt", "a", encoding="utf8")
f.write("\n2. 비전공자도 쉽게 배 울 수 있 어 용 ")
f.close()

# 3. 파일 읽기
f = open("./myvenv/Ch09/data.txt", "r", encoding="utf8")

# 3.1 파일 전체 읽기
# data = f.read()
# print(data)
# f.close()

# 3.2 파일 한 줄 읽기
while True:
    data = f.readline()
    print(data, end="")
    if data == "":
        break
f.close()