import cups

def print_notification(content):
    conn = cups.Connection()
    printers = conn.getPrinters()
    printer_name = list(printers.keys())[0]  # Use the first printer available
    conn.printFile(printer_name, "/path/to/your/textfile.txt", "Notification", {"title": content})
