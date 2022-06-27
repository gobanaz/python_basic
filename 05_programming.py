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