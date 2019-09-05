import os

MAP_FILE_PATHS = ["../../Desktop/SHCHD/maps/" + path for path in os.listdir("../../Desktop/SHCHD/maps")]


def find_magic_number(path, number = b'\x00\x06\x00\x00'):
    with open(path, 'rb') as f:
        data = f.read()

    return data.index(number)

d = {path: find_magic_number(path) for path in MAP_FILE_PATHS}
s = set(d.values())
assert len(s) == 1
assert 20 in s

PATHS20 = ["map_testing/" + path.split("/")[-1] + "20" for path in MAP_FILE_PATHS]

for path in MAP_FILE_PATHS:
    newpath = "map_testing/" + path.split("/")[-1] + "20"

    if os.path.exists(newpath):
        continue

    with open(path, 'rb') as f:
        with open(newpath, 'wb') as f2:
            f.read(20)
            f2.write(f.read())

import subprocess


PATHS20CONV = [path + ".conv0" for path in PATHS20]

for path in PATHS20:

    if os.path.exists(path + ".conv0"):
        continue

    f1 = open(path, 'rb')
    f2=  open(path + ".conv0", 'wb')

    result = subprocess.run("blast.exe", stdin = f1, stdout = f2)


path = PATHS20CONV[0]
with open(path, 'rb') as f:
    data = f.read()

import io

b = io.BytesIO(data)

import palette

p = palette.build_palette(b)

im = palette.build_image(p, b)

zero_locations = []
start = 0
while True:
    try:
        loc = im.index((0,0,0), start)
        zero_locations.append(loc)
        start = loc + 1
    except Exception as e:
        print(e)
        break

width = int(len(im)**0.5)
height = int(len(im)**0.5)

from PIL import Image, ImageColor

import functools
import operator

b.seek(0)
p = palette.build_palette(b)
palettestream = list(functools.reduce(operator.add, p))
imagedata = list(b.read(200*200))

image = Image.new("P", (width, height))
image.putpalette(palettestream)
image.putdata(imagedata)

