import cv2
print(cv2.__version__)
evt=0
def mouseClick(event,xPos,yPos,flags,params):
    global pnt1
    global pnt2
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        pnt1=(xPos,yPos)
        evt=event
    if event==cv2.EVENT_LBUTTONUP:
        print(event)
        pnt2=(xPos,yPos)
        evt=event
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)



width = 700
height = 500
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore, frame = cam.read()
    if evt==4:
        cv2.rectangle(frame,pnt1,pnt2,(0,0,255),2)
        ROI=frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
        cv2.imshow('ROI', ROI)
        cv2.moveWindow('ROI', int(width*1.1),0)
    if evt == 5:
        cv2.destroyWindow('ROI')
        evt=0
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) %0xff == ord('q'):
        break
cam.release()


