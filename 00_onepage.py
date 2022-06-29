'''
숫자형
문자열 자료형
리스트 자료형
튜플 자료형
딕셔너리 자료형
집합 자료형
불 자료형
변수 : 자료형의 값을 저장하는 공간
'''

#####2-1 숫자형
    #정수형(integer) : int
    #실수형(Floating-point) : float
    #8진수(Octal)
    #16진수(Hexadecimal)

    #사칙연산 : + - * /
        #곱 : *
        #제곱 : **
        
        #나누기 : /
        #몫 : //
        #나머지 : %
        
#14를 3으로 나누었을때 몫과 나머지

14/3
#4.666666666666667

14//3
#4

14%3
#2

#####2-2 문자열 자료형
#줄바꿈 \n
#변수에 여러줄 삽입case
multiline = 'Life is too short\nYou need python'
print(multiline)
'''
Life is too short
You need python
'''

multiline = '''Life is too short
You need python'''
print(multiline)

###이스케이프 코드 : 프로그래밍 문자조합 > 백슬래시(\) + 문자
'''
\n : 줄바꿈
\t : 탭 간격
\\ : \를 문자그대로 사용할때
\' : '를 문자그대로 사용할때
\" : "를 문자그대로 사용할때
\r : 캐리지 리턴(줄바꿈 & 커서를 가장 앞으로 이동)
\f : 폼 피드(줄바꿈 & 현재 커서를 다음줄로 이동)
\a : 벨 소리(출력시 PC 스피커 삑 소리 출력)
\b : 백스페이스
\000 : 널 문자
'''

#문자열 연산(Concatenation)
head = 'Python'
tail = ' is fun!'
head + tail
#'Python is fun!'

#문자열 곱
a = 'python'
a * 2
#'pythonpython'

#문자열 연산 응용
print('=' * 50)
print('My program')
print('=' * 50)
'''
==================================================
My program
==================================================
'''

#문자열 길이 : len()
a = 'Life is too short'
len(a)

b = 'You need python'
len(b)

#문자열 자료형은 요소값을 변경할 수 없다 : immutable 자료형

###문자열 포매팅(Formatting) : 문자열안에 값을 삽입하는 방법
'I eat %d apples.' % 3
'I eat %s apples.' % 'five'

number = 7
'I eat %d apples.' % number

number = 10
day = 'three'
'I ate %d apples. So i was sick for %s days.' % (number, day)

'''문자열 포맷 코드
%s : string(문자열)
%c : Character(문자 1개)
%d : 정수(decimal, int)
%f : 부동 소수(Float)
%o : 8진수
%x : 16진수
%% : Literal %(문자그대로 % 자체)
'''

#정렬과 공백
'%10s' % 'hi'   #전체 길이 10자리 중 hi를 오른쪽 정렬로 표현 > %10s 오른쪽 정렬
#'        hi'

'%-10sjane' % 'hi'  #hi왼쪽정렬(총10자리)+jane 표현
#'hi        jane'

#소수점 표현
'%0.4f' % 3.42134234    #소수점 이하 4자리까지 표현
#'3.4213'

'%10.4f' % 3.42134234    #전체 10자리 & 소수점 이하 4자리까지 표현(공백4, 숫자5, 소수점1)
#'    3.4213'

###format 함수를 사용한 포맷팅
'I eat {0} apples.'.format(3)
'I eat {0} apples.'.format('five')

number = 7
'I eat {0} apples.'.format(number)

number = 10
day = 'three'
'I ate {0} apples. So i was sick for {1} days.'.format(number, day)

'I ate {number} apples. So i was sick for {day} days.'.format(number = 12, day = 'seven')

'I ate {0} apples. So i was sick for {day} days.'.format(15, day = 'eight')

#왼쪽정렬
'{0:<10}'.format('hi')
    #'hi        '

#오른쪽정렬
'{0:>10}'.format('hi')
    #'        hi'

#가운데정렬
'{0:^10}'.format('hi')
    #'    hi    '

#공백채우기 2가지 방법
'{0:=^10}'.format('hi')
    #'====hi===='
    
'{0:!<10}'.format('hi')
    #'hi!!!!!!!!'

#소수점 표현
y = 3.42134234

'{0:0.4f}'.format(y)
    #'3.4213'

'{0:10.4f}'.format(y)
    #'    3.4213'
    
#literal {} 표현
'{{ and }}'.format()

###f문자열 포매팅(up to python ver3.6)
name = '홍길동'
age = 30
f'나의 이름은 {name}, 나이는 {age} 입니다.'

f'나는 내년에 {age+1}살 입니다.'

#딕셔너리 f문자열 포매팅
dic = {'name' : '홍길동', 'age' : 30}
f'나의 이름은 {dic["name"]}입니다. 나이는 {dic["age"]}입니다.'

#f문자열 포매팅 정렬
f'{"hi":<10}'
    #'hi        '
    
f'{"hi":>10}'
    #'        hi'
    
f'{"hi":^10}'
    #'    hi    '

#f문자열 포매팅 공백채우기
f'{"hi":=^10}'  #'====hi===='
f'{"hi":!>10}'  #'!!!!!!!!hi'

#f문자열 포매팅 소수점
y = 3.42134234

f'{y:0.4f}'     #'3.4213'
f'{y:10.4f}'    #'    3.4213'

#literal {} 표현
f'{{ and }}'    #'{ and }'

f'{"python":!^12}'
'{0:!^12}'.format('python')

###문자열 관련 함수
'''
count : 문자 개수 세기
find : 위치 찾기
index : 위치 찾기
join : 문자열 삽입
upper : 대문자 치환
lower : 소문자 치환
lstrip : 왼쪽 공백 제거
rstrip : 오른쪽 공백 제거
strip : 양쪽 공백 제거
replace : 문자열 치환
split : 문자열 나누기
'''
#count : 문자 개수 세기
a = 'hobby'
a.count('b')    #2

#find : 위치 찾기
a = 'Python is the best choice'
a.find('b') #14
a.find('k') #없으면 -1 리턴

#index : 위치 찾기
a = 'Python is the best choice'
a.index('b') #14
a.index('k') #없으면 에러 발생

#join : 문자열 삽입
','.join('abcd')    #'a,b,c,d'  #'abcd'사이에 , join
','.join(['a','b','c','d'])    #'a,b,c,d'  #'[a, b, c, d]'사이에 , join

#upper : 대문자 치환
a = 'hi'
a.upper()   #'HI'

#lower : 소문자 치환
a = 'HI'
a.lower()   #'hi'

#lstrip : 왼쪽 공백 제거
a = ' hi '
a.lstrip()  #'hi '

#rstrip : 오른쪽 공백 제거
a = ' hi '
a.rstrip()  #' hi'

#strip : 양쪽 공백 제거
a = ' hi '
a.strip()   #'hi'

#replace('1', '2') : 1을 2로 문자열 치환
a = 'Life is too short'
a.replace('Life', 'your leg')   #대소문자 가림

#split(기준) : 기준으로 문자열 나누기 - 리스트로 리턴
a = 'Life is too short'
a.split()   #['Life', 'is', 'too', 'short'] #공백기준 split

b = 'a:b:c:d'
b.split(':')

#####2-3 리스트 자료형
#리스트명 = [요소1, 요소2, 요소3, ...]

#삼중 리스트 인덱싱
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[-1][2][0] #'Life'

#리스트 슬라이싱(문자열 슬라이싱과 동일)
A = [1, 2, 3, 4, 5]
result = A[1:3]

#중첩리스트 슬라이싱
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][:2]

###리스트 연산
#리스트 합
a = [1, 2, 3]
b = [4, 5, 6]
a + b   #[1, 2, 3, 4, 5, 6]

#리스트 곱
a = [1, 2, 3]
a * 3   #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 길이 : len(a)
a = [1, 2, 3]
len(a)  # 3

#리스트 연산 오류
a = [1, 2, 3]
a[2] + 'hi' #TypeError: unsupported operand type(s) for +: 'int' and 'str'
str(a[2]) + 'hi'    #'3hi'

###리스트 수정과 삭제 : 리스트는값을 수정하거나 삭제할 수 있음(뮤터블)
a = [1, 2, 3]
a[2] = 4
a   #[1, 2, 4]

###리스트 요소 삭제 : del 객체
a = [1, 2, 3]
del a[1]
a   #[1, 3]

    #리스트 요소 삭제방법은 remove, pop으로도 가능
    
###리스트 관련 함수
'''
append(x) : 리스트 맨뒤로 x 추가
sort() : 정렬
reverse() : 뒤집기
index(x) : x index 반환
insert(a,b) : a index에 b요소 삽입
remove(x) : 리스트 내 먼저 확인되는 x요소 삭제
pop(index) : 리스트 index 요소 꺼내기(default : 맨뒤, index안적으면 맨뒤요소 pop)
count(x) : 리스트 내 x의 갯수 리턴
extend : 리스트 확장
'''
#append : 리스트 맨뒤로 요소 추가
a = [1, 2, 3]
a.append(4)
a   #[1, 2, 3, 4]

a.append([5,6])
a   #[1, 2, 3, 4, [5, 6]]

#sort : 정렬
a = [1, 4, 3, 2]
a.sort()
a   #[1, 2, 3, 4]

a = ['a', 'c', 'b']
a.sort()
a   #['a', 'b', 'c']

#reverse : 뒤집기 정렬 > 역순정렬 아니고 리스트 그 자체를 뒤집음
a = ['a', 'c', 'b']
a.reverse()
a   #['b', 'c', 'a']

#index : 위치 반환
a = [1, 2, 3]
a.index(3)  #2 > 2번째라는게 아니고 a[index] index번호를 반환
a[2]    #3

#insert(a,b) : a index에 b요소 삽입
a = [1, 2, 3]
a.insert(0,4)
a   #[4, 1, 2, 3] > 0번 index에 4 삽입

#remove(x) : 리스트 내 먼저 확인되는 x요소 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a   #[1, 2, 1, 2, 3]

#pop(index) : 리스트 index 요소 꺼내기(default : 맨뒤, index안적으면 맨뒤요소 pop)
a = [1, 2, 3]
a.pop(1) #2
a   #[1, 3]

a = [1, 2, 3]
a.pop() #3
a   #[1, 2]

#count(x) : 리스트 내 x의 갯수 리턴
a = [1, 2, 3, 1, 1, 1, 1]
a.count(1)  #5

#extend(x) : 리스트 확장, x는 리스트 형만 가능, 기존리스트 + x리스트
a = [1, 2, 3]
a.extend([4, 5])
a   #[1, 2, 3, 4, 5]

b = [6, 7]
a.extend(b)
a   #[1, 2, 3, 4, 5, 6, 7]

#####2-4 튜플 자료형
#리스트와 거의 비슷하나, 아래의 2가지가 큰 차이점
    #1. 튜플은 괄호로 둘러싼다 () > 리스트는 대괄호로 둘러싼다 []
    #★★★2. 튜플은 값을 바꿀수 없다 > 리스트는 값의 생성, 삭제, 수정이 가능
        #이 말은, 정의한 하나의 튜플 이후에 해당튜플에 append같은 행위가 불가하다는 얘기지
            #다른 튜플간 더하기, 곱하기 등 연산이 불가능 하다는 얘기가 아님
    
    #또 다른 2가지
        #3. 1개의 요소를 가질때는 요소뒤에 반드시 ,를 찍어야함(튜플임을 구분하기 위해)
        #4. 괄호 생략 가능
#ex)
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
type(t4)    #<class 'tuple'>
t5 = ('a', 'b', ('ab', 'cd'))

#(1, 2, 3) 튜플에 4 추가해서 (1, 2, 3, 4) 만들어 출력해보기
(1, 2, 3)+(4,)

#####2-5 딕셔너리 자료형
    #연관배열(Associative array) 또는 해시(Hash) 형 구조
    #{key1:Value1, Key2:Value2, Key3:Value3 ...}

###딕셔너리 쌍 추가/삭제
#추가
a = {1:'a'}
a[2] = 'b'
a   #{1: 'a', 2: 'b'}

a['name'] = 'pey'   #{'name':'pey'} 쌍 추가
a   #{1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1, 2, 3]
a   #{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

#삭제
del a[1]    #key가 1인 key:value > 1:'a' 삭제
a   #{2: 'b', 'name': 'pey', 3: [1, 2, 3]}

###딕셔너리 사용법
#Key로 Value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey']    #10
grade['julliet']    #99

    #딕셔너리는 무조건 key값을 통해 Value를 찾는다
    
