import cv2
import load_model
import numpy as np

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

PATH = "/home/user/repos/heatmap-location-car-plates/video/"
# PATH = "C:/Users/Anna/Documents/sirius/"


def search_number(video, name="test"):
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        logging.debug("Unable to read video")
        ret = False
    else:
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        out = cv2.VideoWriter(PATH + name + "_detect.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (w, h))
        ret = True
    while ret:
        ret, frame = cap.read()
        if ret:
            state, cords = load_model.detect_number(frame)
            if state:
                for c in cords:
                    logging.info(c)
                    pts = np.array(c, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(frame, [pts], True, (255, 0, 0), 2)
    cap.release()
    cv2.destroyAllWindows()
