# convert video to images
import cv2
import os

frameRate = 0.3 # it will capture image in each 0.5 second

req_video = '' #set path to video
video_name = os.path.splitext(os.path.basename(req_video))[0]

try:
    os.makedirs(f'images_from_video_{video_name}')
except FileExistsError:
    pass

vidcap = cv2.VideoCapture(req_video)

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    
    if hasFrames:
        cv2.imwrite(f"./images_from_video_{video_name}/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

sec = 0
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