#딕셔너리 생성시 주의사항
    #1. Key값 중복되면 하나빼고 나머지는 무시된다
    #2. Key값으로 리스트, 딕셔너리는 사용불가(튜플은 가능)
    #3. Value값으로는 아무값이나 가능
    
###딕셔너리 관련 함수
'''
keys() : Key값 dict_keys 보여주기, 리턴도 리스트로 받으려면 list(딕셔너리.keys())
values() : Values dict_list 보여주기
items() : key, value 쌍 얻기
clear() : key:value 쌍 모두 지우기
get(key, default return value) : key로 value 얻기
'Key' in dic : 해당 key가 딕셔너리에 있는지 확인
'''
#Keys() : Key값 모아 리스트화
a = {'name': 'pey', 'phone':'0112223333', 'birth':'1118'}
a.keys()    #dict_keys(['name', 'phone', 'birth'])

    #리스트로 리턴받고 싶은경우 list(a.keys()) 쓸것
list(a.keys())  #['name', 'phone', 'birth']

#values() : Values dict_list 보여주기, 리스트 리턴받으려면 list(a.values())
a.values()
list(a.values())

#items() : key, value 쌍 얻기
a.items()
list(a.items())

#clear() : key:value 쌍 모두 지우기
a.clear()
a   #{}

#get(key, default return value) : key로 value 얻기
a = {'name': 'pey', 'phone':'0112223333', 'birth':'1118'}
a.get('name')   #'pey'
a.get('phone')  #'0112223333'

    #key값이 없는경우 none을 리턴
        #이런경우 default값을 설정해주면 none이어도 default값을 리턴
        
print(a.get('nane', 'jessy'))

#in : 해당 key가 딕셔너리에 있는지 확인
a = {'name': 'pey', 'phone':'0112223333', 'birth':'1118'}
'name' in a #True
'email' in a #False

###딕셔너리 만들어보기
dic = {'name': '홍길동', 'bitrh': '1128', 'age': 30}

#####2-6 집합 자료형 set() : 주머니
s1 = set([1,2,3])   #{1, 2, 3}
s2 = set('hello')   #{'o', 'e', 'h', 'l'}

#집합자료형 특징
    #중복이 하나로 합쳐진다(중복이 없다)
    #순서가 없다(Unordered) > 리스트, 튜플은 순서 있음
        #순서가 없으므로, 인덱싱이 불가능
            #set자료형 인덱싱으로 접근하려면 리스트 or 튜플로 변환해야 함
            
l1 = list(s1)
l1  #[1, 2, 3]

t1 = tuple(s1)
t1  #(1, 2, 3)


###교집합, 합집합, 차집합 구하기
    #set자료형은 위의 경우 유용함
    
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합 intersection()
s1 & s2 #{4, 5, 6}

s1.intersection(s2) #{4, 5, 6}

#합집합 unison()
s1 | s2 #{1, 2, 3, 4, 5, 6, 7, 8, 9}

s1.union(s2)    #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#차집합 difference()
s1 - s2 #{1, 2, 3}
s2 - s1 #{8, 9, 7}

s1.difference(s2)   #{1, 2, 3}
s2.difference(s1)   #{8, 9, 7}

###집합 자료형 관련 함수
'''
add() : 값 1개 추가
update() : 값 여러개 추가
remove() : 특정 값 제거
'''
#add() : 값 1개 추가
s1 = set([1, 2, 3])
s1.add(4)
s1  #{1, 2, 3, 4}

#update() : 값 여러개 추가
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1  #{1, 2, 3, 4, 5, 6}

#remove() : 특정 값 제거
s1 = set([1, 2, 3])
s1.remove(2)
s1  #{1, 3}

#####2-7 불(bool) 자료형 : 논리형, True/False 리턴
'''자료형의 참과 거짓
자료형      값          참/거짓
문자열      "python"    참
            ""          거짓
            
리스트      [1,2,3]     참
            []          거짓

튜플        ()          거짓

딕셔너리    {}          거짓

숫자형      0이아닌숫자   참
            0           거짓
            
            None        거짓
'''

#사용예시
a = [1, 2, 3, 4]
while a:
    a.pop()

'''
4
3
2
1
'''    
#while문이 참인동안 반복
    #> a.pop이 다 돌아서 빈 리스트[] 가 되면 거짓
        #> while문 종료
        
###불 연산
bool('python')  #True
bool('')        #False
bool(-1)        #True
bool(0)         #False
bool([1,2,3])   #True
bool([])        #False
bool(None)      #False

#####2-8 변수 : 자료형의 값을 저장하는 공간
a = [1, 2, 3]
id(a)

###리스트 복사
a = [1, 2, 3]
b = a
id(a)   #1836365623168
id(b)   #1836365623168
#참조값이 같음

a is b  #True

a[1] = 4
a   #[1, 4, 3]
b   #[1, 4, 3]
#아직까지도 같음

c = a[:]
id(c)   #1836365667264 달라짐

a[2] = 5
a   #[1, 4, 5]
c   #[1, 4, 3]  따라오지 않음

#즉, b는 [1,2,3]으로 생성한 a를 그대로 참조하면서 동일하게 따라왔지만,
    #c는 a를 슬라이싱 하면서 새로 생성된 객체를 참조, id값이 달라지면서 다른객체가 됨
    
#copy 모듈 사용
from copy import copy

from numpy import average
a = [1, 2, 3]   #새로 정의하면 새로운 메모리에 객체 [1, 2, 3] 생성 > a가 해당객체 주소 참조
b = copy(a)     #b가 a를 copy(a를 그대로 쓰지 않고, a를 새로이 생성)
id(a)   #1836365698688
id(b)   #1836365710272
b is a  #False

###변수 생성 방법들
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a   #'python'
b   #'life'
#위 방법은 모두 같은 결과

a = 3
b = 5
a, b = b, a
a   #5
b   #3

###예제 결과 확인
a = [1, 2, 3]
b = [1, 2, 3]
a is b  #False

#####연습문제
#q1
import numpy as np
score = [80, 75, 55]
np.average(score)

'''교재 답
a, b, c = 80, 75, 55
(a+b+c)/3
'''

#q2
if 13 % 2:
    print('홀수 입니다.')
else:
    print('짝수 입니다.')
    
#q3
pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[-7:]
print(yyyymmdd)
print(num)

yyyymmdd, num = pin.split('-')
print(yyyymmdd)
print(num)

#q4
pin = '881120-1068234'
print(pin[7])   #1이면 남자, 2면 여자

#q5
a = 'a:b:c:d'
b = str(a.replace(':', '#'))
print(b)

#q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#q7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

#q8
a = (1, 2, 3)
a = a + (4,)        #튜플은 add, append 불가하므로 새로 정의해주어야 함
print(a)

#q9
a = dict()
a   #{}

a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python'   #에러발생 > 딕셔너리 key값으로 변하는(mutable) 변수 사용불가 > 즉, 리스트 사용불가
a[250] = 'python'
a

#q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)    #{'A':90, 'C':70} 출력
print(result)   #80출력

#q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)    #[1, 2, 3, 4, 5]

#q12
a = b = [1, 2, 3]
a[1] = 4
print(b)    #[1, 4, 3]

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

#######입력과 출력
'''
함수
사용자 입력과 출력
파일 읽고 쓰기
'''

#####4-1 함수
'''함수 정의 기본구조
def 함수명(매개변수):
    수행문1
    수행문2
    
    return 결과값
'''

#add함수, 2값 입력받아 합쳐 결과값으로 내보낸다
def add(a, b):  #여기서 a,b는 매개변수(parameter)
    return a + b

a = 3
b = 4
c = add(a,b)    #여기 a,b는 인수(arguments)
print(c)    #7

###매개변수와 인수
    #매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수
    #인수(arguments) : 함수를 호출할 때 전달하는 입력값
    
###입력값, 결과값에 따른 함수의 사용법

#일반적인 함수 : 결과값받을변수 = 함수명(입력인수1, 입력인수2, ...)
def add(a, b):      #입력값 a, b
    result = a + b
    return result   #결과값 result

a = add(3, 4)
print(a)

#입력값 없는 함수 : 결과값받을변수 = 함수명()
def say():          #입력값 없음
    return 'Hi'     #결과값 'Hi'

a = say()
print(a)    #Hi

#결과값 없는 함수 : 함수명(입력인수1, 입력인수2, ...)
def add(a, b):
    print(f'{a} + {b} = {a + b}입니다.')

add(3,4)    #7 : 결과값으로 7이 return되는게 아닌, 함수에 따른 명령수행으로 7이 print되는 것일 뿐
a = add(3,4)
print(a)    #None : 실제로 a에 담으려 해도, 아무것도 담기지 않음

#입력값&결과값 모두 없는 함수 : 함수명()
def say():
    print('Hi')

say()   #'Hi'

###매개변수 지정하여 호출
def add(a, b):
    return a + b

result = add(a=3, b=7)
result

result = add(b=5, a=3)  #매개변수 지정시 순서 상관없이 사용할 수 있음
result

###입력값이 몇개가 될지 모를때 : 매개변수 앞에 *을 달아줌
'''
def 함수명(*매개변수):      #매개변수 앞에 *을 달아줌
    수행문
    ...
'''

#여러개 입력값 받는 함수 만들기
def add_many(*args):    # 매개변수 앞에 *을 붙이면, 입력값을 전부 모아 튜플로 만들어줌
    result = 0
    for i in args:
        result += i
    return result

    #args는 매개변수의 약자로, 관례적으로 자주 사용하는 단어(pandas ad pd처럼)
    
result = add_many(1,2,3)
print(result)   #6

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)   #55

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)   #15

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)   #120

###키워드 파라미터 : **매개변수
#매개변수 앞에 **을 붙이면 매개변수(kwargs)는 딕셔너리가 됨 > key=value 형태로 결과값이 저장됨
def print_kwargs(**kwargs): #kwargs : keyward argments 관례용어
    print(kwargs)
    
print_kwargs(a=1)   #{'a': 1}
print_kwargs(name='foo', age=3)   #{'name': 'foo', 'age': 3}

###함수의 결과값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b     #가능 > 튜플형태로 2가지 연산을 한 하나의 결과값을 받음

result = add_and_mul(3,4)
print(result)   #(7, 12)

#결과값을 따로 받으려면 아래처럼 해도 된다
result1, result2 = add_and_mul(3,4)
print(result1)   #7
print(result2)   #12

#그러나 아래처럼은 불가능
def add_and_mul(a,b):
    return a+b  #수행O
    return a*b  #수행X 삭제해도 무방한 코드

result = add_and_mul(2,3)
print(result)   #5  > return a*b 는 수행되지 않음을 알 수 있음

    #즉, 함수는 return문을 만나면 결과값을 돌려주고 종료됨
    
###return의 또 다른 쓰임새
#특별한 상황에서 함수를 빠져나가는 용도로 사용가능
def say_nick(nick):
    if nick == '욕설':
        return
    print(f'나의 별명은 {nick} 입니다.')

say_nick('야호')    #나의 별명은 야호 입니다.
say_nick('욕설')    #
    #위처럼 의도적으로 return문으로 함수를 빠져나갈 수 있음
        #그렇다고 야호를 넣었을때 리턴값이 있는것도 아님(단순 print명령을 수행했을뿐)
            #함수의 결과값은 오직 return문에 의해서만 수행 됨
            
###매개변수 초기값 미리 설정
def say_myself(name, age, man=True):
    print(f'나의 이름은 {name} 입니다.')
    print(f'나이는 {age} 입니다.')
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('박응용', 27)
say_myself('박응용', 27, True)
'''
나의 이름은 박응용 입니다.
나이는 27 입니다.
남자입니다.
'''

say_myself('박응선', 27, False)
'''
나의 이름은 박응선 입니다.
나이는 27 입니다.
여자입니다.
'''

    #초기값 설정시 주의사항 : 초기값 설정 매개변수 뒤에 초치값 비설정 매개변수를 넣지말것
#ex)
''' def say_myself(name, man=True, age):    #Non-default argument follows default argument 에러코드
    print(f'나의 이름은 {name} 입니다.')
    print(f'나이는 {age} 입니다.')
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.') '''
        
#즉 매개변수로 (name, age, man=True) 가능, (name, man=True, age) 불가능

###함수 안에서 선언한 변수 효력범위
a = 1   #함수 밖의 변수 a
def vartest(a):
    a = a + 1
    return a
    
result = vartest(a)

print(a)    #1
print(result)   #2

    #함수 안에서 발생한 일은 함수 밖으로 나오는 순간 없던일이 된다
        #그래서 return 등을 이용해 함수 내부의 결과를 따로 담아 사용하는 것
        
#함수 안에서 함수 밖의 변수를 변경하는 방법
    #1. return
    #2. global
    
