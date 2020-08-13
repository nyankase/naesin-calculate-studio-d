from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('내신 계산기 입력창')

#변수들
subject=['국어','도덕','사회','역사','수학','과학','기가','영어','선택','선택2','선택3']
part=['현재 2학년 1학기 성적을 입력중입니다.','현재 2학년 2학기 성적을 입력중입니다.','현재 3학년 1학기 성적을 입력중입니다.','현재 3학년 2학기 성적을 입력중입니다.','일반교과의 성적이 모두 기입되었습니다. ']
lc = 0
cnt = 0            #과목 카운터
pcnt= 0           #학기 카운터
twoone = 0     #2학년 1학기 내신
twotwo = 0     #2학년 2학기 내신
threeone = 0  #3학년 1학기 내신
threeone = 0  #3학년 2학기 내신
one = 0
two = 0
three = 0
yechenung = 0 #예체능 내신
susang_imwon = 0
susang = 0
imwon = 0
bongsa = 0
rv=IntVar()
#예체능 과목 수행평가 점수

#함수들
def count():
        global cnt,l1,l2,l3,l4,e1,e2,e3,e4,pcnt,b1
        try:     
                #입력되지 않은 칸 있을 시 메세지
                if e1.get()== '' or e2.get()=='' or e3.get()==''or e4.get()=='':
                                messagebox.showerror("오류!","입력하지 않은 칸이 있습니다.")
                elif cnt < 10:
                        cnt +=1
                        t1['text'] = subject[cnt]
                        l1.append(int(e1.get()))
                        l2.append(int(e2.get()))
                        l3.append(int(e3.get()))
                        l4.append(int(e1.get()))
                        #다음 버튼을 누르면 엔트리에 입력되어 있던 글자가 삭제
                        #해당 코드를 삭제해서 빠른 오류 확인이 가능하다.
                        e1.delete(0)
                        e2.delete(0)
                        e3.delete(0)
                        e4.delete(0)
                elif cnt ==10:
                        pcnt+=1
                        cnt =0
                        t1['text'] = subject[cnt]
                        t4['text'] = part[pcnt]
                        #정보를 모두 입력했을 경우 버튼 비활성화
                        if pcnt ==4:
                                b1['state']=DISABLED
                                calculate()
        except:
                messagebox.showerror("오류!","비정상적인 형식으로 입력한 칸이 있습니다.")
                        
def calculate():
        global twoone,twotwo,threeone,threetwo
        twoone = cal(0,11)
        twotwo = cal(11,22)
        threeone = cal(22,33)
        threetwo = cal(33,44)

def cal(start,end):
        global l1,l2,l3,l4
        for i in range(start,end):
                songchido += l1[i] #성취도
                onejomsu += l2[i] #원점수
                pyeongun += l3[i] #평균
                pyeoncha += l4[i] #표준편차
        a= 10+(songchido/6)+(((onejomsu-pyeongun)/pyeoncha)*10)
        return a

def yeche():
        global l5,rv,rb1,rb2,rb3,rb4
        l5.append(rv.get())
        rb1.deselect()
        rb2.deselect()
        rb3.deselect()
        rb4.deselect()

def yecheend():
        global b2,b3,l5
        a=0
        b2['state']=DISABLED
        b3['state']=DISABLED
        for i in l5:
                a += i
        yechenung = (a/len(l5)*10)+10
                
def chulgyol():
        global b4,e5,e6,e7,e8,e9,e10,one,two,three
        b4['state']=DISABLED
        a = int(e5.get())//3+int(e6.get()) #1학년 결석 인정 일수
        b = int(e7.get())//3+int(e8.get()) #2학년 결석 인정 일수
        c = int(e9.get())//3+int(e10.get()) #3학년 결석 인정 일수
        a_list = [6,5.4,4.8,4.2,3.6,3.0,2.4]
        bc_list = [7,6.3,5.6,4.9,4.2,3.5,2.8]
        one = chulgyolcal(a,a_list)
        two = chulgyolcal(b,bc_list)
        three = chulgyolcal(c,bc_list)

def chulgyolcal(a,list):
        if a==0:
                re = list[0]
        if a==1:
                re = list[1]
        if a==2:
                re = list[2]
        if a==3:
                re = list[3]
        if a==4:
                re = list[4]
        if a==5:
                re = list[5]
        if a>=6:
                re = list[6]
        return re

