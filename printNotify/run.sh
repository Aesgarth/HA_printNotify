#!/bin/bash

# Read configuration from options.json
PRINTER_URL=$(jq --raw-output '.printer_url' /data/options.json)
MESSAGE=$(jq --raw-output '.message' /data/options.json)

# Print the values for debugging
echo "Printer URL: $PRINTER_URL"
echo "Message: $MESSAGE"

# Check if both arguments are present
if [ -z "$PRINTER_URL" ] || [ -z "$MESSAGE" ]; then
    echo "Error: Printer URL or message is missing."
    exit 1
fi

# Run the Python script
python3 /notify_printer.py "$PRINTER_URL" "$MESSAGE"
