#2019038027 이동현
#나선형을 그리며 문자열을 출력하는 프로그램

import turtle, random, math #turtle, random, math 모듈을 불러온다
import tkinter #tkinter 모듈을 불러온다

Str = '' #문자열 초기화
swidth, sheight = 500,500 #가로 세로 초기화
tX, tY = 0,0 #XY좌표 초기화

turtle.title('나선 거북이') #타이틀명
turtle.shape('turtle')  #모양설정
turtle.setup(width = swidth+50, height = sheight +50) #배경사이즈
turtle.screensize(swidth, sheight) #스크린사이즈
turtle.penup() #선을그리지 않게 설정

Str = tkinter.simpledialog.askstring('문자열 입력', '거북이가 쓸 문자열을 입력') #inStr에 문자열을 입력받는다

r = 2 #돌릴 바퀴수
l = len(Str) #inStr의 문자 개수
angleinc = 360*r/l #각도증가값 설정
angle = 0 #각도값 초기화
disdec = 200/l #거리감소값 설정
dis = 200 #거리값 초기화

for ch in Str:

    rad = (3.14 * angle / 180) #라디안값 설정
    tX = dis * math.cos(rad) #X좌표 설정
    tY = dis * math.sin(rad) #Y좌표 설정
    r = random.random() #r값 랜덤으로 설정
    g = random.random() #g값 랜덤으로 설정
    b = random.random() #b값 랜덤으로 설정
    txtSize = 20 #텍스트 사이즈 지정

    turtle.goto(tX,tY) #거북이 이됭시키기

    turtle.pencolor(r,g,b) #색깔 랜덤으로 설정

    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold')) #거북이가 쓸 글씨체, 사이즈 지정
    angle += angleinc #각도값 angleinc만큼 증가
    dis -= disdec #거리값 disdec만큼 감소

turtle.done()

