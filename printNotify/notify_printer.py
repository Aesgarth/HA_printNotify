import sys
import requests

def print_notification(printer_url, message):
    print(f"Attempting to send notification to printer at {printer_url}")
    print(f"Message: {message}")

    # IPP document and attributes
    ipp_request = {
        "operation-attributes-tag": {
            "attributes-charset": "utf-8",
            "attributes-natural-language": "en",
            "printer-uri": printer_url,
            "requesting-user-name": "Home Assistant",
            "job-name": "Notification Print",
            "document-format": "text/plain"
        },
        "document": message
    }

    try:
        # Send IPP job to printer using a POST request
        response = requests.post(printer_url, json=ipp_request)
        response.raise_for_status()
        print("Notification successfully sent to printer")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Missing arguments. Usage: python notify_printer.py <printer_url> <message>")
        sys.exit(1)

    # Get command-line arguments
    printer_url = sys.argv[1]
    message = sys.argv[2]

    # Call function to print notification
    print_notification(printer_url, message)
