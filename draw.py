import matplotlib.pyplot as plt


PATH = "/home/user/repos/heatmap-location-car-plates/video/"
file = open(PATH+'test_multy.txt')
line = file.readline()
print("1", line)
w, h, name, fps = line.split()
line = file.readline()
print("2", line)
x = []
y = []
while line:
    print(line)
    x1,x2,x3,x4,y1,y2,y3,y4 = line.split()
    x.extend([x1,x2,x3,x4])
    y.extend([y1,y2,y3,y4])
    line = file.readline()
file.close()

bins=(11, 11)
range = ((0, w), (0, h))
hist = plt.hist2d(x, y, bins=bins, range=range)
plt.colorbar(hist[3])
plt.savefig('video/' + name, bbox_inches='tight')
plt.clf()
plt.cla()
