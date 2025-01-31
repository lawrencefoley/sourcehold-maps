
def rgb15bitto32bit(i):
    b = i & 0x1F
    b = (b >> 2) | (b << 3)

    g = (i >> 5) & 0x1F
    g = (g >> 2) | (g << 3)

    r = (i >> 10) & 0x1F
    r = (r >> 2) | (r << 3)

    return (r, g, b)

import struct

def build_serial_palette(stream):
    palette = []
    for i in range(0x100):
        v = struct.unpack("<H", stream.read(2))[0]
        palette.extend(rgb15bitto32bit(v))

    return palette

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