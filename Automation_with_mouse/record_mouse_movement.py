import time
import json
from pynput.mouse import Listener, Controller
from pynput.keyboard import Listener as KeyboardListener, Key

# List to store mouse events
mouse_events = []

# Mouse controller to simulate mouse actions
mouse_controller = Controller()

# Function to track mouse position and clicks
def on_move(x, y):
    mouse_events.append({"event": "move", "x": x, "y": y})
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        mouse_events.append({
            "event": "click", "x": x, "y": y, "button": button.name, "action": "pressed"
        })
        print(f"Mouse clicked at ({x}, {y}) with {button.name} pressed")

def on_scroll(x, y, dx, dy):
    mouse_events.append({"event": "scroll", "x": x, "y": y, "dx": dx, "dy": dy})
    print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# Save the events to a JSON file
def save_to_file(filename="mouse_events.json"):
    with open(filename, "w") as file:
        json.dump(mouse_events, file, indent=4)
    print(f"Mouse events saved to {filename}")

# Stop tracking flag
stop_tracking = False

# Function to stop the program when spacebar is pressed
def on_press(key):
    global stop_tracking
    try:
        if key == Key.space:
            stop_tracking = True
            print("\nSpacebar pressed, stopping tracking...")
            return False  # Stop the listener
    except AttributeError:
        pass

# Start listening to mouse events and keyboard events
def start_tracking():
    global stop_tracking
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener:
        with KeyboardListener(on_press=on_press) as keyboard_listener:
            while not stop_tracking:
                # We keep checking if the stop flag is set to True
                time.sleep(0.1)  # Small delay to prevent high CPU usage

            # Stop both listeners once space is pressed
            mouse_listener.stop()
            keyboard_listener.stop()

# Main loop to repeat the process
if __name__ == "__main__":
    print("Starting to track mouse movements and clicks...")
    try:
        start_tracking()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # After stopping, save the events to a file
        if mouse_events:
            save_to_file()
        else:
            print("No mouse events were recorded.")
