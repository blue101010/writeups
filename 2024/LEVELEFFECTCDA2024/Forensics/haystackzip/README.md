# Challenge

Haystack (250 pts) - Intermediate Made by CDA Alumni
The flag is in here somewhere...

## Analysis

Looking at the files they seems all with the same content so let's write a  C++ script to search for files witth a different content.

```bash
└─$ ./check_txt_files haystack                                                                                                                    
File: "haystack/Level17/Effect13/flag37.txt"
Content: 62 47 56 32 5a 57 78 6c 5a 6d 5a 6c 59 33 52 37 63 6a 4e 6e 4d 33 68 66 5a 6e 52 33 66 51 3d 3d


└─$ python                                                                                                                                                                                 
>>> hex_string = "62 47 56 32 5a 57 78 6c 5a 6d 5a 6c 59 33 52 37 63 6a 4e 6e 4d 33 68 66 5a 6e 52 33 66 51 3d 3d"
>>> ascii_string = bytes.fromhex(hex_string.replace(" ", "")).decode('ascii')
>>> print(ascii_string)
bGV2ZWxlZmZlY3R7cjNnM3hfZnR3fQ==
>>> 
KeyboardInterrupt
>>> import base64
>>> 
>>> base64_string = "bGV2ZWxlZmZlY3R7cjNnM3hfZnR3fQ=="
>>> ascii_string = base64.b64decode(base64_string).decode('ascii')
>>> print(ascii_string)
leveleffect{r3g3x_ftw}
>>> 
```

## FLAG

```bash
leveleffect{r3g3x_ftw}
```