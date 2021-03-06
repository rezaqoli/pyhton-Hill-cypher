#!/usr/bin/env python
# coding: utf-8

# In[172]:


import numpy as np
from tkinter import *
import tkinter.messagebox
from tkinter import scrolledtext as st
import math
from tkinter import ttk
from numpy.linalg import inv
root = None


# In[173]:


A=np.zeros((3,3))
A2=np.zeros((3,3))


# In[174]:


textdic={
    " " :28,
    "?":27,
    "." :26
}
#ایجاد یک دیکشنری برای تغییر ورودی به حالت مورد نظر


# In[175]:


asciiDic={
    0:"a",
    1:"b",
    2:"c",
    3:"d",
    4:"e",
    5:"f",
    6:"g",
    7:"h",
    8:"i",
    9:"j",
    10:"k",
    11:"l",
    12:"m",
    13:"n",
    14:"o",
    15:"p",
    16:"q",
    17:"r",
    18:"s",
    19:"t",
    20:"u",
    21:"v",
    22:"w",
    23:"x",
    24:"y",
    25:"z",
    26:".",
    27:"?",
    28:" ",
}
#دیکشنری تعریف شده برای تبدیل عدد به حروف


# In[176]:


def inv_mod_29(self):
    self = int(self)#تبدیل به integer
    t=abs(self)#قدر مطلق
    if t > 30:
        t=t%29
    for i in range(1,30):
        if (i*t)%29 ==1 :#پیدا کردن معکوس در مد 29
            if t==self:
                return i
                break
            else:
                return -i
                
            break    


# In[177]:


#*****************GET KEY MATRIX GROM GUI
def key_matrix():
        for i in range(3):
                for j in range(3):
                    A[i][j]=a[i][j].get()
                    
                    
def matrix_key():
    for i in range(3):
                for j in range(3):
                    A2[i][j]=a2[i][j].get()
    adj_A2=np.dot(inv(A2),round(np.linalg.det(A2))) #بدست آوردن adjoint
    det2mod =inv_mod_29(round(np.linalg.det(A2)))  #مد29 دترمینان              
    new_inv=np.dot(det2mod,adj_A2)%29#ضرب ماتریسی
    return new_inv
    


# In[178]:


#*******************************GET PLIAN TEXT AND CONVERT TO matrix                    
def Plain():
    value=[]
    plaintext=Ptext.get()
    plaintext=plaintext.lower()#تبدیل رسته به حروف کوچک
    for character in plaintext:
        if 96 <ord(character) < 122:#تبدیل به کد اسکی
            number = ord(character)-97 #انتقال اسکی کد به 0
            value.append(number)
        elif (character == " ") or (character == "?") or (character=="."):
            number=textdic.get(character)#خواندن از ddictionarry
            value.append(number)
        else:
            tkinter.messagebox.showinfo("Unvalid input","ورودی در محدوده من نیست!!")
            break
    
    
    def to3():
        sotonha=math.ceil(len(value)/3)
        matrix2=np.zeros(shape=(3,sotonha))
        for soton in range(sotonha):
            for satr in range(3):
                if satr+soton*3 < len(value):
                    matrix2[satr][soton]=value[satr+soton*3]
                else:
                    matrix2[satr][soton]= value[len(value)-1]
        return matrix2
        
        
    
    matrix2=to3()
    
    return matrix2    


# In[179]:


#**********************

def click_me():
    sc.delete("1.0",END)
    amad=[]
    javab = ""
    key_matrix()#تابعی برای گرفتن مقادیر از رابط گرافیکی و تبدیل به آرایه دوبعدی
    amad =Plain()#گرفتن عبارت ورودی و تبدیل به ماتریس به فرم مورد نظر
    result =(np.dot(A,amad))%29 #باقیمانده حاصلضرب ماتریس کلیذ در ورودی
    print(result)
    for j in range(len(result[0])):
        for i in range(len(result)):
            javab+= asciiDic.get(result[i][j]) 
            #تبدیل ماتریس جواب به عبارت کد شده
    sc.insert(END, "coded \n"+javab)                      
    


# In[180]:


def push_me():
    new_inv=matrix_key()
    def encrypted():
        yechiz=[]
        enc=decT.get() #گرفتن ورودی از gui
        enc=enc.lower() #تبدیل به حروف کوچک
        for character in enc:
            if 96 <ord(character) < 122:
                number = ord(character)-97#تبدیل به اعداد اسکی و مپ آن روی 0
                yechiz.append(number)
            elif (character == " ") or (character == "?") or (character=="."):
                number=textdic.get(character)
                yechiz.append(number)
            else:
                tkinter.messagebox.showerror("Unvalid input","ورودی در محدوده من نیست!!")
                break
        sotonha=math.ceil(len(yechiz)/3) #رند کردن رو به بالا تعداد سطر ها تقسیم بر3
        matrix3=np.zeros(shape=(3,sotonha)) #تعریف یک ماتریس خالی با ابعاد مورد نظر
        for soton in range(sotonha):
            for satr in range(3):
                if satr+soton*3 < len(yechiz):
                    matrix3[satr][soton]=yechiz[satr+soton*3] #تبدیل آرایه به یک ماتریس به ابعاد مورد نظر
                else:
                    matrix3[satr][soton]= yechiz[len(yechiz)-1] #اگر به آخر حروف رسیدیم حرف آخر را تکرار میکنیم
                    
        return matrix3
    
    
    
    dochiz =encrypted()
    pasokh=np.dot(new_inv,dochiz)%29  #ضرب دو ماتریس معکوس ماتربس کلیدی و ماتریس ورودی در مد 29
    print(pasokh)
    sechiz=[] 
    for i in range(len(pasokh[0])):
        for j in range(3):
            sechiz.append(round(pasokh[j][i])) #تبدیل ماتریس پاسخ به آرایه تک بعدی
    print(sechiz)        
    
    fina=""
    for i in range(len(sechiz)):
        fina.append(asciiDic.get(sechiz[i])) #تبدیل ماتریس به حروف از روی دیکشنری اسکی که در قبل تعریف کردیم
        print(fina)    
