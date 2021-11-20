# 딕셔너리
# : 사전형태의 자료형

stock_a = {"삼성전자" : 82000, "LG전자" : 150000}
# 키 1 = 삼성전자, 데이터 1 = 82000, 키 2 = LG전자, 데이터 2 = 15-
stock_b = {
    "삼성전자" : [81000, 81500, 82000, 81500, 82000],
    "LG전자" : (150000, 149000, 148000, 151000, 152000)       
}
# 리스트 or 튜플을 이용해서 다수의 데이터 값 입력 가능
stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 81000
    }
}

# 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기

stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자" : 82000,
    "Sk하이닉스" : 123000,
    "NAVER" : 370000,
    "카카오" : 133000

}
# items() : 키와 데이터 쌍
print(stock_d.items())

for item in stock_d.items():
    print(item)
    print(item[0]) # 키 만 출려
    print(item[1]) # 데이터만 출력

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)
