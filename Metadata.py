import os
from PIL import Image
from PIL.ExifTags import TAGS

img_file = '1.jpg'
image = Image.open(img_file)

exif = {}

for tag, value in image._getexif().items():
    if tag in TAGS:
        exif[TAGS[tag]] = value

if 'GPSInfo' in exif:
    geo_coordinate = '{0} {1} {2:2.f} {3}, {4} {5} {6:2.f} {7}'.format(
        exif['GPSInfo'][2][0][0],
        exif['GPSInfo'][2][1][0],
        exif['GPSInfo'][2][2][0] / exif['GPSInfo'][2][2][1],
        exif['GPSInfo'][1],
        exif['GPSInfo'][4][0][0],
        exif['GPSInfo'][4][1][0],
        exif['GPSInfo'][4][2][0] / exif['GPSInfo'][4][2][1],
        exif['GPSInfo'][3]
    )

    print(geo_coordinate)


print(exif)
