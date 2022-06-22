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