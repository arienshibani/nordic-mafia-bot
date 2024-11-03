from datetime import datetime

# Adds a timestamp to whatever message is passed in
def print_with_timestamp(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")
