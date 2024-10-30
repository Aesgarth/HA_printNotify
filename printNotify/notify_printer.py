import sys
from ipptools import IPP, JobTemplate

def print_notification(printer_url, message):
    # Create an IPP connection to the printer
    ipp = IPP(printer_url)

    # Prepare the print job
    job_template = JobTemplate(
        name="Home Assistant Notification",
        attributes={
            'operation-attributes-tag': {
                'requesting-user-name': 'Home Assistant',
                'job-name': 'Notification Print',
            },
            'document-attributes-tag': {
                'document-format': 'text/plain',
            }
        },
    )

    # Create the print job
    try:
        ipp.print_job(job_template, message.encode('utf-8'))
        print("Notification sent to printer")
    except Exception as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    # Get arguments from run.sh
    printer_url = sys.argv[1]
    message = sys.argv[2]

    print_notification(printer_url, message)
