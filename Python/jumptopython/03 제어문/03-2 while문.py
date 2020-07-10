#03-2 while문



#while문의 기본 구조

반복해서 문장을 수행해야 할 경우 while문을 사용. 반복문이라고도 함.
while 문은 조건문이 참인 동안에 while 문 아래의 문장이 반복해서 수행

-----------------------------
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
-----------------------------

-------------------------------
>>> treeHit = 0
>>> while treeHit < 10:                              #treeHit가 10보다 작은 동안에 while문 안의 문장을 계속 수행
...     treeHit = treeHit +1                         # treeHit 값이 계속 1씩 증가, treeHit += 1 처럼 사용하기도 한다.
...     print("나무를 %d번 찍었습니다." % treeHit)
...     if treeHit == 10:                            # 없애고 print while 문 밖으로 빼도 똑같이 돌아감.
...         print("나무 넘어갑니다.")                 
---------------------------------



#while문 만들기



여러 가지 선택지 중 하나를 선택해서 입력받는 예제
-----------------------
>>> prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """
>>>
-------------------------

--------------------------
>>> number = 0      # 변수를 먼저 설정해 놓지 않으면 다음에 나올 while문의 조건문인 number != 4에서 변수가 존재하지 않는다는 오류가 발생
>>> while number != 4:   # number가 4가 아닌 동안 prompt를 출력하고 사용자로부터 번호를 입력받는다.
...     print(prompt)
...     number = int(input())
...


1. Add
2. Del
3. List
4. Quit

Enter number:
>>>     #4를 입력하면 조건문이 거짓이 되어 while문을 빠져나가게 된다
---------------------------





# while문 강제로 빠져나가기 : break 문

------------------
>>> coffee = 10
>>> money = 300
>>> while money:
...     print("돈을 받았으니 커피를 줍니다.")
...     coffee = coffee -1
...     print("남은 커피의 양은 %d개입니다." % coffee)
...     if coffee == 0:
...         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
...         break
...
---------------------

---------------------

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요. 커피값은 300원입니다. : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
-----------------------





# while문의 맨 처음으로 돌아가기 : continue 문

continue 문은 while문의 맨 처음(조건문: a<10)으로 돌아가게 하는 명령어


1 부터 10 까지의 숫자 중에서 홀수만 출력
------------------------
>>> a = 0
>>> while a < 10:
...     a = a + 1
...     if a % 2 == 0: continue
...     print(a)
...
1
3
5
7
9
------------------------






# 무한 루프 : while True:

--------------------------
>>> while True:
...     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
...
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
....
-----------------------------