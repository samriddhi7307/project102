import cv2
import random
import time

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture1.jpg", frame)
        result = False

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()
print(time.time())
print(random.randint(0,20))