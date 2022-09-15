import sys
from calendar import weekday, day_name
year = int(sys.argv[1])
month = int(sys.argv[2])
day = int(sys.argv[3])
output = day_name[weekday(year, month, day)]
print ('this date year = %d month = %d day = %d is a %s' %(year,month,day,output))