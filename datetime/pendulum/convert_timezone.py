# Importing library
import pendulum
 
# Getting current UTC time
utc_time = pendulum.now('UTC')
 
# Switching current timezone to 
# Kolkata timezone using in_timezone().
kolkata_time = utc_time.in_timezone('Asia/Kolkata')
print('Current Date Time in Kolkata =', kolkata_time)
 
# Generating Sydney timezone
sydney_tz = pendulum.timezone('Australia/Sydney')
 
# Switching current timezone to
# Sydney timezone using convert().
sydney_time = sydney_tz.convert(utc_time)
print('Current Date Time in Sydney =', sydney_time)
