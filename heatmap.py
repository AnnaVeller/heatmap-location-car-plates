import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"   # For GPU inference
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # For CPU inference
import warnings
warnings.filterwarnings('ignore')
import read
import logging
import draw

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
log = logging.getLogger('Heatmap')
log.setLevel(logging.DEBUG)

PATH_VIDEO = "test_mini3.mp4"
NAME = os.path.splitext(PATH_VIDEO)[0]
log.info(" Запустили видео %s" % PATH_VIDEO)
x,y, range = read.search_number(PATH_VIDEO, NAME)
log.info(" Закрыли видео %s \n\n" % PATH_VIDEO)
draw.draw_hist(x,y, range)

#PATH_VIDEO = "test_mini2.mp4"
#bins = (9, 9)
#NAME = os.path.splitext(PATH_VIDEO)[0]
#log.info(" Запустили видео %s" % PATH_VIDEO)
#x,y, range = read.search_number(PATH_VIDEO, NAME)
#log.info(" Закрыли видео %s \n\n" % PATH_VIDEO)
#draw.draw_hist(x,y, range)


#PATH_VIDEO = "test_mini4.mp4"
#bins = (11, 11)
#NAME = os.path.splitext(PATH_VIDEO)[0]
#log.info(" Запустили видео %s" % PATH_VIDEO)
#read.search_number(PATH_VIDEO, NAME, bins)
#log.info(" Закрыли видео %s/n/n" % PATH_VIDEO)


