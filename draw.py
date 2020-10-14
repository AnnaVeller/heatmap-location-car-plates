import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import argparse
import logging.config

logging.config.fileConfig('logging.ini', disable_existing_loggers=True)
log = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='tutorial:')
parser.add_argument('--file', dest='file', default='test.txt', help='File txt with coordinates of plates')
parser.add_argument('--k', dest='k', default=40, help='Pixel for one square')
args = parser.parse_args()
k = int(args.k)

PATH = 'files_heatmap/'
file_path = PATH + args.file
file = open(PATH + args.file)
log.debug(' Open %s' % file_path)
line = file.readline()
w, h, name, fps = line.split()
w = int(w)
h = int(h)
fps = float(fps)
x = []
y = []
line = file.readline()
while line:
    [x1, x2, x3, x4, y1, y2, y3, y4] = list(map(lambda x: float(x),  line.split()))
    [y1, y2, y3, y4] = list(map(lambda y: h-y, [y1, y2, y3, y4]))   # because here y begin in left bottom

    x0 = (x1 + x2 + x3 + x4) / 4
    y0 = (y1 + y2 + y3 + y4) / 4
    x5 = (x1 + x4) / 2
    y5 = (y1 + y4) / 2
    x6 = (x1 + x2) / 2
    y6 = (y1 + y2) / 2
    x7 = (x2 + x3) / 2
    y7 = (y2 + y3) / 2
    x8 = (x3 + x4) / 2
    y8 = (y3 + y4) / 2
    x9 = (x1 + x6) / 2
    y9 = (y1 + y6) / 2
    x10 = (x6 + x2) / 2
    y10 = (y6 + y2) / 2
    x11 = (x0 + x7) / 2
    y11 = (y0 + y7) / 2
    x12 = (x3 + x8) / 2
    y12 = (y3 + y8) / 2
    x13 = (x8 + x4) / 2
    y13 = (y8 + y4) / 2
    x14 = (x0 + x5) / 2
    y14 = (y0 + y5) / 2
    x.extend([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14])
    y.extend([y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14])
    line = file.readline()
file.close()
log.debug(' Closed %s' % file_path)

plt.style.use('dark_background')    # 'dark_background', 'ggplot', 'Solarize_Light2'

fig, ax = plt.subplots()
ax.set_title('15 points of plates\n[%dx%d]' % (w, h))
plt.scatter(x, y, s=1.5)
ax.axis('scaled')    # равный масштаб осей
ax.set_xlim(0, w)
ax.set_ylim(0, h)
path_file_15points = PATH + name + '_6points'
plt.savefig(path_file_15points, bbox_inches='tight')
log.debug(' Draw 15 main plates points and save in in %s' %path_file_15points)

bins = (int(w/k), int(h/k))
range = ((0, w), (0, h))


fig, ax = plt.subplots(nrows=1, ncols=1)
ax.axis('scaled')    # равный масштаб осей
hist = ax.hist2d(x, y, bins=bins, range=range, norm=mcolors.PowerNorm(0.5))
ax.set_xlim(0, w)
ax.set_ylim(0, h)
plt.colorbar(hist[3])
ax.grid(color='black', linewidth=0.5, linestyle='--')
ax.set_title('Heatmap for %s\n%s\n[%dx%d]' % (args.file, str(bins), w, h))
path_heatmap = PATH + name + str(bins)
plt.savefig(path_heatmap, bbox_inches='tight')
log.debug(' Draw heatmap and save it in %s' %path_heatmap)
plt.show()
plt.clf()
plt.cla()
