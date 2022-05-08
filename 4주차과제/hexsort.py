#2019038207이동현
#16진수를 정렬하는 프로그램

import random #랜덤함수를 사용하기 위해 모듈 사용

S = 5 #리스트의 사이즈를 정한다

hexalist = [S] #16진수를 담는 리스트

for i in range(0,S): #hexalist에 S만큼 랜덤한 16진수를 넣는다
    hexalist.append(hex(random.randrange(0,500)))

print("정렬 전의 hexalist: ",hexalist) #정렬 전의 hexalist를 출력

for i in range(0,S): #버블정렬을 사용(인접한 두수를 비교하며 정렬하는 방법)
    for j in range(i + 1, S): 
        if int(str(hexalist[j]),base=16) <= int(str(hexalist[i]),base=16): #hexalist[j]의 값이 hexalist[j]의 값보다 작다면
            hexalist[i], hexalist[j] =  hexalist[j], hexalist[i] #hexalist[j]와 hexalist[i]의 값과 바꾼다


print("정렬 후의 hexalist: ", hexalist) #정렬 후의 hexalist를 출력

