import turtle as t # turtle 모듈을 불러오고 turtle은 t로 한다.

import random as r # random 모듈을 불러오고 random은 r로 한다.

t.shape("turtle") # t의 모양은 거북이로 한다.

t.speed(2) # 거북이의 속도를 10(빠른속도)로 한다.

t.bgcolor("black") # 배경색을 검은색으로 한다.

t.color("gold") # 펜색을 금색으로 한다.

n=100

for x in range(n): # x값을 n번 실행한다.

    a = r.randint(1, 360) # 1 ~ 360에서 아무 수나 골라 a에 저장한다.

    t.setheading(a) # 거북이 방향을 a각도 만큼 회전 시킨다.

    t.forward(10) # 앞으로 10만큼 전진한다.

    b = r.randint(1,20) # 1~20에서 아무 수나 골라 b에 저장한다.

    if b >= 10: # b가 10 이상인지 비교한다.

        t.circle(b) # true이면 반지름 b인 원을 그린다.

    else: # 그렇지 않으면

        for b in range(4): # b값을 4번 실행한다.

            t.forward(50) # 앞으로 50 전진한다.

            t.left(90) # 왼쪽으로 90각도 만큼 회전한다.
    
