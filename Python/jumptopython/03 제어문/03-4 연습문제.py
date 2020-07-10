Q1 다음 코드의 결괏값은 무엇일까?

"""
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
"""

shirt
Need 


#풀이
가장 먼저 참이 되는 조건이 세 번째 조건이므로 "shirt" 출력




Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.


a = 0
b = 0
while a < 1001: # 콜론(:) 을 잊지말것
    a += 1 
    if a % 3 == 0: # 조건문에는 비교연산자 (==) 를 쓰자. = 써서 오류났었음
        b += a
print(b)


#풀이
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result) # 166833 출력







Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

*
**
***
****
*****


a = 0
while a < 5:   # <= 5로 잡았을 시 5일때 +1 돼서 6이 되어버리므로
    a += 1
    print('*'*a)



#풀이
i = 0
while True:
    i += 1 # while문 수행 시 1씩 증가
    if i > 5: break     # i 값이 5이상이면 while문을 벗어난다.
    print ('*' * i)     # i 값 개수만큼 *를 출력한다.









Q4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

for i in range(1, 101):
    print(i, end=" ") # end=" "


#풀이
>>> for i in range(1, 101):
...    print(i)






Q5
A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for문을 사용하여 A 학급의 평균 점수를 구해 보자.



ever = 0
midterm = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in midterm: # :콜론 을 까먹지마라!!!!!!!!!!!!!!!!!!!!!!!!!
    ever += i
print(ever/len(midterm))



# 풀이
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score   # A학급의 점수를 모두 더한다.

average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
print(average) # 평균 79.0이 출력된다.






Q6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.



numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]


# 풀이
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)
[2, 6, 10]