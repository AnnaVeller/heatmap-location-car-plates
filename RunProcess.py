import os
#os.environ['CUDA_VISIBLE_DEVICES'] = '0'   # For GPU inference
os.environ['CUDA_VISIBLE_DEVICES'] = ''  # For CPU inference
import warnings
warnings.filterwarnings('ignore')
import argparse
import logging.config
import SearchNumbers

logging.config.fileConfig('logging.ini', disable_existing_loggers=True)
log = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='tutorial:')
parser.add_argument('--video', dest='video', default='test_mini2.mp4', help='Videofile or stream url')
parser.add_argument('--file', dest='filename', default='test.txt', help='File with coordinates of plates')
parser.add_argument('--type', dest='type', default='v', help='s-stream, v-videofile')
args = parser.parse_args()

PATH = 'video/'
name = os.path.splitext(args.video)[0]
log.info(' Run video %s' % args.video)
SearchNumbers.search_number(PATH + args.video, args.filename, args.type, name)
log.info(' Close video %s \n\n' % args.video)
