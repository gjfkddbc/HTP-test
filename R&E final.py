from roboflow import Roboflow
import cv2
import sys

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


cr=0
tr=0
br=0
rt=0
ho=0
fr=0
big=0
size=0
totx=0
toty=0

results = model.predict(img,confidence=40,overlap=30).json()#인식 중
#model.predict(img, confidence=40, overlap=30).save("prediction.jpg")

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

for key, value in tr.items():
    print(key, value)

print("그림의 인식이 다 되었습니다. 다음 질문들에 답해 주시기를 바랍니다.")

crtr = input("나무의 기둥이 휘어져 있습니까? y/n")#휘어진 기둥
only = input("가지, 수관 없이 그루터기만 그렸습니까? y/n")#그루터기
sharp = input("나무의 가지의 끝이 날카롭습니까? y/n")#날카로운
kneel = input("나무의 가지가 힘없이 늘어져 있습니까? y/n")#늘어진 가지 
cut = input("나무의 가지가 잘려 있다고 생각하십니까? y/n")#잘린 가지
cloud = input("나무의 수관이 구름 혹은 목화 솜 모양입니까? y/n")#구름
many = input("나무의 수관이 여러 영역으로 나뉘어 있습니까? y/n")#영역 
des = input("나무의 뿌리를 자세히 묘사했습니까? y/n")#뿌리 

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

