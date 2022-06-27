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