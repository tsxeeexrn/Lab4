from datetime import datetime
date1 = datetime(2025, 2, 10, 14, 30, 0)
date2 = datetime(2025, 2, 12, 16, 45, 30)
time_difference = date2 - date1
difference_in_seconds = time_difference.total_seconds()
print(f"The difference between the two dates is {difference_in_seconds} seconds.")
