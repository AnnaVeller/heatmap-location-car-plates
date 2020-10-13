import cv2
import time
import logging
import load_model

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
log = logging.getLogger('Heatmap')
log.setLevel(logging.DEBUG)

PATH = "/home/user/repos/heatmap-location-car-plates/video/"
SEC_TO_WRITE = 0   # 0 - process all cadr


def search_number(video, file, name="test"):
    file = open(PATH + file, 'w')      # a - add to file
    cap = cv2.VideoCapture(video)
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    file.write('%d %d %s %d \n' % (w, h, name, fps))
    log.debug(' Video [%dx%d]' % (w, h))
    ret = True
    cadr = 0
    time_between = 0
    start_time = time.time()
    last_cadr_time = time.time() + SEC_TO_WRITE 
    while ret:
        try:
            if time.time()-last_cadr_time >= SEC_TO_WRITE:
                ret, frame = cap.read()
                last_cadr_time = time.time()
                if ret:
                    length = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
                    log.debug(" In video now : %f sec" % length)
                    run_time = time.time() - start_time
                    log.debug(" Last from begin real time : %f sec" % run_time)
                    state, cords = load_model.detect_number(frame)
                    if state:
                        log.debug(' Found on %d cadr' % cadr)
                        for c in cords:
                            log.info(' Number plate: ' + str(c[0]) + '...')
                            x1 = c[0][0]
                            x2 = c[1][0]
                            x3 = c[2][0]
                            x4 = c[3][0]
                            y1 = c[0][1]
                            y2 = c[1][1]
                            y3 = c[2][1]
                            y4 = c[3][1]
                            file.write('%f %f %f %f %f %f %f %f\n' %(x1,x2,x3,x4,y1,y2,y3,y4))
                    cadr += 1
        except KeyboardInterrupt:
            log.debug(' KeyboardInterrupt by ctrl+c')
            break
    file.close()
    cap.release()
    cv2.destroyAllWindows()
