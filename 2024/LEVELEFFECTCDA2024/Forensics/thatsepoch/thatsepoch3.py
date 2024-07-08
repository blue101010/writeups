import datetime

# Provided timestamp
timestamp = 1721387471
dt_object = datetime.datetime.fromtimestamp(timestamp)
formatted_time = dt_object.strftime('%d %B %Y %H:%M:%S')
print("Date without TZ", formatted_time)

# Convert to human-readable date and time using timezone-aware objects
date_time = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
date_time_str = date_time.strftime("%d %B %Y %H:%M:%S")
print("Original Date and Time as UTC:", date_time_str)



