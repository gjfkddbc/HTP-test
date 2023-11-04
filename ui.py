from tkinter import *
import tkinter.font
from PIL import ImageTk, Image
from roboflow import Roboflow
import cv2
import sys
import time

window=Tk()
window.title("HTP test")
window.geometry("1280x800+50+50")
window.resizable(False, False)
window.iconphoto(False, tkinter.PhotoImage(file='12.png'))
window.configure(bg="pink")
img = Image.open('backgroundImage.png')
vertex = Image.open('vertex.png')
bg = ImageTk.PhotoImage(img)
vt = ImageTk.PhotoImage(vertex)
 
def font(a, b, c):
    return tkinter.font.Font(family=c, size=a, weight=b )
def openFrame(frame):
	frame.tkraise()

Questionframe = tkinter.Frame(window, relief="solid", width=1180, height=650, bg="pink1", bd=2)


bgi = Label(window, image=bg, borderwidth=0, highlightthickness=0)
bgi.place(x=0, y=0)

Title1 = Label(window, text='그림에 확실하지 않은 부분이 있습니다\n다음 질문에 대답해주세요',fg='violetred4',bg='pink', font=font(20,'bold', 'Courier'),pady=40)
Title1.pack()

Questionframe.place(x=30,y=120)

openFrame(Questionframe)

def Question (s1):
    return Label(Questionframe, text=s1, fg='black', bg='light pink', font=font(18, 'normal', 'Raleway'))

crtr = Question('나무의 기둥이 휘어져 있습니까?')#휘어진 기둥
crtr.grid(row=0, column=0)
only = Question("가지, 수관 없이 그루터기만 그렸습니까?")#그루터기
only.grid(row=1, column=0)
sharp = Question("나무의 가지의 끝이 날카롭습니까?")#날카로운
sharp.grid(row=2, column=0)
kneel = Question("나무의 가지가 힘없이 늘어져 있습니까?")#늘어진 가지 
kneel.grid(row=3, column=0)
cut = Question("나무의 가지가 잘려 있다고 생각하십니까?")#잘린 가지
cut.grid(row=4, column=0)
cloud = Question("나무의 수관이 구름 혹은 목화 솜 모양입니까?")#구름
cloud.grid(row=5, column=0) 
many = Question("나무의 수관이 여러 영역으로 나뉘어 있습니까?")#영역 
many.grid(row=6, column=0)
des = Question("나무의 뿌리를 자세히 묘사했습니까?")#뿌리 
des.grid(row=7, column=0)

ver1 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver1.grid(row=7, column=1)
ver2 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver2.grid(row=7, column=2)
ver3 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver3.grid(row=7, column=3)
ver4 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver4.grid(row=7, column=4)
ver5 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver5.grid(row=7, column=5)
ver6 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver6.grid(row=7, column=6)
ver7 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver7.grid(row=0, column=6)
ver8 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver8.grid(row=1, column=6)
ver9 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver9.grid(row=2, column=6)
ver10 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver10.grid(row=3, column=6)
ver11 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver11.grid(row=4, column=6)
ver12 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver12.grid(row=5, column=6)
ver13 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver13.grid(row=6, column=6)
ver14 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver14.grid(row=8, column=6)
ver15 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver15.grid(row=9, column=6)
ver16 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver16.grid(row=9, column=7)
ver17 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver17.grid(row=9, column=8)
ver18 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver18.grid(row=9, column=9)
ver19 = Label(Questionframe, image=vt, borderwidth=0, highlightthickness=0)
ver19.grid(row=9, column=10)


window.mainloop()