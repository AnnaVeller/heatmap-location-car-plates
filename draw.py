import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='tutorial:')
parser.add_argument('--file', dest='file', default="test.txt", help="File txt with")
args = parser.parse_args()

PATH = "/home/user/repos/heatmap-location-car-plates/files_heatmap/"
file = open(PATH + args.file)
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
    x_mean = x1 + x2 + x3 + x4
    [y1, y2, y3, y4] = list(map(lambda x: h-x, [y1, y2, y3, y4]))
    y_mean = y1 + y2 + y3 + y4
    x.extend([x1, x2, x3, x4, x_mean])
    y.extend([y1, y2, y3, y4, y_mean])
    line = file.readline()
file.close()

bins = (25, 25)
range = ((0, w), (0, h))
hist = plt.hist2d(x, y, bins=bins, range=range)
plt.colorbar(hist[3])
plt.savefig(PATH + name + str(bins), bbox_inches='tight')
plt.clf()
plt.cla()
