FROM alpine:3.13

# Install Python and CUPS
RUN apk add --no-cache python3 py3-pip cups libcups

# Install Python CUPS library
RUN pip3 install pycups

# Copy the add-on script into the container
COPY notify_printer.py /notify_printer.py

# Run the add-on
CMD ["python3", "/notify_printer.py"]
  
