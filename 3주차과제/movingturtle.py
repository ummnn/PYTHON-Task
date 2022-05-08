#2019038027 이동현
#거북이 세마리를 서로 만나게 하는 프로그램
import turtle   #turtle모듈 사용
import random   #random모듈

#전역 변수 선언 부분
swidth, sheight = 100, 100  #스크린 너비, 높이 설정
angle, dist, t1X, t1Y, t2X, t2Y, t3X, t3Y = [0]*8 #각도, 거리, x좌표, y좌표 설정
s = 1 #거북이 크기 지정

#메인함수
turtle.title('거북이 만나기')   #타이틀 이름
turtle.setup(width=swidth + 30, height=sheight + 30) #그래픽 창 크기 지정
turtle.screensize(swidth, sheight)  #배경의 너비와 폭 지정

t1 = turtle.Turtle()    #t1 거북이 객체 생성
t2 = turtle.Turtle()    #t2 거북이 객체 생성
t3 = turtle.Turtle()    #t3 거북이 객체 생성

t1.shape('turtle')
t1.color('red')
t1.shapesize(s)  # 거북이 크기

t2.shape('turtle')
t2.color('blue')
t2.shapesize(s)  # 거북이의 크기

t3.shape('turtle')
t3.color('yellow')
t3.shapesize(s)  # 거북이의 크기

t1.penup()
t2.penup()
t3.penup()

t1.goto(random.randrange(-swidth / 2, swidth / 2), random.randrange(-sheight / 2, sheight) / 2)
t2.goto(random.randrange(-swidth / 2, swidth / 2), random.randrange(-sheight / 2, sheight) / 2)
t3.goto(random.randrange(-swidth / 2, swidth / 2), random.randrange(-sheight / 2, sheight) / 2)

while True:

    angle = random.randrange(0, 360) #각도의 범위 지정
    dist = random.randrange(1, 100) #거리의 범위


    t1.left(angle)      #거북이 방향
    t1.forward(dist)    #거북이 이동거리
    t1X = t1.xcor()  # 거북이의 현재 x좌표
    t1Y = t1.ycor()  # 거북이의 현재 y좌표

    if (-swidth / 2 <= t1X and t1X <= swidth / 2) and (-sheight / 2 <= t1Y and t1Y <= sheight / 2):
        pass #거북이가 배경 내에 있다면 계속 실행
    else:
        t1.goto(0,0)
        t1X = t1.xcor()  # 거북이의 현재 x좌표
        t1Y = t1.ycor()  # 거북이의 현재 y좌표

    angle = random.randrange(0, 360)  # 각도의 범위 지정
    dist = random.randrange(1, 100)  # 거리의 범위 지정


    t2.left(angle)  # 거북이 방향
    t2.forward(dist)  # 거북이 이동거리
    t2X = t2.xcor()  # 거북이의 현재 x좌표
    t2Y = t2.ycor()  # 거북이의 현재 y좌표

    if (-swidth / 2 <= t2X and t2X <= swidth / 2) and (-sheight / 2 <= t2Y and t2Y <= sheight / 2):
        pass #거북이가 배경 내에 있다면 계속 실행
    else:
        t2.goto(0,0)
        t2X = t2.xcor()  # 거북이의 현재 x좌표
        t2Y = t2.ycor()  # 거북이의 현재 y좌표

    angle = random.randrange(0, 360)  # 각도의 범위 지정
    dist = random.randrange(1, 100)  # 거리의 범위 지정


    t3.left(angle)  # 거북이 방향
    t3.forward(dist)  # 거북이 이동거리
    t3X = t3.xcor()  # 거북이의 현재 x좌표
    t3Y = t3.ycor()  # 거북이의 현재 y좌표

    if (-swidth / 2 <= t3X and t3X <= swidth / 2) and (-sheight / 2 <= t3Y and t3Y <= sheight / 2):
        pass #거북이가 배경 내에 있다면 계속 실행
    else:
        t3.goto(0,0)
        t3X = t3.xcor()  # 거북이의 현재 x좌표
        t3Y = t3.ycor()  # 거북이의 현재 y좌표

    if (t1X == t2X and t1Y == t2Y) or (t1X == t3X and t1Y == t3Y) or (t2X == t3X and t2Y == t3Y):
        t1.shapesize(s * 3)
        t2.shapesize(s * 3)
        t3.shapesize(s * 3)
        break

turtle.done()
