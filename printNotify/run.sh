#!/bin/bash

LOG_FILE="/data/debug.log"

# Function to log messages
log() {
    echo "$(date) - $1" >> $LOG_FILE
}

# Check if options.json exists
if [ ! -f /data/options.json ]; then
    log "Error: /data/options.json not found."
    echo "Check /data/options.json exists."
    sleep 30  # Pause to allow access to logs
    exit 1
fi

# Print contents of options.json for debugging
log "Contents of /data/options.json:"
cat /data/options.json >> $LOG_FILE

# Read configuration values from options.json
PRINTER_URL=$(jq --raw-output '.printer_url' /data/options.json)
MESSAGE=$(jq --raw-output '.message' /data/options.json)

# Log the values for debugging
log "Printer URL: $PRINTER_URL"
log "Message: $MESSAGE"

# Check if both arguments are present
if [ -z "$PRINTER_URL" ] || [ -z "$MESSAGE" ]; then
    log "Error: Printer URL or message is missing."
    echo "Missing Printer URL or Message."
    sleep 30  # Pause to allow access to logs
    exit 1
fi

# Call the Python script with both arguments
python3 /notify_printer.py "$PRINTER_URL" "$MESSAGE"
