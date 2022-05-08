#2019038027이동현
#거북이를 크기순으로 정렬하고 선을 긋는 프로그램

import turtle   #거북이 모듈 사용
import random   #랜덤 모듈 사용

swidth, sheight, = 1000, 1000  #스크린 너비, 높이 설정

turtle.screensize(swidth, sheight)  #배경의 너비와 폭 지정
turtle.setup(width=swidth + 30, height=sheight + 30) #그래픽 창 크기 지정

turtle.title("정렬하고 선 긋는 거북이") #타이틀 이름

t1 = turtle.Turtle()    #t1 거북이 객체 생성
t2 = turtle.Turtle()    #t2 거북이 객체 생성
t3 = turtle.Turtle()    #t3 거북이 객체 생성
t4 = turtle.Turtle()    #t4 거북이 객체 생성
t5 = turtle.Turtle()    #t5 거북이 객체 생성

tList = [t1, t2, t3, t4, t5]    #거북이 객체를 담는 리스트 생성
sList = [] #거북이 크기를 담는 리스트 생성

t1.penup()  # 첫 번째 거북이는 선을 그리지 않게 설정

for t in tList: #거북이를 초기화 시키는 루프
    t.shape('turtle')  #거북이 모양 설정
    t.penup()   #거북이가 선을 긋지 않게 설정
    t.hideturtle()  # 거북이 모습을 보이지 않게 설정
    s = random.randrange(1, 100) / 10 #거북이 크기를 정하는 변수 s를 랜덤으로 설정
    sList.append(s)  # 거북이 크기를 sList에 추가

    r = random.random() #r값 랜덤으로 설정
    g = random.random() #g값 랜덤으로 설정
    b = random.random() #b값 랜덤으로 설정

    t.color((r, g, b))  #거북이 색깔 설정
    t.pensize(1) #펜사이즈 설정

for i in range(0,5): #거북이크기를 정렬하는 루프
    for j in range(i+1,5):
        if sList[i] >= sList[j]: #sList[i]가 sList[j]보다 크거나 같으면
            sList[i], sList[j] = sList[j], sList[i] #sList[i]가 sList[j] 교환

for i in range(0,5): #거북이를 작은순서대로 크기를 부여하는 루프
    t = tList[i] #tlist[i]의 거북이를 t로 설정
    t.shapesize(sList[i]) #t거북이 크기 설정

X = 0 #거북이의 X좌표를 나타내는 X 초기화
Y = 0 #거북이의 Y좌표를 나타내는 Y 초기화

first = True #첫번째 거북이를 확인하는 변수 first
for t in tList: #거북이를 이동시키는 루프


    t.goto(X, Y) #이전 거북이의 좌표로 이동
    t.showturtle()  #거북이를 보이게 설정

    t.pendown() #선을 그리게 설정
    if first: #첫번째 거북이인 경우에만 실행
        t.penup() #선을 그리지 않는다
        first = False #첫번째 거북이인 경우가 끝나면 first를 False로 바꿔 if문을 실행하지 않도록 한다.

    angle = random.randrange(0, 360) #거북이가 바라보는 각도 지정
    dist = random.randrange(1, 400) #거북이가 움직이는 거리 지정
    t.left(angle)      #거북이 방향
    t.forward(dist)    #거북이 이동거리

    X = t.xcor()    #거북이의 현재 X좌표
    Y = t.ycor()    #거북이의 현재 Y좌표


turtle.done()




