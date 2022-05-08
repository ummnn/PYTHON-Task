#2019038027 이동현
#거북이 세마리를 서로 만나게 하는 프로그램
import turtle   #turtle모듈 사용
import random   #random모듈
import math     #math 모듈

swidth, sheight = 500, 500  #스크린 너비, 높이 설정

t1 = turtle.Turtle()    #t1 거북이 객체 생성
t2 = turtle.Turtle()    #t2 거북이 객체 생성
t3 = turtle.Turtle()    #t3 거북이 객체 생성
tList = [t1, t2, t3]    #거북이 객체를 담는 리스트 생성

turtle.title('거북이 만나기') #타이틀 이름
turtle.setup(width=swidth + 30, height=sheight + 30) #그래픽 창 크기 지정
turtle.screensize(swidth, sheight)  #배경의 너비와 폭 지정
sswidth = int(swidth / 2) #스크린 너비의 절반
ssheight = int(sheight / 2) #스크린 높이의 절반
s = 2 #거북이 크기 지정

def distance(t1, t2) : #거북이들 사이의 거리를 구하는 함수
    t1x = t1.xcor() #t1의 x좌표
    t1y = t1.ycor() #t1의 y좌표
    t2x = t2.xcor() #t2의 x좌표
    t2y = t2.ycor() #t1의 y좌표

    return math.sqrt(((t1x - t1x) * (t1x - t2x)) + ((t1y - t2y) * (t1y - t2y)))

for t in tList: #거북이를 초기화 시키는 루프
    t.shape('turtle')  #거북이 모양 설정
    r = random.random() #r값
    g = random.random() #g값
    b = random.random() #b값

    t.color((r, g, b))  #거북이 색깔 설정
    t.shapesize(s)      #거북이 크기 설정
    t.penup()           #선을 그리지 않게 설정
    t.goto(random.randrange(-sswidth,sswidth ), random.randrange(-ssheight, ssheight)) #거북이 초기위치를 랜덤으로 설정

while True: #거북이가 만날떄까지 무한 반복
    for t in tList: #거북이를 이동시키는 루프
        angle = random.randrange(0, 360) #각도의 범위 지정
        dist = random.randrange(1, min(sswidth,ssheight)) #거리의 범위
        t.speed(399)
        t.left(angle)      #거북이 방향
        t.forward(dist)    #거북이 이동거리
        X = t.xcor()    #거북이으 현재 X좌표
        Y = t.ycor()    #거북이의 현재 Y좌표
        if (-sswidth <= X and X <= sswidth) and (-ssheight <= Y and Y <= ssheight):
            pass #거북이가 배경 내에 있다면 계속 실행
        else:
            t.goto(random.randrange(-sswidth, sswidth),random.randrange(-ssheight, ssheight)) #거북이가 배경 밖으로 나갈 경우 중앙으로 이동

    if distance(tList[0], tList[1]) < s : break #거북이1과 거북이2 사이의 거리가 거북이 크기보다 작다면 break
    if distance(tList[0], tList[2]) < s : break #거북이1과 거북이3 사이의 거리가 거북이 크기보다 작다면 break
    if distance(tList[1], tList[2]) < s : break #거북이2와 거북이3 사이의 거리가 거북이 크기보다 작다면 break

for t in tList:
    t.shapesize(s * 3)  #거북이의 크기를 세배로 변경

turtle.done()
