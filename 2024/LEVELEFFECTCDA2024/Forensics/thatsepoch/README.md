# Challenge

```
├──[-] Forensics
│   ├── That's epoch (100)
```

Learning about the Y2K38 problem will lead you to a way to decode the flag. 1721387471
The flag is in the format leveleffect{dd MMMM yyyy HH:mm:ss}

## Analysis

The year 2038 problem (also known as Y2038,[1] Y2K38, Y2K38 superbug or the Epochalypse[2][3])
 is a time computing problem that leaves some computer systems unable to represent times after 03:14:07 UTC on 19 January 2038 from <https://en.wikipedia.org/wiki/Year_2038_problem>

```
$ python thatsepoch3.py 
Date without TZ 19 July 2024 07:11:11
Original Date and Time as UTC: 19 July 2024 11:11:11
```

Testing both dates, the one converted in UTC is correct, 
```
# Convert to human-readable date and time using timezone-aware objects
date_time = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
date_time_str = date_time.strftime("%d %B %Y %H:%M:%S")
print("Original Date and Time as UTC:", date_time_str)
```

## FLAG

```
leveleffect{19 July 2024 11:11:11}
```
