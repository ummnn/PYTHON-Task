#2019038027 이동현
#날짜 세기 및 요일을 구하는 함수

from time import* # time모듈을 불러옴
from datetime import* # datetime모듈을 불러옴

#날짜의 수를 세는 함수
def countDays(date1,date2):
    retDays = 0 #반환할 날짜수
    year, month, day = date1.split('/') #년.월,일을 /기준으로 나눈다
    sDay = date(int(year),int(month),int(day)) #시작날짜

    year, month, day = date2.split('/') #년.월,일을 /기준으로 나눈다
    eDay = date(int(year),int(month),int(day)) #현재날짜

    diffDays = eDay - sDay #날짜간의 차이 계산
    retDays = diffDays.days #날짜만 추출
    return retDays #날짜간의 차이 반환

#요일을 구하는 함수
def getDay(t):
    weeks = ['월','화','수','목','금','토','일']
    return weeks[t.tm_wday] #요일 반환

startDate,curDate,tm='','',None

startDate = input('시작 날짜(연/월/일) --> ') #시작날짜를 입력받는다
tm = localtime() #localtime()을 이용하여 현재 날짜를 구한다
curDate = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday) #현재날짜를 구하여 문자열로 저장
print(startDate,'부터 오늘(',curDate,')까지는', countDays(startDate,curDate),'일이 지났습니다') #countDays함수로 날짜간의 차이를 구해 출력
print('그리고 오늘은', getDay(tm),'요일입니다') #getDay함수로 요일값 구한후 출력
