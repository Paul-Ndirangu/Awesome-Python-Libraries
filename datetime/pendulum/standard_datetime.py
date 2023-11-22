import pendulum

now = pendulum.now("Europe/Paris")

# Changing timezone
now.in_timezone("America/Toronto")

# Default support for common datetime formats
now.to_iso8601_string()
print(f"Time now: {now}")

# Shifting
now.add(days=2)

print(f" Time after adding 2 days: {now}")