#RPJDXCFUWW? WNFCOT?FXF?PLXGXSN    
        


# In[181]:


root = Tk()
root.title("Number3 project: Hill Cipher")
root.minsize(640,400) #حداقل سایز gui
tabControl= ttk.Notebook(root) #مقدار دهی اولیه برای اضافه کردن tab

tab1=Frame(tabControl)#مقدار دهی اولیه تب
tabControl.add(tab1,text="Coddig")#نامگذاری tab
tabControl.pack(expand=1,fill="both")#ایجاد تب

tab2=Frame(tabControl)
tabControl.add(tab2,text="decoding")
tabControl.pack(expand=1,fill="both")
#888888888888888888888888888888888888
Label(tab2,text="enter the value:",font=("Galapogos BRK Normal",12),padx=4,pady=4,borderwidth=12).grid(column=0,row=0,padx=3,pady=3)
key_frame=LabelFrame(tab2,text="matrix key (3*3)",font=("Junior Star",12))#ایجاد یک قالب در در رابط گرافیکی
key_frame.grid(column=1,row=0)#تعیین موقعیت قالب در رابط گرافیکی
a2=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        a2[i][j]=IntVar()#ایجاد متغییر های پویا با قابلیت تغییر خودکار
        Entry(key_frame,width=4,borderwidth=3,textvariable=a2[i][j]).grid(column=j,row=i,sticky="E",padx=4,pady=6)#ایجاد یک ورودی 
Label(tab2,text="Enter encrypted text : ",font=("default",13)).grid(column=0,row=1,padx=3,pady=5,sticky="W")
decT=StringVar()
Dec_t=Entry(tab2,width=30,bd= 8,relief=GROOVE,textvariable=decT)
Dec_t.grid(column=1,row=1)

Button(tab2,text="رمزگشایی",command=push_me,borderwidth=2,bg="khaki").grid(column=1,row=2)#ایجاد یک دکمه برای رمز گشایی
        
#******************KEY MATRIX ARRAY(tab1)***********
a=[[1,2,3],[1,2,3],[1,2,3]]
matrix_frame=LabelFrame(tab1,text="3*3 key matrix") #ساخت برچسب برای نامگذاری قالب
matrix_frame.grid(column=1,row=1)
for i in range(3):# برای ایجاد یک آرایه از ورودی ها
    for j in range(3):
        a[i][j]=IntVar()#ایجاد یک متغیر ورودی صحیح با قابلیت بروز شدن
        Entry(matrix_frame,width=4,borderwidth=3,textvariable=a[i][j],).grid(column=j,row=i,sticky='E',padx=3,pady=5)
       #ایجاد ورودی ها و مشخص کردن موقعیت آن ها

#***********************Menu************************
menu_bar=Menu(root)
root.config(menu=menu_bar)

about_menu=Menu(menu_bar)

dir_menu=Menu(about_menu)
dir_menu.add_command(label="محمدرضا قلی پور")
dir_menu.add_command(label="با همکاری امیرحسین نجاتی")

lib_menu=Menu(about_menu)
lib_menu.add_command(label="pure python")
lib_menu.add_command(label="tkinter")
lib_menu.add_command(label="numpy")
lib_menu.add_command(label="math")


about_menu.add_cascade(label="تهیه کننده",menu=dir_menu)
about_menu.add_cascade(label="کتابخانه های استفاده شده",menu=lib_menu)

menu_bar.add_cascade(label='about',menu=about_menu)


#***********************PLAIN TEXT*************************
Label(tab1,text='Enter plain text:').grid(column=0,row=2,padx=4,pady=6) #ایجاد یک برچسب برای گرفتن متن ساده قبل از رمز نگاری

Ptext=StringVar() #متغیر پویا

pText=Entry(tab1,width=32,textvariable=Ptext,borderwidth=5) #ایجاد ورودی
pText.grid(column=1,row=2,padx=2,pady=2)#تعیین موقعیت در صفحه و مقدار حاشیه اطراف
pText.focus()#ست کردن اشاره گر 
#***********************BUTTON***************************************
Action = Button(tab1,text="رمزنگاری",command=click_me,borderwidth=2,bg="khaki") #ایجاد یک دکمه برای شروع عملکرد
Action.grid(column=1,row=4,padx=4,pady=4)
       
entry_label = Label(tab1,text="Enter the value : ",borderwidth=4,font =("Agency FB",16),)
entry_label.grid(column=0,row=1)

#*********************Scrolled text**************
sc=st.ScrolledText(tab1,width=25,height=6,)
sc.grid(column=2,columnspan=4,row=1,padx=3,pady=5)



root.mainloop() #نمایش صفحه گرافیکی


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




