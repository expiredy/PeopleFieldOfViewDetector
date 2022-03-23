import cv2 as opencv
import imutils

HOGCV = opencv.HOGDescriptor
scale_percent = 60 # percent of original size


def detect(frame):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        opencv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        opencv.putText(frame, f'person {person}', (x,y), opencv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
    opencv.putText(frame, 'Status : Detecting ', (40,40), opencv.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    opencv.putText(frame, f'Total Persons : {person-1}', (40,70), opencv.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    return frame

# def humanDetector(args):
#     image_path = args["image"]
#     video_path = args['video']
#     if str(args["camera"]) == 'true' : camera = True 
#     else : camera = False
#     writer = None
#     if args['output'] is not None and image_path is None:
#         writer = opencv.VideoWriter(args['output'],opencv.VideoWriter_fourcc(*'MJPG'), 10, (600,600))
#     if camera:
#         print('[INFO] Opening Web Cam.')
#         detectByCamera(ouput_path,writer)
#     elif video_path is not None:
#         print('[INFO] Opening Video from path.')
#         detectByPathVideo(video_path, writer)
#     elif image_path is not None:
#         print('[INFO] Opening Image from path.')
#         detectByPathImage(image_path, args['output'])


def connect_detection_session():
    global HOGCV
    HOGCV = opencv.HOGDescriptor()
    HOGCV.setSVMDetector(opencv.HOGDescriptor_getDefaultPeopleDetector())


def test_from_video():
    video_capturing = opencv.VideoCapture("./database/video.mp4")
    is_running = True
    connect_detection_session()
    while is_running:
        try:
            frame_status, image_frame = video_capturing.read()

            if opencv.waitKey(1) == 27:
                is_running = False
            if frame_status:
                width = int(image_frame.shape[1] * scale_percent / 100)
                height = int(image_frame.shape[0] * scale_percent / 100)
                dim = (width, height)
                
                # resize image
                resized = opencv.resize(image_frame, dim, interpolation = opencv.INTER_AREA)
                image_frame = imutils.resize(image_frame , width=min(800,image_frame.shape[1]))
                image_frame = detect(image_frame)
            opencv.imshow("Debug window", image_frame)
        except KeyboardInterrupt:
            is_running = False




if __name__ == "__main__":
    test_from_video()