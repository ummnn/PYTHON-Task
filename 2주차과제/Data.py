#2019038027 이동현
#데이터형의 크기를 확인하는 프로그램

import sys  #sys 모듈 사용

l = [] #list형 생성
t = () #tuple형 생성
d = {} #dictionary형 생성
s = set()   #set형 생성

print('int형 기본 크기 -> ' , sys.getsizeof(1))      #int형 크기 출력
print('float형 기본 크기 -> ', sys.getsizeof(34.5))  #float형 크기 출력
print('bool형 기본 크기 -> ', sys.getsizeof(True))   #bool형 크기 출력
print('str형 기본 크기 -> ', sys.getsizeof('o'))     #string형 크기 출력
print('list형 기본 크기 -> ', sys.getsizeof(l))      #list형 크기 출력
print('tuple형 기본 크기 -> ', sys.getsizeof(t))     #tuple형 크기 출력
print('dictionary형 기본 크기 -> ', sys.getsizeof(d))#dictionary형 크기 출력
print('set형 기본 크기 -> ', sys.getsizeof(s))       #set형 크기 출력