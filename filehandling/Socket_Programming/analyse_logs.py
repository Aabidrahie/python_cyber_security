from pathlib import Path

# 1. Define the path (Replace 'aabid' with your actual username)
# You can also use Path.home() / "Desktop" / "access.log" to make it automatic
log_path = Path("/home/aabid/Desktop/PythonPrograms/access.log")

try:
    # 2. Open and read the file
    with log_path.open("r", encoding="utf-8") as file:
        # We read line by line to avoid crashing if the log is huge
        for line in file:
            print(line.strip())
            
except FileNotFoundError:
    print(f"Error: Could not find the file at {log_path}")
except PermissionError:
    print("Error: You don't have permission to read this file. Try 'sudo' in the terminal.")