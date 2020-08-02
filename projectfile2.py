from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('일반교과 입력창')

#변수들
subject=['국어','도덕','사회','역사','수학','과학','기가','영어','선택','선택2','선택3']
part=['현재 2학년 1학기 성적을 입력중입니다.','현재 2학년 2학기 성적을 입력중입니다.','현재 3학년 1학기 성적을 입력중입니다.','현재 3학년 2학기 성적을 입력중입니다.','일반교과의 성적이 모두 기입되었습니다. ']
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
rv=tkinter.IntVar() #예체능 과목 수행평가 점수

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
                songchido =+ l1[i] #성취도
                onejomsu =+ l2[i] #원점수
                pyeongun =+ l3[i] #평균
                pyeoncha =+ l4[i] #표준편차
        a= 10+(songchido/6)+(((onejomsu-pyeongun)/pyeoncha)*10)
        return a

def yeche():
        global l5,vc,rb1,rb2,rb3,rb4
        l5.append(vc.get())
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
                a =+ i
        yechenung = ((a/(l5.len))*10)+10
                
def chulgyol():
        global b4,e5,e6,e7,e8,e9,e10,one,two,three
        b4['state']=DISABLED
        a = e5.get()//3+e6.get() #1학년 결석 인정 일수
        b = e7.get()//3+e8.get() #2학년 결석 인정 일수
        c = e9.get()//3+e10.get() #3학년 결석 인정 일수
        a_list = [6,5.4,4.8,4.2,3.6,3.0]
        bc_list = [7,6.3,5.6,4.9,4.2,3.5]

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
t5 = Label(window, text = '예체능 수행평가 성적을 입력해주세요.',bg='blue')
t5.grid(row = 7, column = 0,columnspan = 4,width='40')
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
t6 = Label(window, text = '지각·결석을 입력해주세요.',bg='blue',fg='blue')
t6.grid(row = 7, column = 0,columnspan = 4,width=40)
t7 = Label(window,text = '지각·조퇴·결과', width = 20, bg = 'skyblue')
t7.grid(row = 8,column = 0,columnspan = 2)
t8 = Label(window,text = '결석',width=20,bg='skyblue')
t8.grid(row = 8,column = 2,columnspan = 2)
#1학년 출결
t9 = Label(window,text = '1학년',width=20,bg='blue',fg='white')
t9.grid(row = 8,column = 2,columnspan = 2)
e5 = Entry(window)
e5.grid(row = 9, column = 0,columnspan = 2,width=20)
e6 = Entry(window)
e6.grid(row = 9, column = 2,columnspan = 2,width=20)
#2학년 출결
t10 = Label(window,text = '2학년',width=20,bg='blue',fg='white')
t10.grid(row = 10,column = 0,columnspan = 4)
e7 = Entry(window)
e7.grid(row = 11, column = 0,columnspan = 2,width=20)
e8 = Entry(window)
e8.grid(row = 11, column = 2,columnspan = 2,width=20)
#3학년 출결
t11 = Label(window,text = '3학년',width=20,bg='blue',fg='white')
t11.grid(row = 12,column = 0,columnspan = 4)
e9 = Entry(window)
e9.grid(row = 13, column = 0,columnspan = 2,width=20)
e10 = Entry(window)
e10.grid(row = 13, column = 2,columnspan = 2,width=20)
#다음 버튼
b4 = Button(window,text = '다음',command = chulgyol,width=40)
b4.grid(row = 14,column = 0,columnspan = 4)

#결과창
 = Label(window,text='학기별 성적',bg='blue',fg='white')
.grid(row = 0,column = 0,columnspan = 4)
 = Label(window,text='2학년',bg='skyblue',fg='white',width=20)
.grid(row = 1,column = 0,columnspan = 2)
 = Label(window,text='3학년',bg='skyblue',fg='white',width=20)
.grid(row = 1,column = 2,columnspan = 2)
 = Label(window,text='1학기') #2-1
.grid(row = 2,column = 0)
 = Label(window,text='2학기') #2-2
.grid(row = 2,column = 1)
 = Label(window,text='1학기') #3-1
.grid(row = 2,column = 2)
 = Label(window,text='2학기') #3-2
.grid(row = 2,column = 3)
 =Label(window,text='0')
.grid(row = 3,column = 0)
 =Label(window,text='0')
.grid(row = 3,column = 1)
 =Label(window,text='0')
.grid(row = 3,column = 2)
 =Label(window,text='0')
.grid(row = 3,column = 3)
 = Label(window,text='최종결과',bg='blue',fg='white',width=40)
.grid(row = 4,column = 0,columnspan = 4)
 =Label(window2,text='0')
.grid(row = 5,column = 0,columnspan = 4)
window.mainloop()