import cv2
import logging
import load_model

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
log = logging.getLogger('Heatmap')
log.setLevel(logging.DEBUG)

PATH = "/home/user/repos/heatmap-location-car-plates/video/"

def search_number(video, name="test"):
    file = open(name + '.txt', 'a')
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        log.debug("Unable to read video")
        ret = False
    else:
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        file.write('%d %d %s' % (w,h,name))
        log.debug('Видео [%dx%d]' % (w, h))
        ret = True
    cadr = 0
    delta_time = 0
    time_between = 0
    while ret:
        ret, frame = cap.read()
        cadr += 1
        if ret:
            length = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
            delta_time = length - delta_time
            if time_between >= 0.5:
                state, cords = load_model.detect_number(frame)
                if state:
                    log.debug('Нашли номер на %d кадре' % cadr)
                    for c in cords:
                        log.info('Координаты' + str(c[0]))
                        file.write(str(c))
                time_between = 0
            else:
                time_between = time_between + length - delta_time
            log.debug(" Прошло: %f sec, между обработанными кадрами %f sec" % (length, time_between))
    cap.release()
    cv2.destroyAllWindows()
