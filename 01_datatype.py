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
