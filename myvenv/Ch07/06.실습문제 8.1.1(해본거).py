# 실습문제 8.1.1

# 직접 만들어 보자!

class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def sale(self):
        print(f"{self.name}을 착용했다!")

    def discard(self):
        print(f"{self.name}을 해제했다!")        

class WearableItem(Item):
    def equip(self):
        print(f"{self.name}을 착용했다!")
        print(f"무게가{self.weight}만큼 상승했다!")

    def discard(self):
        print(f"{self.name}을 해제했다!")    

class useableItem(Item):
     def equip(self):
        print(f"{self.name}을 사용했다!")

     def discard(self):
        print(f"{self.name}을 버렸다!")             

sword = WearableItem("검", 500, 3, "착용가능")
sword.equip()

Red_potion = useableItem("체력물약", 300, 1, "사용가능")
Red_potion.equip()
