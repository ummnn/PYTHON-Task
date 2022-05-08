#2019038027이동현
#하트를 출력하는 프로그램

numStr = [] #리스트 numStr리스트 생성
numStr = input("숫자를 여러개 입력하세요: ") #숫자를 입력받는다

i = 0
ch = numStr[i] #ch를 numStr의 첫번째 값으로 초기화
while True:
    heartNum = int(ch)

    heartStr="" #heartStr 초기화
    for k in range(0,heartNum): #heartNum
        heartStr += "\u2665" #heartStr에 하트모양 입력
        k += 1  #k값 1증가

    print(heartStr) #하트모양 출력

    i+=1 #i값 1 증가
    if(i > len(numStr) -1):
        break #i가 numStr의 길이보다 길어지면 탈풀

    ch = numStr[i] #ch에 numStr[i]값 입력
