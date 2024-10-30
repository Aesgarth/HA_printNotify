#FROM alpine:3.13

# Install Python and CUPS
#RUN apk add --no-cache python3 py3-pip cups libcups
FROM alpine:latest

# Install Python, pip, and IPP libraries
RUN apk update #&& \
RUN apk add --update python3 
RUN apk add --update py3-pip 
RUN pip3 install pyipp

#RUN apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main libcups
#RUN apk add --no-cache  build-base gcc musl-dev python3-dev libc-dev
#RUN apk add --no-cache python3 
#RUN apk add --no-cache py3-pip 
#RUN apk add --no-cache cups 
#RUN apk add --no-cache libcups

# Install Python CUPS library
#RUN pip3 install pycups

# Copy the add-on script into the container
COPY notify_printer.py /notify_printer.py

# Run the add-on
CMD ["python3", "/notify_printer.py"]
