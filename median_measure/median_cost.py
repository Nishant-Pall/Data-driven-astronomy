# Write your function median_FITS here:
import numpy as np
from astropy.io import fits
import time


def median_fits(filenames):
    start = time.time()
    FITS_list = []
    for filename in filenames:
        hdulist = fits.open(filename)
        FITS_list.append(hdulist[0].data)
        hdulist.close()

    FITS_stack = np.dstack(FITS_list)
    median = np.median(FITS_stack, axis=2)
    memory = FITS_stack.nbytes

    memory /= 1024

    stop = time.time() - start   # stop timer
    return median, stop, memory

    # You can use this to test your function.
    # Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with first example in the question.
    result = median_fits(['image0.fits', 'image1.fits'])
    print(result[0][100, 100], result[1], result[2])

    # Run your function with second example in the question.
    # result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
    # print(result[0][100, 100], result[1], result[2])
