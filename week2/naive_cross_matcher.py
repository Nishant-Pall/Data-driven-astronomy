# Write your crossmatch function here.
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


def import_super():
    res = []
    data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
    for i, row in enumerate(data, 1):
        res.append((i, row[0], row[1]))
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


def crossmatch(bss_cat, super_cat, max_dist):
    matches = []
    no_matches = []
    for id1, ra1, dec1 in (bss_cat):
        closest_dist = np.inf
        closest_id2 = None
        for id2, ra2, dec2 in (super_cat):
            ang = angular_dist(ra1, dec1, ra2, dec2)
            if(ang < closest_dist):
                closest_dist = ang
                closest_id2 = id2
        if(closest_dist < max_dist):
            matches.append((id1, closest_id2, closest_dist))
        else:
            no_matches.append(id1)

    return matches, no_matches


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    bss_cat = import_bss()
    super_cat = import_super()

    # First example in the question
    max_dist = 40/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(no_matches))

    # Second example in the question
    max_dist = 5/3600
    matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
    print(matches[:3])
    print(no_matches[:3])
    print(len(no_matches))
