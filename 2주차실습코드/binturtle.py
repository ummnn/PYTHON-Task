#2019038027 이동현
#거북이로 2진수 숫자를 표현하는 프로그램

import turtle

#메인함수
turtle.title('이진수 거북이') #타이틀 이름
t = turtle.Turtle()  #거북이 생성
t.shape("turtle")    #모양 지정

print('숫자를 입력하세요')

num = int(input())      #숫자를 입력받는다
bina = ()               #2진수를 담을 배열 설정
bina = str(bin(num))    #2진수로 변환해 저장한다
bina = bina.replace("0b", "") #문자열에서 0b 지우기

t.penup()   #펜흔적을 남기지 않는다
t.speed(0)  #거북이 속도 설정

for i in bina :

    if( i =="1"):   #1일경우
        t.forward(80)   #거북이 이동
        t.left(90)      #거북이가 북쪽을 바라보게 한다
        t.color("red")  #색깔을 빨간색으로 설정
        t.shapesize(2)  #거북이의 크기는 2
        t.stamp()       #거북이를 찍는다
        t.setheading(0) #거북이가 동쪽을 바라보게 한다
    else:
        t.forward(80)   #거북이 이동
        t.left(90)      #거북이가 북쪽을 바라보게 한다
        t.color("blue") #색깔을 파란색으로 설정
        t.shapesize(1)  #거북이의 크기는 1
        t.stamp()       #거북이를 찍는다
        t.setheading(0) #거북이가 동쪽을 바라보게 한다

t.hideturtle()  #거북이를 숨긴다
turtle.done()   #거북이 종료

