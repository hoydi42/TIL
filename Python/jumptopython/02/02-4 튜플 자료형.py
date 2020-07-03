#02-4 튜플 자료형


#튜플(tuple)

리스트와 거의 비슷함
리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.


>>> t1 = ()
>>> t2 = (1,) #1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
>>> t3 = (1, 2, 3)
>>> t4 = 1, 2, 3 #괄호( )를 생략해도 무방하다
>>> t5 = ('a', 'b', ('ab', 'cd'))

"값이 변화 가능해야 하면 리스트, 값이 변하지 않아야 하면 튜플"



#튜플의 요소값을 지우거나 변경하려고 하면

1. 튜플 요솟값을 삭제하려 할 때

>>> t1 = (1, 2, 'a', 'b')
>>> del t1[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion

2. 튜플 요솟값을 변경하려 할 때

>>> t1 = (1, 2, 'a', 'b')
>>> t1[0] = 'c'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


#튜플 다루기

인덱싱
>>> t1 = (1, 2, 'a', 'b')
>>> t1[0]
1
>>> t1[3]
'b'

슬라이싱
>>> t1 = (1, 2, 'a', 'b')
>>> t1[1:]
(2, 'a', 'b')

더하기
>>> t1 = (1, 2, 'a', 'b')
>>> t2 = (3, 4)
>>> t1 + t2
(1, 2, 'a', 'b', 3, 4)

곱하기
>>> t2 = (3, 4)
>>> t2 * 3
(3, 4, 3, 4, 3, 4)

길이 구하기
>>> t1 = (1, 2, 'a', 'b')
>>> len(t1)
4


