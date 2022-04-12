# Write your find_closest function here
import numpy as np


def hms2dec(hr, m, s):
    dec = hr + m/60 + s/3600
    return dec*15


def dms2dec(d, m, s):
    sign = d/abs(d)
    dec = abs(d) + m/60 + s/3600
    return sign*dec


def import_bss():
    res = []
    data = np.loadtxt('bss.dat', usecols=range(1, 7))
    for i, row in enumerate(data, 1):
        res.append((i, hms2dec(row[0], row[1], row[2]),
                   dms2dec(row[3], row[4], row[5])))
    return res


def angular_dist(ra1, dec1, ra2, dec2):
    ra1 = np.radians(ra1)
    dec1 = np.radians(dec1)
    ra2 = np.radians(ra2)
    dec2 = np.radians(dec2)

    a = np.sin(np.abs(dec1 - dec2)/2)**2
    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
    d = 2*np.arcsin(np.sqrt(a+b))
    return np.degrees(d)


def find_closest(cat, ra, dec):
    min_dist = np.inf
    min_id = None
    for id1, ra1, dec1 in cat:
        dist = angular_dist(ra1, dec1, ra, dec)
        if dist < min_dist:
            min_id = id1
            min_dist = dist
    return min_id, min_dist


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    cat = import_bss()

    # First example from the question
    print(find_closest(cat, 175.3, -32.5))

    # Second example in the question
    print(find_closest(cat, 32.2, 40.7))
