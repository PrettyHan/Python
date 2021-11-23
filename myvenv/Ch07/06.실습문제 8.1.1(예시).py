# 클래스 생성
class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] 버렸습니다")
        else:
            print(f"[{self.name}] 버릴 수 없습니다")    

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect): # 오버라이딩 됬기때문에 super.로 다시 가져와야댐
        super().__init__(name, price, weight, isdropable) # 부모클래스의 생성자를 갖고 옴.
        self.effect = effect
    def wear(self):
        print(f"[{self.name}] 착용했습니다. {self.effect}")

class UseableItem(Item):
     def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable) # 부모클래스의 생성자를 갖고 옴.
        self.effect = effect
     def use(self):
         print(f"[{self.name}] 사용했습니다. {self.effect}")

# 인스턴스 생성

sword = WearableItem("이가닌자의 검", 30000, 3.5, True, "체력 5000 증가, 마력 5000 증가")
sword.wear()
sword.sale()
sword.discard()

potion = UseableItem("신비한투명물약", 15000, 0.1, False, "투명화 300초 지속")
potion.discard()
potion.sale()
potion.use()




