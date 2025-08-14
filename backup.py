import shutil        # will provide make_archive which is used to create a backup
import datetime
import os

def backup_of_folder(source , destination):
    today = datetime.date.today()   # this variable will store today's date
    backup_file_name = os.path.join(destination,f"backup_{today}") # create a backup file name with today's date aand by join it will create a path for the backup file , f stands for formatted string ...you can use it when you are using variable in between the string
    shutil.make_archive(backup_file_name,"gztar",source)    # where backup is stored, type of file, source of backup

source = r"C:\Users\rupal\OneDrive\Desktop\Python"          # r is there because without it windows path will interpreted as escape sequence

destination = r"C:\Users\rupal\OneDrive\Desktop\Python\backups"

backup_of_folder(source, destination)