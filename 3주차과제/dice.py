#2019038027 이동현
#주사위 여러 개를 동시에 던지는 프로그램
import random #random모듈 사용

loopCount = 0 #주사위를 던진 횟수
contCount = 0 #1~6까지 연속된 적이 몇번인지 카운트

while True:

    dice = []  #주사위 숫자를 담는 리스트
    loopCount += 1 #주사위를 던진 횟수 +1

    for i in range(1, 7):  #6번 반복
        dice.append(random.randrange(1, 7)) #리스트에 1~6까지의 랜덤한 숫자를 넣는다

    sameFirst = 0   #동일한 숫자가 나왔는지 확인하기 위해 사용하는 변수
    contFirst = 0   #연속된 숫자가 나오는지 확인하기 위해 저장하는 변수
    contNum = 0     #숫자가 몇번 연속되었는지 세는 변수 초기화

    for i in dice: #dice에서 숫자를 하나씩 꺼내 i에 넣는다
        if sameFirst == 0:   #가장 처음 sameFirst에 i값을 넣기위해 사용
            sameFirst = i    #dice안의 첫번째 값을 sameFirst에 넣는다
            sameCount = 1    #sameCount 초기화
        else:
            if sameFirst == i: #첫번째 나온 숫자가 i값과 같다면
                sameCount += 1 #같은 숫자가 몇번 나왔는지 세는 sameCount에 1을 더한다

        contFirst += 1  #연속된 숫자인지 확인하기 위해 사용하는 변수 contFirst에 1씩 더한다
        if contFirst == i:  #i값과 같다면
            contNum += 1    #몇번 연속되었는지 세는 contNum에 1추가

    if contNum == 6:    #6번 연속되었다면
        contCount += 1  #contCount에 1추가

    if sameCount == 6: #같은값이 6번 나왔다면
        break   #while문 탈출


print("6개 주사위가 모두 동일한 숫자가 나옴 -->", dice)
print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->", loopCount)
print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 -->", contCount)