#1. return 사용
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)    #2

#2. global 명령어 사용
a = 1
def vartest():
    global a    #함수밖의 a함수를 직접 사용하겠다는 의미
    a = a + 1
    
vartest()
print(a)    #2

#global을 사용함으로써 a가 2가 되었지만
    #이 경우, 외부함수(a)가 vartest함수에 종속변수가 되어버림
        #따라서 권장하지 않음 > 1의 방법(return)을 권장함
        
###lambda : 함수를 생성하는 예약어 def와 동일한 역할
    # def를 사용할 정도로 복잡하지 않거나
    # def를 사용할 수 없는 곳에 쓰임
    # 보통 함수를 한줄로 간결하게 정의할때 주로사용
    
'''람다 사용법
함수명 = lambda 매개변수1, 매개변수2, ... : 표현식
'''

add = lambda a, b: a + b    #람다함수는 return문이 없어도 결과값을 return함
result = add(3,4)
print(result)   #7

#위 람다 함수는 아래와 동일한 함수
def add(a, b):
    return a + b
result = add(3, 4)
print(result)

#####4-2 사용자 입력과 출력
###사용자입력 : input('질문내용') > 입력되는 모든 것을 문자열로 취급
a = input()
a   #'Life is too short, you need python'

number = input('숫자를 입력하세요 : ')
print(number)

###print 자세히 알기
a = 123
print(a)    #123    #int 출력

a = 'Python'
print(a)    #Python    #str 출력

a = [1, 2, 3]
print(a)    #[1, 2, 3]    #list 출력

#''로 둘러싸인 문자열은 +연산과 동일
print('life''is''too short')    #lifeistoo short
print('life'+'is'+'too short')  #lifeistoo short

#문자열 띄어쓰기는 콤마로 함
print('life','is','too short')    #life is too short

#한 줄에 결과값 출력
for i in range(10):
    print(i, end=' ')   #0 1 2 3 4 5 6 7 8 9 >>>
    
#####4-3 파일 읽고 쓰기 : 파일객체 = open(파일명, 파일열기모드)
f = open('새파일.txt', 'w')
f.close()

'''
파일열기모드    설명
r              읽기모드 - 파일 읽기만 할때 사용
w              쓰기모드 - 파일 내용 쓸때 사용
a              추가모드 - 파일의 마지막에 새로운 내용 추가 시 사용
'''

#새 파일을 다른 디렉토리에 생성하고 싶다면, 다음과 같이 작성
f = open('C:/디렉토리명/새파일.txt', 'w')
f.close()

###파일을 쓰기 모드로 열어 출력값 적기
f = open('D:/Dev/Python/새파일.txt', 'w')
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()

###프로그램 외부에 저장된 파일을 읽는 여러방법
#1. readline() : 파일을 한줄씩 읽어옴
f = open('D:/Dev/Python/새파일.txt', 'r')
line = f.readline()
print(line) #1번째 줄입니다.
f.close()

    #모든 줄 읽기
f = open('d:/Dev/Python/새파일.txt','r')
while True:
    line = f.readline()     #더 읽을 줄 없는경우 readline이 None을 리턴
    if not line: break      #line이 None이 되면 not line > true > break
    print(line)
f.close()

#2. readlines() : 파일의 모든 줄을 읽어 하나의 리스트로 리턴
f = open('d:/Dev/Python/새파일.txt','r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#3. read() : 파일 내용 전체를 문자열로 리턴
f = open('d:/Dev/Python/새파일.txt','r')
data = f.read()
print(data)
f.close()

###파일에 새로운 내용 추가
f = open('d:/Dev/Python/새파일.txt','a')    # add모드
for i in range(11, 20):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()

###with문과 함께 쓰기
#지금까지 사용한 방식
f = open('새파일.txt', 'w') #파일을 열었으면
f.write('Life is too short, you need python')
f.close()   #꼭 닫아줄것

#with문을 사용하면 자동으로 닫아줌
with open('새파일.txt', 'w') as f:
    f.write('Life is too short, you need python')
#with 블록을 벗어나는 순간, 열린파일 객체 f가 자동으로 close되어 편리함

###sys모듈로 매개변수 주기
#sys1.py 로 저장한다고 가정
from re import I
import sys

args = sys.argv[1:]
for i in args:
    print(i)
    
#cmd창 > python sys1.py aaa bbb ccc
'''
aaa
bbb
ccc
'''

#sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

#cmd창 > python sys2.py life is too short, you need python
'''
LIFE IS TOO SHORT, YOU NEED PYTHON
'''
#####연습문제
#q1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
'''람다로 하면
is_odd = lambda number: True if number % 2 == 1 else False
'''

#q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)

#q3
input1 = int(input('첫번째 숫자 입력 : '))
input2 = int(input('두번째 숫자 입력 : '))

total = input1 + input2
print(f'두 수의 합은 {total}입니다.')   #두 수의 합은 36입니다. > 9가 되도록 고칠것

#q4 3

#q5
f1 = open('test.txt', 'w')
f1.write('Life is too short')
f1.close()  #이거 빠져서 안읽힌듯

f2 = open('test.txt', 'r')
print(f2.read())
f2.close()

'''with구문이라면
with open('test.txt', 'w') as f1:
    f1.write('Life is too short')
with open('test.txt', 'r') as f2:
    print(f2.read())
'''

#q6
user_input = input('저장할 내용 입력 : ')
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()

#q7
'''
Life is too short
you need java
'''

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()

'''
클래스
모듈
패키지
예외처리
내장함수
라이브러리
'''

#####5-1 클래스
    #과자 틀 > 클래스(class)
    #과자 틀로 만든 과자 > 객체(Object)
class Cookie:
    pass

a = Cookie()
b = Cookie()
#a와 b는 하나의 틀(Cookie 클래스)로 만들었지만, 서로 다른과자
    #따라서 a,b 상호간에는 영향을 끼치지 않음

###객체와 인스턴스
    #클래스로 만든 객체 > 인스턴스
        #위에서 정의한 a는 객체
        #그리고 a는 Cookie의 인스턴스
        
###사칙연산 클래스 만들기
'''클래스를 어떻게 만들지 먼저 구상하기
사칙연산을 하려면? > 두 숫자를 입력 받아야한다 > setdata 메서드 생성
더하기 기능은? > add메서드
빼기 기능은? > sub메서드
곱하기 기능은? > mul메서드
나누기 기능은? > div메서드

구상한 FourCal 클래스가 작동하려면?
a = FourCal()
a.setdata(x, y)
print(a.add())  #return x+y
print(a.sub())  #return x-y
print(a.mul())  #return x*y
print(a.div())  #return x/y
'''

#참고) 클래스 안에 구현된 함수 : 메서드(method)라고 부름
    #객체를 통해 클래스의 메서드를 호출할때 : 객체.메서드 > 도트(.)연산자를 사용해서 호출

class FourCal:
    # 사칙연산을 하려면? > 두 숫자를 입력 받아야한다 > setdata 메서드 생성
    def setdata(self, first, second):   #매개변수 self는 생성하는 객체 자신을 의미함
        #setdata를 호출하는 2가지 방법
        #a = FourCal()
        #a.setdata(4, 2)            #객체.메서드로 호출하는 경우 self는 반드시 생략해야함
        #FourCal.setdata(a, 4, 2)   #클래스.메서드로 호출하는 경우 첫 매개변수는 반드시 self로 전달해야함
        
        self.first = first      #a.first = 4 와 동일
        self.second = second    #a.second = 2 와 동일
        
    # 더하기 기능은? > add메서드
    def add(self):
        result = self.first + self.second
        return result
    
    # 빼기 기능은? > sub메서드
    def sub(self):
        result = self.first - self.second
        return result
        
    # 곱하기 기능은? > mul메서드
    def mul(self):
        result = self.first * self.second
        return result
    
    # 나누기 기능은? > div메서드
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)
    #이렇게 a객체에 first = 4, second = 2 / b객체에 first = 3, second = 8이 생성되는데
        #이렇듯이 객체에 생성되는 객체만의 변수를 객체변수라 함

a.add() #6
a.sub() #2
a.mul() #8
a.div() #2.0

b.add() #11
b.sub() #-5
b.mul() #24
b.div() #0.375

###생성자(Constructor) : 객체가 생성될 때 자동으로 호출되는 메서드
a = FourCal()
a.add()     #AttributeError: 'FourCal' object has no attribute 'first'
    #setdata안해서 오류 발생
        #이렇게 객체 초기값을 설정해야 할 필요가 있는경우
            #매번 함수를 통해 설정하는것 보다 생성자를 구현하는 것이 효율적
                #메서드 이름으로 __init__ 사용하면 생성자가 됨

class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
        
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()   #TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
#생성자 안써서 에러 발생
a = FourCal(4, 2)
print(a.first)
print(a.second)
a.add() #6
a.div() #2.0
    #이제 최초 생성시에 first, second지정가능 > setdata는 first, second 데이터 변경시에 사용
    
###클래스의 상속(Inheritance) : 어떤 클래스를 만들 때, 다른 클래스의 기능을 물려받을 수 있게 만드는 것
'''상속 기본구조
class 클래스명(상속받을클래스명)
'''
class MoreFourCal(FourCal): #이렇게만 해줘도 FourCal 클래스 기능 모두 이용 가능
    pass

a = MoreFourCal(4, 2)
a.add()
a.mul()
a.sub()
a.div()

#상속은 보통 기존클래스(FourCal)을 변경하지 않으면서
    #기능을 추가하거나, 기존 기능을 변경하고자 할때 사용
    #또 기존클래스가 라이브러리 형태로 제공되거나
        #수정이 허용되지 않는 경우도 있으므로 이럴때 사용하게 됨
        
class MoreFourCal(FourCal): #이제 사칙연산 + 제곱연산(pow메서드)까지 사용할 수 있음
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
a.pow()

###메서드 오버라이딩(Overriding, 덮어쓰기)
a = FourCal(4,0)
a.div() #ZeroDivisionError: division by zero 오류발생
    #0으로 나눌때 0을 리턴하고 싶을때

class SafeFourCal(FourCal):
    def div(self):  #기존클래스(FourCal)의 div함수를 상속받은 SafeFourCal에서 덮어씀
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
a = SafeFourCal(4, 0)
a.div() #0 에러 안남

###클래스 변수
'''클래스 변수 사용법
클래스명.클래스변수명
'''
class Family:
    lastname = '김'

print(Family.lastname)  #클래스 내부에서 정의한 변수를 불러서 사용함

#다른예시
a = Family()
b = Family()
print(a.lastname)   #김
print(b.lastname)   #김

Family.lastname = '박'  #클래스변수 김 > 박 으로 변경
print(a.lastname)   #박
print(b.lastname)   #박

id(Family.lastname) #1547979115616
id(a.lastname)      #1547979115616
id(b.lastname)      #1547979115616
#같은 주소(메모리)를 참조함

#####5-2 모듈 : 함수 / 변수 / 클래스를 모아놓은 파일 > .py를 따로 저장해야 아래 실습 가능
###모듈 만들기
#mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

###모듈 불러오기 : import 모듈명 or from 모듈명 import 함수명
    #모듈명은 .py 로 저장한 파일의 이름이 모듈명이 된다

'''모듈사용예시1 : import 모듈명 > 함수사용법 : 모듈명.함수명
mod1.py 를 저장
cmd > mod1.py저장경로 이동 ex) cd C:\doit > python
(cmd에서 파이썬 실행되었다고 가정)
>>> import mod1
>>> print(mod1.add(3,4))
7
>>> print(mod1.sub(4,2))
2
'''

'''모듈사용예시2 : from 모듈명 import 함수명 > 함수사용법 : 함수명
>>> from mod1 import add
>>> add(3,4)
7
'''

#모듈사용예시2는 add함수만 사용할수있음 > add, sub 모두 사용하고 싶다면?
'''모듈사용예시3 : from 모듈명 import 함수명들
from mod1 import add, sub   #콤마로 구분하여 필요한 함수들만 불러오기
from mod1 import *          #mod1 모듈 내 모든 함수 불러오기
'''

###if __name__=='__main__': 의 의미
#위에서 만든 모듈 mod1.py에 출력문을 추가
#mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

print(add(1,4)) #추가
print(sub(4,2)) #추가

#위 모듈(파일)을 직업 열어 작업을 수행할때는 문제 없지만,
    #다른 파일을 작업할때 위 모듈(mod1)을 import하여 수행하게되면
        #출력문(추가한 두 줄)이 수행되는 문제 발생
            #따라서 아래 추가한 출력문은 파일을 직접 작업할때만 수행하게 하고싶음
            
#mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__=='__main__':
    print(add(1,4)) #추가
    print(sub(4,2)) #추가
#if __name__=='__main__': 문으로 출력문을 감싸줌으로써 해결
    #__name__ : 파이썬 내부적인 특별변수, 현재 작업중인 파일의 __name__은 __main__이고,
        #현재 작업중인 파일에서 import mod1을 하면 불려온 모듈의 __name__은 모듈명이 됨
            #따라서 import한, mod1 == __name__ != '__main__'이 되어 출력문이 작동하지 않음

'''추가내용) __name__ 변수란?
파이썬의 __name__ 변수는 파이썬 내부적으로 사용하는 특별한 변수 이름이다.

만약 C:\doit\python mod1.py처럼 직접 mod1.py 파일을 실행할 경우
__name__변수에는 __main__값이 저장된다.

하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우
mod1.py의 __name__변수에는 mod1.py의 모듈이름값 mod1이 저장된다.
'''

###클래스나 변수 등을 포함한 모듈
#mod2.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r**2)
    
def add(a, b):
    return a+b

'''mod2.py 모듈 사용예시
>>> import mod2
>>> print(mod2.PI)
3.141592

>>> a = mod2.Math()
>>> print(a.solv(2))
12.566368

>>> print(mod2.add(mod2.PI, 4.4))
7.541592
'''

###mod2.py 모듈 사용해 반지름 5인 원의 넓이 계산
import mod2
a = mod2.Math()
print(a.solv(5))

###다른 파일 모듈 불러오기
#modtest.py
import mod2
result = mod2.add(3,4)
print(result)

###모듈을 불러오는 방법
'''cmd창
C:\Users>cd C:\doti
C:\doit>mkdir mymod
C:\doit>move mod2.py mymod

#1. sys.pathappend(모듈을 저장한 디렉토리) 사용
C:\doit>python
>>>import sys
>>>sys.path         #lib 이용가능한 경로
['', 'C:\\Windows\\... 쭉 경로들이 나옴]

>>>sys.path.append('C:\doit\mymod') #path경로 추가를 통한 모듈사용방법
>>>import mod2

#2.PYTHONPATH 환경 변수 사용
C:\doit>set PYTHONPATH=C:\doit\mymod
C:\doit>python
>>>import mod2
'''

###5-3 패키지 : 도트(.)를 사용해 파이썬 모듈을 계층적(폴더, 디렉토리구조)로 관리할 수 있게 해줌
    #모듈이름이 A.B인경우 A는 패키지명, B는 A패키지의 B모듈이 됨
'''ex)game 파이썬 패키지
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
'''

###패키지 만들기
#1. 패키지 기본 구성 요소 준비 
'''D:/doit 디렉토리 밑에 파일들 생성
D:\doit\game\__init__.py
D:\doit\game\sound\__init__.py
D:\doit\game\sound\echo.py
D:\doit\game\graphic\__init__.py
D:\doit\game\graphic\render.py
'''

#2. __init__.py는 만들어만 두고 비워둠
#3. echo.py
def echo_test():
    print('echo')

#4. render.py
def render_test():
    print('render')

#5. set PYTHONPATH=D:\doit 추가
'''cmd
C:\>set PYTHONPATH=D:\doit
C:\>python

에러나면 아래 방법으로
C:\>python
>>> import sys
>>> sys.path.append('D:\doit')
'''

#패키지 안 함수 실행(3가지 방법)
'''#1 echo 모듈 import
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
'''

'''#2 echo 모듈이 있는 디렉토리까지 from ... import
>>> from game.sound import echo
>>> echo.echo_test()
echo
'''

'''#3 echo 모듈 echo_test함수를 직접 import
>>> from game.sound.echo import echo_test
>>> echo_test()
echo
'''

#3가지 import는 결국 경로의 문제
    #어디까지 import를 할것이고, 명령어를 어디서부터 불러와야 하는지
'''
D:\doit\game\sound\echo\echo_test

위 경로에서 환경설정(PATH)으로 D:\doit 까지 접속
#1 : game\sound\echo\ 를 통째 import
    그래서 함수를 불러오기 위해 통째 명렁어 불러와야함
        game.sound.echo.echo_test()

#2 : from game\sound\ import echo로 사실상 echo만 import
    명령어도 echo 부터 불러옴
        echo.echo_test()
        
#3 : from game\sound\echo\ import echo_test로
    함수만 직접적으로 import
        echo_test()
'''    

#즉, 만약 import game만 했다면
    #game 디렉터리의 __init__.py 까지만 참조 할 수 있음(더 하위 디렉토리 참조 불가)
'''
>>> import sys
>>> sys.path.append('D:\doit')
>>> import game
>>> echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'echo_test' is not defined
>>> game.sound.echo.echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'game' has no attribute 'sound'
'''

#참고) import a.b.c 형태일때, c는 반드시 모듈 or 패키지 여야 한다

###__init__.py : 해당 디렉토리가 패키지의 일부임을 알려주는역할(python3.3 이전버전)
'''
>>> import sys
>>> sys.path
>>> sys.path.append('D:\doit')
>>> from game.sound import *
>>> echo.echo_test()    #NameError: name 'echo' is not defined
'''

#D:\doit\game\sound\__init__.py
__all__ = ['echo']  #sound디렉토리에서 import *을 할경우 echo 모듈을 import 한다는 의미
    #__all__에 적힌 모듈들이 from game.sound import *을 할때 import 가능한 모듈 목록이 되는것

'''
>>> from game.sound import *
>>> echo.echo_test()
echo
'''

###나혼자 코딩 : *을 사용해 render.py 파일 안 render_test 함수를 사용해볼것
#D:\doit\game\graphic\__init__.py
__all__ = ['render']

'''
>>> import sys
>>> sys.path
>>> sys.path.append('D:\doit')

>>> from game.graphic import *
>>> render.render_test()
render
'''

###relative 패키지
#만약 graphic 디렉토리 render.py 모듈이, sound디렉토리 echo.py모듈을 사용하고 싶다면?
    #render.py에 아래의 코드 삽입
    
#render.py
from game.sound.echo import echo_test
def render_test():
    print('render')
    echo_test()
    
'''경로 잡아두고
>>> import sys
>>> sys.path.append('D:\doit')

>>> from game.graphic.render import render_test
>>> render_test()
render
echo
'''

#위 처럼 정석적인 루트의 import도 가능하나, 아래처럼 relative import도 가능
    #단, relative import사용하려면 경로관계를 구체적으로 파악하고 있어야함
        #또한, 인터프리터 공간에서는 사용이 불가능하며
            #.py같이 모듈(작업페이지) 공간에서만 사용 가능하다
#render.py
from ..sound.echo import echo_test

def render_test():
    print('render')
    echo_test()
    
'''
>>> import sys
>>> sys.path.append('D:\doit')
>>> from game.graphic.render import render_test
>>> render_test()
render
echo    #정상작동 확인
'''
#인터프리터에서 relative import 사용시 에러출력(SystemError: cannot perform relative import)

#####5-4 예외처리
'''오류 종류
1. f = open('없는파일', 'r')
FileNotFoundError: [Errno 2] No such file or directory: '없는파일' #없는파일 열기시도

2. 4/0
ZeroDivisionError: division by zero #4는 0으로 나눌 수 없다

3. a=[1,2,3]
a[4]
IndexError: list index out of range #리스트 범위 초과

등 수도없이 다양한 오류 종류가 존재
'''

#오류 예외 처리 기법
'''try, except문 기본구조
try : 
    수행문
except [발생오류[as 오류메시지변수]:
    수행문
'''

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
    
#division by zero

try:
    a=[1,2,3]
    a[4]
except IndexError as e:
    print(e)
    
#try ... finally
    #finally절은 try문 수행시, 에러가 나더라도 반드시 수행시키는 명령(강제수행문)
    
#ex)
f = open('foo.txt', 'w')
try:
    f.write('123')
finally:
    f.close()
#f.close는 예외 발생여부와 무관하게 항상 수행
    #보통 finally절은 사용한 리소스를 close 할때 많이 사용
    
#여러개의 오류 처리
'''
try:
    ...
except 발생오류1:
    ...
except 발생오류2:
    ...
'''
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없음')
except IndexError:
    print('인덱싱 불가')

#인덱싱 불가    > IndexError가 먼저 발생하여 ZeroDivisionError는 발생하지 않음
#오류메시지 그대로 가져오기
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

    #아래처럼 함께 처리할 수도 있음
try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

###오류 회피 : 프로그래밍시, 특정 오류 발생해도 그냥 통과시켜야 할 때가 옴
try:
    f = open('없는파일', 'r')
except FileNotFoundError:   #찾는 파일이 없더라도
    pass                    #pass 시켜라

###오류 발생시키기 : 프로그래밍시, 특정 오류를 발생시키는 경우도 생김
#부모인 Bird 클래스 > 자식 Eagle 클래스, 반드시 fly 함수를 구현하도록 강제해야 하는 경우
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()     #NotImplementedError

#자식 클래스(Eagle)에서 fly함수를 사용하기 위해 에러를 처리해야함
    #Eagle 클래스에서 fly를 반드시 구현하게 강제됨
        #추가)상속받는 클래스에서 함수를 재구현하는것 : 메서드 오버라이딩
            #추가2) 부모클래스의 메서드를 자식클래스에서 재 정의
            
class Eagle(Bird):
    def fly(self):
        print('very fast')
        
eagle = Eagle()
eagle.fly()     #very fase

###예외 만들기 : 프로그램 수행중, 특수한 경우에만 예외처리를 하기위해 종종 예외를만들어서 사용함
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '욕설':
        raise MyError()
    print(nick)
    
say_nick('천사')    #천사
say_nick('욕설')    #__main__.MyError

#예외처리 기법으로 MyError 발생 예외처리
try:
    say_nick('천사')
    say_nick('욕설')
except MyError:
    print('비속어 사용 금지')
'''
천사
비속어 사용 금지
'''

#오류메시지를 활용하고 싶은경우 아래처럼 예외만들고 예외처리
#__str__메서드 : print(e)처럼 오류메시지를 print문으로 출력할 경우 호출되는 메서드
class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'
    
try:
    say_nick('천사')
    say_nick('욕설')
except MyError as e:
    print(e)
'''
천사
허용되지 않는 별명입니다.
'''

#####5-5 내장함수
abs(3) #절대값 리턴 함수

all([1,2,3])    #반복가능한(iterable) 자료형 중 모두 참이면 True 리턴, 하나라도 거짓이면 False
    #반복 가능한 자료형 : for문으로 값을 출력할 수 있는 것, 리스트, 튜플, 문자열, 딕셔너리, 집합 등
all([1,2,3,0])  #False

any([1,2,3])    #하나라도 참이면 True, 모두 거짓이면 False

#dir() : 객체의 자료형이 자체적으로 가지고 있는 변수와 함수를 보여줌
dir([1,2,3])
dir({'1':'a'})

divmod(a,b) #a를 b로 나눈 몫과 나머지를 튜플형태로 리턴
divmod(7,3) #(2, 1)

#enumerate : 열거하는 함수
    #순서가 있는 자료형(리스트, 튜플 문자열)을 입력받아 인덱스와 함께 리턴
    
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
'''
0 body
1 foo
2 bar
'''
#for문에 enumerate를 함께 사용시, 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있음
    #for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 유용
    
#eval(expression) : 실행가능한 문자열을 입력받아 실행결과값을 리턴
    #입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행할때 사용
eval('1+2')         #3
eval("'hi'+'a'")    #hia
eval('divmod(4,3)') #(1,1)

#filter(함수명, 좌측함수로차례로들어갈반복가능한자료형)
    #두번째 인수 자료형들을 첫번째 인수로 입력해 참인것만 묶어서 리턴

#positive.py
def positive(l):
    result = [] #반환값이 참인것만 걸러내 저장할 변수
    for i in l:
        if i > 0:
            result.append(i)    #리스트에 i 추가
    return result

print(positive([1, -3, 2, 0, -5, 6]))   #[1, 2, 6]
#위 positive함수는 양수를 걸러내는 함수
    #filter함수를 쓰면 아래처럼 간단히 구현가능
    
#filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6]))) #[1, 2, 6]

#람다를 쓰면 더 줄일수 있음
list(filter(lambda x: x>0, [1, -3, 2, 0, -5, 6]))   #[1, 2, 6]

#hex(x) : 16진수 변환
hex(234)    #'0xea'
hex(3)  #'0x3'

#id(object) : 객체 고유 주소값(레퍼런스) 리턴
a = 3
b = a
id(3)   #1853368658288
id(a)   #1853368658288
id(b)   #1853368658288

