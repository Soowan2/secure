import random

def get_random_num():
    return random.randint(1,600)

num = 0
key = [] #key 값
string = [] #원본 문자열
strtonum = [] #원본 문자열을 정수 변환
cipher = []#암호문
decode = []

print("암호문 만들기를 시작합니다!")
plain = input("암호문으로 만들 문장을 입력해주세요 : ")
#입력한 문장을 string 배열에 나누어 저장
for char in plain:
    string.append(char)

#string 배열에 저장된 문자를 정수화
num = 0
for char in plain:
    strtonum.append(ord(string[num]))
    num += 1

for char in plain:
            key.append(get_random_num())

while True:
    

    print("암호화 : 1, 복호화 : 2, 암호문출력 : 3, 복호화된 문장 출력 : 4 문장 재설정 : 5 프로그램 종료 : 6")
    button = int(input("숫자를 입력하세요 : "))

    if button == 1:
        cipher = []     
        num = 0
        for char in plain:
            cipher.append(key[num]^strtonum[num])
            num += 1

    elif button == 2:
        if not cipher:
            print("암호화를 진행하세요.")
        else:
            decode = []
            num = 0
            for char in plain:
                decode.append(key[num]^cipher[num])
                num += 1

    elif button == 3:
        if not cipher:
            print("암호화를 진행하세요.")
        else:
            num = 0
            for char in plain:
                print(chr(cipher[num]),end="")
                num += 1
            print("")

    elif button == 4:
        if not decode:
            print("복호화를 진행하세요.")
        else:
            num = 0
            for char in plain:
                print(chr(decode[num]),end="")
                num += 1
            print("")

    elif button == 5:
        #초기화
        key = []
        string = []
        strtonum = []
        cipher = [] 
        decode = []
        #암호화 하고싶은 문장 입력
        plain = input("암호문으로 만들 문장을 입력해주세요 : ")

        for char in plain:
            key.append(get_random_num())
        
        #입력한 문장을 string 배열에 나누어 저장
        for char in plain:
            string.append(char)

        #string 배열에 저장된 문자를 정수화
        num = 0
        for char in plain:
            strtonum.append(ord(string[num]))
            num += 1

    elif button == 6:
        break

