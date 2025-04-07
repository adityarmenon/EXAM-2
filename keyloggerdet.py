import os

def check_for_keylogger():
    try:
        with open("log.txt", "r") as f:
            data = f.read()

        if "Key" in data:
            print("🔴 Keylogger detected!")
        else:
            print("🟢 No keylogger detected.")

    except FileNotFoundError:
        print("⚠️ log.txt file not found. No keylogger activity recorded.")

# Run the keylogger detection
check_for_keylogger()

