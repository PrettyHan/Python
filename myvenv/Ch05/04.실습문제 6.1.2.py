# 실습문제 6.1.2

# 문자열 포매팅
def printSumAvg(x,y,z):
    """
    세개의 숫자를 받아 합계와 평균을 출력하는 함수
    """
    Sum = x + y + z
    Avg = Sum / 3
    print("합계 :", Sum)
    print("평균 :", Avg)
    print(f"합계 : {Sum} 평균 : {Avg}")
       
printSumAvg(10,20,30)