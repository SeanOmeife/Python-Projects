import time # Import the time module so we can use the sleep function

# Ask the user to enter how many seconds to count down from, and store it as an integer
my_time = int(input("Enter the time in seconds: "))

# Loop from my_time - 1 down to 0 (reversed makes it count down)
# Alternative option,for x in reversed(range(0, my_time)):

# loop from my_time to 1, decreasing by 1 each time
for x in range(my_time, 0, -1):
    # calculate the number of seconds left (0-59)
    seconds = x % 60
    # calculate the number of minutes left
    minutes = int (x /60) % 60
    # calculate the number of hours left
    hours = int(x / 3600) 
    # print the time left in HH:MM:SS format showing the digits for each
    print(f"{hours:02}:{minutes:02}:{seconds:02}") 
    time.sleep(1) # Pauses the program for 1 second before showing the next number

# Countdown is finished, prints a message
print("Time's Up!")