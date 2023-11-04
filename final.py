import threading
from tkinter import *
import tkinter.font
from PIL import ImageTk, Image
from roboflow import Roboflow
import cv2
import sys

def font(a, b, c):
    return tkinter.font.Font(family=c, size=a, weight=b )

global loading
loading = 0
    

def function1():

    global loading
    global cr
    global tr
    global br
    global rt
    global ho
    global fr
    global big
    global size
    global totx
    global toty
    global height
    global width
    global crtr
    global only
    global sharp
    global kneel
    global cut
    global cloud
    global many
    global des

    cr = 0
    tr = 0
    br = 0
    rt = 0
    ho = 0
    fr = 0
    big = 0
    size = 0
    totx = 0
    toty = 0
    height = 0
    width = 0

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

    bgi = Label(window, image=bg, borderwidth=0, highlightthickness=0)
    bgi.place(x=0, y=0)

    loading = 0
    
    load = tkinter.Frame(window, width=1280, height=800, bg="pink1")
    load.place(x=0, y=0)

    bgi2 = Label(load, image=bg, borderwidth=0, highlightthickness=0)
    bgi2.place(x=0, y=0)

    main = tkinter.Frame(window, width=1280, height=800, bg="pink1")

    result = tkinter.Frame(window, width=1280, height=800, bg="pink1")
    bgi3 = Label(result, image=bg, borderwidth=0, highlightthickness=0)
    bgi3.place(x=0, y=0)

 
    loadt = Label(load, text='LOADING...\n그림 인식중',fg='violetred4',bg='pink', font=font(90, 'bold', 'Courier'))
    loadt.place(x=300,y=40)

    compt = Label(load, text='그림인식 완료!',fg='violetred4',bg='pink', font=font(90, 'bold', 'Courier'))
    unchoice = Label(load, text='선택을 완료해주세요',fg='violetred4',bg='pink', font=font(40, 'bold', 'Courier'))


    def gotomain():
        load.place_forget()
        main.place(x=0,y=0)

    def gotores():
        global loading
        global cr
        global tr
        global br
        global rt
        global ho
        global fr
        global big
        global size
        global totx
        global toty
        global height
        global width
        global crtr
        global only
        global sharp
        global kneel
        global cut
        global cloud
        global many
        global des

        cr = 0
        tr = 0
        br = 0
        rt = 0
        ho = 0
        fr = 0
        big = 0
        size = 0
        totx = 0
        toty = 0
        height = 0
        width = 0


        if (crtr=='미선택' or only=='미선택' or kneel=='미선택' or sharp=='미선택' or cut=='미선택' or cloud=='미선택' or many=='미선택' or des=='미선택'):
            unchoice.grid(row=10, column=5)
        else:
            main.place_forget()
            result.place(x=0,y=0)
            print("\n크기 관련:\n")

            if(size>=0.33):#크기 관련 출력
                print("지나치게 큰 나무를 그렸습니다. 공격성이나 충동 조절의 문제가 있을 가능성이 있습니다. 내면의 열등감이 매우 심하여, 이를 과잉보상하려는 시도를 하고 있습니다.")
            elif(size<=0.1):
                print("지나치게 작은 나무를 그렸습니다. 열등감, 부적절감, 자신 없음 등의 특징이 나타납니다. 사회적 상황에서 압박감을 느끼고 있을 수 있습니다.")
            else:
                print("보통 크기의 나무를 그렸습니다. 자신감이나 스스로에 대해 느끼는 적절감이 적당한 수준입니다.")

            print("\n위치 관련:\n")

            if(totx>=0.33 and totx<=0.66 and toty<=0.8 and toty>=0.2):#위치 관련 출력
                print("중앙에 나무를 그렸습니다. 적정한 수준의 안정감을 느끼고 있습니다.")
            elif(totx>0.66 and toty<0.33):
                print("오른쪽 상단에 치우친 나무를 그렸습니다. 불쾌한 과거 기억을 억압하고자 하는 바람, 미래에 대한 과도한 낙관주의, 미래 지향적인 환상을 나타냅니다.")
            elif(totx<0.33 and toty<0.33):
                print("왼쪽 상단에 치우친 나무를 그렸습니다. 퇴행적인 경향성, 불안정감, 위축감, 불안감이 있습니다.")
            elif(totx>0.66 and toty>0.66):
                print("오른쪽 하단에 치우친 나무를 그렸습니다. 미래와 관련된 절망적인 감정을 나타냅니다.")
            elif(totx<0.33 and toty>0.66):
                print("왼쪽 하단에 치우친 나무를 그렸습니다. 과거와 관련된 우울감을 나타냅니다.")
            elif(totx>0.66):
                print("오른쪽에 치우친 나무를 그렸습니다. 안정되어 있고 행동 통제를 잘하며, 지적인 만족감을 선호하는 경향이 있습니다. 감정을 통제하려 하거나 억제하려는 경향이 있습니다.")
            elif(totx<0.33):
                print("왼쪽에 치우친 나무를 그렸습니다. 충동적으로 행동하려는 경향성이나 변화에 대한 욕구, 외향성이 있습니다.")
            elif(toty<0.33):
                print("위쪽에 치우친 나무를 그렸습니다. 욕구나 포부 수준이 높아, 달성하기 어려운 목표를 설정해놓고 스트레스를 느끼고 있습니다. 현실 세계보다는 공상 속을 더 좋아하는 경향이 있습니다.")
            elif(toty>0.66):
                print("아래쪽에 치우친 나무를 그렸습니다. 내면에 상당한 불안정, 부적절감이 있거나, 우울한 상태에 있을 수 있습니다. 공상보다 현실에서 실제를 추구하는 경향이 있습니다.")


            if(tr!=0):
                print("\n기둥 관련:\n")

                if(only=="y"):
                    print("그루터기만 그렸습니다. 심한 유약감, 위축감, 우울감을 가지고 있습니다.")
                else:
                    if (cr!=0):
                        if((cr["height"]/tr["height"])>=1 and (cr["height"]/tr["height"])<=2 and (cr["width"]/width)>=0.4):#기둥 관련 출력
                            print("지나치게 큰 기둥을 그렸습니다. 실제로는 자아의 강도가 약하고 부족하지만, 이에 따른 불안감을 과잉보상하려는 시도를 하고 있습니다.")
                            big=1
                        elif((cr["height"]/tr["height"])>=1 and (cr["height"]/tr["height"])<=2 and (cr["width"]/width)<=0.3):
                            print("지나치게 좁거나 가는 기둥을 그렸습니다. 자기 자신에 대해 위축되고 약하게 느끼고 무력해있습니다.")
                        else:
                            print("보통 크기의 기둥을 그렸습니다.")
                    if (cr==0 and br!=0):
                        if((br["height"]/tr["height"])>=1 and (br["height"]/tr["height"])<=2 and (br["width"]/width)>=0.4):#기둥 관련 출력
                            print("지나치게 큰 기둥을 그렸습니다. 실제로는 자아의 강도가 약하고 부족하지만, 이에 따른 불안감을 과잉보상하려는 시도를 하고 있습니다.")
                            big=1
                        elif((br["height"]/tr["height"])>=1 and (br["height"]/tr["height"])<=2 and (br["width"]/width)<=0.3):
                            print("지나치게 좁거나 가는 기둥을 그렸습니다. 자기 자신에 대해 위축되고 약하게 느끼고 무력해있습니다.")
                        else:
                            print("보통 크기의 기둥을 그렸습니다.")
                    if(crtr=="y" and only=="n"):
                        print("휘어진 기둥를 그렸습니다. 자아의 힘이 외부 요인에 의해 손상되거나 압박을 받고 있습니다.")

            print("\n가지 관련:\n")

            if(br==0):#가지 관련 출력
                print("가지를 그리지 않았습니다. 세상과의 상호작용에 있어 매우 억제되어 있으며, 사회적으로 심하게 위축되어있거나 우울감을 느끼고 있습니다.")
            elif(cr!=0):
                if((br["width"]*br["height"])/(cr["width"]*cr["height"])>=0.5):
                    print("지나치게 큰 가지를 그렸습니다. 성취동기나 포부 수준이 매우 높습니다. 주변과의 상호작용에 자신이 없지만, 이를 보상하려 과잉활동적인 행동을 하고 있습니다.")
                elif((br["width"]*br["height"])/(cr["width"]*cr["height"])<=0.2):
                    print("지나치게 작은 가지를 그렸습니다. 상황에 대처하는 데 있어 수동적이고, 세상을 향해 나아가는 태도가 부족합니다.")
            elif(big==1 and br["width"]>tr["width"]):
                print("옆으로 퍼지는 가지를 그렸습니다. 주변으로부터 만족을 얻는 것을 두려워하고 있기 때문에, 스스로에게서 만족을 찾으려 하고 있습니다.")
            elif(cr==0 and (br["height"]/tr["height"])>=0.5):
                print("길쭉한 가지를 그렸습니다. 지나치게 내향적이고 위축되어 있습니다.")
            else:
                print("보통 크기의 가지를 그렸습니다.")
            if(sharp=="y"):
                print("끝이 날카로운 가지를 그렸습니다. 내면에 적대감이나 공격성이 내제되어 있습니다.")
            if(kneel=="y"):
                print("늘어진 가지를 그렸습니다. 심한 우울감, 무기력감을 가지고 있으며, 사회적 상호작용 능력이 매우 억제되어 있습니다.")
            if(cut=="y"):
                print("끝이 잘린 가지를 그렸습니다. 스스로의 발전과 활동이 억제되어있다고 느끼고 있습니다.")


            if(cr!=0):
                print("\n수관 관련:\n")
                if((cr["width"]/width)<=0.4 and (tr["height"]/height)>=0.33):#수관 관련 출력
                    print("지나치게 작은 수관을 그렸습니다. 이러한 그림을 그린 사람은 주로 정신 발달이 지체, 퇴행하고 있습니다.")
                elif((cr["width"]/width)>=0.5 and (tr["height"]/height)<=0.2):
                    print("지나치게 큰 수관을 그렸습니다. 자신감과 야망을 가지고 무언가에 몰두하고 있습니다.")
                elif((cr["width"]/width)>=0.5 and (tr["width"]/width)<=0.3):
                    print("지나치게 큰 수관을 그렸습니다. 완전한 만족을 위해 마음의 안정을 상실하고 있습니다.")
                else:
                    print("보통 크기의 수관을 그렸습니다.")
                if(cloud=="y"):
                    print("구름 모양의 수관을 그렸습니다. 타인에게 잘 동조하며 생활에 잘 적응하고 있으며, 평범하고 형식적인 사람임을 의미합니다.")
                if(many=="y"):
                    print("수관을 여러 영역으로 나누어 그렸습니다. 자신이 의도한 것을 은폐시키며 현실과의 접촉을 두려워하며, 조심성이 많습니다.")

            print("\n뿌리 관련:\n")

            if(rt==0):
                print("뿌리를 그리지 않았습니다. 자신에 대한 불안정감을 느끼고 자신감이 없습니다.")
            elif(des==0):
                print("뿌리를 자세하게 묘사했습니다. 실제로는 자신에 대해 불안정하게 느끼지만, 이를 과도하게 보상하려고 시도하고 있다.")

            print("\n기타:\n")

            if(ho==1):
                print("나무의 기둥에 옹이구멍을 그렸습니다. 성장 과정에서 자아의 상처가 생겼을 가능성이 있습니다.")
            if(fr==1):
                print("나무에 열매를 그렸습니다. 사랑과 관심을 받거나 주길 원하고 있습니다.")
    

    btnTomain = tkinter.Button(load, text="시작하기", command= gotomain)

    def refresh():
        if loading == 1:   
            loadt.place_forget()
            btnToref.place_forget()
            compt.place(x=300,y=40)
            btnTomain.place(x=600, y=600)

    btnToref = tkinter.Button(load, text="새로고침", command=refresh)
    btnToref.place(x=600,y=600)

    bgi2 = Label(main, image=bg, borderwidth=0, highlightthickness=0)
    bgi2.place(x=0, y=0)


    Title1 = Label(main, text='그림에 확실하지 않은 부분이 있습니다\n다음 질문에 대답해주세요',fg='violetred4',bg='pink', font=font(20,'bold', 'Courier'))
    Title1.place(x=340, y=40)

    Questionframe = tkinter.Frame(main, relief="solid", width=1180, height=650, bg="pink1", bd=2)
    Questionframe.place(x=30,y=120)

    def Question (s1):
        return Label(Questionframe, text=s1, fg='black', bg='light pink', font=font(18, 'normal', 'Raleway'))
    
    crtr=tkinter.StringVar()
    crtr.set("미선택")
    only=tkinter.StringVar()
    only.set("미선택")
    sharp=tkinter.StringVar()
    sharp.set("미선택")
    kneel=tkinter.StringVar()
    kneel.set("미선택")
    cut=tkinter.StringVar()
    cut.set("미선택")
    cloud=tkinter.StringVar()
    cloud.set("미선택")
    many=tkinter.StringVar()
    many.set("미선택")
    des=tkinter.StringVar()
    des.set("미선택")


    crtrl = Question('나무의 기둥이 휘어져 있습니까?')#휘어진 기둥
    crtrl.grid(row=0, column=0)
    crtry=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=crtr)
    crtry.grid(row=0, column=7)
    crtrn=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=crtr)
    crtrn.grid(row=0, column=8)

    onlyl = Question("가지, 수관 없이 그루터기만 그렸습니까?")#그루터기
    onlyl.grid(row=1, column=0)
    onlyy=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=only)
    onlyy.grid(row=1, column=7)
    onlyn=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=only)
    onlyn.grid(row=1, column=8)

    sharpl = Question("나무의 가지의 끝이 날카롭습니까?")#날카로운
    sharpl.grid(row=2, column=0)
    sharpy=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=sharp)
    sharpy.grid(row=2, column=7)
    sharpn=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=sharp)
    sharpn.grid(row=2, column=8)

    kneell = Question("나무의 가지가 힘없이 늘어져 있습니까?")#늘어진 가지 
    kneell.grid(row=3, column=0)
    kneely=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=kneel)
    kneely.grid(row=3, column=7)
    kneeln=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=kneel)
    kneeln.grid(row=3, column=8)

    cutl = Question("나무의 가지가 잘려 있다고 생각하십니까?")#잘린 가지
    cutl.grid(row=4, column=0)
    cuty=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=cut)
    cuty.grid(row=4, column=7)
    cutn=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=cut)
    cutn.grid(row=4, column=8)

    cloudl = Question("나무의 수관이 구름 혹은 목화 솜 모양입니까?")#구름
    cloudl.grid(row=5, column=0) 
    cloudy=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=cloud)
    cloudy.grid(row=5, column=7)
    cloudn=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=cloud)
    cloudn.grid(row=5, column=8)

    manyl = Question("나무의 수관이 여러 영역으로 나뉘어 있습니까?")#영역 
    manyl.grid(row=6, column=0)
    manyy=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=many)
    manyy.grid(row=6, column=7)
    manyn=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=many)
    manyn.grid(row=6, column=8)

    desl = Question("나무의 뿌리를 자세히 묘사했습니까?")#뿌리 
    desl.grid(row=7, column=0)
    desy=tkinter.Radiobutton(Questionframe, text="예", value="y", variable=des)
    desy.grid(row=7, column=7)
    desn=tkinter.Radiobutton(Questionframe, text="아니오", value="n", variable=des)
    desn.grid(row=7, column=8)

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
    
    btnTores = tkinter.Button(Questionframe, text="결과보기", command=gotores)
    btnTores.grid(row=9, column=5)

    window.mainloop()


