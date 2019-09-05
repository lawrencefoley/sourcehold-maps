
basepalette = """0D F0 AD BA """*16 #or more

with open("pkware/zlib/contrib/blast/test.dat", 'rb') as f:
    testdat = f.read()

esi = -3
for i in range(0x100):
    eax = testdat[i*2]
    esi += 3
    eax &= 0x1F #32, 5-bits
    edx = eax
    edx >>= 2
    eax = eax << 3
    edx |= eax


def rgb15bitto32bit(i):
    b = i & 0x1F
    b = (b >> 2) | (b << 3)

    g = (i >> 5) & 0x1F
    g = (g >> 2) | (g << 3)

    r = (i >> 10) & 0x1F
    r = (r >> 2) | (r << 3)

    return (r, g, b)

import struct

def build_palette(stream):
    palette = []
    for i in range(0x100):
        v = struct.unpack("<H", stream.read(2))[0]
        palette.append(rgb15bitto32bit(v))

    return palette

def build_image(palette, stream):

    image = []

    d = stream.read(1)
    # while d == b'\x00':
    #     d = stream.read(1)

    while True:
        #while d == b'\x00':
        #    d = stream.read(1)

        if d == b'':
            break

        i = struct.unpack("B", d)[0]
        color = palette[i]
        image.append(color)

        d = stream.read(1)

    return image

def split_zeros(image):
    zero_locations = []
    start = 0
    while True:
        try:
            loc = image.index((0, 0, 0), start)
            zero_locations.append(loc)
            start = loc + 1
        except Exception as e:
            print(e)
            break

    lines = []
    pos = 0
    for loc in zero_locations:
        line = image[pos:loc]
        if len(line) > 0:
            lines.append(line)
        pos = loc + 1