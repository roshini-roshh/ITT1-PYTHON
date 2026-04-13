from datetime import datetime
# 1. Ask for both timestamps
t1_str = input("Enter timestamp 1 (DD-MM-YYYY HH:MM:SS): ")
t2_str = input("Enter timestamp 2 (DD-MM-YYYY HH:MM:SS): ")
# 2. Define the format of your input string
fmt = "%d-%m-%Y %H:%M:%S"
# 3. Convert strings into datetime objects
time1 = datetime.strptime(t1_str, fmt)
time2 = datetime.strptime(t2_str, fmt)
# 4. Calculate the absolute difference
diff = abs(time1 - time2)
# 5. Get the total seconds and print
print(int(diff.total_seconds()))
