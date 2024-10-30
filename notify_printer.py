import cups
import os

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
    # Read environment variables (set by the add-on schema)
    printer_url = os.getenv("PRINTER_URL")
    printer_name = os.getenv("PRINTER_NAME")
    message = os.getenv("MESSAGE")

    print_notification(printer_url, printer_name, message)
