#2019038027 이동현
#움직이는 거북이가 도장을 찍는 프로그램
import turtle   #turtle모듈 사용
import random   #random모듈 사용

#전역 변수 선언 부분
swidth, sheight, pSize, exitCount = 300, 300, 3, 0  #스크린 너비, 높이, 펜사이즈, 카운트 선언
r, g, b, angle, dist, curX, curY = [0] * 7          #색,각도,거리,좌표 선언

#메인함수
turtle.title('움직이는 거북이')    #타이틀 이름
turtle.shape('turtle')          #모양 설정
turtle.pensize(pSize)           #펜사이즈 설정
turtle.setup(width=swidth + 30, height=sheight + 30) #그래픽 창 크기 지정
turtle.screensize(swidth, sheight)  #배경의 너비와 폭 지정

while True:
    r = random.random()         #r값
    g = random.random()         #g값
    b = random.random()         #b값
    s = random.random()         #거북이 사이즈
    turtle.pencolor((r, g, b))  #펜컬러 지정
    turtle.color((r, g, b))     #거북이 컬러 지정

    angle = random.randrange(0, 360) #각도의 범위 지정
    dist = random.randrange(1, 100) #거리의 범위 지정
    turtle.left(angle)      #거북이 방향
    turtle.forward(dist)    #거북이 이동거리
    curX = turtle.xcor()    #거북이의 현재 x좌표
    curY = turtle.ycor()    #거북이의 현재 y좌표
    turtle.shapesize(s)     #거북이의 크기
    turtle.stamp()          #거북이 찍기

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass #거북이가 배경 내에 있다면 계속 실행

    else:
        turtle.penup()  #선을 남기지 않는다
        turtle.goto(0, 0)   #중앙으로 옮긴다
        turtle.pendown()    #다시 선을 남긴다

        exitCount += 1      #exit카운트를 하나 올린다

        if exitCount >= 5:
            break   #거북이가 5번 나가면 종료

turtle.done()
