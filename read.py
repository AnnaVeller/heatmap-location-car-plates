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
                    logging.info(c[0])
                    x1 = c[0][0]
                    x2 = c[1][0]
                    x3 = c[2][0]
                    x4 = c[3][0]
                    y1 = c[0][1]
                    y2 = c[1][1]
                    y3 = c[2][1]
                    y4 = c[3][1]
                    x_mean = (x1+x2+x3+x4)/4
                    y_mean = (y1+y2+y3+y4)/4
                    pts = np.array(c, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(frame, [pts], True, (255, 0, 0), 2)
                    frame = cv2.circle(frame, (int(x_mean), int(y_mean)), 3, (0,0,255), thickness=1)
            out.write(frame)
    cap.release()
    cv2.destroyAllWindows()
