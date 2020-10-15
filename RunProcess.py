import os
import warnings
warnings.filterwarnings('ignore')
import argparse
import logging.config
import SearchNumbers

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
log = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='tutorial:')
parser.add_argument('--video', dest='video', default='test.mp4', help='Videofile or stream url')
parser.add_argument('--file', dest='filename', default='no', help='File with coordinates of plates')
parser.add_argument('--type', dest='type', default='v', help='s-stream, v-videofile')
parser.add_argument('--gpu', dest='gpu', default='no', help='If you use gpu write --gpu=yes')
args = parser.parse_args()

if args.gpu == 'yes':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'   # For GPU inference
    os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"     # For GPU inference
else:
    os.environ['CUDA_VISIBLE_DEVICES'] = ''  # For CPU inference

if args.type == 'v':
    name = os.path.splitext(args.video)[0]      # name of video without file extension
    PATH_VIDEO = 'video/'+ args.video
else:
    name = 'test_stream'
    PATH_VIDEO = args.video

if args.filename == 'no':       # if name of file with txt doesn't point - it will be name of video
    filename = name + '.txt'
else:
    filename = args.filename

log.info(' Run video %s' % args.video)
SearchNumbers.search_number(PATH_VIDEO, filename, args.type, name)
log.info(' Close video %s \n\n' % args.video)
