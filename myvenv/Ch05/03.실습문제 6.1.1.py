# 실습문제 6.1.1
# 함수호출방법

# docstring : 설명문

def multiply(x, y):
    """
    두수의 곱셈 결과를 반환하는 함수 (docstring)
    """
    result = x + y
    return result

print(multiply(3, 4))    

def printSumAvg(x,y,z):
    Sum = (x + y + z)
    Avg = (x * y * z)
    print("x+y+z""" "합계")
    print("x*y*z""" "평균")
       
print(printSumAvg(10,20,30))
