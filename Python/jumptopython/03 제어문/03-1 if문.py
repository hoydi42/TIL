#03-1 if문




#if문의 필요성

if문 = 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 씀


#if문의 기본 구조

if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
"""
조건문을 테스트, 참이면 if문 바로 다음 문장(if 블록)들을 수행 
조건문이 거짓이면 else문 다음 문장(else 블록)들을 수행
else문은 if문 없이 독립적으로 사용할 수 없다
"""

#들여쓰기(indentation)

if문을 만들 때는 if 조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기를 해야 함
들여쓰기는 언제나 같은 너비로.


money = True
if money:
    print("택시를")
    print("타고")
        print("가라")


들여쓰기를 하지 않거나 너비를 맞추지 앉으면 unexpected indent 오류 뜸


$$[조건문 다음에 콜론(:)을 잊지 말자!]$$
if 조건문 뒤에는 반드시 콜론(:)이 붙는다
앞으로 배울 while이나 for, def, class문에도 역시 문장의 끝에 콜론(:)이 항상 들어간다.





#조건문이란 무엇인가?

if 조건문에서 "조건문"이란 참과 거짓을 판단하는 문장


#비교연산자

비교연산자        설명
x < y	    x가 y보다 작다
x > y	    x가 y보다 크다
x == y	    x와 y가 같다
x != y	    x와 y가 같지 않다
x >= y	    x가 y보다 크거나 같다
x <= y	    x가 y보다 작거나 같다


print("만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.")
money = int(input("돈 얼마있냐 :"))
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라.")




#and, or, not

조건을 판단하기 위해 사용하는 다른 연산자

연산자  	    설명
x or y	    x와 y 둘중에 하나만 참이어도 참이다
x and y	    x와 y 모두 참이어야 참이다
not x	    x가 거짓이면 참이다


---------------------직접---------------------------------
print("돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라.")
money = int(input("돈 얼마있냐 : "))
card = str(input("카드는 있냐? 있으면 o, 없으면 x : "))
if card == "o":
    card = True
else:
    card = False

if money >=3000 or card:
    print("택시를 타고 가라.")
else:
    print("걸어 가라.")
----------------------------------------------------


--------------예시--------------
>>> money = 2000
>>> card = True
>>> if money >= 3000 or card:
...     print("택시를 타고 가라")
... else:
...     print("걸어가라")
...
택시를 타고 가라
----------------------------






# x in s, x not in s


    in          	not in
x in 리스트	    x not in 리스트
x in 튜플	    x not in 튜플
x in 문자열     x not in 문자열


>>> 1 in [1, 2, 3]      # "[1, 2, 3]이라는 리스트 안에 1이 있는가?" 조건문
True
>>> 1 not in [1, 2, 3]  # "[1, 2, 3] 리스트 안에 1이 없는가?" 조건문
False


>>> 'a' in ('a', 'b', 'c')
True
>>> 'j' not in 'python'
True


--------------------------
>>> pocket = ['paper', 'cellphone', 'money']
>>> if 'money' in pocket:
...     print("택시를 타고 가라")
... else:
...     print("걸어가라")
...
택시를 타고 가라
>>>
-----------------------------





$$[조건문에서 아무 일도 하지 않게 설정하고 싶다면? : pass ]$$

"주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."

>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket:
...     pass 
... else:
...     print("카드를 꺼내라")

pocket 리스트 안에 money 문자열이 있기 때문에 if문 다음 문장인 pass가 수행되고 아무 결괏값도 보여 주지 않는다.







#다양한 조건을 판단하는 elif

elif 는 이전 조건문이 거짓일 때 수행된다
elif 는 개수에 제한 없이 사용할 수 있다.

--------------
>>> pocket = ['paper', 'handphone']
>>> card = True
>>> if 'money' in pocket:
...     print("택시를 타고가라")
... else:
...     if card:
...         print("택시를 타고가라")
...     else:
...         print("걸어가라")
...
택시를 타고가라
----------------

-----------------------
>>> pocket = ['paper', 'cellphone']
>>> card = True
>>> if 'money' in pocket:
...      print("택시를 타고가라")
... elif card: 
...      print("택시를 타고가라")
... else:
...      print("걸어가라")
...
택시를 타고가라
------------------------

If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ... 



$$[if문을 한 줄로 작성하기]$$
---------------------------------
>>> if 'money' in pocket:
...     pass 
... else:
...     print("카드를 꺼내라")
-----------------------------------------

-----------------------------------------
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket: pass
... else: print("카드를 꺼내라")
------------------------------------
if문 다음 수행할 문장을 콜론(:) 뒤에 바로 적어 주었다. else문 역시 마찬가지




#조건부 표현식

조건부 표현식 : 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

---------------------------
if score >= 60:
    message = "success"
else:
    message = "failure"
---------------------------

--------------------------
message = "success" if score >= 60 else "failure"
---------------------------




