#2019038027 이동현
#거북이로 구구단을 출력하는 프로그램
import turtle

i, k, tX, tY = [0] * 4 #i,k와 거북이 위치를 저장하는 변수 tX, tY 초기화
swidth, sheight = 800, 450 #스크린의 너비,높이를 지정하는 변수

turtle.title('거북 구구단')  #타이틀 이름
turtle.shape('turtle')  #거북이 모양 설정
turtle.setup(width = swidth + 50, height = sheight + 50) #그래픽 창 크기 지정
turtle.screensize(swidth, sheight)  #배경의 크기 지정
turtle.penup()  #선을 남기지 않게 설정
tX, tY= -500, 250 #x와 y의 좌표
turtle.goto(tX, tY) #거북이 초기위치 설정

for i in range(1, 10):
    for k in range(2, 10):
        turtle.goto(tX + 80 * k, tY - 40 * i) #거북이를 이동
        gugu = str(k) + 'x' + str(i) + '=' + str(k * i) #구구단 글자 만들기
        turtle.write(gugu, font=('Arial',12,'bold')) #글자의 형태를 결정하고 화면에 출력

turtle.done()
