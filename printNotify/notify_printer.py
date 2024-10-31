import sys
import requests

def print_notification(printer_url, message):
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
        print("Notification sent to printer")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    # Get arguments from run.sh
    printer_url = sys.argv[1]
    message = sys.argv[2]

    print_notification(printer_url, message)
