import cv2 
import dropbox
import time 
import random 

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False

    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = 'sl.AyXHl2EoB4yq62gNzgnLEBVNy-ska4kNf2AAtouHiBk_4FMbFotNiPcG-w74X2EUPjiEn9t-W_WRHh5m85B78QuCTkgQfAIi4vIx1gOAK7eQLLVPlCNz-JK8c9xWoJ9AQomWpn0'
    file = img_name
    file_from = file
    file_to = "/text"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_file(name)

main()