#input([prompt]) : 사용자의 입력을 받는 함수
a = input()
b = input('Enter : ')

#int(x) : 정수리턴
int(3.4)    #3

#int(x, radix) : radix진수로 표현된 문자열을 10진수로 변환&리턴
int('11', 2)    #3
int('1A', 16)   #26

#isinstance(object, class) : 인스턴스가 그 클래스의 인스턴스면 True, 아니면 False 리턴
class Person: 
    pass
a = Person()            #Person 클래스의 인스턴스 a 생성
isinstance(a, Person)   #True

b = 3
isinstance(b, Person)   #False

#len(s) : 입력값(s)의 길이(요소의 전체갯수) 리턴
len('python')   #6
len([1,2,3])    #3
len((1, 'a'))   #2

#list(s) : 반복 가능한 자료형 s를 입력받아 리스트화
list('python')  #['p', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3)) #[1, 2, 3]

a = [1, 2, 3]
b = list(a) #리스트를 리스트화하면, a리스트를 새로 복사하여 새로운 리스트로 만들어줌
b   #[1, 2, 3]  #id(a) != id(b)

#map(f, iterable) : 함수(f)와 반복가능한(iterable) 자료형을 입력받음
    #입력받은 자료형의 각 요소를 함수 f로 수행한 결과를 묶어서 돌려받음
#two_times.py
def two_times(numberList):  #2곱한 값 리턴
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)   #[2, 4, 6, 8]

#위 함수를 map을 사용하면
def two_times(x):
    return x*2

list(map(two_times, [1, 2, 3, 4]))  #[2, 4, 6, 8]

#람다를 사용하면
list(map(lambda a: a*2, [1, 2, 3, 4]))  #[2, 4, 6, 8]

#max(iterable) : 최대값 리턴
max([1, 2, 3])  #3
max('python')   #y

#min(iterable) : 최소값 리턴
min([1, 2, 3])  #1
min('python')   #h

#oct(x) : 8진수 변환
oct(34) #'0o42'
oct(12345) #'0o30071'

#open(파일명, [파일모드]) : 파일 열기, 파일모드 기본값 = 'r'
    #파일모드 : 'w', 'r', 'a', 'b'  #'b' : 바이너리 모드로 파일열기(w,r,a와 함께 사용)
f = open('binary_file', 'rb')

#ord(c) : 문자의 아스키 코드값 리턴 <> chr 함수와 반대기능
ord('a')    #97
ord('0')    #48

#pow(x, y)  #x의 y제곱값 리턴
pow(2, 4)   #16
pow(3, 3)   #27

#range([start,] stop [, step]) : 입력받은 숫자 범위, 반복 가능한 객체로 리턴
#인수가 하나인 경우
list(range(5))  #0부터 4까지    [0, 1, 2, 3, 4]

#인수가 2개일때
list(range(5, 10))  #5부터 9까지    [5, 6, 7, 8, 9]

#인수 3개
list(range(1, 10, 2))#1부터 10까지, 2step   [1, 3, 5, 7, 9]
list(range(0, -10, -1))#1부터 10까지, 2step   [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

#round(number[, ndigits]) : 반올림
round(4.6)  #5
round(4.2)  #4
round(5.678, 2)  #ndigits : 소숫점 이하 자릿수

#sorted(iterable) : 입력값 정렬 후 리턴
sorted([3, 1, 2])   #[1, 2, 3]
    #리스트 자료형 sort함수도 있지만, 이 함수는 리스트 객체 그 자체만 정렬할뿐, 리턴은 돌려주지 않음
    
#str(object) : 문자열 변환 리턴
str(3)  #'3'
str('hi')   #'hi'
str('hi'.upper())   #'HI'

#sum(iterable) : 입력받은 리스트나 튜플 요소의 합 리턴
sum([1, 2, 3])  #6
sum((4, 5, 6))  #15

#tuple(iterable) : 반복 가능 자료형 튜플형태로 리턴
tuple('abc')        #('a', 'b', 'c')
tuple([1, 2, 3])    #(1, 2, 3)
tuple((1, 2, 3))    #(1, 2, 3)

#type(object) : 입력한 object의 자료형 리턴
type('abc') #<class 'str'>
type([])    #<class 'list'>
type(open('test', 'w')) #<class '_io.TextIOWrapper'>

#zip(*iterable) : 동일한 개수로 이루어진 자료형을 묶어줌
    #*iterable : 반복 가능한 자료형 여러개를 입력할 수 있다는 의미
    
list(zip([1, 2, 3], [4, 5, 6])) #[(1, 4), (2, 5), (3, 6)]

list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))  #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip('abc', 'def')) #[('a', 'd'), ('b', 'e'), ('c', 'f')]

####5-6 라이브러리
###sys : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

##sys.argv : 명령행에서 인수 전달
#C:/User/home>python test.py abc pey guido

#C:\doit\Mymod 디렉토리에 argv_test.py 저장
#argv_test.py
import sys
print(sys.argv)

#C:\doit\Mymod>python argv_test.py you need python
#['argv_test.py', 'you', 'need', 'python']
    #공백 기준으로 python 뒤 모든 요소가 sys.argv 리스트의 요소가 됨
    
##sys.exit : 강제 스크립트 종료
sys.exit()  #Ctrl+z, Ctrl+D처럼 인터프린터 종료하는 역할

##sys.path : 모듈 경로지정
import sys
sys.path

#path_append.py
import sys
sys.path.append('.py모듈지정할경로')
#sys.path.append(r'C:\doit\Mymod')

###pickle : 객체의 형태를 그대로 유지하면서, 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
f = open('test.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)
#{1: 'python', 2: 'you need'}
f.close()

###os : 환경변수, 디렉토리, 파일 등 os자원을 제어 모듈

##os.environ : 내 시스템 환경 변수 값 알고싶을때
import os
os.environ          #내 환경정보 딕셔너리 형태로 제공
os.environ['PATH']  #PATH의 Value 조회

##os.chdir('경로') : 디렉토리 위치 변경
os.chdir(r'C:\WINDOWS')

##os.getcwd() : 현재 디렉토리 위치 리턴
os.getcwd()

##os.system('명령어') : 시스템 명령어 호출
os.system('dir')

##os.popen('명령어') : 시스템 명령어 실행한 결과값, 읽기 모드형태 파일객체로 리턴
f = os.popen('dir')
print(f.read())

'''기타 유용한 os 관련 함수
os.mkdir(디렉토리) : 디렉토리 생성
os.rmdir(디렉토리) : 디렉토리 삭제_디렉토리 비어있어야 가능
os.unlink(파일명) : 파일 삭제
os.rename(scr, dst) : src라는 파일명을 dst라는 이름으로 변경
'''

###shutil : 파일 복사 모듈
import shutil
shutil.copy('src.txt', 'dst.txt')   #src.txt가 복사 > dst.txt이름으로 저장

###glob : 특정 디렉토리 내, 파일명 전체 리턴
##glob(pathname) : 디렉토리 내 파일들 리스트화
import glob
glob.glob(r'C:\doit\mark*') #C, doit폴더 mark로 시작하는 모든폴더명 리스트화

###tempfile : 파일 임시 생성 모듈
##tempfile.mkstemp() : 중복되지 않는 임시파일의 이름 무작위 생성 및 리턴
import tempfile
filename = tempfile.mkstemp()
filename    #(3, 'C:\\Users\\Mok\\AppData\\Local\\Temp\\tmpebe450wl')

##tempfile.TemporaryFile() : 임시저장공간으로 사용할 파일 객체 리턴
import tempfile
f = tempfile.TemporaryFile()    #기본적으로 wb(바이너리 쓰기모드) 생성
f.close()                       #close하면 임시생성파일 자동 삭제됨

###time : 시간 관련 모듈
##time.time() : UTC 1970년 1월 1일 기준, 지난 시간을 초단위로 리턴
import time
time.time() #1656309432.4520116

#time.localtime() : time.time()으로 받은 현재시간 값을 년,월,일,시,분,초로 쪼개 튜플로 리턴
time.localtime(time.time())
#time.struct_time(tm_year=2022, tm_mon=6, tm_mday=27, tm_hour=14, tm_min=58, tm_sec=31, tm_wday=0, tm_yday=178, tm_isdst=0)

##time.asctime() : time.localtime 리턴값을 받아 날짜와 시간 형태로 리턴
time.asctime(time.localtime(time.time()))   #'Mon Jun 27 15:00:19 2022'

##time.ctime
time.ctime()    #위 내용을 간단히 만든 함수, 현재시간만을 리턴함

##time.strftime('출력할형식포맷코드', time.localtime(time.time()))
'''strftime : 시간관련 여러 포맷코드 제공
포맷코드    설명            예시
%a          요일 줄임말     Mon
%A          요일            Monday
%b          달 줄임말       Jan
%B          달              January
%c          날짜와 시간출력 'Mon Jun 27 15:09:34 2022'
%d          날(day)         [01,31]
%H          시간(hour):24H  [00,23]
%I          시간(hout):12H  [01,12]
%j          1년중누적날짜   [001,366]
%m          달              [01,12]
%M          분              [01,59]
%p          AM or PM        AM
%S          초              [00,59]
%U          1년중누적주     [00,53]     일요일 시작 기준
%w          숫자로 된 요일  [0(일요일),6]
%W          1년중누적주     [00,53]     월요일 시작 기준
%x          날짜출력        [06/01/01]  현재 설정지역 기반
%X          시간출력        [17:22:21]  현재 설정지역 기반
%Y          연도 출력       2001
%Z          시간대출력      대한민국 표준시
%%          문자            %
%y          두자리연도출력   01
'''
#time.strftime 사용 예시
import time
time.strftime('%x', time.localtime(time.time()))    #'06/27/22'
time.strftime('%c', time.localtime(time.time()))    #'Mon Jun 27 15:09:34 2022'

##time.sleep(초) : 루프에 일정시간간격 텀 주기
#sleep1.py
import time
for i in range(10):
    print(i)
    time.sleep(1)
    
###calendar : 달력 모듈
##calendar.calendar(연도) : 그해 전체 달력
import calendar
print(calendar.calendar(2022))

##calendar.prcal(연도)도 위와 동일한 결과
calendar.prcal(2022)

'''
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31
'''

##calendar.prmonth(년도, 월) : 특정년도 특정월 달력출력
calendar.prmonth(2022, 7)
'''
     July 2022
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
'''

#calendar.weekday(연도, 월, 일) : 해당일자 요일정보 리턴 / 0:월, 1:화, ... 6:일
calendar.weekday(2022, 6, 27)

##calendar.monthrange(연도, 월) : 해당 월의 1일이 무슨요일인지 & 며칠까지 있는지 리턴
calendar.monthrange(2022, 7)    #(4, 31) 2022년 7월 1일은 금(4)요일, 7월은 31일까지 있음

    #.weekday와 .monthrange는 프로그래밍에 매우 유용하게 활용되니 참고

###random : 난수 발생 모듈
import random
random.random() #0.17959364435064484    0.0~1.0 실수값 난수 리턴

random.randint(1, 10)   #6              1~10 정수값 난수 리턴
random.randint(1, 55)   #49             1~55 정수값 난수 리턴

#random_pop.py : 데이터 랜덤 추출
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

#random_pop은 아래처럼 조금 더 직관적으로도 만들 수 있음
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)    #리스트 무작위 섞기
data

###webbrowser : 기본브라우저로 url 새창 작동
import webbrowser
webbrowser.open('http://google.com')
webbrowser.open_new('http://google.com')

###threading : 스레드를 다루는 모듈
    #컴퓨터 동작 프로그램을 프로세스(Process)라고 함
        #보통 1개의 프로세스는 한가지 일만 할 수 있음
            #쓰레드를 사용하면 한 프로세스 내에서 2가지 이상의 일을 동시 수행할 수 있음
            
#thread_test.py
import time

def long_task():    #0~4를 반복 출력
    for i in range(5):
        time.sleep(1)
        print(f'working:{i}\n')
        
print('start')
for i in range(5):  #위 작업을 5번 돌림 > 총 25초 소요
    long_task()
    
print('End')

#thread_test.py (수정)
import time
import threading    #쓰레드 생성 위해 threading 모듈 사용

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f'working:{i}\n')
print('Start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  #쓰레드 생성
    threads.append(t)
    
for t in threads:   #쓰레드 실행
    t.start()
    
print('End')
#쓰레드 5개가 동시 작업되어 작업시간은 5초로 단축되었으나, start동작 후 end가 먼저나옴
    #프로그램 정상작동 아니니 다시한번 수정해보자
    
#threat_test.py(수정2)
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f'working:{i}\n')

