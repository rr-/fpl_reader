import io
import struct


class CoolIO:
    def __init__(self, data=None):
        self.file = io.BytesIO(data)

    def __enter__(self):
        self.file.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
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
        self.file.seek(*args)
        return self

    def eof(self):
        return self.tell() == self.size()

    def skip(self, num):
        self.file.seek(num, io.SEEK_CUR)
        return self

    def read_to_zero(self):
        out = b''
        byte = self.file.read(1)
        num = 0
        while byte != b"\x00":
            out += byte
            byte = self.file.read(1)
            if num > 4096:
                raise RuntimeError('String too long (corrupt file?)')
            num += 1
        return out

    def read_to_eof(self):
        return self.file.read()

    def read(self, *args):
        return self.file.read(*args)

    def read_u8(self):
        return struct.unpack('B', self.file.read(1))[0]

    def read_u16_le(self):
        return struct.unpack('<H', self.file.read(2))[0]

    def read_u32_le(self):
        return struct.unpack('<I', self.file.read(4))[0]

    def read_u64_le(self):
        return struct.unpack('<Q', self.file.read(8))[0]

    def read_s32_le(self):
        return struct.unpack('<i', self.file.read(4))[0]

    def read_s64_le(self):
        return struct.unpack('<q', self.file.read(8))[0]

    def read_f32(self):
        return struct.unpack('f', self.file.read(4))[0]

    def read_f64(self):
        return struct.unpack('d', self.file.read(8))[0]
