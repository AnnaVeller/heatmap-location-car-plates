import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"   # For GPU inference
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # For CPU inference
import warnings
warnings.filterwarnings('ignore')
import argparse
import logging
import read

parser = argparse.ArgumentParser(description='tutorial:')
parser.add_argument('--video', dest='video', default="test_mini2.mp4", help="Video file")

parser.add_argument('--file', dest='filename', default="test.txt", help="File with cordinates of plates")
args = parser.parse_args()


logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
log = logging.getLogger('Heatmap')
log.setLevel(logging.DEBUG)


name = os.path.splitext(args.video)[0]
log.info(" Run video %s" % args.video)
read.search_number(args.video, args.filename, name)
log.info(" Close video %s \n\n" % args.video)
