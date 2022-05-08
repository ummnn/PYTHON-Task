#2019038027 이동현
#수송량에 따라 순위를 매기는 프로그램

traintuple = (('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), ('토마스', 4), ('헨리', 7), ('토마스', 3), ('에밀리', 8), ('퍼시', 5),('고든', 13))
#기차수송량 목록을 담은 tuple
print("기차의 수송량 목록: ", traintuple) #정렬전 기차의 수송량 목록을 출력

traindict = dict(traintuple) #traintuple을 dictionary로 변환

for k in traindict.keys():
    traindict[k] = 0  #key값으로 k를 가진 traindict의 value를 초기화

    for t in traintuple: #traintuple에서 tuple를 하나씩 뽑는다.
        if t[0] == k:  #키값과 tuole(t)의 첫번째 값이 동일한지 비교
            traindict[k] += t[1] #동일하다면 튜플의 두번쨰값을 키값으로 k를 가진 traindict의 value에 더한다.

print("기차의 총 수송량 목록: ",traindict) #정렬전의 수송량 목록을 출력

trainlist=list(traindict.items()) #traindict를 튜플로 변환

for i in range(len(trainlist)): #버블정렬을 사용(인접한 두수를 비교하며 정렬하는 방법)
    for j in range(i + 1, len(trainlist)):
        if trainlist[i][1] <= trainlist[j][1]: #hexalist[j]의 값이 hexalist[j]의 값보다 작다면
           trainlist[i],trainlist[j] = trainlist[j],trainlist[i] #hexalist[j]와 hexalist[i]의 값과 바꾼다

print("--------------------")
print("순위   이름  총 수송량")
print("--------------------")
for i in range(len(trainlist)):
    if i == 0:  #첫번째 값일 때
        rank = 1 #순위를 보여주는 rank를 1로 초기화
        same = 1 #연속하여 같은 수송량이 나왔을때 카운트하는 same을 1로 초기화
        print(rank, "\t", trainlist[i][0], "\t", trainlist[i][1]) #등수,이름,총수송량 출력

    elif trainlist[i-1][1] == trainlist[i][1]:  #trainlist의 다음 사람과 수송량이 같을 경우
        print(rank, "\t", trainlist[i][0], "\t", trainlist[i][1]) #등수,이름,총수송량 출력
        same+=1 #연속하여 같은 수송량이 나왔을 때 카운트하는 same 1 증가

    else: #trainlist의 다음사람과 수송량이 같지 않을 경우
        if same==1: #전사람이 연속한 수송량이 나오지 않았을 경우
            rank += 1 #순위를 보여주는 rank 1 증가
            print(rank, "\t", trainlist[i][0], "\t", trainlist[i][1]) #등수,이름,총수송량 출력

        else: #전 사람이 연속한 수송량이 나왔을 경우
            rank += same #rank에 same을 더한다
            print(rank, "\t", trainlist[i][0], "\t", trainlist[i][1]) #등수,이름,총수송량 출력
            same=1 #same을 다시 1로 초기화한다
