import mpack, sys

CASES = [
    b"\x81\xc0\xc0",          # {None: None)}
    b"\x81\xc2\xc2",          # {False: False}
    b"\x81\xc3\xc3",          # {True: True}
    b"\x81\x00\x00",          # {0: 0}
    b"\x81\x00\xd1\x00\x00",  # {0: int16(0)}
    b"\xde\x00\x01\x00\x00",  # map16({0: 0})
    b"\x82\x00\x01\x00\x02",  # {0: 1, 0: 2}, does NOT segfault
    b"\x82\x00\x01\x00\x02",  # {0: 1, 0: 2}, does NOT segfault
    b"\x82\x00\x01\x02\x00",  # {0: 1, 2: 0}, does NOT segfault
    b"\x81\xc4\x00\xc4\x00",  # {b"": b""}, does NOT segfault,
                              # probably because mpack allocates two different b""'s
    b"\x92\xc0\xc0",          # [None, None], does NOT segfault
    ]

case = CASES[int(sys.argv[1])]
print(ascii(case))
mpack.unpack(case)
