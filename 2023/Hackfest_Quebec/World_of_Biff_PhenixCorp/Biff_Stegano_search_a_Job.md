# Challenge

```
─ World of Biff (PhenixCorp)
    ├── Biff Stegano search a Job! (300)
```


# Solution

```
$ zsteg Talenty-CTF.png
[?] 118227 bytes of extra data after image end (IEND), offset = 0x408d9
extradata:imagedata ..
    00000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    *
    00000100:
extradata:0         .. file: Zip archive data, at least v5.1 to extract, compression method=AES Encrypted
    00000000: 50 4b 03 04 33 00 01 00  63 00 8e 61 c7 4a 00 00  |PK..3...c..a.J..|
    00000010: 00 00 0d cd 01 00 00 d8  03 00 15 00 0b 00 50 68  |..............Ph|
    00000020: 65 6e 69 78 48 65 6c 70  53 74 65 67 61 6e 6f 2e  |enixHelpStegano.|
    00000030: 65 78 65 01 99 07 00 02  00 41 45 03 08 00 49 85  |exe......AE...I.|
    00000040: 14 a6 c8 05 69 2d 51 8d  da 4f 5a 46 23 ee 04 5d  |....i-Q..OZF#..]|
    00000050: 00 8c 37 bc 4e 97 e1 81  79 d3 45 1a d4 37 05 e5  |..7.N...y.E..7..|
    00000060: 3a 79 f7 62 90 18 45 ee  94 20 2a 14 b1 2e 6b 72  |:y.b..E.. *...kr|
    00000070: 23 9d 97 8f 89 76 79 d9  36 7b 6d e8 35 04 25 bf  |#....vy.6{m.5.%.|
    00000080: ed 91 a8 e4 8a 52 36 d3  44 93 44 91 ba 5f 53 39  |.....R6.D.D.._S9|
    00000090: cf 08 08 0b 7f 36 3b 1d  ee fc b3 9d 4a 74 15 a5  |.....6;.....Jt..|
    000000a0: da 7a cd 23 51 0e a4 1a  c9 23 e9 f4 3a 57 b6 3d  |.z.#Q....#..:W.=|
    000000b0: aa 6b 0e b3 f5 b4 dd 1b  79 af 85 47 23 21 69 a2  |.k......y..G#!i.|
    000000c0: 7a 8e e2 8b 95 34 bb 4a  0a c7 eb 73 bd b8 c1 5d  |z....4.J...s...]|
    000000d0: f0 d7 ad 26 13 5c 0a 4e  9e cb 7d 71 35 45 cd 45  |...&.\.N..}q5E.E|
    000000e0: db 90 6f 1c 0d c4 63 ca  a1 3d bc 13 0d 78 bc f4  |..o...c..=...x..|
    000000f0: 37 c4 2d bb f9 2c 34 55  3b 76 03 61 53 42 47 2f  |7.-..,4U;v.aSBG/|
imagedata           .. text: "6.\t6.\t6.\t6.\t6.\t6/\t70\t82\t:4\t<5\t=8\t@:\tA<"
b1,rgb,msb,xy       .. text: "HF-735fcd9781d79b80fe55ddee65b852f1"
b2,b,msb,xy         .. file: MacBinary INVALID date "* "
b2,rgb,lsb,xy       .. file: Commodore PET BASIC program, offset 0x0414, line 4165, token (0x54), offset 0x0150, line 16464, token (0x50)
b2,rgb,msb,xy       .. text: "*\n\n\n\"\n((\n( ("
b2,bgr,lsb,xy       .. file: MacBinary INVALID date, creator '\024', type '\001' "E@AAUD\001\024DAQ\004AP"
b2,bgr,msb,xy       .. file: MacBinary INVALID date, creator '   (', type '\200' "\242\002\202\202\252"\200("
b3,g,lsb,xy         .. file: MacBinary INVALID date, creator '   (', type '\200' "H$\002@ \002\001\004\022\010\004\022@\004\002\010"
b4,r,lsb,xy         .. file: TeX font metric data (\020)
b4,g,lsb,xy         .. file: Targa image data - Map (4368-4352) 257 x 4112 x 1 +16 +272 - 1-bit alpha
b4,b,lsb,xy         .. file: Targa image data 4097 x 4096 x 1 +4113 +16
b4,rgb,lsb,xy       .. file: raw G3 (Group 3) FAX, byte-padded
```


# Flag
```
HF-735fcd9781d79b80fe55ddee65b852f1
```