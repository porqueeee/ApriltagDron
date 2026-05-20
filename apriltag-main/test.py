import sys
sys.path.insert(0, "C:/Users/valef/Desktop/ApriltagDrone/apriltag-main")  

from apriltag import apriltag  

import cv2
import numpy as np
#from apriltag import apriltag

imagepath = '/tmp/tst.jpg'
image     = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)
detector = apriltag("tag36h11")

detections = detector.detect(image)

print("Saw tags {} at\n{}". \
        format([d['id']     for d in detections],
                np.array([d['center'] for d in detections])))
