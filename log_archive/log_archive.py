'''This will take a log directory as an argument when runing the tool 
This will compress the logs into a tar.gz file and store them in a new directory
This tool will log the date and time of the archive to a file
'''

def get_log_location():
    while True:
        try:
            location = input("Log Archiver, enter your log directory: ")