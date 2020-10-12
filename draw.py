import matplotlib.pyplot as plt


def draw_hist(x,y, range, bins=(11,11), name='test'):
    range = ((0, w), (0, h))
    hist = plt.hist2d(x, y, bins=bins, range=range)
    plt.colorbar(hist[3])
    plt.savefig('video/' + name, bbox_inches='tight')
    plt.clf()
    plt.cla()


PATH = "/home/user/repos/heatmap-location-car-plates/video/"
file = open(PATH+'test_multy.txt')
w, h, name, fps = file[0].split()
x = []
y = []
for line in file[1:]:
    x.append()
