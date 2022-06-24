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

###__init__.py 의 용도
