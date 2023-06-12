import cv2
import datetime
import numpy as np

events=[i for i in dir(cv2) if 'EVENT' in i]
print(events)

def mouse_events(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        text="The Left mouse button is clicked"
        cv2.putText(img, text,(x,y), font,0.5, (0,255,0),2,cv2.LINE_AA)
        cv2.imshow('Lena',img)

img=cv2.imread('G:\MyStuff_Luxa\MyGit\MyPython\MyImage.png',1);# 0 grayscale 1 Color
print(img)
img= cv2.line(img,(0,0),(234,234),(255,0,0),4)
img=cv2.arrowedLine(img, (300,0),(300,300),(0,0,255),10)
img=cv2.rectangle(img,(50,50),(100,100),(0,255,0),5)#-1 will be fill
img=cv2.circle(img,(90,90),50,(0,255,0),5)#-1 will be fill
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,"My Text",(0,300),font,4,(0,250,1),10,cv2.LINE_AA)
cv2.imshow('Lena', img)

cv2.setMouseCallback('Lena', mouse_events)

key = cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite('Image3.png',img)#save image
    cv2.destroyAllWindows()


#cap=cv2.VideoCapture("file.mp4")# play a video
cap=cv2.VideoCapture(0)# default camera
fourcc=cv2.VideoWriter_fourcc(*'XVID')  #fourcc.org
out=cv2.VideoWriter("MyOutPut.avi",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame=cap.read()
    dt =datetime.datetime.now()
    text="MyText"+str(dt)
    font=cv2.FONT_HERSHEY_SIMPLEX
    frame=cv2.putText(frame,text,(10,20),font,1,(0,0,255),2,cv2.LINE_AA)
    out.write(frame)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret==True:
        
        cv2.imshow('Video Frame',frame) 
        if cv2.waitKey(1)==ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()

frame =cv2.imread('G:\MyStuff_Luxa\MyGit\MyPython\MyBolls.png',1)
hsv_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
l_r=np.array([0,120,70])
u_r=np.array([10,255,255])

mask =cv2.inRange(hsv_image,l_r,u_r)
result=cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow('Frame bgr',frame)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()



