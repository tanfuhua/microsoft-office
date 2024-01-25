python
# This Python code prints the current date and time.

import datetime

# Get the current date and time.
now = datetime.datetime.now()

# Print the current date and time.
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))