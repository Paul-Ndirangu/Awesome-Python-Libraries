import pendulum

starting = pendulum.datetime(2021, 1, 1)
ending = starting.add(hours = 10)

# Subtracting date-time instances
# to get a period instance
period_rslt = ending - starting
print(f"Period is: {period_rslt.hours} hours")

# OPTION 2:
# You can create period instance
# by using the period() method
start = pendulum.datetime(2021, 1, 1)
end = pendulum.datetime(2021, 1, 31)

period = pendulum.period(start, end)
print(f"Period is: {period.days} days")
