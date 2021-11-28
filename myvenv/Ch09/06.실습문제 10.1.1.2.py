import csv

def show_profit(data):
    name = data[0] # 종목
    pruchase_price = int(data[1]) # 매입가
    amount = int(data[2])
    target_price = int(data[3])

    profit = (target_price - pruchase_price) * amount # 수익금
    profit_ratio = (target_price / pruchase_price - 1) * 100 # 수익률
    print(f"{name} {profit} {profit_ratio:.2f}")


# 파일 열기
file = open("./myvenv/Ch09/mystock.csv", "r", encoding="utf8")


# 파일 데이터 읽기 # csv 는 자료형이 아니기 때문에 리스트형으로 만들어줌
reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)
    

file.close()
