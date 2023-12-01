# Import library
import pendulum

dt = pendulum.parse('1997-11-21T22:00:00', tz='Asia/Tokyo')
print(f"Created DateTime: {dt}")


# Parsing of a non standard string
dt = pendulum.from_format('2020/11/21', 'YYYY/MM/DD')
print(f"Formated DateTime: {dt}")
