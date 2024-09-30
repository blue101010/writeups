
# 123-Boom - 50 pts

Le vieux souvenir de l'an 2000 va revenir, réglez votre horloge sur notre service pour tester, doomsday.linux.. LinuxMUP{%d_%m_%Y}

```bash
┌──(fhp㉿L)-[/mnt/c/DATA/CTF/LINUXMUP2024/CHIFFREM/Dec6b]
└─$ ntpdate -q doomsday.linux
2036-02-07 01:28:15.0 (-0500) +359029153.111650 +/- 1.006607 doomsday.linux 172.21.20.11 s1 no-leap
```


Given the date 2036-02-07 01:28:15.0 (-0500), you need it in the format LinuxMUP{%d_%m_%Y}. Here's the formatted date:

Explanation:
%d: Day (07)
%m: Month (02)
%Y: Year (2036)

## FLAG

```bash
LinuxMUP{07_02_2036}
```