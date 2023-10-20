# Challenge

```
├── Lost in History (TheRage)
│   ├── 01 - Tiny changes (75)
```


# Solution

Review the output format with git show: 
```
└─$ git show
commit d4a12c04fc8047a467143e77765a89220976286b (HEAD)
Author: S<C3><A9>bastien Huneault <sebastien.huneault@cyberquebec.org>
Date:   Sun Oct 8 16:02:55 2023 -0400

    37920c69a1efa74f8a15e7930b4c6baaaa3656e7

diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..2e65efe
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
+a
\ No newline at end of file
```

Follow a chain of commits going down from the latest commit and read one character from flag.txt for each one.
The names of the commits were sometimes random hashes, but sometimes they referred to other commits, so in those cases you had to jump to said commit.
This command in bash gets the job done, just make sure to have the branch checked out first (so that HEAD is at the latest commit):
```
└─$ while true; do cat flag.txt; git checkout $(git log -1 --pretty=format:%s) 2>/dev/null || git checkout HEAD~1 2>/dev/null; done
e737fkahm1nYxoWhGucH SEYtYWE4ODQ0NDI5MGM5ZDExMjI3NzljZDU5MWFmMTQzMDA=ugBlkqTqf3oMVhHA7jZbBhS6BnFdkCQshTPmSjtRwOf2HX7Laaaaaaaaaaaaaaaaaaa
```

Extract the following then from base64 :
```
SEYtYWE4ODQ0NDI5MGM5ZDExMjI3NzljZDU5MWFmMTQzMDA=
```

# FLAG
```
HF-aa88444290c9d1122779cd591af14300
```