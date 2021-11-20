class monster:
    def say(self):
        print("나는 몬스터다!")

goblin = monster()
goblin.say()


# 파이썬에서는 자료형도 클래스다.
a = 10 # int 형 클래스
b = "문자열객체" # str 형 클래스
c = True # bool 형 클래스

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__())
