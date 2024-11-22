import subprocess
import time

# Specify the path to your script
script_path = 'play_mouse_movement.py'

# Set how many times you want to run the script
repeat_times = 5000

# Use a loop to repeat the script execution
for _ in range(repeat_times):
    subprocess.run(['python', script_path])  # or 'python3' depending on your environment
    time.sleep(2)  # Optional: Wait for 2 seconds before running the script again
