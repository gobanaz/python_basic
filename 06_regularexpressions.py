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
from calendar import c
import re

from pyrsistent import b

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

a[.]b   #a와 b사이 문자그대로의 .이 있으면 매치 : "a + . + b"
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
{m} #바로앞 문자가 m회 반복되면 매치
{m,}    #바로앞 문자가 m회 이상 반복되면 매치
            #{0,} == *, {1,} == +과 같아지게 됨
    
ca{2}t  #'c + a(2번만 반복시 매치) + t'
    #caat과 매치, cat과는 매치X

{m,n}   #바로앞 문자가 m~n회 반복시 매치
ca{2,5}t    #caat 매치, caaaaat 매치, cat 매치X : "c + a(2~5회) + t"

##반복과 유사한 개념 : ? == {0, 1}
ab?c    #b가 0~1번 사용되면 매치 : "a + b(0~1회) + c"
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
end()       매치된 문자열의 끝인덱스 리턴
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