def other():
        global susang_imwon,susang,imwon,bongsa,e11,e12,e13
        a= int(e11.get)
        if  a<=4:
                bongsa = 8
        elif  a<=9:
                bongsa = 9
        elif  a<=14:
                bongsa = 10
        elif  a<=19:
                bongsa = 11
        elif  a<=24:
                bongsa = 12
        elif  a<=29:
                bongsa = 13
        elif  a<=34:
                bongsa = 14
        elif  a<=39:
                bongsa = 15
        elif  a<=44:
                bongsa = 16
        elif  a<=49:
                bongsa = 17
        elif  a<=54:
                bongsa = 18
        elif  a<=59:
                bongsa = 19
        else:
                bongsa = 20
        susang = 0.5*int(e12.get())
        imwon = 0.1*int(e13.get())
        if susang+imwon < 20:
                susang_imwon=susang+imwon
        else:
                susang_imwon = 20
        b5['state']= DISABLED

def last():
        t22['text'] = str(twoone)
        t23['text'] = str(twotwo)
        t24['text'] = str(threeone)
        t25['text'] = str(threetwo)
        t28['text'] = str(yechenung)
        t33['text'] = str(one+two+three) + '/20'
        t34['text'] = str(bongsa) + '/20'
        t35['text'] = str(susang)
        t36['text'] = str(imwon)
        a = twoone + twotwo + threeone + threetwo + one + two + three + bongsa + susang_imwon + yechenung
        if a < 200:
                t36['text'] = str(a)                
#입력한 정보를 저장해주는 리스트들
l1=[]  #성취도
l2=[]  #원점수
l3=[]  #평균
l4=[]  #표준편차
l5=[]  #예체능

#일반과목

#설명란
t1 = Label(window,text = subject[cnt],width=40,bg = 'skyblue')
t1.grid(row = 0,column = 0,columnspan = 2)
t2=Label(window,text = '성취도/원점수/평균/표준편차',width=40,bg = 'skyblue')
t2.grid(row = 1,column = 0,columnspan = 2)
t3=Label(window,text = '※성취도는 5/4/3/2/1로 입력※',bg='skyblue',fg='red')
t3.grid(row = 2,column = 0,columnspan = 2)

#입력창
e1 = Entry(window)
e1.grid(row = 3, column = 0)
e2 = Entry(window)
e2.grid(row = 3, column = 1)
e3 = Entry(window)
e3.grid(row = 4, column = 0)
e4 = Entry(window)
e4.grid(row = 4, column = 1)

#학년,학기,기입완료 표시
t4 = Label(window,text = part[pcnt])
t4.grid(row = 5,column = 0,columnspan = 2)

#다음 버튼
b1 = Button(window,text = '다음',command = count,width=40)
b1.grid(row = 6,column = 0,columnspan = 2)

#예체능
t5 = Label(window, text = '예체능 수행평가 성적을 입력해주세요.',bg='blue',width='40')
t5.grid(row = 7, column = 0,columnspan = 4)
rb1 = Radiobutton(window, text = 'A', variable = rv, value = 3,width=10,bg='skyblue')
rb1.grid(row = 7, column = 0)
rb2 = Radiobutton(window, text = 'B', variable = rv, value = 2,width=10,bg='skyblue')
rb2.grid(row = 7, column = 1)
rb3 = Radiobutton(window, text = 'C', variable = rv, value = 1,width=10,bg='skyblue')
rb3.grid(row = 7, column = 2)
rb4 = Radiobutton(window, text = 'F', variable = rv, value = 0,width=10,bg='skyblue')
rb4.grid(row = 7, column = 3)
#예체능 다음 버튼
b2 = Button(window,text = '다음',command = yeche,width=20)
b2.grid(row = 6,column = 0,columnspan = 2)
#예체능 종료 버튼
b3 = Button(window,text = '종료',command = yecheend,width=20)
b3.grid(row = 6,column = 0,columnspan = 2)

