import ctypes
import io

dll = ctypes.CDLL("explode.dll")


class TDataInfo(ctypes.Structure):
    _fields_ = [('pbInBuff', ctypes.POINTER(ctypes.c_ubyte)),
                ('pbInBuffEnd', ctypes.POINTER(ctypes.c_ubyte)),
                ('pbOutBuff', ctypes.POINTER(ctypes.c_ubyte)),
                ('pbOutBuffEnd', ctypes.POINTER(ctypes.c_ubyte))]

class TDcmpStruct(ctypes.Structure):
    _fields_ = [('offs0000', ctypes.c_ulong),
                ('ctype', ctypes.c_ulong),
                ('outputPos', ctypes.c_ulong),
                ('dsize_bits', ctypes.c_ulong),
                ('dsize_mask', ctypes.c_ulong),
                ('bit_buff', ctypes.c_ulong),
                ('extra_bits', ctypes.c_ulong),
                ('in_pos', ctypes.c_int),
                ('in_bytes', ctypes.c_ulong),
                ('param', ctypes.c_void_p),
                ('read_buf', ctypes.c_void_p),
                ('write_buf', ctypes.c_void_p),
                ('out_buff', ctypes.c_ubyte*0x2204),
                ('in_buff', ctypes.c_ubyte*0x800),
                ('DistPosCode', ctypes.c_ubyte*0x100),
                ('LengthCodes', ctypes.c_ubyte*0x100),
                ('offs2C34', ctypes.c_ubyte*0x100),
                ('offs2D34', ctypes.c_ubyte*0x100),
                ('offs2E34', ctypes.c_ubyte*0x80),
                ('offs2EB4', ctypes.c_ubyte*0x100),
                ('ChBitsAsc', ctypes.c_ubyte*0x100),
                ('DistBits', ctypes.c_ubyte*0x40),
                ('LenBits', ctypes.c_ubyte*0x10),
                ('ExLenBits', ctypes.c_ubyte*0x10),
                ('LenBase', ctypes.c_ushort*0x10)
                ]
    





import struct

TESTSIZE = 100000


dll.explode.restype = ctypes.c_int
dll.explode.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(TDcmpStruct), ctypes.POINTER(TDataInfo)]

o = io.BytesIO(b'')

@ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(TDataInfo))
def write(buf, size, param):
    info = param.contents
    nMaxWrite = ctypes.cast(info.pbOutBuffEnd, ctypes.c_void_p).value - ctypes.cast(info.pbOutBuff,
                                                                                    ctypes.c_void_p).value
    nToWrite = size.contents.value

    if nToWrite > nMaxWrite:
        nToWrite = nMaxWrite

    for i in range(nToWrite):
        info.pbOutBuff[i] = buf[i]

    # my:
    o.write(b''.join(struct.pack("B", v) for v in buf[:nToWrite]))

    ctypes.cast(ctypes.pointer(info.pbOutBuff), ctypes.POINTER(ctypes.c_void_p)).contents.value += nToWrite

    # print(ctypes.cast(info.pbOutBuffEnd, ctypes.c_void_p).value - ctypes.cast(info.pbOutBuff, ctypes.c_void_p).value)
    return None


@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_uint),
                  ctypes.POINTER(TDataInfo))
def read(buf, size, param):
    info = param.contents
    nMaxAvail = ctypes.cast(info.pbInBuffEnd, ctypes.c_void_p).value - ctypes.cast(info.pbInBuff,
                                                                                   ctypes.c_void_p).value
    nToRead = size.contents.value

    if nToRead > nMaxAvail:
        nToRead = nMaxAvail

    for i in range(nToRead):
        buf[i] = info.pbInBuff[i]

    ctypes.cast(ctypes.pointer(info.pbInBuff), ctypes.POINTER(ctypes.c_void_p)).contents.value += nToRead

    # print(ctypes.cast(info.pbInBuffEnd, ctypes.c_void_p).value - ctypes.cast(info.pbInBuff, ctypes.c_void_p).value)

    return nToRead

def convert_file(f, o):
    data = f.read()
    data = data[20:]

    indata = data

    work_buf = TDcmpStruct()

    info = TDataInfo()

    info.pbInBuff = ctypes.cast(indata, ctypes.POINTER(ctypes.c_ubyte))
    newaddr = ctypes.cast(info.pbInBuff, ctypes.c_void_p).value + len(indata)
    pvoid = ctypes.cast(newaddr, ctypes.c_void_p)
    info.pbInBuffEnd = ctypes.cast(pvoid, ctypes.POINTER(ctypes.c_ubyte))

    outdata = b'\x00' * TESTSIZE

    info.pbOutBuff = ctypes.cast(outdata, ctypes.POINTER(ctypes.c_ubyte))
    newaddr = ctypes.cast(info.pbOutBuff, ctypes.c_void_p).value + TESTSIZE
    pvoid = ctypes.cast(newaddr, ctypes.c_void_p)
    info.pbOutBuffEnd = ctypes.cast(pvoid, ctypes.POINTER(ctypes.c_ubyte))

    #decodeddata = io.BytesIO(b'')



    result = dll.explode(read, write, work_buf, info)

    if result != 0:
        raise Exception("conversion returned {}".format(result))

    return result

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        sys.argv.append("MxM_unseen_1.map")
    
    file = sys.argv[1]

    #o = io.BytesIO()

    with open(file, 'rb') as f:
        convert_file(f, o)

    with open(file + ".dat", 'wb') as f2:
        o.seek(0)
        r = o.getvalue()
        print(len(r))
        f2.write()

