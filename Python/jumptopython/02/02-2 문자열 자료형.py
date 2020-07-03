#02-2 문자열 자료형

#"", '', """, " \n "
이스케이프 코드(# \n,t,\,',",r,f,a,n,000)
len 함수 len(a)
문자열 인덱싱 슬라이싱 a[n], a[n:n] 
문자열 포매팅 % %
문자열 포맷 코드 (# %s, c, d, f, o, x, %)
우좌정렬공백, 소수점가능
format 함수 "{}" .format()
f 문자열 포매팅 f " {} "
문자열 관련 함수 (# count, find, index, join, upper, lover, lstrip, rstrip, strip, replace, split, etc)




#문자열(String) : 문자, 단어 등으로 구성된 문자들의 집합

#문자열 만드는 방법(큰따옴표, 작은따옴표, 3개씩)

1 "Hello World"
2 'Hello World'
3 """Hello World"""
4 '''Hello World'''

#문자열에 따옴표 포함시키기(다른 종류 쓰기, 백슬래시(\) 앞에 삽입)

1 '"I am a boy." he says.'
2 "'I am a boy.' he thinks."
3 "\"I am a boy.\"he says."

#여러 줄인 문자열을 변수에 대입하고 싶을 때(이스케이프 코드 \n 삽입, """,''' 사용)

1. multiline = "Life is too short\nYou need python"

#이스케이프 코드(미리 정의해 둔 "문자 조합")
"""
\n	문자열 안에서 줄을 바꿀 때 사용
\t	문자열 사이에 탭 간격을 줄 때 사용
\\	문자 \를 그대로 표현할 때 사용
\'	작은따옴표(')를 그대로 표현할 때 사용
\"	큰따옴표(")를 그대로 표현할 때 사용
\r	캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
\f	폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
\a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
\b	백 스페이스
\000	널 문자
"""

#문자열 연산하기

문자열 더해서 연결하기(Concatenation)

>>> head = "Python"
>>> tail = " is fun!"
>>> head + tail
'Python is fun!'

문자열 곱하기
>>> a = "python"
>>> a * 2
'pythonpython'

문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

응용 결과물
==================================================
My Program
==================================================


#문자열 길이 구하기

len 함수를 사용하면 구할 수 있다. 
len 함수는 print 함수처럼 파이썬의 기본 내장 함수로 
별다른 설정 없이 바로 사용할 수 있다.

>>> a = "Life is too short"
>>> len(a)
17


#문자열 인덱싱(Indexing)과 슬라이싱(Slicing)
# * 파이썬은 0부터 숫자를 센다, 공백도 문자임

#인덱싱 a[n]

a = "Life is too short, You need Python"

Life is too short, You need Python
0         1         2         3 
0123456789012345678901234567890123

a[0]:'L', a[1]:'i', a[2]:'f', a[3]:'e', a[4]:' '

a[-1]: 뒤에서 첫번째문자인 'n' #왜 0이 아니냐면 0은 -0도 0이므로.


#슬라이싱 a[n:n]

>>> a = "Life is too short, You need Python"
>>> b = a[0] + a[1] + a[2] + a[3]
>>> b
'Life'

이것을

>>> a = "Life is too short, You need Python"
>>> a[0:4]
'Life'

이렇게 간단하게 처리할 수 있게 해줌.
# a[0:3] =  0 <= a < 3
            'Lif'


#응용

>>> a[19:]
'You need Python'

>>> a[:17]
'Life is too short'

>>> a[:]
'Life is too short, You need Python'

>>> a[19:-7]
'You need'



#슬라이싱으로 문자열 나누기


>>> a = "20010331Rainy"
>>> year = a[:4]
>>> day = a[4:8]
>>> weather = a[8:]
>>> year
'2001'
>>> day
'0331'
>>> weather
'Rainy'



#["Pithon"이라는 문자열을 "Python"으로 바꾸려면?]


>>> a = "Pithon"
>>> a[1]
'i'
>>> a[1] = 'y'
*오류가 발생한다. 왜냐하면 문자열의 요솟값은 바꿀 수 있는 값이 아니기 때문이다
(문자열 자료형은 그 요솟값을 변경할 수 없다. 
그래서 immutable한 자료형이라고도 부른다).

>>> a = "Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
>>> a[:1] + 'y' + a[2:]
'Python'

슬라이싱을 사용하면 "Pithon" 문자열을 'P' 부분과 'thon' 부분으로 
나눌 수 있기 때문에 그 사이에 'y' 문자를 추가하여 'Python'이라는 
새로운 문자열을 만들 수 있다.


#문자열 포매팅(Formatting) :문자열 안의 특정한 값을 바꿔야 할 경우가 있을 때 문자열 안에 어떤 값을 삽입하는 방법


1. 숫자 바로 대입

>>> "I eat %d apples." % 3
'I eat 3 apples.'

* %d는 문자열 포맷 코드


2. 문자열 바로 대입

>>> "I eat %s apples." % "five"
'I eat five apples.'

* %s는 문자를 넣을 때. *문자열을 대입할 때는 따옴표 반드시 사용할것.

3. 숫자 값을 나타내는 변수로 대입

>>> number = 3
>>> "I eat %d apples." % number
'I eat 3 apples.'

4. 2개 이상의 값 넣기

>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'
위 예문처럼 2개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 콤마(,)로 구분하여 
각각의 값을 넣어 주면 된다.


#문자열 포맷 코드


코드    설명

%s	    문자열(String)
%c	    문자 1개(character)
%d  	정수(Integer)
%f	    부동소수(floating-point)
%o  	8진수
%x  	16진수
%%  	Literal % (문자 % 자체)

*%s 는 % 뒤에 있는 값을 자동으로 문자열로 바꾸기 때문에 
어떤 형태의 값이든 넣을 수 있음. 3, 3.234 같은 숫자도.

*포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다

>>> "Error is %d%." % 98
(Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: incomplete format) 에러남

>>> "Error is %d%%." % 98
'Error is 98%.'



#포맷 코드와 숫자 함께 사용하기


1. 정렬과 공백
>>> "%10s" % "hi"
'        hi'
%10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 
그 앞의 나머지는 공백으로 남겨 두라는 의미이다.

>>> "%-10sjane." % 'hi'
'hi        jane.'


2. 소수점 표현하기

>>> "%0.4f" % 3.42134234
'3.4213'
3.42134234를 소수점 네 번째 자리까지만 나타내고 싶은 경우에는 위와 같이 사용한다. 
즉 여기서 '.'의 의미는 소수점 포인트를 말하고 그 뒤의 숫자 4는 
소수점 뒤에 나올 숫자의 개수를 말한다. 다음 예를 살펴보자.

>>> "%10.4f" % 3.42134234
'    3.4213'
위 예는 숫자 3.42134234를 소수점 네 번째 자리까지만 표시하고 
전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하는 예를 보여 준다.



#format 함수를 사용한 포매팅


숫자 바로 대입하기

>>> "I eat {0} apples".format(3)
'I eat 3 apples'


문자열 바로 대입하기

>>> "I eat {0} apples".format("five")
'I eat five apples'


숫자 값을 가진 변수로 대입하기

>>> number = 3
>>> "I eat {0} apples".format(number)
'I eat 3 apples'


2개 이상의 값 넣기 #{0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다

>>> number = 10
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'


이름으로 넣기 #{name} 형태를 사용할 경우 format 함수에는 반드시 name=value 와 같은 형태의 입력값이 있어야

>>> "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days.'


인덱스와 이름을 혼용해서 넣기

>>> "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
'I ate 10 apples. so I was sick for 3 days.'

왼쪽 정렬

>>> "{0:<10}".format("hi")
'hi        '

*:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.


오른쪽 정렬

>>> "{0:>10}".format("hi")
'        hi'

가운데 정렬

>>> "{0:^10}".format("hi")
'    hi    '

공백 채우기

>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:!<10}".format("hi")
'hi!!!!!!!!'

# " {0:'암거나' '> < ^(우,좌,중앙) '칸수'} " .format


소수점 표현하기

>>> y = 3.42134234
>>> "{0:0.4f}".format(y)
'3.4213'

(자릿수 10으로 맞추기)
>>> "{0:10.4f}".format(y)
'    3.4213'

{ 또는 } 문자 표현하기

>>> "{{ and }}".format()
'{ and }'
#format 함수를 사용해 문자열 포매팅을 할 경우 { }와 같은 중괄호(brace) 문자를 
포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우에는 위 예의 {{ }}처럼 2개를 연속해서 사용하면 된다.



# f 문자열 포매팅(파이썬 3.6 미만 버전에서는 사용할 수 없는 기능)

# a = 예스
# b = 노
# f ' 블라블라{a} 블라블라 {b} ' 

>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'


※ 표현식 지원. 표현식이란 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용하는 것을 말한다.

>>> age = 30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'

딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용할 수 있다.
※ 딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형이다. 02-5 에서 자세히 알아본다.

>>> d = {'name':'홍길동', 'age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'


정렬

>>> f'{"hi":<10}'  # 왼쪽 정렬
'hi        '
>>> f'{"hi":>10}'  # 오른쪽 정렬
'        hi'
>>> f'{"hi":^10}'  # 가운데 정렬
'    hi    '

공백 채우기

>>> f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
'====hi===='
>>> f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기
'hi!!!!!!!!'

소수점 표현

>>> y = 3.42134234
>>> f'{y:0.4f}'  # 소수점 4자리까지만 표현
'3.4213'
>>> f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
'    3.4213'

f 문자열에서 { } 문자를 표시

>>> f'{{ and }}'
'{ and }'


format 
{} " .format()
f " {} "





#문자열 관련 함수들


문자열 자료형은 자체적으로 함수를 가지고 있다. 
이들 함수를 다른 말로 문자열 내장 함수라 한다. 
내장 함수를 사용하려면 문자열 "변수(a=time 같은것)" 이름 뒤에 ‘.’를 붙인 다음에 함수 이름을 써주면 된다. 

문자 개수 세기(count)

>>> a = "hobby"
>>> a.count('b')
2


위치 알려주기1(find)

>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1

* 문자열 중 문자 b가 처음으로 나온 위치를 반환한다. 
*만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다


위치 알려주기2(index)

>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found

*문자열 중 문자 t가 맨 처음으로 나온 위치를 반환한다. 
*만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다. 


문자열 삽입(join)

>>> ",".join('abcd')
'a,b,c,d'


*join 함수는 문자열뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있다
join 함수의 입력으로 리스트를 사용하는 예

>>> ",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'


소문자를 대문자로 바꾸기(upper)

>>> a = "hi"
>>> a.upper()
'HI'


대문자를 소문자로 바꾸기(lower)

>>> a = "HI"
>>> a.lower()
'hi'


왼쪽 공백 지우기(lstrip)

>>> a = " hi "
>>> a.lstrip()
'hi '


오른쪽 공백 지우기(rstrip)
>>> a= " hi "
>>> a.rstrip()
' hi'


양쪽 공백 지우기(strip)
>>> a = " hi "
>>> a.strip()
'hi'


문자열 바꾸기(replace)
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'



문자열 나누기(split)
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']



