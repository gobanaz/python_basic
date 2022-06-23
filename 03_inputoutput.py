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