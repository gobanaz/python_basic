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
