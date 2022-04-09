# Write your load_fits function here.
from astropy.io import fits
import numpy as np


def load_fits(file):
    '''
    This function works on a flattened (or ravelled) array, i.e. the array gets
    converted to a 1D array internally before the maximum is found.
    And the max_pos returned is rather a single digit instead of (x,y) co-ordinate
    To revert this, or to "unravel" the result, we can call the function unravel_index
    and pass it the dimension of the initial data array as second argument.
    '''
    hdulist = fits.open(file)
    data = hdulist[0].data
    arg_max = np.argmax(data)

    max_pos = np.unravel_index(arg_max, data.shape)

    return max_pos


if __name__ == '__main__':
    # Run your `load_fits` function with examples:
    bright = load_fits('image1.fits')
    print(bright)

    # # You can also confirm your result visually:
    # from astropy.io import fits
    # import matplotlib.pyplot as plt

    # hdulist = fits.open('image1.fits')
    # data = hdulist[0].data

    # # Plot the 2D image data
    # plt.imshow(data.T, cmap=plt.cm.viridis)
    # plt.colorbar()
    # plt.show()


# def load_fits(file):
#     hdulist = fits.open(file)
#     data = hdulist[0].data
#     min = -sys.maxsize - 1
#     x, y = 0, 0
#     for index_i, i in enumerate(data):
#         for index_j, j in enumerate(i):
#             if(data[index_i][index_j] > min):
#                 min = data[index_i][index_j]
#                 x = index_i
#                 y = index_j
#     return x, y
