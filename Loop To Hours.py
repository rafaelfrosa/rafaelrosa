data = [125, 135, 59, 103, 65, 72, 35, 83, 141, 67, 3, 35, 101, 95, 84, 142, 87, 21, 48, 125, 137, 95, 0, 43 , 95, 128, 105, 95, 79, 69, 85, 137, 1, 67, 104, 137, 47, 133, 77, 117, 35, 79, 59, 81, 89, 125, 131, 75, 68 , 91, 43, 59, 98, 16, 19, 3, 116, 101, 19, 107, 17, 111, 35, 119, 107, 141, 49, 1, 33, 13, 79, 21, 115, 52 , 125, 111, 61, 43, 9, 13, 23, 99, 73, 77, 67, 65, 81, 61, 23, 55, 37, 91, 89, 101, 75, 25, 74, 81, 39 , 95, 33]

hours = [data * 10 / 60 for data in data] # Converting loops to hours

frequencies = {hour: hours.count(hour) for hour in set(hours)} # Calculating 

frequencies

time_highest_frequency = max(frequencies, key=frequencies.get) # Identifying the time with the highest frequency

# Converting the average hours into hours and minutes
integer_hours = int(time_highest_frequency)
minutes = (time_highest_frequency - integer_hours) * 60

print(f"The average number of hours that has the highest frequency is {integer_hours} hours and {int(minutes)} minutes")