import matplotlib.pyplot as plt

def draw_hist(x,y, range, bins=(11,11), name='test'):
    #hist = plt.hist2d(x, y, bins=bins, range=range)
    #plt.colorbar(hist[3])
    #plt.savefig('video/' + name, bbox_inches='tight')

    H, xedges, yedges, img = plt.hist2d(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(H, cmap=plt.cm.jet, extent=range)
    fig.colorbar(im, ax=ax)
    plt.savefig('video/' + name)