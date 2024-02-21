import cv2
import matplotlib.pyplot as plt
config_file = 'Image-recognition_L-1_T-1/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'Image-recognition_L-1_T-1/frozen_inference_graph.pb.pb'

model = cv2.dnn_DetectionModel(frozen_model,config_file)
classLabels = []
file_name = 'Image-recognition_L-1_T-1/labels.txt'
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
# print(classLabels)
# print(len(classLabels))
model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean(127.5)
model.setInputSwapRB(True)
# img = cv2.imread('man.jpg')
# plt.imshow(img)
# plt.show()
# ClassIndex, confidece, bbox = model.detect(img, confThreshold = 0.5)
# print(ClassIndex)
# font_scale = 3
# font = cv2.FONT_HERSHEY_PLAIN
# for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
#     cv2.rectangle(img,boxes,(255,0,0), 2)
#     cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font, fontScale=font_scale, color=(0,255,0), thickness=3)
# # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR))
# plt.imshow(img)
# plt.show()

vid = cv2.VideoCapture("Image-recognition_L-1_T-1/video3.mp4")  #detect by video
# vid = cv2.VideoCapture(1)  #detect by WebCam

if not vid.isOpened():
    vid = cv2.VideoCapture(0)
if not vid.isOpened():
    # raise IOError("Can not open Webcam")
    raise IOError("Can not open video")

font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN

while True:
    ret, frame = vid.read()
    ClassIndex, confidece, bbox = model.detect(frame, confThreshold= 0.55)

    print(ClassIndex)
    if(len(ClassIndex)!=0):
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
            if(ClassInd<=80):
                cv2.rectangle(frame,boxes,(255,0,0), 2)
                cv2.putText(frame,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font, fontScale=font_scale, color=(0,255,0), thickness=3)
    cv2.imshow('Object Detection : ', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()

