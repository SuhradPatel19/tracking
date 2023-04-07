import cv2

# small change

video=cv2.VideoCapture("bb3.mp4")

# load the tracker
tracker=cv2.TrackerCSRT_create()
# print(tracker)

# tracker should take the first frame in video
returned,myImage=video.read()
#print(myImage)

bbox=cv2.selectROI("Tracking",myImage,False)
print("The bbox is: ",bbox)

# init the tracker
tracker.init(myImage,bbox)

def drawBox(myImage,myBox):
    x,y,w,h=int(myBox[0]),int(myBox[1]),int(myBox[2]),int(myBox[3])

    cv2.rectangle(myImage,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(myImage,"Tracking",(100,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(000,255,255),1)
    

while True:
    dummy,frame=video.read()

    success,myBox= tracker.update(frame)
    print(myBox)

    if(success==True):
        drawBox(frame,myBox)
    else:
        cv2.putText(frame,"Lost Object",(100,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(000,255,255),1)


    cv2.imshow("object tracking",frame)
    if cv2.waitKey(25)==32:                         
        break
video.release()
cv2.release()
cv2.destroyAllWindows()            