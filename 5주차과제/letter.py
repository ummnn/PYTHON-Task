#2019038027 이동현
#대문자 소문자 변환 프로그램

before = input("문자열을 입력하세요")
after = []

print("변환 전의 문자열: ", before) #변환전 문자열 출력
l = len(before) #문자열의 길이 저장

for i in range(0,l):
    u = before[i].isupper() #문자가 대문자인지 판별

    if u == True: #대문자라면 after에 소문자로 변환해 추가
        after.append(before[i].lower())

    elif u == False: #소문자라면 after에 대문자로 변환해 추가
        after.append(before[i].upper())

print("변환 후의 문자열: ",end='') #변환후 문자열 출력
for a in after:
    print(a,end='')
