# This program converts time from a 24-hour format to a 12-hour format.
# For further information, details, and a compelling story about this code,
# please check out the following Medium article: {}
# replace 12 with the hour in 24-hour format that you want to convert.

hour = 12 
HOURS_IN_HALF_DAY = 12
hour_12 = hour % HOURS_IN_HALF_DAY
print(hour_12)