print('Start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()        #join으로 쓰레드 종료시 까지 대기
    
print('End')

#쓰레드 join함수는 해당 스레드가 종료될때까지 기다리게 함
    #우리가 원하는 결과인지 확인 해보자
    
#####연습문제
#q1
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val
        
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)    #10-7이 되도록 UpgrageCalculator 클래스 정의해볼것

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

#q2
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)    #100출력

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100 : self.value = 100

#q3
all([1, 2, abs(-3)-3])  #False  all : 모두 참이면 Trye, 하나라도 거짓이면 False
chr(ord('a')) == 'a'    #True   chr 아스키 > 문자 / ord 문자 > 아스키코드

#4 filter와 lambda를 사용, [1, -2, 3, -5, 8, -3] 음수 모두 제거
list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3]))

#5
hex(234)    #'0xea'
int('0xea', 16) #234

#6
list(map(lambda x: x*3, [1, 2, 3, 4]))  #[3, 6, 9, 12]

#7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
max(a) + min(a)

#8
17/3
round(17/3, 4)

#9 모르겠는데?
'''
C:\>cd doit
C:\doit>python myargv.py 1 2 3 4 5 6 7 8 9 10
'''
import sys
numbers = sys.argv[1:]  #파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)


#10
import os
os.getcwd()
os.chdir(r'C:\doit')

result = os.popen('dir')
print(result.read())

#q11
import glob
glob.glob(r'C:\doit\*.py')

#q12
import time
time.strftime('%Y/%m/%d %H:%M:%S')  #'2022/06/27 16:41:48'
#time.strftime('%c', time.localtime(time.time()))   #'Mon Jun 27 16:41:56 2022'

#q13
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
print(result)

'''
lotto = list(range(1, 46))
lotto_list = []
for i in range(6):
    a = random.choice(lotto)
    lotto_list.append(a)
    lotto.remove(a)
    
print(lotto_list)
'''

#######프로그래밍 : 프로그램을 만들려면 가장 먼저 '입력'과 '출력'을 생각할 것.
#####6-1 구구단 2단 만들기
'''구구단 2단 구상
1.함수 이름? gugu
2.입력받는값? 2
3.출력하는 값? 2단(2,4,...,18)
4.결과값 형태?연속된 자료형 - 리스트
'''
#result = gugu(2)    #1,2
#result = [2, 4, 6, 8, 10, 12, 14, 16, 18]   #3,4

def gugu(n):
    #print(n)
    result = []
#     result.append(n*1)
#     result.append(n*2)
#     result.append(n*3)
#     result.append(n*4)
#     result.append(n*5)
#     result.append(n*6)
#     result.append(n*7)
#     result.append(n*8)
#     result.append(n*9)
#     너무 길다 줄여보자
    i = 1
    while i < 10:
        #print(i)
        result.append(n * i)
        i += 1
    
    return result
print(gugu(2))  #[2, 4, 6, 8, 10, 12, 14, 16, 18]

#####6-2 3과 5의 배수 합하기
'''다음 프로그래밍 구상해보자
10 미만의 자연수에서 3과 5의 배수를 구하면, 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3과 5의 배수 총합을 구해보자

1. 입력받는값? 1~999(1000미만의 자연수)
2. 출력하는값? 3의 배수 & 5의 배수
3. 생각해볼것은?
    3-1 3의 배수와 5의 배수 어떻게 찾을지
    3-2 겹칠때는 어쩌지
'''

#1. 입력받는값? 1~999(1000미만의 자연수)
n = 1
while n < 1000:
    print(n)
    n += 1
    
#또는
for n in range(1, 1000):
    print(n)
    
#2. 출력하는 값
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)

#코딩 연습 사이트 : 프로젝트 오일러
#projecteuler.net/archives

#####6-3 게시판 페이징
'''
함수명 : getTotalPgae
인풋 : 게시물 총 건수(m), 한페이지 보여줄 게시물 수(n)
아웃풋 : 총 페이지 수
'''

#총 페이지 수 = (총 게시물 수 / 한 페이지당 노출 건수) + 1
def getTotalPage(m, n):
    return m // n + 1

print(getTotalPage(5, 10))  #1
print(getTotalPage(15, 10)) #2
print(getTotalPage(25, 10)) #3
print(getTotalPage(30, 10)) #4  3이 나와야 함

def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1
    
print(getTotalPage(5, 10))  #1
print(getTotalPage(15, 10)) #2
print(getTotalPage(25, 10)) #3
print(getTotalPage(30, 10)) #3

###6-4 간단한 메모장
'''
필요한 기능 : 메모추가, 메모조회
인풋 : 메모 내용, 프로그램 실행 옵션
아웃풋 : memo.txt

python memo.py -a 'Life is too short'
위 명령어를 쳤을때 메모를 추가 할 수 있도록 만들어볼것
'''

#D:\doit\memo.py
import sys

option = sys.argv[1]
memo = sys.argv[2]
#sys.argv : 실행시, 입력된 값을 읽어들이는 파이썬 라이브러리
    #sys.argv[0]은 python제외, 입력받은 값 중 가장 앞(memo.py, 파일명)을 의미함
    #sys.argv[1] : -a
    #sys.argv[2] : 'Life is too short'
    

print(option)
print(memo)

'''test
PS D:\doit> python memo.py -a 'Life is too short'
-a
Life is too short
'''

#D:\doit\memo.py -a 기능 담기
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
    
'''
PS D:\doit> python memo.py -a 'Life is too short'
PS D:\doit> python memo.py -a 'You need python'
PS D:\doit> type memo.txt 
Life is too short
You need python
'''

#D:\doit\memo.py -v 기능 추가
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
    
'''
PS D:\doit> python memo.py -v
Life is too short
You need python

'''

#####6-5 탭 > 공백4개 로 바꾸기
'''
필요기능 : 문서 파일 읽기, 문자열 변경
입력 : 탭을 포함한 문서파일
출력 : 탭이 공백으로 수정된 문서파일

python tabto4.py src dst
tabto4 : 파일명
src : 탭을 포함한 원본파일
dst : 공백 4개 변환 파일
'''

#D:\doit\tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)
'''
PS D:\doit> python tabto4.py a.txt b.txt
a.txt
b.txt
'''

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t', ' '*4)
print(space_content)

f = open(dst, 'w')
f.write(space_content)
f.close()

#####6-6 하위 디렉토리 검색
#D:\doit\sub_dir_search.py
import os

def search(dirname):
    #print(dirname)
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)
    
search('D:/')
'''python sub_dir_search.py
D드라이브 전체 폴더명 출력됨
'''

#하위디렉토리 .py 만 출력하도록 변경해보자
#D:\doit\sub_dir_search.py
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):    #현재 경로에 폴더가 있으면
                search(full_filename)           #해당 폴더로 search 재귀함수 호출
            else:
                ext = os.path.splitext(full_filename)[-1]   #확장자 추출
                if ext == '.py':
                    print(full_filename)
    except PermissionError: #권한없는 폴더 접근불가능하면 패스
        pass    
    
search('D:/')


###os.walk : 하위 디렉토리 쉽게 검색
import os

for (path, dir, files) in os.walk('D:/'):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print(f'{path}/{filename}')
            
#디렉토리와 파일을 검색하는 일반적인 경우라면 os.walk 사용을 추천

#######정규표현식(Regular Expressions)
#####7-1 정규표현식 살펴보기
#주민등록번호 포함하는 텍스트 > 주민등록번호 뒷자리 *로 변경할때
'''정규식을 모른다면
1. 전체 텍스트 공백 기준 split
2. 주민등록번호 형식 찾기
3. 뒷자리 *로 변환
4. 나뉜 단어 다시 조합
'''

data = '''
park 800905-1049118
kim 700905-1059119
'''

result = []
for line in data.split('\n'):   #줄바꿈 기준 split
    word_result = []
    for word in line.split(" "):    #공백 기준 split
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():   #주민등록번호 형식 검사
            word = word[:6] + '-' + '*******'   #조건 맞으면 뒷자리 *로
        word_result.append(word)    #바꾼문자 삽입
    result.append(' '.join(word_result))    #공백 기준 split 원복
print('\n'.join(result))    #줄바꿈 기준 split 원복

#정규표현식으로 하면 아래와같이 구현가능
import re

data = '''
park 800905-1049118
kim 700905-1059119
'''

pat = re.compile('(\d{6})[-]\d{7}')
print(pat.sub('\g<1>-*******', data))

#####7-2 정규 표현식 시작하기
###정규 표현식의 기초 - 메타 문자(meta characters)
    #메타문자 : . ^ $ * + ? {} [] \ | ()

##문자 클래스 : []
    #문자클래스 정규식은 [] 사이의 문자들과 매치 라는 의미
        #문자 클래스를 만드는 메타문자 대괄호[] 안에는 어떤 문자도 들어갈 수 있음
            #ex) [abc] : a,b,c 중 한 개의 문자와 매치 라는 의미

'''예시 : a, before, dude가 정규식 [abc]와 어떻게 매치되는지
정규식  문자열  매치여부    설명
        a       Y         'a'는 정규식 [abc]의 a와 매치
[abc]   before  Y         'before'은 정규식 [abc]의 b와 매치
        dude    N         'dude'는 정규식에 매치되는 문자 없음
'''

#[]안에서 두 문자 사이에 하이픈(-)을 사용하면, 두 문자 사이의 범위(From-To)를 의미
    #ex) [a-c] == [abc], [0-5] == [012345]
    #[a-zA-Z] : 알파벳 모두
    #[0-9] : 숫자
    #[^0-9] : 숫자가 아닌 문자 모두, [^...]은 not의 의미를 지님
        #^가 대괄호[] 안에 있을때는 not의 의미를 지니지만
            #일반 문자열'' 에 있을때는 문자열 또는 줄의 시작을 지정하는 의미
                #ex) '^abc'라면 abc로 시작하는 문자열과 매치
            #추가) $는 문자열 또는 줄의 끝을 지정
                #ex) 'abc$'라면 abc로 끝나는 문자열과 매치

'''자주 사용하는 문자 클래스
RE  설명
\d  숫자와 매치, [0-9]와 동일 표현식
\D  숫자 아닌것과 매치, [^0-9]와 동일 표현식
\s  whitespace(space, tab)와 매치, [ \t\n\r\f\v]와 동일 표현식. 맨 앞의 빈칸은 공백문자(space)를 의미한다
\S  not whitespace와 매치, [^ \t\n\r\f\v]와 동일 표현식
\w  문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일 표현식
\W  not 문자+숫자(alphanumeric)와 매치, [^a-zA-Z0-9_]와 동일 표현식

즉, 대문자는 소문자의 반대의미를 지님
'''

##.(Dot) : 정규 표현식의 메타문자 .은 줄바꿈문자(\n)을 제외한 모든 문자와 매치
    #re.DOTALL 옵션을 주면 \n와도 매치
    
a.b #a와 b사이에 줄바꿈을 제외한 어떤 문자와도 매치 : "a + 모든문자 + b"
'''예시 : aab, a0b, abc가 정규식 a.b와 어떻게 매치되는지
정규식  문자열  매치여부    설명
        aab     Y         'aab'의 가운데 a가 .과 매치
a.b     a0b     Y         'a0b'의 가운데 0과 .이 매치
        abc     N         'abc'는 a와 b사이에 문자가 없어서 매치X
'''

#a[.]b   #a와 b사이 문자그대로의 .이 있으면 매치 : "a + . + b"
    #'a.b'와는 매치, 'a0b'와는 매치X

##반복 : *
ca*t    # *바로앞 문자(a)가 0번이상 반복되면 매치됨(a가 없어도 매치된다는 의미) : "c + a*(0~무한대) + t"
            #무한대라고는 하지만 사실 메모리 제한으로 2억개 정도까지 가능하다고 함
'''예시 : ct, cat, caaat가 정규식 ca*t와 어떻게 매치되는지
정규식  문자열  매치여부    설명
        ct      Y         c와 t사이에 a가 0번 반복되며 매치
ca*t    cat     Y         c와 t사이에 a가 0번 이상 반복되며 매치(1회)
        caaat   Y         c와 t사이에 a가 0번 이상 반복되며 매치(3회)
'''

##반복 : + (+는 최소 1번 이상 반복될때 사용 <> *은 0번 이상)
ca+t    # +바로앞 문자(a)가 1번이상 반복되면 매치 : "c + a(1번 이상 반복) +t"
'''예시 : ct, cat, caaat가 정규식 ca+t와 어떻게 매치되는지
정규식  문자열  매치여부    설명
        ct      N         c와 t사이에 a가 0번 반복되며 매치X
ca+t    cat     Y         c와 t사이에 a가 0번 이상 반복되며 매치(1회)
        caaat   Y         c와 t사이에 a가 0번 이상 반복되며 매치(3회)
'''

