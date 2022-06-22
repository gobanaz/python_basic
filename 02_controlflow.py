#######제어문 : 들여쓰기(indentation) 주의할 것!
'''
비교연산자  설명
x < y       x가 y보다 작다
x > y       x가 y보다 크다
x == y      x와 y가 같다
x != y      x는 y와 다르다
x <= y      x는 y보다 작거나 같다
x >= y      x는 y보다 크거나 같다
'''

'''
연산자      설명
x or y      x와 y 둘 중, 하나만 참이면 참
x and y     x와 y 모두 참이어야 참
not x       x가 거짓이면 참
'''
'''in, not in
in              not in
x in [list]     x not in [list]
x in (tuple)    x not in (tuple)
x in 'string'   x not in 'string
'''

#####3-1 if문
'''if문 기본구조
if 조건문:
    수행문1
    수행문2
    ...
elif 조건문:
    수행문1
    수행문2
    ...
else:
    수행문1
    수행문2
    ...
'''

'''1줄 if문
if 조건문: 수행문
elif 조건문: 수행문
else: 수행문
'''

'''1줄 if문 - 조건부 표현식
참수행문 if 조건문 else 거짓수행문
'''


from re import I

from numpy import average


pocket = ['paper', 'money', 'card']
if 'card' not in pocket:
    print('걸어가')
else:
    print('버스 타')

#아무일도 일어나지 않게 설정하기 : pass
pocket = ['paper', 'money', 'card']
if 'card' not in pocket:
    print('걸어 가')
else:
    pass
    
###다양한 조건 : elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시 타')
elif card:
    print('버스 타')
else:
    print('걸어가')
    
###if문 한줄 작성
if 'money' in pocket:
    pass
else:
    print('카드 꺼내')

    #아래처럼 줄일 수 있다
if 'money' in pocket: pass
else: print('카드꺼내')

###조건부 표현식(conditional expression) : 조건문이참인경우 if 조건문 else 조건문이거짓인경우
score = 60

if score >= 60:
    message = 'success'
else:
    message = 'failure'

    #아래처럼 간단히 표현할 수 있음
message = 'success' if score >= 60 else 'failure'

#####3-2 while문
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print(f'나무를 {treeHit}번 찍었습니다.')
    if treeHit == 10:
        print('나무 넘어갑니다.')

###while문 만들기 : 조건문이 참인동안 반복수행
'''while문 기본구조
while 조건문:
    수행문1
    수행문2
    ...
'''

prompt = '''
1. Add
2. Del
3. List
4. Quit

Enter number: '''
    
number = 0
while number != 4:
    print(prompt, end='')
    number = int(input())
    
###while문 강제로 빠져나가기 : break
coffee = 10
money = 300

while money:
    print('커피 판매 중')
    coffee -= 1
    print(f'남은 커피 양은 {coffee}개 입니다.')
    if coffee == 0:
        print('커피 매진, 판매종료')
        break

#실제 자판기처럼 로직짜보기(coffee.py)
coffee = 10
while True:
    money = int(input('돈을 넣어주세요'))
    if money == 300:
        print('커피를 제공합니다.')
        coffee -= 1
    elif money > 300:
        print(f'커피를 제공합니다. 거스름 돈 {money - 300}원을 받아주세요.')
        coffee -= 1
    else:
        print('금액이 부족합니다.')

    print(f'남은 커피수량은 {coffee}개 입니다.')
    if coffee == 0:
        print('커피 매진, 판매를 종료합니다.')
        break
    
###while의 맨 처음으로 돌아가기 : continue
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue #a가 짝수일때 print 수행하지 않고, while 조건문으로 돌아간다
    print(a)
    
###1부터 10까지의 숫자 중, 3의 배수를 뺀 나머지 값을 출력
a = 0
while a < 10:
    a += 1
    if a % 3 == 0: continue
    print(a)
    
###무한 루프(터미널에서 ctrl + c 로 빠져나올 수 있음)
while True:
    print('Ctrl + C를 눌러야 while문을 빠져나갈 수 있습니다.')
    
#####3-3 for문
'''for문 기본구조
for 변수 in 리스트(or 튜플, 문자열):
    수행문1
    수행문2
    ...
'''

#전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:     #변수 i에 one, two, three가 순차적으로 대입 됨
    print(i)
    

#다양한 for문
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
'''
3
7
11
'''

#for문 응용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print(f'{number}번 학생은 합격입니다.')
    else :
        print(f'{number}번 학생은 불합격입니다.')
        
###for문과 continue
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue  #60점 이하 학생이면 for 조건문으로 이동(print 수행x)
    print(f'{number}번 학생 합격입니다. 축하합니다!')

###for문과 함께 자주 쓰는 range함수
a = range(10)
a   #range(0, 10) > 0~9

a = range(1, 11)
a   #range(1, 11) > 1~10

#1~10까지 더하는 for문
add = 0
for i in range(1, 11):
    add += i
    
print(add)

#위 continue문 range함수 이용
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue  #60점 이하 학생이면 for 조건문으로 이동(print 수행x)
    print(f'{number+1}번 학생 합격입니다. 축하합니다!')
    
###for와 range를 이용해 1~100까지 더하는 함수 만들기
add = 0
for i in range(1, 101):
    add += i
    
print(add)

#for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f'({i} * {j} = {i * j})', end=' ')
    print()

###리스트 내포(List comprehension) 사용하기
'''리스트 내포 일반문법
[표현식 for 항목 in 반복객체 if 조건]

for문 2개 이상 사용도 가능
[표현식 for 항목1 in 반복객체 if 조건1
        for 항목2 in 반복객체 if 조건2
        ...
        for 항목n in 반복객체 if 조건n]
'''
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
    
print(result)
    #위 코드에 리스트 내포를 사용하면 아래와 같이 간단히 표현할 수 있다
    
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

#위에서 만든 구구단 리스트 내포 사용하면
result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)

#####연습문제
#q1     #shirt
#q2
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
    
print(result)

#q3
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)
    
#q4
for i in range(1,101):
    print(i)

#q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

#q6 
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)

#리스트 내포(List comprehension)
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)