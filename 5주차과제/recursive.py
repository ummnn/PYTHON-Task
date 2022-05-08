#2019038027 이동현
#재귀함수를 이용하여 2/8/16진수로 변환하는 프로그램

#2진수를 구하는 함수
def base2(binbin):
    div = 0 #몫 초기화
    mod = 0 #나머지 초기화
    div = binbin // 2 #몫을 구하고 소수점은 버린다
    mod = binbin % 2 #나머지를 구한다
    binlist.append(mod) #binlist에 mod값을 추가
    if binbin < 2: return  #몫이 2보다 작아지면 종료
    base2(div) #base2함수를 div값을 매개변수로 다시 호출

def base8(octoct):
    div = 0 #몫 초기화
    mod = 0 #나머지 초기화
    div = octoct // 8 #몫을 구하고 소수점은 버린다
    mod = octoct % 8 #나머지를 구한다
    octlist.append(mod) #octlist에 mod값을 추가
    if octoct < 8: return #몫이 8보다 작아지면 종료
    base8(div) #base8함수를 div값을 매개변수로 다시 호출

def base16(hexhex):
    div = 0 #몫 초기화
    mod = 0 #나머지 초기화
    div = hexhex // 16 #몫을 구하고 소수점은 버린다
    mod = hex(hexhex % 16) #나머지를 구하고 16진수로 변환
    hexlist.append(str(mod).replace("0x","")) #hexlist에 0x를 제거한 mod값을 추가
    if hexhex < 16: return #몫이 16보다 작아지면 종료
    base16(div) #base16함수를 div값을 매개변수로 다시 호출

binlist = [] #2진수를 담는 리스트
octlist = [] #8진수를 담는 리스트
hexlist = [] #16진수를 담는 리스트

decimal = int(input('10진수 입력:'))

base2(decimal) #2진수를 구하는 함수 실행
base8(decimal) #8진수를 구하는 함수 실행
base16(decimal) #16진수를 구하는 함수 실행

binlist.reverse() #binlist의 순서를 거꾸로 바꾼다
octlist.reverse() #octlist의 순서를 거꾸로 바꾼다
hexlist.reverse() #hexlist의 순서를 거꾸로 바꾼다

print("2진수: ",end='') #2진수 출력
for i in range(0,len(binlist)):
    print(binlist[i],end='')

print("\n8진수: ",end='') #8진수 출력
for i in range(0,len(octlist)):
    print(octlist[i],end='')

print("\n16진수: ",end='') #16진수 출력
for i in range(0,len(hexlist)):
    print(hexlist[i],end='')









