import matplotlib.pyplot as plt

def draw_hist(x,y, range, bins=(11,11), name='test'):
    #hist = plt.hist2d(x, y, bins=bins, range=range)
    #plt.colorbar(hist[3])
    #plt.savefig('video/' + name, bbox_inches='tight')

    H, xedges, yedges, img = plt.hist2d(x, y)
    extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(H, cmap=plt.cm.jet, extent=extent)
    fig.colorbar(im, ax=ax)
    plt.savefig('video/' + name)