##반복 : {m, n} : 반복횟수 제한할때
#{m} #바로앞 문자가 m회 반복되면 매치
#{m,}    #바로앞 문자가 m회 이상 반복되면 매치
            #{0,} == *, {1,} == +과 같아지게 됨
    
#ca{2}t  #'c + a(2번만 반복시 매치) + t'
    #caat과 매치, cat과는 매치X

#{m,n}   #바로앞 문자가 m~n회 반복시 매치
#ca{2,5}t    #caat 매치, caaaaat 매치, cat 매치X : "c + a(2~5회) + t"

##반복과 유사한 개념 : ? == {0, 1}
#ab?c    #b가 0~1번 사용되면 매치 : "a + b(0~1회) + c"
    #abc 매치, ac 매치
    
###re 모듈 : 파이썬에서 정규 표현식 지원 모듈
import re
p = re.compile('ab*')   #패턴 : 정규식을 컴파일한 결과

###정규식을 사용한 문자열 검색
    #컴파일 한 패턴 객체를 사용, 문자열 검색 수행
        #컴파일 한 패턴 객체는 아래 4가지 메서드 제공
'''패턴 객체 제공 메서드(4가지)
메서드      목적
match()     문자열의 처음부터 정규식과 매치여부 조사
search()    문자열 전체 검색, 정규식과 매치여부 조사
findall()   정규식과 매치되는 모든 문자열(substring) 리스트로 리턴
finditer()  정규식과 매치되는 모든 문자열(substring) 반복 가능 객체로 리턴
'''


#match : 문자열의 처음부터 정규식과 매치되는지 조사, match 객체 리턴
import re
p = re.compile('[a-z]+')

m = p.match('python')
print(m)    #<re.Match object; span=(0, 6), match='python'>

m = p.match('3 python') #처음에 나오는문자가 3이므로, 매치X, None리턴
print(m)    #None

    #match의 결과로 match객체 또는 None을 리턴받으므로, 보통 아래와 같이 코딩함
p = re.compile(정규표현식)
m = p.match('조사할문자열')
if m:
    print('Match found: ', m.group())
else:
    print('No match')

        #match의 결과값이 있을때만 다음 작업을 수행하겠다는 의미

##search : 문자열 전체 검색
import re
p = re.compile('[a-z]+')

m = p.search('python')
print(m)    #<re.Match object; span=(0, 6), match='python'>
    #여기까지는 match와 search가 동일하게 동작

m = p.search('3 python')
print(m)    #<re.Match object; span=(2, 8), match='python'>
    #match는 맨 처음부터 맞지 않으면 매치되지 않지만
        #search는 문자열 전체를 검색하므로 매칭에 성공함
        
##findall : 정규식과 매치되는 문자열의 모든 단어 리스트화
import re
p = re.compile('[a-z]+')

result = p.findall('life is too short') 
print(result)   #['life', 'is', 'too', 'short']

result = p.match('life is too short')   #<re.Match object; span=(0, 4), match='life'>
result = p.search('life is too short')  #<re.Match object; span=(0, 4), match='life'>

##finditer : findall과 동일하게 정규식과 매치되는 모든 문자열을 리턴하지만,
    #각 요소를 반복가능한객체(iterator object), match객체로 리턴
import re
p = re.compile('[a-z]+')

result = p.finditer('life is too short') 
print(result)   #<callable_iterator object at 0x0000026E03214FA0>
for r in result:
    print(r)
'''
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
'''

###match 객체의 메서드
    #re 컴파일 > 패턴 > match, search(, finditer?) > match 객체
        #match 객체 사용법 : match객체 메서드
        
'''match 객체 메서드
메서드      목적
group()     매치된 문자열을 리턴
start()     매치된 문자열의 시작인덱스 리턴
end()       매치된 문자열의 끝인덱스+1 리턴
span()      매치된 문자열의 (시작, 끝) 인덱스 튜플형태로 리턴
'''

import re
p = re.compile('[a-z]+')
m = p.match('python')
m.group()   #'python'
m.start()   #0
m.end()     #6
m.span()    #(0, 6)

#search로 '3 python을 검색했다면?
m = p.search('3 python')
m.group()   #'python'
m.start()   #2
m.end()     #8
m.span()    #(2, 8)

###모듈 단위 수행
    #지금까지는 패턴화 > 매치를 사용했으나, re모듈을 통해 축약가능
p = re.compile('[a-z]+')
m = p.match('python')

#아래 한줄로, 컴파일 & match메서드 한번에 수행 가능
m = re.match('[a-z]+', 'python')

    #한번 만든 패턴 객체를 여러번 사용할때, re.compile을 사용하는게 편함
    
###컴파일 옵션
'''정규식 컴파일 사용시, 다음 옵션 사용 가능
옵션명      약어    설명
DOTALL      S       .(dot문자)가 줄바꿈을 포함한 모든 문자와 매치
IGNORECASE  I       대/소문자 무시 매치
MULTILINE   M       여러줄 매치(^,$ 메타문자 사용시 관계있는 옵션)
VERBOSE     X       verbose모드 사용(정규식을 보기 편하게 하거나, 주석 사용 등)

옵션사용시, re.DOTALL or re.S 모두 가능
'''
##DOTALL, S : 여러줄로 이루어진 문자열에서 줄바꿈 상관없이 검색할 때 주로 사용
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)    #None

    #컴파일 옵션 사용
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)    #<re.Match object; span=(0, 3), match='a\nb'>

##IGNORECASE, I : 대소문자 무시하고 정규식 적용시킬때
p = re.compile('[a-z]', re.I) #[a-z]는 소문자만을 의미하지만, re.I가 대/소문자를 무시하게 함
p.match('python')   #<re.Match object; span=(0, 1), match='p'>
p.match('Python')   #<re.Match object; span=(0, 1), match='P'>
p.match('PYTHON')   #<re.Match object; span=(0, 1), match='P'>

##MULTILINE, M : 길고 줄바꿈 있는 문자열일때, 각 줄의 시작 또는 끝을 지정해 문자열을 뽑아내고 싶을때
    #^는 문자열의 시작 지정을 의미
        #ex)정규식이 '^python' 인경우 문자열의 처음은 항상 python으로 시작해야 매치
    #$는 문자열의 마지막 지정을 의미
        #ex)정규식이 'python$' 인경우 문자열의 마지막이 python으로 끝나야 매치
        
import re
p = re.compile('^python\s\w+')  #'python으로 시작, 그 뒤에 공백, 그 뒤에 단어'와 매치

data = '''python one
life is too short
python two
you need python
python three'''

print(p.findall(data))  #['python one']
#이렇게하면 문자열 첫줄만 매칭됨
    #각 라인의 처음을 인식하고 싶은 경우에 MULTILINE 옵션 사용
    
import re
p = re.compile('^python\s\w+', re.MULTILINE)

data = '''python one
life is too short
python two
you need python
python three'''

print(p.findall(data))  #['python one', 'python two', 'python three']

##VERBOSE, X : 정규식을 주석 또는 줄 단위로 구분할 수 있도록
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')    #의미 알아보기 어려움

charref = re.compile(r'''
                     &[#]               #Start of a numeric entity reference
                     (
                         0[0-7]+        #Octal form
                        | [0-9]+        #Decimal form
                        | x[0-9a-fA-F]+ #Hexadecimal form
                     )
                     ;                  #Trailing semicolon
                     ''', re.VERBOSE)
#re.VERBOSE옵션을 사용하면, 컴파일 시 공백이 제거됨
    #(보이기만 이렇게 보이고 사실상 위와 동일하게 컴파일 된다는 의미)
#줄 단위 주석문도 가능

###백슬래시 문제
    #'\section' 문자열을 찾는 정규식을 만든다면, \s가 whitespace로 인식됨
        #[ \t\n\r\f\v]ection 으로 인식됨
    
    #의도대로 매치하기 위해 \\section으로 써주어야 함
p = re.compile('\\section')
    #그런데 위처럼 만들면, 컴파일 시 파이썬 문자열 리터럴 규칙에 따라 \\section > \section으로 전달됨
        #결국 '\\\\section' 으로 넣어줘야 함
            #위 문제는 파이썬에서만 발생하는문제, 유닉스의 grep, vi등에서는 발생하지 않음
p = re.compile('\\\\section')
            
#그래서 파이썬 정규식에 Raw String 규칙이 생겨남
p = re.compile(r'\\section')


#####7-3 정규 표현식
###메타 문자
    #이미 살펴본 +, *, [], {} 등의 메타문자는 매치와 동시에 소비됨
    #문자열 소비가 없는(zero-width assertions) 메타문자 살펴보자
    
## | : or와 동일한 의미
    #A|B : A or B 라는 의미
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)    #<re.Match object; span=(0, 4), match='Crow'>

## ^ : 문자열 맨 처음과 일치함을 의미
print(re.search('^Life', 'Life is too short'))
#<re.Match object; span=(0, 4), match='Life'>

print(re.search('^Life', 'It\'s My Life'))  #Life가 맨 앞에 없으면 매치되지 않음
#None

## $ : 문자열의 맨 끝과 일치함을 의미(^와 반대)
print(re.search('short$', 'Life is too short'))
#<re.Match object; span=(12, 17), match='short'>

print(re.search('short$', 'Life is too short, you need python'))
#None

## \A : 문자열의 처음과 매치됨의미
    # ^와 동일한 의미이나, re.MULTILINE옵션 적용시에도 \A는 문자열의 처음에만 적용됨(^는 각 줄마다 적용되는 점과 차이남)

## \Z : 문자열의 끝과 매치
    # $와 동일하나, re.MULTILINE에도 문자열의 끝에만 적용($는 각줄 끝에도 적용됨과 차이)

## \b : 단어구분자(Word boundary), 보통 단어는 whitespace에 의해 구분됨
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  #<re.Match object; span=(3, 8), match='class'>

print(p.search('the declassified algorithm'))   #None
print(p.search('one subclass is'))   #None
    #위 문자열들에도 class는 있지만, 공백 구분되지 않아 매치X
    
## \B : \b의 반대경우, 즉 whitespace로 구분된 단어가 아닌 경우 매치
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  #None

print(p.search('the declassified algorithm'))   #<re.Match object; span=(6, 11), match='class'>
print(p.search('one subclass is'))   #None


###그루핑(Grouping) : 특정 문자열 반복여부 검색 정규식
    #그룹을 묶어주는 메타문자 : ()
        #ex) (ABC)+
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)    #<re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group(0))   #ABCABCABC

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')    #문자&숫자+공백+숫자+[-]숫자+[-]숫자
    #'이름 + " " + 전화번호' 형태의 문자열을 찾는 정규식
m = p.search('park 010-1234-1234')    

    #이름만 뽑아내고 싶다면?
p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')  # \w+ 를 ()로 group
m = p.search('park 010-1234-1234')
print(m.group(1))   #park

'''match객체.group(인덱스) 메서드
group(인덱스)   설명
group(0)        매치된 전체 문자열
group(1)        첫번째 그룹에 해당하는 문자열
group(2)        두번째 그룹에 해당하는 문자열
group(n)        n번째 그룹에 해당하는 문자열

그룹 인덱스 순서는 바깥쪽 ()부터 인덱싱
'''
    #전화번호도 group화 해보자
p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')  # \d+[-]\d+[-]\d+를 ()로 group
m = p.search('park 010-1234-1234')
print(m.group(2))   #010-1234-1234
    
    #국번(번호중 맨 앞자리)만 추가 group 해보자
p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')  # \d+를 ()로 group
m = p.search('park 010-1234-1234')
print(m.group(3))   #010
    
##그루핑된 문자열 재참조(Backreferences)
p = re.compile(r'(\b\w+)\s+\1') #'(그룹) + " " + 그룹과동일한단어' 와 매치, 잘 모르겠네
    # \1 : group(1)을 재참조 하게 해주는 메타문자
        # \2를 쓰면 group(2)를 재참조함

p.search('Paris in the the spring') #<re.Match object; span=(9, 16), match='the the'>

### ?P<그룹명> : 그루핑 네이밍(그루핑된 문자열에 이름 붙이기)
    #정규식 내부 그룹이 10개가 넘어가고, 정규식이 추가 삭제되면 인덱스로 프로그램을 다루기 혼란스러워짐
        #그룹을 인덱스가 아닌 이름으로 참조할 수 있다면, 그룹인덱스가 바뀌어도 데이터 무결성 등의 문제 해결가능

