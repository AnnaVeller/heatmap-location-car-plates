import cv2
import logging
import load_model

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
log = logging.getLogger('Heatmap')
log.setLevel(logging.DEBUG)

PATH = "/home/user/repos/heatmap-location-car-plates/video/"
SEC_TO_WRITE = 0.5

def search_number(video, name="test"):
    file = open(PATH + name + '.txt', 'a')
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        log.debug("Unable to read video")
        ret = False
    else:
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        file.write('%d %d %s %d \n' % (w, h, name, fps))
        log.debug('Видео [%dx%d]' % (w, h))
        ret = True
    cadr = 0
    time = 0
    while ret:
        ret, frame = cap.read()
        if ret:
            length = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
            log.debug(" Прошло: %f sec" % length)
            if length-time >= SEC_TO_WRITE:
                log.debug(" Ищем на: %f sec" % length)
                state, cords = load_model.detect_number(frame)
                if state:
                    log.debug('Нашли номер на %d кадре' % cadr)
                    for c in cords:
                        log.info('Координаты' + str(c[0]))
                        file.write(str(c) + '\n')
                time = length
            cadr += 1
    file.close()
    cap.release()
    cv2.destroyAllWindows()
