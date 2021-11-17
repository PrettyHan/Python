# 실습문제 5.3.1
# 구구단 출력하기

x = int(input("몇 단을 출력할까요? >>>"))

for i in range(1, 10):
    print(x, "*", i, "=", x*i)

#i = 1
#while 1 <= i < 10:
#    i += 1
#    i = int(input("몇 단을 출력할까요? >>>"))
#    print(i * 5)
# or
#numbers = [1,2,3,4,5,6,7,8,9]
#for number in numbers:
#    print(number*5)
