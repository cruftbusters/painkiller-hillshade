import json
import sys
import tempfile

from osgeo import gdal, gdalconst


def generate(sourcePath, metadata):
    output = tempfile.mktemp()
    source = gdal.Open(sourcePath)
    band = source.GetRasterBand(1)
    stats = band.GetStatistics(True, True)
    minimum = stats[0]
    maximum = stats[1]
    gdal.Translate(
        output,
        source,
        options=gdal.TranslateOptions(
            format='JPEG',
            outputType=gdalconst.GDT_Byte,
            scaleParams=[[minimum, maximum, 0, 255]],

            width=metadata['size']['width'],
            height=metadata['size']['height'],
        )
    )
    return output


if __name__ == "__main__":
    source = '/home/arctair/ws/cruftbusters/heightmap/3dep13/n46w106.img'
    with open(generate(source, json.load(sys.stdin)), 'rb') as f:
        sys.stdout.buffer.write(f.read())
