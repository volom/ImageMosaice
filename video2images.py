# convert video to images
import cv2
import os

frameRate = 0.3 # it will capture image in each 0.5 second

req_video = '' #set path to video
data = cv2.VideoCapture(req_video)
# count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
fps = int(data.get(cv2.CAP_PROP_FPS))

# calculate dusration of the video
seconds = int(frames / fps)
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

for i in range(int(round(seconds/frameRate, 0))):
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
