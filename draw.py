import matplotlib.pyplot as plt

def draw_hist(x,y, range, bins=(11,11), name='test'):
    range = ((0, w), (0, h))
    hist = plt.hist2d(x, y, bins=bins, range=range)
    plt.colorbar(hist[3])
    plt.savefig('video/' + name, bbox_inches='tight')
    plt.clf()
    plt.cla()