#q1 a:b:c:d > a#b#c#d
from numpy import empty


a = 'a:b:c:d'
'#'.join(a.split(':'))

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
num = int(input('n 입력 : '))
piv = [0, 1]
while True:
    if (piv[-2]+piv[-1]) > num:
        break
    else:
        piv.append(piv[-2]+piv[-1])
print(piv)

#q6 숫자 총합
num_list = input('총합을 구할 숫자를 입력하세요(숫자는 콤마로 구분합니다) : ').split(',')

num = 0
for i in num_list:
    num += int(i)
print(num)

#q7 한 줄 구구단

gugu = int(input('구구단을 출력할 숫자를 입력하세요(2~9) : '))

i = 1
while i < 10:
    print(i * gugu, end=" ")
    i += 1
print('\n')

#q8 역순 저장
'''
abc = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']

f = open('abc.txt', 'w')
for i in abc:
    f.write(i+'\n')
f.close()

'''
abc = []
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
f.close()

#q9 평균값 구하기
f = open('sample.txt', 'r')
sample = f.readlines()

sum = 0
for i in sample:
    sum += int(i)
aver = sum / len(sample)
f.close()

f = open('result.txt', 'w')
f.write(f'평균 : {aver}')
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

#q11 모듈 사용 방법 ???
'''
>>>import mymod
>>>

import sys 이용해서 path추가하는방법

from 경로 import mymod 하는 방법
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
def DashInsert(string):
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
DashInsert(a)

#q14 문자열 압축
a = 'aaabbcccccca'

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
print(result)

#q15 Duplicate Numbers
result = ''

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
            
print(result)
