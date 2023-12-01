# Import library
import pendulum

# Creating new DateTime Instance
dt = pendulum.datetime(2020, 11, 27, 12, 30, 15)
print(f"Created DateTime: {dt}")

# Formatting DateTime Instance
dt.to_day_datetime_string()
formatted_str = dt.format('dddd Do [of] MMMM YYYY HH:mm:ss A')
print(f"Formated DateTime: {formatted_str}")
