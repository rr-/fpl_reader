import io
import struct


class CoolIO(object):
    def __init__(self, data=None):
        self.file = io.BytesIO(data)

    def __enter__ (self):
        self.file.__enter__()
        return self

    def __exit__ (self, exc_type, exc_value, traceback):
        self.file.__exit__(exc_type, exc_value, traceback)

    def size(self):
        pos = self.file.tell()
        self.file.seek(0, io.SEEK_END)
        size = self.file.tell()
        self.file.seek(pos, io.SEEK_SET)
        return size

    def tell(self):
        return self.file.tell()

    def seek(self, *args):
        return self.file.seek(*args)

    def eof(self):
        return self.tell() == self.size()

    def skip(self, bytes):
        self.file.seek(bytes, io.SEEK_CUR)

    def peek(self, *args):
        return self.PeekObject(self.file, *args)

    def read_to_zero(self):
        out = b''
        byte = self.file.read(1)
        n = 0
        while byte != b"\x00":
            out += byte
            byte = self.file.read(1)
            if n > 1000:
                raise RuntimeError('dude, I\'m reading for too long (1000+ bytes)')
            n += 1
        return out

    def read_to_eof(self):
        return self.file.read()

    def read(self, *args):
        return self.file.read(*args)

    def read_u8(self): return struct.unpack('B', self.file.read(1))[0]
    def read_u16_le(self): return struct.unpack('<H', self.file.read(2))[0]
    def read_u32_le(self): return struct.unpack('<I', self.file.read(4))[0]
    def read_u64_le(self): return struct.unpack('<Q', self.file.read(8))[0]
    def read_u16_be(self): return struct.unpack('>H', self.file.read(2))[0]
    def read_u32_be(self): return struct.unpack('>I', self.file.read(4))[0]
    def read_u64_be(self): return struct.unpack('>Q', self.file.read(8))[0]
    def read_s32_le(self): return struct.unpack('<i', self.file.read(4))[0]
    def read_s64_le(self): return struct.unpack('<q', self.file.read(8))[0]
    def read_f32(self): return struct.unpack('f', self.file.read(4))[0]
    def read_f64(self): return struct.unpack('d', self.file.read(8))[0]

    class PeekObject(object):
        def __init__(self, file, *seek_args):
            self.file = file
            self.seek_args = seek_args
        def __enter__(self):
            self.old_pos = self.file.tell()
            self.file.seek(*self.seek_args)
        def __exit__(self, *unused):
            self.file.seek(self.old_pos)

