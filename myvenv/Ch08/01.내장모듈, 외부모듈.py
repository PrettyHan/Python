# 내장 모듈
# : 파이썬 설치 시 자동으로 설치되는 모듈

import math
print(math.pi)
print(math.ceil(2.7))

from math import pi, ceil as c
print(pi)
print(c(2.7))

# 외부 모듈
# : 다른 사람이 만든 파이썬 파일 pip로 설치
# pyautogui (매크로)
import pyautogui as pg

pg.moveTo(500, 500, duration=2)



