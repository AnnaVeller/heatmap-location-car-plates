import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"   # For GPU inference
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # For CPU inference
import warnings
warnings.filterwarnings('ignore')
import read
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
log = logging.getLogger('Heatmap')
log.setLevel(logging.DEBUG)

PATH_VIDEO = "video1.mp4"
NAME = os.path.splitext(PATH_VIDEO)[0]
log.info(" Запустили видео %s" % PATH_VIDEO)
read.search_number(PATH_VIDEO, NAME)
log.info(" Закрыли видео %s/n/n" % PATH_VIDEO)

PATH_VIDEO = "video2.mp4"
NAME = os.path.splitext(PATH_VIDEO)[0]
log.info(" Запустили видео %s" % PATH_VIDEO)
read.search_number(PATH_VIDEO, NAME)
log.info(" Закрыли видео %s/n/n" % PATH_VIDEO)
