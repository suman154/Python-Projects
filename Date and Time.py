# Date and Time

import datetime

x = datetime.datetime.now()
print(x)

# Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Time
import datetime

x = datetime.datetime(2010,1, 25)

print(x)