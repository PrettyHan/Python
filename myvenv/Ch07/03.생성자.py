# 생성자
# : 인스턴스를 만들 때 호출되는 메서드

class Monster:
    def __init__(self, health, attack, speed): # __init__ 가장먼저 실행
        self.health = health # (goblin or wolf .health 로 저장 )
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)
goblin.decrease_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1500, 200, 350)
wolf.decrease_health(1000)
print(wolf.get_health())
