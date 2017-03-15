import mpack, unittest

class TestTemporary(unittest.TestCase):
    def test_unpacking_c1(self):
        u = mpack.Unpacker()
        u(b"\xc1")
