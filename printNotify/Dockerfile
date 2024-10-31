# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
FROM alpine:3.14 

# Install Python, pip, and IPP libraries
RUN apk update #&& \
RUN apk add --no-cache python3 py3-pip 

# Install Python requests library
#RUN pip3 install pycups
#RUN pip3 install pyipp
RUN pip3 install requests

# Copy the add-on script into the container
COPY notify_printer.py /notify_printer.py

# Run the add-on
CMD ["python3", "/notify_printer.py"]
