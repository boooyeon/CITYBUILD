from cmath import atan, cos, exp, pi, log, tan
from math import floor


def lon2tile(lon, zoom=19):
    return floor((lon + 180) / 360 * pow(2, zoom))


def lat2tile(lat, zoom=19):
    return floor(
        (
            (1 - log(tan(lat * pi / 180) + 1 / cos(lat * pi / 180)) / pi)
            / 2
            * pow(2, zoom)
        ).real
    )


def tile2lon(x_tile, zoom=19):
    return x_tile / pow(2, zoom) * 360 - 180


def tile2lat(y_tile, zoom=19):
    ret = pi - 2 * pi * y_tile / pow(2, zoom)
    return (180 / pi * atan(0.5 * (exp(ret) - exp(-ret)))).real
