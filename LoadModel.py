import os
import sys
from NomeroffNet import filters, RectDetector, Detector
import logging.config

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
log = logging.getLogger('load_model')

NOMEROFF_NET_DIR = os.path.abspath('../')
MASK_RCNN_DIR = os.path.join(NOMEROFF_NET_DIR, 'Mask_RCNN')
MASK_RCNN_LOG_DIR = os.path.join(NOMEROFF_NET_DIR, 'logs')
log.debug(' Path to Mask_RCNN ' + MASK_RCNN_DIR)
sys.path.append(NOMEROFF_NET_DIR)

nnet = Detector(MASK_RCNN_DIR, MASK_RCNN_LOG_DIR)
nnet.loadModel('latest')
rectDetector = RectDetector()


def detect_number(img):       # кадр, номер, который должны обнаружить
    NP = nnet.detect([img])
    # Generate image mask.
    cv_img_masks = filters.cv_img_mask(NP)
    # Detect points.
    arrPoints = rectDetector.detect(cv_img_masks)

    state = False  # нашли ли номер?
    if len(arrPoints) > 0:
        state = True

    return state, arrPoints
