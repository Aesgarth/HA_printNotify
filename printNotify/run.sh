#!/bin/bash
# Read configuration from options
PRINTER_URL=$(jq --raw-output '.printer_url' /data/options.json)
MESSAGE=$(jq --raw-output '.message' /data/options.json)

# Call the Python script to send the message to the printer
python3 /notify_printer.py "$PRINTER_URL" "$MESSAGE"
