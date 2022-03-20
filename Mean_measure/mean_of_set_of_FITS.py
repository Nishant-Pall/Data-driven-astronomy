# Write your mean_fits function here:
import numpy as np
from astropy.io import fits


# def mean_fits(arr):
#     n = len(arr)
#     if(n > 0):
#         data = fits.open(arr[0])[0].data
#         for i in range(1, n):
#             data += fits.open(arr[i])[0].data

#         mean_data = data/n

#         return mean_data


def mean_fits(files):
    n = len(files)
    if n > 0:

        hdulist = fits.open(files[0])
        data = hdulist[0].data
        hdulist.close()

        for i in range(1, n):
            hdulist = fits.open(files[i])
            data += hdulist[0].data
            hdulist.close()

        mean = data / n
        return mean


if __name__ == '__main__':
    # Test your function with examples from the question
    data = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
    print(data[100, 100])

    # You can also plot the result:
    # import matplotlib.pyplot as plt
    # plt.imshow(data.T, cmap=plt.cm.viridis)
    # plt.colorbar()
    # plt.show()
