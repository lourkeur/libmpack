import mpack, unittest

class TestTemporary(unittest.TestCase):
    def test_issue28(self):
        p, u = mpack.Packer(), mpack.Unpacker()
        obj = {(): None}
        packed_obj = p(obj)
        self.assertEqual(packed_obj, b"\x81\x90\xc0")
        unpacked_obj, n = u(p(obj))
        self.assertEqual(n, len(packed_obj))
        self.assertEqual(unpacked_obj, obj)