def function2():

    global loading
    global cr
    global tr
    global br
    global rt
    global ho
    global fr
    global big
    global size
    global totx
    global toty
    global height
    global width

    img2 = cv2.imread("./tree.jpg", cv2.IMREAD_UNCHANGED)

    height = img2.shape[0]
    width = img2.shape[1]
    img = cv2.resize(img2, dsize=(0, 0), fx=(320/width), fy=(320/height), interpolation=cv2.INTER_LINEAR)
    height = img.shape[0]
    width = img.shape[1]
    imgsz=height*width

    rf = Roboflow(api_key="snoFcuVjU5ifyxAu8czp")
    project = rf.workspace().project("re-ittgd")
    model = project.version(35).model

    cr = 0
    tr = 0
    br = 0
    rt = 0
    ho = 0
    fr = 0
    big = 0
    size = 0
    totx = 0
    toty = 0



    results = model.predict(img,confidence=40,overlap=30).json()#인식 중

    for i in range(0,len(list(results["predictions"]))):
        result = list(results["predictions"])[i]
        if(result["class_id"]==3):#수관
            cr=result
        if(result["class_id"]==2):#가지
            br=result
        if(result["class_id"]==7):#기둥
            tr=result
        if(result["class_id"]==0):
            fr=result
        if(result["class_id"]==4):
            ho=result
        if(result["class_id"]==6):
            rt=result

    loading = 1

    if (cr!=0 and br!=0 and tr!=0):#전부 있을 때
        size=((cr["width"] * cr["height"]) + (tr["width"] * tr["height"]))/imgsz #크기 파트 
        totx=(cr["x"]+tr["x"]+br["x"])/(3*width) #위치 파트
        toty=(cr["y"]+tr["y"]+br["y"])/(3*height) #위치 파트
    elif (cr==0 and br!=0 and tr!=0):#수관만 없을 때
        size=((br["width"] * br["height"]) + (tr["width"] * tr["height"]))/imgsz 
        totx=(tr["x"]+br["x"])/(2*width) 
        toty=(tr["y"]+br["y"])/(2*height) 
    elif (cr!=0 and br==0 and tr!=0):#가지만 없을 때
        size=((cr["width"] * cr["height"]) + (tr["width"] * tr["height"]))/imgsz 
        totx=(tr["x"]+cr["x"])/(2*width) 
        toty=(tr["y"]+cr["y"])/(2*height) 
    elif (cr==0 and br==0 and tr!=0):#가지,수관 둘다 없을 때
        size=((tr["width"] * tr["height"]))/imgsz 
        totx=(tr["x"])/(width) 
        toty=(tr["y"])/(height)
    elif (cr==0 and br==0 and tr==0):#가지, 수관, 기둥 없을 때
        print("\그림을 인식하지 못했습니다.")
        sys.exit("종료")


thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)


thread1.start()
thread2.start()


thread1.join()
thread2.join()
