import json
import time
from pynput.mouse import Controller, Button

# Load mouse events from file
def load_from_file(filename="mouse_events.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Replay the mouse events
def replay_mouse_events(events):
    mouse_controller = Controller()
    for event in events:
        if event["event"] == "move":
            # Move the mouse to the recorded position
            mouse_controller.position = (event["x"], event["y"])
            print(f"Moved to ({event['x']}, {event['y']})")
        
        elif event["event"] == "click":
            # Handle mouse click events (press and release)
            if event["action"] == "pressed":
                # Convert the string button name to the corresponding Button enum
                if event["button"] == "left":
                    button = Button.left
                elif event["button"] == "right":
                    button = Button.right
                elif event["button"] == "middle":
                    button = Button.middle
                else:
                    print(f"Unknown button {event['button']}, skipping click")
                    continue

                # Perform the click (press and release)
                mouse_controller.press(button)
                print(f"Pressed {event['button']} at ({event['x']}, {event['y']})")
                
                # Release the button after a small delay to simulate a click
                time.sleep(0.1)  # Adjust this delay if necessary
                mouse_controller.release(button)
                print(f"Released {event['button']} at ({event['x']}, {event['y']})")
        
        elif event["event"] == "scroll":
            # Scroll the mouse (up or down)
            mouse_controller.scroll(event["dx"], event["dy"])
            print(f"Scrolled at ({event['x']}, {event['y']}) with delta ({event['dx']}, {event['dy']})")
        
        # Add a small delay to simulate realistic timing
        time.sleep(0.05)

if __name__ == "__main__":
    # Load events from the file
    events = load_from_file()

    # Replay the events
    print("Replaying mouse events...")
    replay_mouse_events(events)
