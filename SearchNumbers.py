import cv2
import time
import logging.config
import LoadModel

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
log = logging.getLogger(__name__)

PATH = 'files_heatmap/'
SEC_TO_WRITE = 0.5   # 0 - process all cadr


def search_number(video, file, type, name_video='test'):
    
    path_to_file_txt = PATH + file
    file = open(path_to_file_txt, 'w')      # a - add to file
    log.debug(' Created/opened %s' % path_to_file_txt)

    cap = cv2.VideoCapture(video)
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    file.write('%d %d %s %d \n' % (w, h, name_video, fps))
    log.debug(' Video [%dx%d]' % (w, h))
    ret = True

    if not cap.isOpened():
        ret = False
        log.debug(" %s didn't open" % video)
    
    last_cadr_time_video = -SEC_TO_WRITE  # time of last capture cadr on video 
    start_time = time.time()  # time os starting process video/stream
    last_cadr_time_stream = time.time() - SEC_TO_WRITE # time of last capture cadr on stream
    
    while ret:
        ret, frame = cap.read()
        length = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
        
        try:
            if (time.time()-last_cadr_time_stream >= SEC_TO_WRITE and type=='s') or (length-last_cadr_time_video >= SEC_TO_WRITE and type=='v'):
                if ret:
                    if type=='v':
                        last_cadr_time_video = length
                        log.debug(' In video now : %f sec' % length)
                    else:
                        last_cadr_time_stream = time.time()
                    run_time = time.time() - start_time
                    log.debug(' Last from begin in real time : %f sec' %run_time)
                    state, cords = LoadModel.detect_number(frame)
                    if state:
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
        
        except KeyboardInterrupt:
            log.debug(' KeyboardInterrupt by ctrl+c')
            break
    
    file.close()
    cap.release()
    cv2.destroyAllWindows()

