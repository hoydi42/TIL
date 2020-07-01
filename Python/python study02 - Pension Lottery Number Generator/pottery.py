import random
import time
import sys

jojo = random.randint(1,6)

while(True):
    print("="*30)
    print("☆ ★ ☆ 연금복권 번호 생성기 ★ ☆ ★")
    print("연금복권 번호를 몇 개 생성하시겠습니까? 1 이상의 수를 입력해주세요.")
    print("※ 0을 입력하면 종료 ")

    Pention = int(input(">>> : "))
    if Pention <= 0:
        break
    while Pention >0:
        print("행운의 번호를 뽑는 중입니다...")
        for i in range(3):
            time.sleep(0.2)
            print(".")
        print("뽑기가 완료되었습니다 !")
        print("="*30)
        time.sleep(0.5)
        for i in range(1,Pention+1):
            print("[%-2d]" %i, end=" ") #end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨. 공백 한칸을 넣어 
            for j in range(6):
                print("{0:3d}".format(random.randint(0,9)), end=" ") #0:3d 
            print()
        print("="*30)
        print()
        print()
        time.sleep(0.5)
        print("조를 뽑을까요? 0 : 뽑지 않기,  1 : 조 뽑기")
        jochoice = int(input(">>> : "))
        if jochoice == 0:
            print("한번 더 할까요? 0 : 종료하기,  1 : 한번 더 하기")
            bye1 = int(input(">>> : "))
            if bye1 == 0:
                print("="*30)
                print("종료합니다. 꼭 당첨되길!")
                sys.exit()
            if bye1 == 1:
                break
        if jochoice == 1:
            print("조를 몇개 생성할까요? 0 : 종료하기,  1 : 한번만,  2 : 복권 번호 생성한만큼!")
            oneormany = int(input(">>> : "))
            if oneormany == 0:
                print("="*30)
                print("종료합니다. 꼭 당첨되길!")
                sys.exit()

            if oneormany == 1:
                print("행운의 번호를 뽑는 중입니다...")
                time.sleep(0.2)
                print(".")
                time.sleep(0.2)
                print(".")
                time.sleep(0.2)
                print(".")
                print("뽑기가 완료되었습니다 !")
                time.sleep(0.5)                
                print("행운의 조는... {} 조 !" .format(random.randint(1,5)))
                print()
                print("한번 더 할까요? 0 : 종료하기,  1 : 한번 더 하기")
                final = int(input(">>> : "))
                if final == 0:
                    print("="*30)
                    print("종료합니다. 꼭 당첨되길!")
                    sys.exit()
                if final == 1:
                    break
            if oneormany == 2:
                print("행운의 번호를 뽑는 중입니다...")
                for i in range(3):
                    time.sleep(0.2)
                    print(".")
                print("뽑기가 완료되었습니다 !")
                time.sleep(0.5)
                print("행운의 조는...")
                print()
                time.sleep(0.5)
                for i in range(1,Pention+1):
                    time.sleep(0.2)
                    print("{0:<2d}조".format(random.randint(1,5)))
                print()
                print("입니다!")
                print()
                print("한번 더 할까요? 0 : 종료하기,  1 : 한번 더 하기")
                final = int(input(">>> : "))
                if final == 0:
                    print("="*30)
                    print("종료합니다. 꼭 당첨되길!")
                    sys.exit()
                if final == 1:
                    break



        break
print("="*30)
print("종료합니다. 꼭 당첨되길!")

#뿝!
