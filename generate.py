import json
import sys
import tempfile

from osgeo import gdal, gdalconst


def generate(sourcePath, metadata):
    left = metadata['position']['left']
    top = metadata['position']['top']
    right = left + 1
    bottom = top - 1
    if left == 0 and top == 0:
        left = metadata['bounds']['left']
        top = metadata['bounds']['top']
        right = metadata['bounds']['right']
        bottom = metadata['bounds']['bottom']

    source = gdal.Open(sourcePath)
    band = source.GetRasterBand(1)
    stats = band.GetStatistics(True, True)
    minimum = stats[0]
    maximum = stats[1]

    warp = tempfile.mktemp()
    translate = tempfile.mktemp()

    gdal.Warp(
        warp,
        source,
        options=gdal.WarpOptions(
            outputBounds=[left, top, right, bottom],
            outputBoundsSRS="EPSG:4326",
            width=metadata['size']['width'],
            height=metadata['size']['height'],
        )
    )

    gdal.Translate(
        translate,
        warp,
        options=gdal.TranslateOptions(
            format='JPEG',
            outputType=gdalconst.GDT_Byte,
            scaleParams=[[minimum, maximum, 0, 255]],
        )
    )
    return translate


if __name__ == "__main__":
    source = '/home/arctair/ws/cruftbusters/heightmap/3dep13/n46w106.img'
    with open(generate(source, json.load(sys.stdin)), 'rb') as f:
        sys.stdout.buffer.write(f.read())
