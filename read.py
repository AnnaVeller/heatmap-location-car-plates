import cv2
import logging
import load_model

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
log = logging.getLogger('Heatmap')
log.setLevel(logging.DEBUG)

PATH = "/home/user/repos/heatmap-location-car-plates/video/"
SEC_TO_WRITE = 0.5


def search_number(video, name="test"):
    file = open(PATH + name + '.txt', 'w')      # a - дозапись
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
                        x1 = c[0][0]
                        x2 = c[1][0]
                        x3 = c[2][0]
                        x4 = c[3][0]
                        y1 = c[0][1]
                        y2 = c[1][1]
                        y3 = c[2][1]
                        y4 = c[3][1]
                        file.write('%f %f %f %f %f %f %f %f\n' %(x1,x2,x3,x4,y1,y2,y3,y4))
                time = length
            cadr += 1
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            log.info("Нажали q для выхода")
            break
    file.close()
    cap.release()
    cv2.destroyAllWindows()
