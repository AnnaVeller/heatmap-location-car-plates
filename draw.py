import matplotlib.pyplot as plt


PATH = "/home/user/repos/heatmap-location-car-plates/video/"
file = open(PATH+'test_multy.txt')
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
    x.extend([x1, x2, x3, x4])
    y.extend([y1, y2, y3, y4])
    line = file.readline()
file.close()

bins = (20, 20)
range = ((0, w), (0, h))
hist = plt.hist2d(x, y, bins=bins, range=range)
plt.colorbar(hist[3])
plt.savefig('video/' + name, bbox_inches='tight')
plt.clf()
plt.cla()
