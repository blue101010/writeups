

# Commands
```
root@attackdefense:~# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: ip_vti0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/ipip 0.0.0.0 brd 0.0.0.0
136908: eth0@if136909: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:0a:01:00:08 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.1.0.8/16 brd 10.1.255.255 scope global eth0
       valid_lft forever preferred_lft forever
136911: eth1@if136912: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:c0:9c:46:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.156.70.2/24 brd 192.156.70.255 scope global eth1
       valid_lft forever preferred_lft forever
root@attackdefense:~# 


root@attackdefense:~# nmap -sU -p 161 -sV 192.156.70.3
Starting Nmap 7.70 ( https://nmap.org ) at 2023-12-29 18:42 UTC
Nmap scan report for target-1 (192.156.70.3)
Host is up (0.00025s latency).

PORT    STATE SERVICE VERSION
161/udp open  snmp    SNMPv1 server; net-snmp SNMPv3 server (public)
MAC Address: 02:42:C0:9C:46:03 (Unknown)
Service Info: Host: victim-1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.67 seconds
```

The SNMP server is running on port 161 of the target machine. The snmp server is configured
to use the community string "public"
​Identify the processes running on the target machine. Nmap script is available to
identify the processes and the parameters passed to them.
https://nmap.org/nsedoc/scripts/snmp-processes.html

```
root@attackdefense:~# nmap -sU -p 161  --script snmp-processes  192.156.70.3
Starting Nmap 7.70 ( https://nmap.org ) at 2023-12-29 19:55 UTC
Nmap scan report for target-1 (192.156.70.3)
Host is up (0.000098s latency).

PORT    STATE SERVICE
161/udp open  snmp
| snmp-processes: 
|   1: 
|     Name: sh
|     Path: /bin/sh
|     Params: -c "/startup.sh"
|   7: 
|     Name: startup.sh
|     Path: /bin/bash
|     Params: /startup.sh
|   10: 
|     Name: snmpd
|     Path: snmpd
|   12: 
|     Name: apache2
|     Path: apache2
|   13: 
|     Name: processor
|     Path: processor
|     Params: -u bruce -p s3cr3tP4ss
|   14: 
|     Name: supervisord
|     Path: /usr/bin/python
|     Params: /usr/bin/supervisord -n
|   15: 
|     Name: apache2
|     Path: apache2
|   16: 
|     Name: apache2
|_    Path: apache2
MAC Address: 02:42:C0:9C:46:03 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.47 seconds

```

Snmpwalk requires the options and oid to be passed along with the IP address of the remote machine. Identifying the OID required to view the interface information. The information regarding processes are stored in the hrSWRunTable. Search for hrSWRunTable in the OID
repository. OID Repository Link: ​http://www.oid-info.com/basic-search.htm  
Ref http://www.oid-info.com/get/1.3.6.1.2.1.25.4.2


There are 8 child OIDs for hrSWRUNEntry. Two of the child OID are hrSWRunName and
hrSWRunParameters. The first OID will reveal the name of the process and the second OID will
reveal the parameters passed to the program.
hrSWRunName OID: 1.3.6.1.2.1.25.4.2.1.2
hrSWRunParameters OID: 1.3.6.1.2.1.25.4.2.1.5
​Pass the hrSWRunName OID along with other required arguments to the snmpwalk tool.


```
root@attackdefense:~# snmpwalk -v 2c -c public 192.156.70.3 .1.3.6.1.2.1.25.4.2.1.2
Created directory: /var/lib/snmp/mib_indexes
iso.3.6.1.2.1.25.4.2.1.2.1 = STRING: "sh"
iso.3.6.1.2.1.25.4.2.1.2.7 = STRING: "startup.sh"
iso.3.6.1.2.1.25.4.2.1.2.10 = STRING: "snmpd"
iso.3.6.1.2.1.25.4.2.1.2.12 = STRING: "apache2"
iso.3.6.1.2.1.25.4.2.1.2.13 = STRING: "processor"
iso.3.6.1.2.1.25.4.2.1.2.14 = STRING: "supervisord"
iso.3.6.1.2.1.25.4.2.1.2.15 = STRING: "apache2"
iso.3.6.1.2.1.25.4.2.1.2.16 = STRING: "apache2"
root@attackdefense:~# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   2384   704 ?        Ss   18:31   0:00 /bin/sh /startup.sh
root          19  0.2  0.0 105924 20252 ?        Sl   18:31   0:12 /usr/local/bin/ttyd -p 45654 bash
root          21  0.0  0.0   3812  2756 pts/0    Ss   18:34   0:00 bash
root          27  0.0  0.0   7636  2596 pts/0    R+   20:14   0:00 ps aux
root@attackdefense:~# 
```

Pass the hrSWRunParameters OID along with other required arguments to identify the parameters to the process :

```
root@attackdefense:~# snmpwalk -v 2c -c public 192.156.70.3 .1.3.6.1.2.1.25.4.2.1.5 | grep STRING
iso.3.6.1.2.1.25.4.2.1.5.1 = STRING: "-c \"/startup.sh\""
iso.3.6.1.2.1.25.4.2.1.5.7 = STRING: "/startup.sh"
iso.3.6.1.2.1.25.4.2.1.5.13 = STRING: "-u bruce -p s3cr3tP4ss"
iso.3.6.1.2.1.25.4.2.1.5.14 = STRING: "/usr/bin/supervisord -n"
```

The parameters can be related to the processes by relating the last digit (Process ID) in the OID string. For example, the OID string for the "processor" process has "12" in the end, therefore the OID string for the parameters will also have the same digit in the end. The username and password are passed as parameters to the processor program. The password of user bruce is "s3cr3tP4ss"

# References:
1. Process Discovery (​https://attack.mitre.org/techniques/T1057/​)
2. Nmap Script SNMP Processes (​https://nmap.org/nsedoc/scripts/snmp-processes.html​)
3. OID Repository (​http://www.oid-info.com​)
4. Snmpwalk (​https://linux.die.net/man/1/snmpwalk​)