#출결
t6 = Label(window, text = '지각·결석을 입력해주세요.',bg='blue',fg='blue',width=40)
t6.grid(row = 7, column = 0,columnspan = 4)
t7 = Label(window,text = '지각·조퇴·결과', width = 20, bg = 'skyblue')
t7.grid(row = 8,column = 0,columnspan = 2)
t8 = Label(window,text = '결석',width=20,bg='skyblue')
t8.grid(row = 8,column = 2,columnspan = 2)
#1학년 출결
t9 = Label(window,text = '1학년',width=20,bg='blue',fg='white')
t9.grid(row = 8,column = 2,columnspan = 2)
e5 = Entry(window,width=20)
e5.grid(row = 9, column = 0,columnspan = 2)
e6 = Entry(window,width=20)
e6.grid(row = 9, column = 2,columnspan = 2)
#2학년 출결
t10 = Label(window,text = '2학년',width=20,bg='blue',fg='white')
t10.grid(row = 10,column = 0,columnspan = 4)
e7 = Entry(window,width=20)
e7.grid(row = 11, column = 0,columnspan = 2)
e8 = Entry(window,width=20)
e8.grid(row = 11, column = 2,columnspan = 2)
#3학년 출결
t11 = Label(window,text = '3학년',width=20,bg='blue',fg='white')
t11.grid(row = 12,column = 0,columnspan = 4)
e9 = Entry(window,width=20)
e9.grid(row = 13, column = 0,columnspan = 2)
e10 = Entry(window,width=20)
e10.grid(row = 13, column = 2,columnspan = 2)
#다음 버튼
b4 = Button(window,text = '완료',command = chulgyol,width=40)
b4.grid(row = 14,column = 0,columnspan = 4)

#다른 것들
t12 = Label(window, text = '각종 성적 반영.',bg='blue',fg='blue',width=40)
t12.grid(row = 15, column = 0,columnspan = 4)
t13 = Label(window,text = '봉사', width = 10, bg = 'skyblue')
t13.grid(row = 16,column = 0)
t14 = Label(window,text = '수상 개수', width = 10, bg = 'skyblue')
t14.grid(row = 16,column = 1)
t15 = Label(window,text = '임원활동', width = 10, bg = 'skyblue')
t15.grid(row = 16,column = 2)
e11 = Entry(window,width=10)
e11.grid(row = 17, column = 0)
e12 = Entry(window,width=10)
e12.grid(row = 17, column = 1)
e13 = Entry(window,width=10)
e13.grid(row = 17, column = 2)
b5 = Button(window,text = '완료',command = other,width=40)
b5.grid(row = 18,column = 0,columnspan = 4)

#결과창
t16 = Label(window,text='학기별 성적',bg='blue',fg='white')
t16.grid(row = 19,column = 0,columnspan = 4)
t17 = Label(window,text='2학년',bg='skyblue',fg='white',width=20)
t17.grid(row = 20,column = 0,columnspan = 2)
t18 = Label(window,text='3학년',bg='skyblue',fg='white',width=20)
t18.grid(row = 20,column = 2,columnspan = 2)
t19 = Label(window,text='1학기',width=10) #2-1
t19.grid(row = 21,column = 0)
t20 = Label(window,text='2학기',width=10) #2-2
t20.grid(row = 21,column = 1)
t21 = Label(window,text='1학기',width=10) #3-1
t21.grid(row = 21,column = 2)
t22 = Label(window,text='2학기',width=10) #3-2
t22.grid(row = 21,column = 3)
t23 =Label(window,text='0',width=10)
t23.grid(row = 22,column = 0)
t24 =Label(window,text='0',width=10)
t24.grid(row = 22,column = 1)
t25 =Label(window,text='0',width=10)
t25.grid(row = 22,column = 2)
t26 =Label(window,text='0',width=10)
t26.grid(row = 22,column = 3)
t27 = Label(window,text='예체능',width=40)
t27.grid(row = 23,column = 0)
t28 =Label(window,text='0',width=40)
t28.grid(row = 24,column = 0)
t29 = Label(window,text='출결',bg='skyblue',fg='white',width=10)
t29.grid(row = 25,column = 0)
t30 = Label(window,text='봉사',bg='skyblue',fg='white',width=10)
t30.grid(row = 25,column = 1)
t31 = Label(window,text='수상',bg='skyblue',fg='white',width=10)
t31.grid(row = 26,column = 2)
t32 = Label(window,text='임원',bg='skyblue',fg='white',width=10)
t32.grid(row = 26,column = 3)
t33 =Label(window,text='0',width=10)
t33.grid(row = 27,column = 0)
t34 =Label(window,text='0',width=10)
t34.grid(row = 27,column = 1)
t35 =Label(window,text='0',width=10)
t35.grid(row = 27,column = 2)
t36 =Label(window,text='0',width=10)
t36.grid(row = 27,column = 3)
t37 = Label(window,text='최종결과',bg='blue',fg='white',width=40)
t37.grid(row = 25,column = 0,columnspan = 4)
t38 =Label(window,text='0')
t38.grid(row = 26,column = 0,columnspan = 4)
b6 = Button(window,text = '결과 확인',command = last,width=40)
b6.grid(row = 27,column = 0,columnspan = 4)
window.mainloop()
