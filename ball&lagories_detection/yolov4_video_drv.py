import numpy as np 
import argparse
import logging
import imutils
import time
import cv2
import sys
import os


# Initiate Logging 
# logging.basicConfig(
#     level=logging.INFO,
#     format=f"%(asctime)s [%(levelname)s:] ->  %(message)s",
#     handlers=[
#         logging.FileHandler("vid_info.log"),
#         logging.StreamHandler(sys.stdout)
#     ])

# logging.info(msg="Start Session")

# Define Arguments to script
ap  =  argparse.ArgumentParser()
ap.add_argument('-i', '--input' , required=True, help='path to input video')
ap.add_argument('-o', '--output', required=True, help='path to output video')
ap.add_argument('-y', '--yolo'  , required=True, help='Base path to yolo dir')
ap.add_argument('-c', '--confidence', type=float, default=0.2, help='Minimum probability to filter weak detections')
ap.add_argument('-t', '--threshold' , type=float, default=0.3, help='threshold when applying non-maxima suppression')
args = vars(ap.parse_args())
logging.info(msg='Finish Defining Arguments')

# Load Yolo directory 
labels_path  = os.path.sep.join([args['yolo'], "classes.names"])
weights_path = os.path.sep.join([args['yolo'], 'yolov4.weights'])
config_path  = os.path.sep.join([args['yolo'], 'yolov4.cfg'])
# logging.info(msg='Finish Loading Files')

# Get data from label names file and assign color to each
np.random.seed(42)
LABELS = open(labels_path).read().strip().split('\n')
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype='uint8')
# logging.info(msg='Finish Defining Label names')

# Load out Yolo object detection 
net    =  cv2.dnn.readNetFromDarknet(config_path, weights_path)
# logging.info(msg='Finish load model to dnn object')

# Read output layer names
ln     =  net.getLayerNames()
ln     =  [ln[i - 1] for i in net.getUnconnectedOutLayers()]
# logging.info(msg='Finish read output layer name')

# initiate video stream, pointer to output video file
if len(args['input']) == 1:
    stream = int(args['input'])
else:
    stream = args['input']
vs     =  cv2.VideoCapture(stream)
writer =  None
(W, H) =  (None, None)

# try to determine the total number of frames in the video file
try:
	prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() else cv2.CAP_PROP_FRAME_COUNT
	total = int(vs.get(prop))
	# logging.info(msg ="{} total frames in video".format(total))
# an error occurred while trying to determine the total
# number of frames in the video file
except:
	# logging.info("Could not determine Number of frames in video")
	# logging.info("No approx. completion time can be provided")
	total = -1
 

# Loop over frames from the video
count = 1
while True:
    # read next frame from file
    (grabbed, frame) = vs.read()

    if not grabbed:
        # logging.info(msg='Reach end of frame')
        break

    #increment counter
    # logging.info(msg=f'Read {count} frame')
    count+=1

    # if the frame dimensions are empty, grab them
    if W is None or H is None:
        (H, W) = frame.shape[:2]

    # Construct a blob from the input frame then perform a forward
    blob  =  cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    #logging.info(msg='Constructed a blob image')

    # Feed blob image to Neural netwotk and inference output
    #logging.info(msg='Feed image to neural network')
    net.setInput(blob)
    start  = time.time()
    layerOutputs = net.forward(ln)
    end   = time.time()
    # logging.info(msg=f'Take {end-start} sec Inference time')

    # Initialize out lists
    boxes       = []
    confidences = []
    classIDs    = []

    # loop over each of the layer outputs
    #logging.info(msg='Start looping over each layer')
    for output in layerOutputs:
		# loop over each of the detections
        #logging.info(msg='Start looping over each Detection')
        for detection in output:
			# extract the class ID and confidence (i.e., probability)
			# of the current object detection
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
			# filter out weak predictions by ensuring the detected
			# probability is greater than the minimum probability
            if confidence > args["confidence"]:
				# scale the bounding box coordinates back relative to
				# the size of the image, keeping in mind that YOLO
				# actually returns the center (x, y)-coordinates of
				# the bounding box followed by the boxes' width and
				# height
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
				# use the center (x, y)-coordinates to derive the top
				# and and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
				# update our list of bounding box coordinates,
				# confidences, and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping
	# bounding boxes
    #logging.info(msg='Start Non-maximam supperssion routine')
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
		args["threshold"])

    #logging.info(msg='Draw Bounding Boxes')
	# ensure at least one detection exists
    if len(idxs) > 0:
		# loop over the indexes we are keeping
        for i in idxs.flatten():
			# extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
			# draw a bounding box rectangle and label on the frame
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(LABELS[classIDs[i]],
				confidences[i])
            cv2.putText(frame, text, (x, y - 5),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    cv2.imshow('Stream', frame)
    cv2.waitKey(1)
    
    # check if the video writer is None
    #logging.info(msg=f"Write {count} frame")
    if writer is None:
		# initialize our video writer
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(args["output"], fourcc, 30,(frame.shape[1], frame.shape[0]), True)
		# some information on processing single frame
        if total > 0:
            elap = (end - start)
            #logging.info("Single frame took {:.4f} seconds".format(elap))
            #logging.info("Estimated total time to finish: {:.4f}".format(elap * total))
	# write the output frame to disk
    writer.write(frame)
    logging.info(msg='-------------------------')

# release the file pointers
# logging.info("Cleaning up...")
writer.release()
vs.release()
