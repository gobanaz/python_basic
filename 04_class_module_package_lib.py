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

