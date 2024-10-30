import cups
import sys

def print_notification(printer_url, printer_name, message):
    # Set up CUPS connection
    conn = cups.Connection(printer_url)
    
    # Create a temporary text file with the message
    with open("/tmp/notification.txt", "w") as f:
        f.write(message)

    # Send the file to the printer
    try:
        conn.printFile(printer_name, "/tmp/notification.txt", "Home Assistant Notification", {})
        print("Notification sent to printer")
    except cups.IPPError as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    # Get arguments from run.sh
    printer_url = sys.argv[1]
    printer_name = sys.argv[2]
    message = sys.argv[3]

    print_notification(printer_url, printer_name, message)