p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print(m.group('name'))  #park

#위에서 \1로 사용한 재참조도 가능
    # ?P=그룹명 : 그루핑 네이밍 재참조
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group() #the the

###전방탐색(Lookahead Assertions) 확장구문
'''전방탐색
정규식      종류            설명
(?=...)     긍정전방탐색    ...에 해당하는 정규식과 매치 & 조건 통과시에도 문자열 소비하지 않음
(?!...)     부정전방탐색    ...에 해당하는 정규식과 매치X & 조건 통과시에도 문자열 소비하지 않음
'''

##긍정형 전방 탐색
p = re.compile('.+:')
m = p.search('http://google.com')
print(m.group())    #http:

#http만 출력하고 싶다면?, 그루핑도 할수 없다면?
#긍정형 전방 탐색 사용    
p = re.compile('.+(?=:)')
m = p.search('http://google.com')
print(m.group())    #http
    # 기존 정규식을 : 에서 (?=:)으로 바꾸면서 검색에는 :이 충족되었으나
        #문자열이 소비되지 않아 검색에는 포함되고, 검색결과에서는 제외

##부정형 전방 탐색
p = re.compile('.*[.].*$')  #'파일이름' + . + '확장자' 형태의 정규식

#확장자가 bat인 파일은 제외하고 싶다면?
p = re.compile('.*[.][^b].*$')  #[]안의 ^는 not을 의미, 확장자 b로시작하면 다 제외됨
p = re.compile('.*[.]([^b]..|.[^a].|..[^t])$')  #bat확장자 제외하나, 확장자가 2개인 파일도 제외됨
p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t])$') #조건은 갖추었으나 정규식이 너무 복잡해짐

#아래처럼 부정형 전방 탐색 사용
p = re.compile('.*[.](?!bat$).*$')  #확장자가 bat가 아닌 경우에만 통과
    #문자열이 소비되지 않으므로, bat아닌여부만 판단되면 그 이후 정규식 매치가 진행

#추가)exe 확장자도 추가로 제외시
p = re.compile('.*[.](?!bat$|exe$).*$')

###sub('바꿀문자열' 또는 함수, '대상문자열', count=바꾸기횟수) : 문자열 바꾸기
    #정규식과 매치되는 부분을 다른문자로 쉽게 변환 가능
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes') #'colour socks and colour shoes'

    #한번만 바꾸고 싶은경우
p.sub('colour', 'blue socks and red shoes', count=1)    #'colour socks and red shoes'


###sub 메서드와 유사한 subn 메서드
    #subn은 튜플로 리턴해주는 차이점이 있음 : ('변경된문자열', 바꾼횟수)
p = re.compile('(blue|white|red)')
p.subn('colour', 'blue socks and red shoes')    #('colour socks and colour shoes', 2)

## \g<그룹명 or 그룹인덱스> : sub 메서드를 사용할 때 참조 구문 사용
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub('\g<phone> \g<name>', 'park 010-1234-1234'))    #010-1234-1234 park
print(p.sub('\g<2> \g<1>', 'park 010-1234-1234'))    #010-1234-1234 park

# sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
#'Call 0xffd2 for printing, 0xc000 for user code.'

###Greedy(*) vs Non-Greedy(?)
s = '<html><head><title>Title</title>'
len(s)  #32
print(re.match('<.*>', s).span())    #(0, 32)
print(re.match('<.*>', s).group())   #<html><head><title>Title</title>

#정규식 '<.*>'의 결과로 <html> 만 받으려 했지만 전체가 소비됨
    # *의 탐욕 제한방법 : ?
print(re.match('<.*?>', s).group()) #<html>
#Non-Greedy 문자인 ?는 * / + / ? / {m,n}등의 반복 메타문자와 함께 사용할 수 있다
    # *? / +? / ?? / {m,n}?
        #이는 가능한 한 가장 최소한의 반복만을 수행하도록 돕는다.
        
#q1 a:b:c:d > a#b#c#d
a = 'a:b:c:d'
b = a.split(':')
c = '#'.join(b)
c   #'a#b#c#d'

#q2 딕셔너리 값 추출
a = {'A':90, 'B':80}
a.get('C', 70)

#q3
a = [1, 2, 3]
a = a + [4, 5]
a   #[1, 2, 3, 4, 5]
#위의 경우 a를 재정의함으로써 id(a)값이 달라짐

#아래의 경우 기존 a를 확장함으로써 id(a)값, 참조값은 변하지 않음
a = [1, 2, 3]
a.extend([4, 5])
a

#q4
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i >= 50:
        sum += i

print(sum)  #481

#q5 피보나치 함수
def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))

''' num = int(input('n 입력 : '))
piv = [0, 1]
while True:
    if (piv[-2]+piv[-1]) > num:
        break
    else:
        piv.append(piv[-2]+piv[-1])
print(piv)
'''

#q6 숫자 총합
num_list = input('총합을 구할 숫자를 입력하세요(숫자는 콤마로 구분합니다) : ').split(',')

num = 0
for i in num_list:
    num += int(i)   #input으로 받은 변수가 문자열이므로, int로 변환
print(num)

#q7 한 줄 구구단

gugu = int(input('구구단을 출력할 숫자를 입력하세요(2~9) : '))

for i in range(1, 10):
    print(i * gugu, end = ' ')

'''
i = 1
while i < 10:
    print(i * gugu, end=" ")
    i += 1
print('\n')
'''

#q8 역순 저장
'''
abc = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']

f = open('abc.txt', 'w')
for i in abc:
    f.write(i+'\n')
f.close()

'''

f = open('abc.txt', 'r')
lines = f.readlines()   #모든 라인 읽기
f.close()

lines.reverse()         #읽은 라인 역순 정렬

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip() #줄바꿈 문자 제거
    f.write(line)
    f.write('\n')       #줄바꿈 문자 삽입
f.close()

'''abc = []
f = open('abc.txt', 'r')
lines = f.readlines()

for line in lines:
    abc.append(line)
print(abc)
f.close()

a = abc.reverse()
f = open('abc.txt', 'w')
for i in abc:
    f.write(i)
f.close()'''

#q9 평균값 구하기
f = open('sample.txt', 'r')
sample = f.readlines()
f.close()

sum = 0
for i in sample:
    sum += int(i)
aver = sum / len(sample)

f = open('result.txt', 'w')
f.write(f'평균 : {aver}')   #f.write(str(aver))     #숫자는 result.txt에 바로쓸수 없어 str로 변경해주어야함
f.close()

#10 사칙연산 계산기
class Calculator:
    def __init__(self, num_list):
        self.num_list = num_list

    def sum(self):
        result = 0
        for i in self.num_list:
            result += i
        return result
    
    def avg(self):
        return self.sum()/len(self.num_list)
    
cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()  #15
cal1.avg()  #3.0

cal2 = Calculator([6, 7, 8, 9, 10])
cal2.sum()  #40
cal2.avg()  #8.0

#q11 모듈 사용 방법
'''C:\doit에 있는 mymod.py 임포트하는 3가지 방법

1)sys 모듈 사용 : 
>>>import sys
>>>sys.path.append('c:\doit')
>>>import mymod

2)PYTHONPATH 환경 변수 사용
C:\Users\home>set PYTHONPATH=c:\doit
C:\Users\home>python
>>>import mymod

3)현재 디렉터리 사용
C:\Users\home>C:\doit
C:\doit>python
>>import mymod
'''

#q12 오류와 예외처리
'''
7
[1, 2, 3][3] 에서 인덱스 에러 발생 +3
finally 문 실행 +4

+1, +2 도 물론 에러지만, 발생하기전에 이미 인덱스에러발생하여 수행되지 않음
'''

result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4/0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)

#q13 DashInsert 함수    오래걸림
data = '4546793'

numbers = list(map(int, data))
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:                  #다음 수가 있을때
        is_odd = num % 2 == 1               #현재 수가 홀수
        is_next_odd = numbers[i+1] % 2 == 1 #다음 수가 홀수
        if is_odd and is_next_odd:          #연속 홀수라면
            result.append('-')
        elif not is_odd and not is_next_odd:#연속 짝수라면
            result.append('*')

print(''.join(result))

''' def DashInsert(string):
    lst = list(string)
    r_string = f'{lst[0]}'
    
    for i in range(1,len(lst)):
        print(i)
        if int(lst[i-1]) % 2 != 0 and int(lst[i]) % 2 != 0:
            print(i)
            r_string += '-' + lst[i]
        elif int(lst[i-1]) % 2 == 0 and int(lst[i]) % 2 == 0:
            print(i)
            r_string += '*' + lst[i]
        else:
            print(i)
            r_string += lst[i]
    
    return r_string

a = '4546793'
DashInsert(a) '''

#q14 문자열 압축
def compress_string(s):
    _c = ''
    cnt = 0
    result = ''
    for c in s:
        if c != _c: #중복문자 아니라면
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:       #중복문자라면
            cnt += 1
            
    if cnt: result += str(cnt)
    return result

print(compress_string('aaabbcccccca'))  #a3b2c6a1

''' a = 'aaabbcccccca'

cnt = 1
char = a[0]
result = ''

for i in range(1, len(a)):
    if char == a[i]:
        cnt += 1
    else:
        result += f'{char}{cnt}'
        cnt = 1
        char = a[i]
        
    if i == (len(a)-1) and (cnt == 1 or a[i] == a[i-1]):
        result += f'{char}{cnt}'
    
    #print(i, len(a), cnt, char , a[i])
print(result) '''

#q15 Duplicate Numbers
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum('0123456789'))  #True
print(chkDupNum('01234'))       #False
print(chkDupNum('01234567890')) #False
print(chkDupNum('6789012345'))  #True
print(chkDupNum('012322456789'))#False

''' result = ''

num = '0123456789 01234 01234567890 6789012345 012322456789'
dup_list = num.split(' ')

for i in dup_list:
    num_list = list(range(10))
    
    try:
        if len(i) == len(num_list):
            for j in i:
                num_list.remove(int(j))
                if not num_list:
                    result += 'True '
        else:
            result += 'False '
    except:
            result += 'False '
             
print(result)'''

#q16 모스 부호 해독
#딕셔너리로 해서 키(모스) : 밸류(스펠링)
mos = {
    '.-' : 'A',
    '-...' : 'B',
    '-.-.' : 'C',
    '-..' : 'D',
    '.' : 'E',
    '..-.' : 'F',
    '--.' : 'G',
    '....' : 'H',
    '..' : 'I',
    '.---' : 'J',
    '-.-' : 'K',
    '.-..' : 'L',
    '--' : 'M',
    '-.' : 'N',
    '---' : 'O',
    '.--.' : 'P',
    '--.-' : 'Q',
    '.-.' : 'R',
    '...' : 'S',
    '-' : 'T',
    '..-' : 'U',
    '...-' : 'V',
    '.--' : 'W',
    '-..-' : 'X',
    '-.--' : 'Y',
    '--..' : 'Z'    
}

def morse(src):
    result = []
    for word in src.split('  '):
        for char in word.split(' '):
            result.append(mos[char])
        result.append(' ')
    return ''.join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

''' message1 = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'

def mosf1(message1):
    sp1 = message1.split('  ')
    recov = ''
    for i in sp1:
        sp2 = i.split(' ')
        for j in sp2:
            recov += mos[j]
        recov += ' '
    return recov

mosf1(message1) '''

#q17 기초 메타 문자 a....b

#q18 문자열검색 10
import re
p = re.compile('[a-z]+')
m = p.search('5 python')
m.start()+m.end()   #2 + (7 + 1) = 10

#q19
import re
data = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''
p = re.compile('(\d{3}[-]\d{4})[-]\d{4}')
result = p.sub('\g<1>-####', data)

print(result)

"""data = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''

import re
p = re.compile(r'((\w+\s+\d+[-]\d+)[-]\d+)')
data_sub = p.sub(r'\g<2>-****', data)
print(data_sub)
'''
park 010-9999-****
kim 010-9909-****
lee 010-8789-****
'''
"""
#q20 긍정형 전방 탐색 : .com, .net 아닌 주소 제외 정규식
p = re.compile('.*[@].*[.](?=com$|net$).*$')

import re
p = re.compile('.*[@].*[.](?=com$|net$).*$')

print(p.match('pahkey@gmail.com'))  #<re.Match object; span=(0, 16), match='pahkey@gmail.com'>
print(p.match('kim@daum.net'))      #<re.Match object; span=(0, 12), match='kim@daum.net'>
print(p.match('lee@myhome.co.kr'))  #None
