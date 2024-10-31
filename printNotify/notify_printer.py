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
        # Send IPP job to printer using POST request
        response = requests.post(printer_url, json=ipp_request)
        response.raise_for_status()
        print("Notification successfully sent to printer")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    # Get arguments from run.sh
    printer_url = sys.argv[1]
    message = sys.argv[2]

    print("Starting print notification...")
    print_notification(printer_url, message)
