# 모듈 불러오기
import csv
import random
import time

# 파일 열기
f= open('프로젝트.csv', 'r', encoding='utf-8')
data = csv.reader(f)
data = list(data)

# 데이터 분석
number = len(data[0]) -1 # 학생 번호 수 
subject_number = list(zip(*data))[0].index('학기말 종합의견') -list(zip(*data))[0].index('관찰 기록') -1 # 과목 수
A = list(zip(*data))[0].index('관찰 기록') # 문장 시작점
sub_unit = []
grade =[]
sub = 0
unit = 0
a= 0

# 과목 별 수행평가 단원 수 분석  = sub_unit 리스트 안에 과목 별로 수행평가 수가 저장됨. ex) [0,4] : 1번째 과목은 4개의 수행평가가 있음
for i in list(zip(*data))[0][A+1 : A+subject_number+1] :
    for j in list(zip(*data))[0][:A] :
        if i in j :
            unit += 1
    sub_unit.append([sub, unit])
    sub += 1
    unit = 0 
print(sub_unit)

reverse_sub_unit = list(zip(*sub_unit)) 

# 프로그램 구동
print('성적 처리 도우미 프로그램입니다.')
time.sleep(1)
print('엑셀 파일 작성 데이터를 기반으로 성적 처리 도와드리겠습니다.')
print('총 인원 수는 {0}명 입니다.'.format(number))

# 관찰 기록 3 문장 출력 ( 성적과 관련없이 무작위로 출력 )
for j in range(subject_number) :
    print('입력하신 수행평가 성적에 기반한 {0} 과목 관찰 기록 문장입니다.'.format(list(zip(*data))[0][20+j]))
    for i in range(number) :
        while a <= 3 :
            if '3' in list(zip(*data))[i+1][sum(reverse_sub_unit[1][:j], start = 2) : sum(reverse_sub_unit[1][:j+1]) + 2 ] :
                A = data[20+j][1].split('\n')
                print('{0}번 학생 : {1}'.format(i+1, A[random.randint(0,len(A)-1)]))
                a += 1
                del A
            if '2' in list(zip(*data))[i+1][sum(reverse_sub_unit[1][:j], start = 2) : sum(reverse_sub_unit[1][:j+1]) + 2 ] :
                A = data[20+j][2].split('\n') 
                print('{0}번 학생 : {1}'.format(i+1,A[random.randint(0,len(A)-1)]))
                a += 1
                del A
            if '1' in list(zip(*data))[i+1][sum(reverse_sub_unit[1][:j], start = 2) : sum(reverse_sub_unit[1][:j+1]) + 2 ] :    
                A = data[20+j][3].split('\n')
                print('{0}번 학생 : {1}'.format(i+1, A[random.randint(0,len(A)-1)]))
                a += 1
                del A
        a = 0

a= 0

# 학기말 종합의견 출력 ( 부족한 기록이 있다면 그 부분 우선 출력 )
for j in range(subject_number) : 
    print('입력하신 수행평가 성적에 기반한 {0} 과목 학기말 종합의견 문장입니다.'.format(list(zip(*data))[0][20+j]))
    for i in range(number) :
        if '1' in list(zip(*data))[i+1][sum(reverse_sub_unit[1][:j], start = 2) : sum(reverse_sub_unit[1][:j+1]) + 2 ] :
            A = data[28+j][3].split('\n')
            print('{0}번 학생 : {1} '.format(i+1,A[random.randint(0,len(A)-1)] ))
            a += 1
            del A
        if '2' in list(zip(*data))[i+1][sum(reverse_sub_unit[1][:j], start = 2) : sum(reverse_sub_unit[1][:j+1]) + 2 ] : 
            A = data[28+j][2].split('\n')
            print('{0}번 학생 : {1}'.format(i+1,A[random.randint(0,len(A)-1)] ))
            a += 1
            del A
        if '3' in list(zip(*data))[i+1][sum(reverse_sub_unit[1][:j], start = 2) : sum(reverse_sub_unit[1][:j+1]) + 2 ] :
            if a == 3 :
                a = 0
                pass
            else : 
                while a != 3 :
                    A = data[28+j][1].split('\n')
                    print('{0}번 학생 : {1}'.format(i+1,A[random.randint(0,len(A)-1)] ))
                    a += 1
                    del A
                a = 0
        

'''# 성적 분석 모드
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.font_manager._rebuild()
findfont = mpl.font_manager.fontManager.findfont
mpl.font_manager.findfont = findfont
mpl.backends.backend_agg.findfont = findfont

plt.rc('font', family = 'NanumGothic')
plt.rcParams['axes.unicode_minus']=False
plt.title('한글제목')
plt.plot([-1,0,1])
plt.show()

f, ax = plt.subplot()'''
