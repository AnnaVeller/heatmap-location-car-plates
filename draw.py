import matplotlib.pyplot as plt

def draw_hist(x,y, bins=(10,10), name='test'):
    hist = plt.hist2d(x, y, bins=bins, range=range)
    plt.colorbar(hist[3])
    plt.savefig('video/' + name, bbox_inches='tight')