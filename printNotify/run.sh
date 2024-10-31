#!/bin/bash

# Check if options.json exists
if [ ! -f /data/options.json ]; then
    echo "Error: /data/options.json not found."
    exit 1
fi

# Print contents of options.json
echo "Contents of /data/options.json:"
cat /data/options.json

# Read configuration values
PRINTER_URL=$(jq --raw-output '.printer_url' /data/options.json)
MESSAGE=$(jq --raw-output '.message' /data/options.json)

# Debugging output
echo "Printer URL: $PRINTER_URL"
echo "Message: $MESSAGE"

# Check if both arguments are present
if [ -z "$PRINTER_URL" ] || [ -z "$MESSAGE" ]; then
    echo "Error: Printer URL or message is missing."
    exit 1
fi

# Run the Python script
#python3 /notify_printer.py "$PRINTER_URL" "$MESSAGE"
